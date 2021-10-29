import os

from aioresponses import aioresponses

from homework10.hw_10_task_1 import GatherCompanyData


def read_file(file):
    with open(file, 'r', encoding="utf8") as f:
        return f.read()


path = os.getcwd() + "/tests/homework10/"
table_html = read_file(path + "table.html")
mmm_html = read_file(path + "3M.html")
aos_html = read_file(path + "AOSmith.html")
av_html = read_file(path + "AV.html")

growth = read_file(path + "growth.json")
profit = read_file(path + "profit.json")
p_e = read_file(path + "pe.json")
cost = read_file(path + "cost.json")

dollar = read_file(path + "XML_daily.asp")


def test_GatherCompanyData():
    with aioresponses() as m:
        m.get("https://markets.businessinsider.com/index/components/s&p_500", body=table_html)
        m.get("https://markets.businessinsider.com/index/components/s&p_500?p=1", body=table_html)
        m.get("https://markets.businessinsider.com/stocks/mmm-stock", body=mmm_html)
        m.get("https://markets.businessinsider.com/stocks/aos-stock", body=aos_html)
        m.get("https://markets.businessinsider.com/stocks/abt-stock", body=av_html)
        m.get("https://www.cbr.ru/scripts/XML_daily.asp", body=dollar)

        data = GatherCompanyData().sort_and_save_data()

        assert growth == read_file("companies_with_highest_growth.json")
        assert profit == read_file("companies_with_highest_profit.json")
        assert p_e == read_file("companies_with_lowest_pe.json")
        assert cost == read_file("most_expensive_companies.json")

        os.remove("companies_with_highest_growth.json")
        os.remove("companies_with_highest_profit.json")
        os.remove("companies_with_lowest_pe.json")
        os.remove("most_expensive_companies.json")
