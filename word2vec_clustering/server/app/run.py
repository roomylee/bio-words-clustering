# -*- coding: utf-8 -*-

from flask import Flask, render_template
from word2vec_module import *

app = Flask(__name__)


def jsonify(module, key_word):
    vector_list = list()
    for word in key_word:
        try:
            vector_list.append((word, module.model[word], module.model.most_similar(word)))
        except:
            print("'"+word+"' is not in the dictionary")
            # print(word, module.model[word], module.model.most_similar(word))
            vector_list.append(('error', [0, 0, 0], [('error', 0), ('error', 0), ('error', 0), ('error', 0), ('error', 0)
                                                , ('error', 0), ('error', 0), ('error', 0), ('error', 0), ('error', 0)]))

    json_data = '['
    for idx in range(len(vector_list)):
        if idx != 0:
            json_data += ","
        json_data += "{word:`%s`, x:%s, y:%s, z:%s" \
                      % (vector_list[idx][0], vector_list[idx][1][0], vector_list[idx][1][1], vector_list[idx][1][2])
        for rank in range(10):
            json_data += ",top%d:`%s`" % (rank, vector_list[idx][2][rank][0])
        json_data += '}'
    json_data += ']'

    return json_data


def vectorize(corpus_type='full'):
    module = word2vec_module(corpus_type)

    bacteria, disease, relation = module.get_key_word()

    print('Bacteria Size :', len(bacteria))
    print('Disease Size :', len(disease))
    print('Relation Size :', len(relation))

    bacteria_vec = jsonify(module, bacteria)
    disease_vec = jsonify(module, disease)
    relation_vec = jsonify(module, relation)

    return bacteria_vec, disease_vec, relation_vec


# 메인 페이지 라우팅
@app.route('/')
def main():
    bacteria_vector, disease_vector, relation_vector = vectorize()
    return render_template('3d_plot.html', bac = bacteria_vector, dis = disease_vector, rel = relation_vector)

# 메인 페이지 라우팅
@app.route('/relation')
def relation():
    bacteria_vector, disease_vector, relation_vector = vectorize('relation')
    return render_template('3d_plot.html', bac = bacteria_vector, dis = disease_vector, rel = relation_vector)

# 메인 페이지 라우팅
@app.route('/triplet')
def triplet():
    bacteria_vector, disease_vector, relation_vector = vectorize('triplet')
    return render_template('3d_plot.html', bac = bacteria_vector, dis = disease_vector, rel = relation_vector)

# 실행
if __name__ == '__main__':
    app.run()
    #app.run(host="166.104.140.76", port=50000)
