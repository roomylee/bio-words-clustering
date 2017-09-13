import gensim
import mysql.connector as msc
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer


class word2vec_module:
    # 파라미터의 코퍼스를 객관식처럼 한정적으로 선택할 수 있을까? 찾는중...
    def __init__(self, corpus_type='full'):
        try:
            print("Loading a pre-trained model...")
            self.model = gensim.models.Word2Vec.load('../../%s.model' % corpus_type)
            print("Load success!")
        except:
            print("Pre-trained model not exist!")
            print("Training a word2vec model...")
            self.train(corpus_type)
            self.model = gensim.models.Word2Vec.load('../../%s.model' % corpus_type)
            print("Training success!")

    def query_generator(self, corpus_type):
        return {
            # Full Corpus
            'full': "SELECT sentence FROM sentence",
            # Relation-Contained Corpus
            'relation': 'SELECT SENTENCE_STRING FROM result',
            # Entity-Relation Triplets
            'triplet': 'SELECT Subject, Object, Relation FROM relation'
        }.get(corpus_type, 'nothing')

    def train(self, corpus_type='full'):
        config = {'host': '***REMOVED***',
                      'port': '***REMOVED***',
                      'user': '***REMOVED***',
                      'password': '***REMOVED***',
                      'database': '***REMOVED***'}

        conn = msc.connect(**config)
        qry = conn.cursor(buffered=True)

        query = self.query_generator(corpus_type)

        qry.execute(query)
        row = qry.fetchone()


        lemmatizer = WordNetLemmatizer()

        train_docs = list()
        while row is not None:
            try:
                train_docs.append([lemmatizer.lemmatize(w, 'v') for w in word_tokenize(' '.join(row))])
            except Exception as e:
                print(e)
                continue
            row = qry.fetchone()

        print('Train Data Size :', len(train_docs))
        model = gensim.models.Word2Vec(train_docs, min_count=1, size=3)

        model.save('../../%s.model' % corpus_type)


    def get_key_word(self):
        config = {'host': '***REMOVED***',
                  'port': '***REMOVED***',
                  'user': '***REMOVED***',
                  'password': '***REMOVED***',
                  'database': '***REMOVED***'}

        conn = msc.connect(**config)
        qry = conn.cursor(buffered=True)

        query = 'SELECT Subject, Object, Relation FROM ***REMOVED***.relation'

        qry.execute(query)
        row = qry.fetchone()

        bacteria_list = list()
        disease_list = list()
        relation_list = list()
        while row is not None:
            try:
                bacteria_list.append(row[0])
                disease_list.append(row[1])
                relation_list.append(row[2])
            except Exception as e:
                print(e)
                continue
            row = qry.fetchone()

        return (bacteria_list, disease_list, relation_list)

if __name__ == '__main__':
    module = word2vec_module('full')
    module.get_key_word()
    # module = word2vec_module('relation')
    # module = word2vec_module('triplet')
