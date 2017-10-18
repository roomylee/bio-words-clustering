# Relation Extraction in Bio Corpus
Bio 분야 논문(Abstract)에서 박테리아(Bacteria)와 질병(Disease) 간의 관계를 Deep Learning을 통해 추출해보자!

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


## 170825 Meeting
- Requirement
패턴 추가 생성을 통한 성능 향상
precision / recall을 통한 수치적 성능 보여주기

- Extra 1
	1. 관계 추출 후, 관계에 대한 클러스터링
	그래서 관계어를 보고 한 번 더 클러스터링
	그러면 cause-effect 등의 관계 클래스를 추려낼 수 있음.
	2. 1번에 이어서, 해당 관계 클래스와 다른 논문에서 사용하는 일반적인 관계 클래스간의 비교를 통해 도메인 디펜던트한 클래스를 추리고 최종 클래스를 정의함.
	아래와 같은 느낌으로 관계 클래스를 정의함. Examples는 관계 클래스에 포함되는 실제 문장에서의 관계어이다. (Ex. He married to her -> class: Affiliations)
	![image](/README_image/170825_relation_example.png)
	3. 정의한 클래스를 통해 모델을 학습시킨다.

- Extra 2
	1. Extra 1에서 후반부 단계에서 사용할 학습 모델 및 알고리즘, 라이브러리 사용법 등을 미리 익힐 수 있는 예제를 만들어본다.
	2. 리서치를 통해 텐서플로우 등 딥러닝 모델을 찾아서 구현하고 성능을 뽑아본다.


## 170810 Meeting
* 300개 데이터 검증하기 -> 노미나 교수님 연구실에서 검증해줄 예정
* 패턴을 좀 더 러프하게 만들 것
* 지금은 패턴의 precision이 100에 가까움
* 지금은 precision을 100에 맞추고 최대한 recall을 올리려고 했는데 precision이 좀 딸려도 괜찮을듯 함

## 170719 Meeting
* 서로 사용하고 있는 데이터 셋 공유하기
* 데이터 셋에 반드시 포함 되어야 하는 것은 ‘sentence'와 ‘relation여부’
* relation은 파싱 결과인 트리의 구조에 기반하여 결정되는 것이 아니라,
문장의 의미적으로 BAC과 DIS 간의 관계를 나타내는지 여부로 결정된다.
* 따라서 relation은 동사, 명사 등 모두 가능하며 이들의 결합된 형태도 가능하다.
* 성능 평가의 기준은 relation을 포함한 문장인지와 정확한 relation인지이다.
* 정확한 relation인지에 대한 평가는 정성적이다.
즉, 복수 정답을 허용하는 셈이다. pathogen, pathogen that cause, cause 모두 답으로 볼 수 있다.

* 다음 미팅까지 할 것
	1. relation 포함 여부를 다시 체크한다.(test 용)
	2. 패턴 역시 새로운 relation 기준에 따라 추가 생성한다.
	3. 추출된 문장에 대해서 잘 추출하였는지 평가한다.


## 170522 Meeting
* 트리 패턴을 많이 만들자.
	* 타이트한 패턴을 여러개 만드는 방향으로 진행.
	* 추출한 문장에서 Relation Sentence를 뽑아내자.
	* 꼭 동사가 관계는 아니고 pathogen 같은 명사도 둘 간의 관계를 나타낼 수 있으니 이 또한 고려하여 패턴 개발.

어느정도 찾아지면 대진님 dependency트리랑 비교.

나중에는, 패턴을 러닝을 통해서 만들어낼 수 있게.

TPE 알고리즘을 잘 까서 이해하면 쉽다는 교수님 의견, 역으로 알고리즘을 적용하면 된다는 직관이 있다고 하심.

딥러닝을 하더라도 학습데이터가 필요하니 일단 TPE로 만들어보자. 또한 단순한 관계 + 구체적으로 어떤 관계인지까지 찾을 수 있게.


* Extra Work
	* 딥러닝을 통한 관계 추출에 대해서 공부하자.
	* 딥러닝을 통해 TPE 생성하는 것도 고려하면서.


## 170508 Meeting
* 모든 박테리아 & 질병 조합에 대한 관계를 뽑아낼 때, 쿼리로 모든 조합을 넣는게 아니라 프리픽스인 BAC.+에 대해서 쿼리를 넣는 식으로
* 그리고 나중에 웹으로 매번 쿼리를 던지는 상황에서는 프리픽스 검색으로 한 번 걸러진 것들 중에서 검색하면 빨라질 것이다.


## 170417 Meeting
* 노미나 교수님 랩 담당 - 고대진 님
	* 디펜던시 트리에 대해서 키워드 기반 관계 정보 추출
	* 여러 문장의 디펜던시 트리에 대해서 공통된 노드를 하나로 묶어 큰 트리 생성해봐도 괜찮을 것 같다.

* 우리 랩
	* tpe 기반 정보 검색
	* predicate을 통해서 (술어) (명사) (명사) 이런 식으로 관계에 대한 정보를 검색 가능
	* 로직은 tell you ? 라는 쿼리일 때,
	* 이를 여러가지 tpe 쿼리 { <you.~~~> } 뭔가 이런 느낌으로 바꿔야 하는데
	* 이는 수동으로 패턴을 만들어야 함. (1~5형식 문장에 맞춘다든지)
	* 이를 자동으로 만들 수는 없을까?
	* 수동으로라도 bio 도메인 한정이기에 잘 맞는 패턴을 만들어보자.


고대진님 디펜던시 트리를 이용한 방법이랑 우리 꺼랑 성능을 비교해보자
	
	
* 공부해볼 것들
	1. relation extraction, with deep learning
	2. dependency tree
	3. Neural Net Parser tree