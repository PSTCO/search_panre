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



이텔릭체는 *별표(asterisks)* 혹은 _언더바(underscore)_ 

두껍게는 **별표(asterisks)** 혹은 __언더바(underscore)__ 

**_이텔릭체_와 두껍게**를 같이 사용할 수 있다. 

취소선은 ~~물결표시(tilde)~~를 사용 

<u>밑줄</u>은 `<u>밑줄글씨</u>`를 사용 



1. 순서가 필요한 목록

1. 순서가 필요한 목록

   - 순서가 필요하지 않은 목록(서브) 

   - 순서가 필요하지 않은 목록(서브) 

1. 순서가 필요한 목록

   1. 순서가 필요한 목록(서브)

   1. 순서가 필요한 목록(서브)

1. 순서가 필요한 목록

- 순서가 필요하지 않은 목록에 사용 가능한 기호

      - 대쉬(hyphen) 

   * 별표(asterisks)

   + 더하기(plus sign)

​

> This is a first blockqute.

>   > This is a second blockqute.

>   >   > This is a third blockqute.

​
<pre>

<code>
public class BootSpringBootApplication {

public static void main(String[] args) {

   System.out.println("Hello, Honeymon");

}
</code>

</pre>

​

```
public class BootSpringBootApplication {

   public static void main(String[] args) {

      System.out.println("Hello, Honeymon");

   }

}
```


* * *

***

*****

- - -

---------------------------------------
