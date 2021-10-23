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
import os

from aiohttp import ClientSession
import asyncio
from bs4 import BeautifulSoup
from datetime import datetime


class WebScraper:
    def __init__(self):
        self.url = "https://markets.businessinsider.com/index/components/s&p_500"
        # self.headers = {
        #     "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,\
        #             */*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        #     "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
        #      Chrome/94.0.4606.81 Safari/537.36",
        # }
        self.date = datetime.now().strftime("%d/%m/%Y")
        self.dollar_value = None

    async def get_amount_of_pages(self, session: ClientSession) -> int:
        """Count amount of pages on the website"""
        async with session.get(self.url) as response:
            data = await response.text()
            soup = BeautifulSoup(data, "lxml")
            return int(soup.find("div", class_="finando_paging margin-top--small").find_all("a")[-2].text)

    async def get_dollar_value(self, session: ClientSession) -> float:
        """Get value of 1 dollar in rubles"""
        response = await session.get("https://www.cbr.ru/scripts/XML_daily.asp?date_req=".join(self.date))
        data = await response.text()
        return float(BeautifulSoup(data, "lxml").find("valute", {"id": "R01235"}).find("value").text.strip())

    async def get_company_data(self, session: ClientSession, url: str):
        response = await session.get(url)
        data = response.text()
        print(data)

    async def gather_data(self):
        tasks = []
        async with ClientSession() as session:
            self.dollar_value = await self.get_dollar_value(session)
            for page in range(1, self.get_amount_of_pages(session) + 1):
                url = self.url.join(f"?p={page}")
                task = asyncio.create_task(self.get_company_data(session, url))
                tasks.append(task)
            await asyncio.gather(*tasks)


t = WebScraper()
loop = asyncio.get_event_loop()
loop.run_until_complete(t.gather_data())
