# HitChat


문서 벡터를 이용한 판례 검색 
​

# 제목 1

## 제목 2

### 제목 3

#### 제목 4

##### 제목 5

###### 제목 6

​

​

이텔릭체는 *별표(asterisks)* 혹은 _언더바(underscore)_ 

두껍게는 **별표(asterisks)** 혹은 __언더바(underscore)__ 

**_이텔릭체_와 두껍게**를 같이 사용할 수 있다. 

취소선은 ~~물결표시(tilde)~~를 사용 

<u>밑줄</u>은 `<u>밑줄글씨</u>`를 사용 

​

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

​

> This is a first blockqute.

>   > This is a second blockqute.

>   >   > This is a third blockqute.

​

​

<pre>

<code>

html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    title = soup.select('#bmunStart > h2')
    sub_title = soup.select('#bmunStart > p')
    content = soup.select('#areaDetail > div.page_area > div')

​

}

</code>

</pre>

​

```

import time
import pandas as pd

from selenium import webdriver
from bs4 import BeautifulSoup

```

​

* * *

***

*****

- - -

---------------------------------------
