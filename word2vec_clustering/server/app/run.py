# -*- coding: utf-8 -*-

from flask import Flask, render_template

app = Flask(__name__)


def make_point_data(word_list, vec_list, inclinatation):
    point_data = '['
    for idx in range(len(vec_list)):
        if idx != 0:
            point_data += ","
        point_data += "{name:'%s',word:'%s',x:%s,y:%s,z:%s" \
                      % (inclinatation,word_list[idx][0], vec_list[idx][0][0], vec_list[idx][0][1], vec_list[idx][0][2])
        for rank in range(10):
            point_data += ",top%d:'%s'" % (rank, vec_list[idx][1][rank][0])
        point_data += '}'
    point_data += ']'

    return point_data


# 메인 페이지 라우팅
@app.route('/')
def main():

    # 통합 버전 html 파일로 실행
    return render_template('3d_plot.html')

# 실행
if __name__ == '__main__':
    app.run()
    #app.run(host="166.104.140.76", port=50000)
