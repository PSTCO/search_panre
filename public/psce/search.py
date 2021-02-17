# -*- coding: utf-8 -*-

#필요 라이브러리 임포트
import pandas as pd
import numpy as np
import re
import sys
import warnings
import gensim
from gensim.models import KeyedVectors
from sklearn.metrics.pairwise import cosine_similarity
from konlpy.tag import Okt
from konlpy.tag import Komoran

loaded_model = gensim.models.Word2Vec.load('ko.bin') # 모델 불러오기
df = pd.read_csv('pancr4.csv')#판례불러오기
np_load = np.load('tarr4.npy')#벡터값 배열 불러오기

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
    
    okt = Komoran()##
    tokenized_data = []

    temp_X = okt.morphs(story) # 토큰화
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
    books = df[['title','sub_title', 'link']]

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
    with open("foo.txt", "w", encoding='utf-8') as f:
        f.write('')

    for i in range(len(recommend)):
        with open("foo.txt", "a", encoding='utf-8') as f:
            f.write(str(recommend.title[i])+'\n')
            f.write(str(recommend.sub_title[i])+'\n')
            if(i == len(recommend)-1):
                f.write(str(recommend.link[i]))
            else:
                f.write(str(recommend.link[i])+'\n')

if __name__ == '__main__':
    warnings.filterwarnings('ignore')

    input_story(sys.argv[1])
    #input_story('【판시사항】[1] 저장매체에 대한 압수ㆍ수색 과정에서 전자정보가 담긴 저장매체, 하드카피나 이미징(imaging) 등 형태(복제본)를 수사기관 사무실 등으로 옮겨 복제ㆍ탐색ㆍ출력하는 경우, 피압수자나 변호인에게 참여 기회를 보장하고 혐의사실과 무관한 전자정보의 임의적인 복제 등을 막기 위한 적절한 조치를 취하여야 하는지 여부(적극) 및 이러한 조치를 취하지 않은 경우, 압수ㆍ수색의 적법 여부(원칙적 소극) / 이는 수사기관이 저장매체 또는 복제본에서 혐의사실과 관련된 전자정보만을 복제ㆍ출력한 경우에도 마찬가지인지 여부(적극)[2] 형사소송법 제219조, 제121조에서 규정한 변호인의 참여권이 피압수자의 보호를 위하여 변호인에게 주어진 고유권인지 여부(적극) / 피압수자가 수사기관에 압수ㆍ수색영장의 집행에 참여하지 않는다는 의사를 명시한 경우, 그 변호인에게는 미리 집행의 일시와 장소를 통지하는 등으로 압수ㆍ수색영장의 집행에 참여할 기회를 별도로 보장하여야 하는지 여부(원칙적 적극)[3] 위법수집증거 배제 원칙을 명시한 형사소송법 제308조의2의 취지 / 적법한 절차에 따르지 않고 수집한 증거 및 이를 기초로 하여 획득한 2차적 증거의 증거능력 유무(원칙적 소극) / 위법수집증거 및 이를 기초로 하여 획득한 2차적 증거의 증거능력을 예외적으로 인정할 수 있는 경우와 그 판단 기준【판결요지】[1] 수사기관이 압수ㆍ수색영장을 집행할 때에는 피압수자 또는 변호인은 그 집행에 참여할 수 있다(형사소송법 제219조, 제121조). 저장매체에 대한 압수ㆍ수색 과정에서 범위를 정하여 출력ㆍ복제하는 방법이 불가능하거나 압수의 목적을 달성하기에 현저히 곤란한 예외적인 사정이 인정되어 전자정보가 담긴 저장매체, 하드카피나 이미징(imaging) 등 형태(이하 ‘복제본’이라 한다)를 수사기관 사무실 등으로 옮겨 복제ㆍ탐색ㆍ출력하는 경우에도, 피압수자나 변호인에게 참여 기회를 보장하고 혐의사실과 무관한 전자정보의 임의적인 복제 등을 막기 위한 적절한 조치를 취하는 등 영장주의 원칙과 적법절차를 준수하여야 한다. 만일 그러한 조치를 취하지 않았다면 피압수자 측이 위와 같은 절차나 과정에 참여하지 않는다는 의사를 명시적으로 표시하였거나 절차 위반행위가 이루어진 과정의 성질과 내용 등에 비추어 피압수자에게 절차 참여를 보장한 취지가 실질적으로 침해되었다고 볼 수 없을 정도에 해당한다는 등의 특별한 사정이 없는 이상 압수ㆍ수색이 적법하다고 할 수 없다. 이는 수사기관이 저장매체 또는 복제본에서 혐의사실과 관련된 전자정보만을 복제ㆍ출력한 경우에도 마찬가지이다.[2] 형사소송법 제219조, 제121조가 규정한 변호인의 참여권은 피압수자의 보호를 위하여 변호인에게 주어진 고유권이다. 따라서 설령 피압수자가 수사기관에 압수ㆍ수색영장의 집행에 참여하지 않는다는 의사를 명시하였다고 하더라도, 특별한 사정이 없는 한 그 변호인에게는 형사소송법 제219조, 제122조에 따라 미리 집행의 일시와 장소를 통지하는 등으로 압수ㆍ수색영장의 집행에 참여할 기회를 별도로 보장하여야 한다.[3] 형사소송법 제308조의2는 ‘적법한 절차에 따르지 아니하고 수집한 증거는 증거로 할 수 없다’고 정하고 있다. 이는 위법한 압수ㆍ수색을 비롯한 수사 과정의 위법행위를 억제하고 재발을 방지함으로써 국민의 기본적 인권 보장이라는 헌법 이념을 실현하고자 위법수집증거 배제 원칙을 명시한 것이다. 헌법 제12조는 기본적 인권을 보장하기 위하여 압수ㆍ수색에 관한 적법절차와 영장주의 원칙을 선언하고 있고, 형사소송법은 이를 이어받아 실체적 진실 규명과 개인의 권리보호 이념을 조화롭게 실현할 수 있도록 압수ㆍ수색절차에 관한 구체적 기준을 마련하고 있다. 이러한 헌법과 형사소송법의 규범력을 확고하게 유지하고 수사 과정의 위법행위를 억제할 필요가 있으므로, 적법한 절차에 따르지 않고 수집한 증거는 물론 이를 기초로 하여 획득한 2차적 증거 또한 기본적 인권 보장을 위해 마련된 적법한 절차에 따르지 않고 확보한 것으로서 원칙적으로 유죄 인정의 증거로 삼을 수 없다고 보아야 한다.그러나 법률에 정해진 절차에 따르지 않고 수집한 증거라는 이유만을 내세워 획일적으로 증거능력을 부정하는 것은 헌법과 형사소송법의 목적에 맞지 않는다. 실체적 진실 규명을 통한 정당한 형벌권의 실현도 헌법과 형사소송법이 형사소송절차를 통하여 달성하려는 중요한 목표이자 이념이기 때문이다. 수사기관의 절차 위반행위가 적법절차의 실질적인 내용을 침해하는 경우에 해당하지 않고, 오히려 증거능력을 배제하는 것이 헌법과 형사소송법이 형사소송에 관한 절차 조항을 마련하여 적법절차의 원칙과 실체적 진실 규명의 조화를 도모하고 이를 통하여 형사 사법 정의를 실현하려 한 취지에 반하는 결과를 초래하는 것으로 평가되는 예외적인 경우라면, 법원은 그 증거를 유죄 인정의 증거로 사용할 수 있다고 보아야 한다. 이에 해당하는지는 수사기관의 증거 수집 과정에서 이루어진 절차 위반행위와 관련된 모든 사정, 즉 절차 조항의 취지, 위반 내용과 정도, 구체적인 위반 경위와 회피가능성, 절차 조항이 보호하고자 하는 권리나 법익의 성질과 침해 정도, 이러한 권리나 법익과 피고인 사이의 관련성, 절차 위반행위와 증거 수집 사이의 관련성, 수사기관의 인식과 의도 등을 전체적ㆍ종합적으로 고찰하여 판단해야 한다. 이러한 법리는 적법한 절차에 따르지 않고 수집한 증거를 기초로 하여 획득한 2차적 증거에 대해서도 마찬가지로 적용되므로, 절차에 따르지 않은 증거 수집과 2차적 증거 수집 사이 인과관계의 희석이나 단절 여부를 중심으로 2차적 증거 수집과 관련된 모든 사정을 전체적ㆍ종합적으로 고려하여 예외적인 경우에는 유죄 인정의 증거로 사용할 수 있다.')
    #print(len(np_load))
    #print(df.shape)

    document_embedding_list = np_load
    #print('문서 벡터의 수 :',len(document_embedding_list))

    cosine_similarities = cosine_similarity(document_embedding_list, document_embedding_list)
    #print('코사인 유사도 매트릭스의 크기 :',cosine_similarities.shape)
    recommendations('검색용')