# -*- coding: utf-8 -*-

#필요 라이브러리 임포트
import pandas as pd
import numpy as np
import re
import sys
from gensim.models import KeyedVectors
from sklearn.metrics.pairwise import cosine_similarity
from konlpy.tag import Okt

loaded_model = KeyedVectors.load_word2vec_format("w2v") # 모델 불러오기
df = pd.read_csv('panre4.csv')#판례불러오기
np_load = np.load('tarr2.npy')#벡터값 배열 불러오기

#불용어 목록 불러오기
f = open("sws2.txt", 'r', encoding='utf-8')
lines = f.readlines()
f.close()

#불용어 리스트만들기
swords = []
for l in lines:
    swords.append(l.rstrip('\n'))


def input_story(story1):
    global df
    global np_load
    #story = input('입력 : ')
    story = story1
    story = re.compile('[^ㄱ-ㅎㅏ-ㅣ가-힣 ]+').sub('',story)
    
    okt = Okt()
    tokenized_data = []

    temp_X = okt.morphs(story, stem=True) # 토큰화
    temp_X = [word for word in temp_X if not word in swords] # 불용어 제거
    tokenized_data.append(temp_X)
    
    if(df.title[len(df)-1] == '검색용'):
        df = df.drop(len(df)-1) 
        
    clean_s = ' '.join(temp_X)
    s_data = {'title':'검색용', 'contents':story, 'cleaned':clean_s}
    df = df.append(s_data,ignore_index=True)
    
    tvec = vectors([clean_s])
    #print(tvec)
    #print('-----------', df.cleaned[len(df)-1])

    np_load = np.concatenate((np_load, tvec), axis=0)

#print(len(np_load))
#print(df.shape)

def vectors(document_list):
    document_embedding_list = []

    # 각 문서에 대해서
    for line in document_list:
        #print('---', line)
        doc2vec = None
        count = 0
        for word in line.split():
            if word in loaded_model.wv.vocab:
                count += 1
                # 해당 문서에 있는 모든 단어들의 벡터값을 더한다.
                if doc2vec is None:
                    doc2vec = loaded_model[word]
                else:
                    doc2vec = doc2vec + loaded_model[word]

        if doc2vec is not None:
            # 단어 벡터를 모두 더한 벡터의 값을 문서 길이로 나눠준다.
            doc2vec = doc2vec / count
            document_embedding_list.append(doc2vec)

    # 각 문서에 대한 문서 벡터 리스트를 리턴
    return document_embedding_list


def recommendations(title):
    books = df[['title','link']]

    # 책의 제목을 입력하면 해당 제목의 인덱스를 리턴받아 idx에 저장.
    indices = pd.Series(df.index, index = df['title']).drop_duplicates()    
    idx = indices[title]
    #print('idx : ',idx)

    # 입력된 책과 줄거리(document embedding)가 유사한 책 5개 선정.
    sim_scores = list(enumerate(cosine_similarities[idx]))
    #print('s1 : ',sim_scores)
    sim_scores = sorted(sim_scores, key = lambda x: x[1], reverse = True)
    #print('s2 : ',sim_scores)
    sim_scores = sim_scores[1:6]
    #print('s3 : ',sim_scores)

    # 가장 유사한 책 5권의 인덱스
    book_indices = [i[0] for i in sim_scores]
    #print('bi', book_indices)

    # 전체 데이터프레임에서 해당 인덱스의 행만 추출. 5개의 행을 가진다.
    recommend = books.iloc[book_indices].reset_index(drop=True)
    #print(type(recommend))
    for i in recommend['title'].tolist():
        print(i)

    #for j in recommend['link'].tolist():
    #    print(j)


if __name__ == '__main__':

    input_story(sys.argv[1])
    #print(len(np_load))
    #print(df.shape)

    document_embedding_list = np_load
    #print('문서 벡터의 수 :',len(document_embedding_list))

    cosine_similarities = cosine_similarity(document_embedding_list, document_embedding_list)
    #print('코사인 유사도 매트릭스의 크기 :',cosine_similarities.shape)

    recommendations('검색용')