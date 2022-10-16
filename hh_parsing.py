
import requests
from bs4 import BeautifulSoup
import json
import time
import tqdm

headers = {'User-Agent': 'Mozilla/5.0', 'Host': 'spb.hh.ru'}

data = {
    "data":[]
}
url = "https://hh.ru"
page = 1
count = 0
while page < 100:
    search_url = f"/search/vacancy?no_magic=true&L_save_area=true&text=python+%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA&salary=&currency_code=RUR&experience=doesNotMatter&order_by=relevance&search_period=0&items_on_page=20&page={page}&hhtmFrom=vacancy_search_list"

    try:
        resp = requests.get(url= url + search_url, headers = headers)
        
        soup = BeautifulSoup(resp.text, "lxml")
        tags = soup.find_all(class_="vacancy-serp-item-body__main-info")

        for iter in tqdm.tqdm(tags):

            vacancy_info = iter.find(class_="serp-item__title")

            resp_object = requests.get(url=vacancy_info.attrs["href"], headers=headers)
            soup_object = BeautifulSoup(resp_object.text, "lxml")

            tag_price = soup_object.find(attrs={"data-qa": "vacancy-salary-compensation-type-net"})
            tag_price = tag_price.text if tag_price else "Не указана"

            tag_experience = soup_object.find(attrs={"data-qa": "vacancy-experience"})
            tag_experience = tag_experience.text if tag_experience else 'Не указан'

            tag_region = soup_object.find(attrs={"data-qa": "vacancy-serp__vacancy-address"})
            tag_region = tag_region.text if tag_region else "Не указан"

            data["data"].append({
                "Title": vacancy_info.text,
                "Work experience": tag_experience,
                "Salary":tag_price, 
                "Region": tag_region
            })
            count +=1

            with open("data.json", "w") as file:
                json.dump(data, file, ensure_ascii=False)
                
        print('page %s(%s)' % (page, count))
        page += 1
        time.sleep(3)
    
    except Exception as error:
        print(error)
        break

print(count)