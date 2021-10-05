from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
import SupFunc as sup
import json
from datetime import  date
import matplotlib.pyplot as plt

driver = webdriver.Chrome()
url = 'https://www.zap.co.il/model.aspx?modelid=1096042'
driver.get(url)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

products = driver.find_elements_by_class_name('StoreLine')
products_list = []
prev_name = []
for product in products:
    price = product.find_element_by_class_name('PriceNum').text
    name2 = product.find_element_by_tag_name('a').get_attribute('aria-label').split(" ")[4:]
    name2 = sup.add_spaces(name2)
    rating = sup.get_numeric_vals(product.find_element_by_tag_name('span').get_attribute('style'))
    num_r = sup.get_numeric_vals(product.find_element_by_class_name('StoreReviewsTxt').find_element_by_tag_name('a').get_attribute('aria-label'))
    if(type(num_r) is list):
        if('825' in num_r):
            num_r.remove('825') # PS5 Giga-Bytes
        num_r = max(num_r)
    else:
        num_r = 0
    print(num_r)
    if(len(rating)>0):
        rating = (int(rating[0])//10)/2
    else:
        rating = None


    if(name2 in prev_name):
        pass
    else:
        p_item = {
            'name' : name2,
            'price': price,
            'rating': rating,
            'rates' : num_r
        }
        products_list.append(p_item)
    prev_name.append(name2)

#df = pd.DataFrame(products_list)

driver.quit()

five_s,four_s = sup.find_best(products_list)
new_l = sup.find_best_offers(five_s) + sup.find_best_offers(four_s)

with open(r"C:\Users\levan\OneDrive\Desktop\Jesus_is_I7\Selenium\Zap.json",'r') as f1:
    jsonObj = json.load(f1)
    jsonObj[str(date.today())] = new_l
    with open(r"C:\Users\levan\OneDrive\Desktop\Jesus_is_I7\Selenium\Zap.json",'w') as f2:
        json.dump(jsonObj,f2,indent=1)
