
from curses import KEY_COMMAND
from bs4 import BeautifulSoup
from ..models import CatSearch
import json
import re
import time
import requests


def search():

    # 검색할 키워드들 리스트로 초기화
    catAll = CatSearch.objects.all()
    catBreedList = catAll.values('breed')
    catNameList = catAll.values()[0].keys()

    num = 0
    count = 1

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Safari/605.1.15'}

    for i in catBreedList:
        breedName = i['breed']
        temp = {}
        temp['breed'] = breedName

        for key in catNameList:
            if not (key == 'id' or key == 'breed'):
                url = "https://www.google.com/search?q="
                keyword = "\"" + breedName + " " + key + "\""
                url += keyword

                # 검색
                time.sleep(60)
                result = requests.get(url, headers=headers)
                result.encoding = result.apparent_encoding
                count += 1
                if count % 30 == 0:
                    time.sleep(1800)
                print(keyword)

                for i in result:
                    soup = BeautifulSoup(result.text, 'html.parser')

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
        requests.put("http://127.0.0.1:8000/api/cat/",
                     data=json.dumps(temp, ensure_ascii=False).encode('utf-8'), headers=headers)

    driver.close()
