
from curses import KEY_COMMAND
from bs4 import BeautifulSoup
from ..models import DogSearch
import json
import re
import time
from selenium.webdriver.common.by import By
import requests


def search():

    # 검색할 키워드들 리스트로 초기화
    dogAll = DogSearch.objects.all()
    dogBreedList = dogAll.values('breed')
    dogNameList = dogAll.values()[0].keys()

    num = 0
    count = 1

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Safari/605.1.15'}

    for i in dogBreedList:
        breedName = i['breed']
        temp = {}
        temp['breed'] = breedName

        for key in dogNameList:
            if not (key == 'id' or key == 'breed'):
                url = "https://www.google.com/search?q="
                keyword = "\"" + breedName + " " + key + "\""
                url += keyword

                # 검색
                result = requests.get(url, headers=headers)
                result.encoding = result.apparent_encoding
                count += 1
                print(keyword)

                for i in result:
                    soup = BeautifulSoup(result.text, 'html.parser')

                    print(soup)
                    total_results_text = soup.find(
                        "div", {"id": "result-stats"}).find(text=True, recursive=False)
                    results_num = ''.join(
                        [num for num in total_results_text if num.isdecimal()])
                    print(results_num)

                    num = int(results_num)
                    temp[key] = num
                    break

        # 검색결과
        headers = {'Content-Type': 'application/json;'}
        requests.put("http://127.0.0.1:8000/api/dog/",
                     data=json.dumps(temp, ensure_ascii=False).encode('utf-8'), headers=headers)
