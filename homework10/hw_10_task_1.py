"""
Ваша задача спарсить информацию о компаниях, находящихся в индексе S&P 500 с данного сайта:
https://markets.businessinsider.com/index/components/s&p_500

Для каждой компании собрать следующую информацию:

Текущая стоимость в рублях (конвертацию производить по текущему курсу, взятому с сайта центробанка РФ)
Код компании (справа от названия компании на странице компании)
P/E компании (информация находится справа от графика на странице компании)
Годовой рост/падение компании в процентах (основная таблица)
Высчитать какую прибыль принесли бы акции компании (в процентах), если бы они были куплены на уровне 52 Week Low
и проданы на уровне 52 Week High (справа от графика на странице компании)
Сохранить итоговую информацию в 4 JSON файла:

Топ 10 компаний с самими дорогими акциями в рублях.
Топ 10 компаний с самым низким показателем P/E.
Топ 10 компаний, которые показали самый высокий рост за последний год
Топ 10 комппаний, которые принесли бы наибольшую прибыль,
если бы были куплены на самом минимуме и проданы на самом максимуме за последний год.

Пример формата:
[
    {
        "code": "MMM",
        "name": "3M CO.",
        "price" | "P/E" | "growth" | "potential profit" : value,
    },
    ...
]

For scrapping you cans use beautifulsoup4
For requesting aiohttp
"""
import asyncio
import json
from typing import Optional

from aiohttp import ClientSession
from bs4 import BeautifulSoup


class GatherCompanyData:
    main_url = "https://markets.businessinsider.com"

    def __init__(self):
        self.dollar_value = 0
        self.parsed_company_data = []
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.main())

    @staticmethod
    async def get_dollar_value(session: ClientSession) -> float:
        async with session.get("https://www.cbr.ru/scripts/XML_daily.asp") as response:
            data = await response.text()
            return float(BeautifulSoup(data, "lxml").find("valute", {"id": "R01235"}).value.text.replace(',', '.'))

    async def get_data_from_table(self, session: ClientSession, url: str):
        async with session.get(url) as response:
            table_data = await response.text()
            table = BeautifulSoup(table_data, "lxml").find_all("tr")[1:]  # с 1, чтобы игнорить заголовки
            for row in table:
                company_info = dict()
                company_info["name"] = row.find("a").text.strip()
                company_info["growth"] = float(row.find_all("td")[-1].find_all("span")[-1].text[:-1])
                href = row.find("a")["href"]
                async with session.get(self.main_url + href) as company_page:
                    company_page_data = await company_page.text()
                    soup = BeautifulSoup(company_page_data, "lxml")
                    price_in_dollars = float(soup.find("span", class_="price-section__current-value")
                                             .text.replace(',', ''))
                    company_info["price"] = round((price_in_dollars * self.dollar_value), 2)
                    company_info["code"] = soup.find("span", class_="price-section__category").find("span").text[2:]
                    company_info["P/E"] = await self.get_company_PE(soup)
                    company_info["profit"] = await self.get_company_profit(soup)
                self.parsed_company_data.append(company_info)

    @staticmethod
    async def get_company_PE(page: BeautifulSoup) -> Optional[float]:
        if n := page.find("div", text="P/E Ratio"):
            return float(n.parent.find(text=True).text.strip().replace(',', ''))

    @staticmethod
    async def get_company_profit(page: BeautifulSoup) -> Optional[float]:
        if n := page.find("div", text="52 Week Low"):
            week_low = float(n.parent.find(text=True).text.strip().replace(',', ''))
            week_high = float(page.find("div", text="52 Week High")
                              .parent.find(text=True).text.strip().replace(',', ''))
            return round(((week_high - week_low) / week_high), 2)

    def sort_and_save_data(self):
        price = sorted(self.parsed_company_data, key=lambda x: x["price"], reverse=True)[:10]
        self.save_data("most_expensive_companies.json", price)

        filtered_pe = list(filter(lambda x: isinstance(x["P/E"], float), self.parsed_company_data))
        pe = sorted(filtered_pe, key=lambda x: x["P/E"])[:10]
        self.save_data("companies_with_lowest_pe.json", pe)

        growth = sorted(self.parsed_company_data, key=lambda x: x["growth"], reverse=True)[:10]
        self.save_data("companies_with_highest_growth.json", growth)

        filtered_profit = list(filter(lambda x: isinstance(x["profit"], float), self.parsed_company_data))
        profit = sorted(filtered_profit, key=lambda x: x["profit"], reverse=True)[:10]
        self.save_data("companies_with_highest_profit.json", profit)

    @staticmethod
    def save_data(file_name: str, data: list):
        with open(file_name, 'w') as f:
            json.dump(data, f, indent=4)

    async def main(self):
        tasks = []
        async with ClientSession() as session:
            self.dollar_value = await self.get_dollar_value(session)
            table_url = self.main_url + "/index/components/s&p_500"
            async with session.get(table_url) as response:
                data = await response.text()
                pages = int(BeautifulSoup(data, "lxml").find("div", class_="finando_paging").find_all("a")[-2].text)
            for page in range(1, pages + 1):
                task = asyncio.create_task(self.get_data_from_table(session, f"{table_url}?p={str(page)}"))
                tasks.append(task)
            await asyncio.gather(*tasks)
