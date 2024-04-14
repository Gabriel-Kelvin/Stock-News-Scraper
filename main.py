import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": "L6QXQXTIBHL1F17J",
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()

stock_data = response.json()["Time Series (Daily)"]
print(stock_data)
stock_list = [value for (key, value) in stock_data.items()]

yesterday_data = stock_list[0]
yesterday_data_closing_price = float(yesterday_data["4. close"])

day_before_data = stock_list[1]
day_before_data_closing_price = float(day_before_data["4. close"])

difference = abs(yesterday_data_closing_price - day_before_data_closing_price)
diff_percent = (difference / float(yesterday_data_closing_price) * 100)

news_params = {
    "apiKey": "a5e2ce4a257144f0aa10b868c9593a64",
    "qInTitle": COMPANY_NAME,
}

news_response = requests.get(NEWS_ENDPOINT, params=news_params)
news_response.raise_for_status()

if diff_percent > 1:
    news_data = news_response.json()
    articles = news_data["articles"]
    three_articles = articles[:3]


    formatted_articles = [f"Headline: {articles['title']}. \nBrief: {articles['description']}"
                          for articles in three_articles]
    print(formatted_articles)