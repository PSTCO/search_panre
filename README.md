# 문서 벡터를 이용한 판례 검색 시스템




## 사용 기술
   - 크롤링
   - 기계학습 
   - 웹 서버
   - 형태소 분석


## 사용 데이터
   - 대한민국 법원 종합법률정보에서 제공하는 2011.01.01~2021.01.01 기간의 판례 약 15,000개 수집
      - https://glaw.scourt.go.kr/  
   - 사전 학습된 Word2Vec모델
      - https://github.com/Kyubyong/wordvectors
      - 다운로드 : https://drive.google.com/file/d/0B0ZXk88koS2KbDhXdWg1Q2RydlU/view  



## 프로그램의 흐름

![설명2](https://user-images.githubusercontent.com/52062016/108313670-10a6db80-71fc-11eb-9499-bff83b33d6e4.png)

## 필요 환경

- 공통
   - Python(3.8.5)
   - PHP(Windows : 8.0.2, Linux : 7.4.3) 
   - Pandas(Windows : 1.1.3, Linux : 0.25.3)
- 크롤링
   - Selenium(3.141.0)
   - BeautifulSoup(4.6.0)
- 자연어 처리
   - Numpy(1.19.x)
   - Konlpy(0.5.2)
   - Gensim(3.8.3)
   - Scikit-learn(0.24.x)
- 웹 서버
   - Apache HTTP Server(2.4.x)

## 사용방법

1. ㅁㄴㅇㄹ
2. ㅋㅌㅊㅍ
3. ㅂㅈㄷㄱ
4. ㄷㄱㅅㅛ
5. ㅜㅠㅍㅊ
