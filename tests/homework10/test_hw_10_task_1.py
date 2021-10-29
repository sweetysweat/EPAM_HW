import os
from homework10.hw_10_task_1 import GatherCompanyData
from aioresponses import aioresponses


def read_file(file):
    with open(file, 'r', encoding="utf8") as f:
        return f.read()


table_html = read_file(os.path.join(os.path.dirname(__file__), "table.html"))
mmm_html = read_file(os.path.join(os.path.dirname(__file__), "3M.html"))
aos_html = read_file(os.path.join(os.path.dirname(__file__), "AOSmith.html"))
av_html = read_file(os.path.join(os.path.dirname(__file__), "AV.html"))

growth = read_file(os.path.join(os.path.dirname(__file__), "growth.json"))
profit = read_file(os.path.join(os.path.dirname(__file__), "profit.json"))
p_e = read_file(os.path.join(os.path.dirname(__file__), "pe.json"))
cost = read_file(os.path.join(os.path.dirname(__file__), "cost.json"))

dollar = read_file(os.path.join(os.path.dirname(__file__), 'XML_daily.asp'))


def test_GatherCompanyData():
    with aioresponses() as m:
        m.get("https://markets.businessinsider.com/index/components/s&p_500", body=table_html)
        m.get("https://markets.businessinsider.com/index/components/s&p_500?p=1", body=table_html)
        m.get("https://markets.businessinsider.com/stocks/mmm-stock", body=mmm_html)
        m.get("https://markets.businessinsider.com/stocks/aos-stock", body=aos_html)
        m.get("https://markets.businessinsider.com/stocks/abt-stock", body=av_html)
        m.get("https://www.cbr.ru/scripts/XML_daily.asp", body=dollar)

        data = GatherCompanyData().sort_and_save_data()

        assert growth == read_file(os.path.join(os.path.dirname(__file__), "companies_with_highest_growth.json"))
        assert profit == read_file(os.path.join(os.path.dirname(__file__), "companies_with_highest_profit.json"))
        assert p_e == read_file(os.path.join(os.path.dirname(__file__), "companies_with_lowest_pe.json"))
        assert cost == read_file(os.path.join(os.path.dirname(__file__), "most_expensive_companies.json"))

        os.remove("companies_with_highest_growth.json")
        os.remove("companies_with_highest_profit.json")
        os.remove("companies_with_lowest_pe.json")
        os.remove("most_expensive_companies.json")
