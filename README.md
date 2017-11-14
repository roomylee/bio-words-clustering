# Bio (Relational) Word Clustering
Bio 분야 논문(Abstract)에서 박테리아(Bacteria)와 질병(Disease) 간의 관계를 나타내는 단어들에 대한 Clustering 분석


## 171114 Memo
* Clustering project
	* word2vec 차원에 따른 성능 비교
	* clustering 결과에 frequency 정보 추가
* triplet visualization
	* BAC-REL-DIS 간의 edge만 나오도록 수정
	* vector 값도 실제 word2vec + PCA 값으로 수정
* (New) cnn for relation extraction
	* cnn을 이용한 관계추출 프로젝트 시작
	* 스켈레톤 코드


## 171027 Meeting
* 미팅내용
	* Clustering 분석은 나쁘지 않았다.
	* word2vec을 100차원으로 고정하는 게 아니고 여러 차원에 대해서 실험을 해보는 게 필요할 것.
	* BELMiner 논문을 읽고 계신데 참고하면 좋을 듯 하다.
	* 단어의 Frequency에 대한 분석도 괜찮을 것이다.
		* Frequency 기반 클러스터링한 다음, 클러스터 별로 벡터 기반 클러스터링하면 어떨지...
	* cyc 온톨로지에서 relation word를 검색해보고, words 간의 온톨로지 컨셉 노드에 대한 거리를 비교해보는 것도 괜찮을 것이다.
* 할일
	* word2vec을 여러 차원(100, 50, 30, ...)에 대해서 생성해보고 이에 대해서 클러스터링 성능 비교해보기
	* <del>Frequency 기반 클러스터링한 다음, 클러스터 별로 벡터 기반 클러스터링 해보기</del>
	* cyc 온톨로지에서 relation word를 검색해보기
	* words 간의 온톨로지 컨셉 노드에 대한 거리를 비교해보기


## 171018 Idea
* To do plan
	1. word embedding to large dimension,
	2. clustering and result checking
	3. what is the best k value for K-means algorithm?
	4. dimension reduction
	5. entity 3d visualization using plotly
	6. triplet network 3d visualization using plotly
* CNN for Relation Extraction
	* MNIST tutorial sucess! implement baseline structure.
	* RE project will be starting soon...


## 170927 Idea
* Relation Extraction Corpus
	* ACE: 17 relations (role, contain, location, family)
	* UMLS: 134 entity types, 54 relations
	* Freebase: nationality, contains, profession, place of birth, etc.
* **Distant Supervision이란, structured data에서 triplet(2-entity, 1-relation)을 추출하고, unstructured data에서 추출한 2-entities를 포함한 문장에 대하여 추출한 relation으로 labeling하여 training data를 생성하는 방법이다.**


## 170922 Meeting
* 미팅 내용
	* Clustering을 더 큰 차원에서 진행하고 그걸 다시 reduction해서 projection하면 Clustering 결과가 더 나아질 것이다.
	* K means에서 적절한 k 값을 찾는 알고리즘이 있으니 찾아보자.
	* embedding 결과에서 vector 간의 거리나 방향(각도)에 대한 수치를 활용하여 우리가 찾은 relation을 guarantee할 수 있을 것 같다.
* 할일
	* K-means에서 적절한 k값 찾기. silhouette?
	* plot된 벡터 포인트를 triplet 단위로 연결시켜 보기
	* 대진님한테 추가 코퍼스 받기
	* tpe랑 dependency 모델 검색 결과 비교하기
	* CNN으로 Relation Extraction


## 170901 Meeting
* 현재 태깅 데이터 300개에 대한 precision / recall은 양쪽(TPE, Dependency Tree) 모두 비슷함. (p=1.0, r=0.8)

* 대진님 측에서 test를 위한 추가 데이터를 태깅해줄 예정

* 나는 현재 뽑힌 relation words에 대한 클러스터링 실험을 진행할 것.
    * 클러스터링 idea 1
전체 코퍼스 학습 후 relation words를 plotting
    * 클러스터링 idea 2
BAC-DIS-Relation 형태로 학습.
단, 데이터가 부족하여 학습이 불가능
    * 기타 아이디어 생각해보기

* Extra Works
    * CNN을 통한 relation classification 예제 만들기
    * LSTM을 통한 relation classification 예제 만들기
    * stanford논문 reasoning, relation classification 관련 읽기



----------------------------

### 이전 미팅은 TPE Search에 대한 것이므로 생략