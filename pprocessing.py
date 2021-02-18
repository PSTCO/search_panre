import pandas as pd
import numpy as np
from konlpy.tag import Komoran
import gensim
from gensim.models import Word2Vec
from gensim.models import KeyedVectors
from sklearn.metrics.pairwise import cosine_similarity

#판례크롤링 파일 로드
#title, sub_title, content, link
df = pd.read_csv('pancr.csv')
#null 확인
df.isnull().sum()
#중복 제거
df.duplicate(['title']).sum()
df.drop_duplicates(['title'])

#필요한 내용들만 넣을 데이터 프레임 생성
#content에서 판시사항, 판결요지, 이유 등 추출
df2 = pd.DataFrame(columns=['title', 'sub_title', 'content', 'link'])

#content에서 필요한 부분만 추출
for i in range(len(df)):
    tmp = []#마지막에 넣을 것들을 합칠 임시배열
    tmp2 = df.content[i].split('【')#스플릿한걸 넣는 임시배열
    for j in tmp2:
        if(j.startswith('판시사항】')):
            tmp.append(j.replace('판시사항】',''))
        elif(j.startswith('판결요지】')):
            tmp.append(j.replace('판결요지】',''))
        elif(j.startswith('이    유】')):
            tmp.append(j.replace('이    유】',''))
        elif(j.startswith('청구취지 및 항소취지】')):
            tmp.append(j.replace('청구취지 및 항소취지】',''))
        elif(j.startswith('결정요지】')):
            tmp.append(j.replace('결정요지】',''))
        elif(j.startswith('이유】')):
            tmp.append(j.replace('이유】',''))
    
    str1 = ' '.join(tmp)
    #title, sub_title, link는 df에서 그대로 가져옴
    #content만 새로 만들어서 넣음
    df2 = df2.append({'title':df.title[i], 'sub_title':df.sub_title[i], 'content':str1, 'link':df.link[i]}, ignore_index=True)

#한글만 남긴다.
df2['content'] = df2['content'].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]","")
#중복(사실상 공백)제거
df2 = df2.drop_duplicates(['content'])

#불용어 목록 불러오기
f = open("sws2.txt", 'r', encoding='utf-8')
lines = f.readlines()
f.close()

#불용어 리스트 생성
swords = []
for l in lines:
    swords.append(l.rstrip('\n'))

#한글만 남긴 content에서 불용어를 제거하고 넣을 부분
df2['cleaned'] = '0'

#형태소 분석은 Komoran 사용
komoran = Komoran()

#형태소 분석을 통한 토큰화, 불용어 제거후 cleaned에 삽입
for i in range(len(df2.content)):
    temp_X = komoran.morphs(df2.content[i]) # 토큰화
    temp_X = [word for word in temp_X if not word in swords] # 불용어 제거
    df2.cleaned[i] = ' '.join(temp_X)
    print(i , '---')
#여기까지 작업후 저장
df2.to_csv('pancr2.csv')

#단어들을 corpus에 모두 넣고 Word2Vec을 훈련
corpus = []
for words in df2['cleaned']:
    corpus.append(words.split())

#사전 훈련된 워드 임베딩 로드
word2vec_model = gensim.models.Word2Vec.load('ko.bin')
#벡터값을 구하는 함수
def vectors(document_list):
    document_embedding_list = []

    # 각 문서에 대해서
    for line in document_list:
        doc2vec = None
        count = 0
        for word in line.split():
            if word in word2vec_model.wv.vocab:
                count += 1
                # 해당 문서에 있는 모든 단어들의 벡터값을 더한다.
                if doc2vec is None:
                    doc2vec = word2vec_model[word]
                else:
                    doc2vec = doc2vec + word2vec_model[word]

        if doc2vec is not None:
            # 단어 벡터를 모두 더한 벡터의 값을 문서 길이로 나눠준다.
            doc2vec = doc2vec / count
            document_embedding_list.append(doc2vec)

    # 각 문서에 대한 문서 벡터 리스트를 리턴
    return document_embedding_list
#벡터값을 구하고 npy파일로 저장
document_embedding_list = vectors(df2['cleaned'])
np.save('tarr.npy', document_embedding_list)
#문서 벡터간 코사인 유사도 구하기
cosine_similarities = cosine_similarity(document_embedding_list, document_embedding_list)
print('코사인 유사도 매트릭스의 크기 :',cosine_similarities.shape)

