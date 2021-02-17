# 문서 벡터를 이용한 판례 검색 시스템




## 사용 기술
   - 파이썬(Python)
   - 크롤링(Selenium, BeautifulSoup4)
   - PHP
   - 기계학습(Machine Learning)
   - 아파치 HTTP서버(XAMPP)
   - 워드 투 벡터(Word2Vec)
   - 형태소 분석(Komoran)


## 사용 데이터
   - 대한민국 법원 종합법률정보에서 제공하는 2011.01.01~2021.01.01 기간의 판례 약 15,000개 수집
   - https://glaw.scourt.go.kr/



## 프로그램의 흐름
![image1](/images/그림1.png)

​

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