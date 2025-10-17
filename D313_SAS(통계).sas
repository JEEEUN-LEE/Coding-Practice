/*-----------------------------------------------------------
 SAS - TF-IDF (Term Frequency - Inverse Document Frequency)
-----------------------------------------------------------*/

/*
 🔹 TF-IDF란?
   - 문서 내 단어의 중요도를 평가하는 지표.
   - Term Frequency (TF) × Inverse Document Frequency (IDF)의 곱으로 계산됨.
   - 특정 문서에서 자주 등장하지만, 전체 문서에는 드물게 나타나는 단어의 중요도를 높게 평가함.
*/


/*-----------------------------------------------------------
 1️⃣ TF (Term Frequency, 단어 빈도)
-----------------------------------------------------------*/
/*
 - 한 문서 내에서 특정 단어가 얼마나 자주 등장하는지를 나타냄.
 - 계산식: TF(t, d) = (단어 t가 문서 d에서 등장한 횟수) / (문서 d의 전체 단어 수)
*/


/*-----------------------------------------------------------
 2️⃣ IDF (Inverse Document Frequency, 역문서 빈도)
-----------------------------------------------------------*/
/*
 - 전체 문서 중 특정 단어가 포함된 문서의 비율을 이용하여, 흔한 단어의 중요도를 낮춤.
 - 계산식: IDF(t) = log(전체 문서 수 / 단어 t가 포함된 문서 수)
*/


/*-----------------------------------------------------------
 3️⃣ TF-IDF 계산식
-----------------------------------------------------------*/
/*
 - TF-IDF(t, d) = TF(t, d) × IDF(t)
 - 예: ‘the’처럼 모든 문서에 등장하는 단어는 낮은 점수,
        특정 문서에만 자주 등장하는 단어는 높은 점수를 가짐.
*/


/*-----------------------------------------------------------
 4️⃣ TF-IDF의 활용
-----------------------------------------------------------*/
/*
 - 문서 분류(Text Classification)
 - 검색 시스템(Search Ranking)
 - 문서 클러스터링(Clustering)
 - 감성 분석(Sentiment Analysis)
*/


/*-----------------------------------------------------------
 5️⃣ 범주형 데이터 인코딩 비교
-----------------------------------------------------------*/
/*
 - TF-IDF : 텍스트 데이터에서 단어의 중요도 수치화
 - 원-핫 인코딩(One-Hot Encoding) : 범주형 데이터를 0/1로 변환 (빈도 고려 X)
*/


/*-----------------------------------------------------------
 6️⃣ 파이썬 구현 예시
-----------------------------------------------------------*/
# Python 예시 코드

from sklearn.feature_extraction.text import TfidfVectorizer

# 예시 문서 리스트
docs = [
    "I love data analysis",
    "Data analysis is essential for AI research",
    "AI and data science are connected"
]

# TF-IDF 벡터화
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(docs)

# 행렬을 배열로 변환
tfidf_array = tfidf_matrix.toarray()

# 단어(feature) 추출
feature_names = vectorizer.get_feature_names_out()

# TF-IDF 행렬을 데이터프레임 형태로 변환
import pandas as pd
tfidf_df = pd.DataFrame(tfidf_array, columns=feature_names)

# 결과 확인
print(tfidf_df)


/*-----------------------------------------------------------
 7️⃣ SAS에서의 TF-IDF 활용
-----------------------------------------------------------*/
/*
 - SAS에서는 Text Mining 전용 모듈을 통해 TF-IDF 계산을 지원함.
 - 대표 모듈:
     1) SAS Text Miner
     2) SAS Enterprise Miner
 - ‘Text Parsing’, ‘Text Filter’, ‘Text Topic’ 노드를 사용하여 
   TF, IDF, TF-IDF 값 자동 계산 가능.
*/