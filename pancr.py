import time
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup

pan = []

driver = webdriver.Chrome()
#판례 시작(2011.01.01~2021.01.01)
driver.get('https://glaw.scourt.go.kr/wsjo/panre/sjo100.do?contId=3224650&q=*&nq=&w=panre&section=panre_tot&subw=&subsection=&subId=2&csq=&groups=6,7,5,9&category=&outmax=1&msort=&onlycount=&sp=&d1=20110101~20210101&d2=&d3=&d4=&d5=&pg=1&p1=&p2=&p3=&p4=&p5=&p6=&p7=&p8=&p9=&p10=&p11=&p12=&sysCd=WSJO&tabGbnCd=&saNo=&joNo=&lawNm=&hanjaYn=N&userSrchHistNo=&poption=&srch=&range=&daewbyn=N&smpryn=N&idgJyul=01&newsimyn=Y&tabId=&save=Y&bubNm=')
time.sleep(1)

for i in range(16550):
    time.sleep(0.2)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    #제목, 부제목, 내용, 링크
    title = soup.select('#bmunStart > h2')
    sub_title = soup.select('#bmunStart > p')
    content = soup.select('#areaDetail > div.page_area > div')
    linkk = driver.current_url
    print(i, ' --- ')
    
    for item in zip(title, sub_title, content, linkk):
        pan.append(
            {
                'title' : item[0].text,
                'sub_title' : item[1].text,
                'content' : item[2].text,
                'link' : linkk
            }
        )
    #1000개마다 파일로 저장
    if(i%1000 == 0):
        data = pd.DataFrame(pan)
        data.to_csv('pancr.csv')
    #다음판례로
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/a[2]/img').click()

data = pd.DataFrame(pan)
data.to_csv('pancr.csv')
        
driver.quit()