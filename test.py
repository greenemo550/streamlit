import time
from selenium import webdriver #Selenium Webdriverをインポートする

driver = webdriver.Chrome("C:\Users\nobuki\Desktop\python\chromedriver.exe") #chromdriverのフルパスを入れてあげる

driver.get('https://www.google.com/')

time.sleep(5) #5秒待つ。冒頭のimport timeで利用可能なtimeメソッド

search_box = driver.find_element_by_name("q") #DOM操作

search_box.send_keys('NakamuraBlog') #Google検索ボックス内に「NakamuraBlog」と入力
search_box.submit() #Google検索ボタンのクリック　

time.sleep(5) #5秒待つ。冒頭のimport timeで利用可能なtimeメソッド

research_result = driver.find_element_by_partial_link_text("nkmrdai") #検索結果hrefタグ内に「nkmradai」があるリンクを探す
research_result.click() #クリックする。 #このタイミングでNakamuraBlogのトップページが開かれたらOK

time.sleep(5) #5秒待つ。冒頭のimport timeで利用可能なtimeメソッド

driver.quit() #Chromeブラウザを閉じる
