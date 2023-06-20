from bs4 import BeautifulSoup
import requests


def naver_finance_crawling(stock_number):
    url = 'https://finance.naver.com/item/main.naver?code=' + str(stock_number)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 현재가 추출
    current_price = soup.select_one("dd:contains('현재가')").get_text(strip=True).split()[1]

    # 시가 추출
    open_price = soup.select_one("dd:contains('시가')").get_text(strip=True).split()[1]

    # 고가 추출
    high_price = soup.select_one("dd:contains('고가')").get_text(strip=True).split()[1]

    # 저가 추출
    low_price = soup.select_one("dd:contains('저가')").get_text(strip=True).split()[1]

    # 거래량 추출
    volume = soup.select_one("dd:contains('거래량')").get_text(strip=True).split()[1].replace(",", "")

    # 시가총액 추출
    market_cap = soup.select_one('#_market_sum').get_text(strip=True)

    # 시가총액순위 추출
    market_cap_rank = soup.select_one('th:-soup-contains("시가총액순위") + td').get_text(strip=True)

    # 상장주식수 추출
    listing_shares = soup.find('th', text='상장주식수').find_next_sibling('td').find('em').get_text(strip=True)

    # 동일업종 등락률 추출
    industry_fluctuation = soup.find('th', text='동일업종 등락률').find_next('em').text.strip()

    return [current_price, open_price, high_price, low_price, volume, market_cap, market_cap_rank, listing_shares,
            industry_fluctuation]
def main():
    print(naver_finance_crawling(102280))

if __name__=="__main__":
    main()