import requests
from requests import get


def news():

    # following query parameters are used
    # source, sortBy and apiKey
    query_params = {
        "source": "the-times-of-india",
        "sortBy": "top",
        "country": "in",
        "apiKey": "10de010a3bfe439e9c70465c15c6c1aa"
    }
    main_url = " https://newsapi.org/v1/articles"

    # fetching data in json format
    res = requests.get(main_url, params=query_params)
    open_bbc_page = res.json()

    # getting all articles in a string article
    article = open_bbc_page["articles"]

    # empty list which will
    # contain all trending news
    results = []

    for ar in article:
        results.append(ar["title"])

    # speak('here are some top news from the times of india')
    print('''=============== TIMES OF INDIA ============''' + '\n')

    for i in range(len(results)):
        # printing all trending news
        print(i + 1, results[i])

    # print("This news will be given to you by The Times of India")
    # speak("This news will be given to you by The Times of India")
    # to read the news out loud for us
    # from win32com.client import Dispatch
    # speak = Dispatch("SAPI.Spvoice")

    # speak(results)
