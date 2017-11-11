import mysql.connector as msc
import db_config
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer


config = db_config.connection_info

conn = msc.connect(**config)
qry = conn.cursor(buffered=True)


def get_triplet():
    query = "SELECT Subject, Object, Relation FROM relation"

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

    return bacteria_list, disease_list, relation_list

def get_corpus(corpus_type='full'):
    corpus_dic = {
            # Full Corpus
            'full': "SELECT sentence FROM sentence",
            # Relation-Contained Corpus
            'relation': 'SELECT SENTENCE_STRING FROM result',
            # Entity-Relation Triplets
            'triplet': 'SELECT Subject, Object, Relation FROM relation'
    }
    corpus = []
    lemmatizer = WordNetLemmatizer()

    query = corpus_dic[corpus_type]
    qry.execute(query)
    row = qry.fetchone()
    while row is not None:
        try:
            corpus.append([lemmatizer.lemmatize(w, 'v') for w in word_tokenize(' '.join(row))])
        except Exception as e:
            print(e)
            continue
        row = qry.fetchone()

    return corpus

if __name__ == "__main__":
    # get_triplet() test
    bac, dis, rel = get_triplet()
    print("Bacteria :", bac[:5])
    print("Disease :", bac[:5])
    print("Relation :", bac[:5])

    # get_corpus() test
    corpus = get_corpus()
    print(corpus[0])
