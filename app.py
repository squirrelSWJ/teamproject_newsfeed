from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient
import random

client = MongoClient('mongodb+srv://test:alskdjfh@cluster0.geumrbf.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta


# 전체 메인 페이지
@app.route('/')
def home():
    return render_template('index.html')

# LEE 개인페이지
@app.route('/lee')
def lee():
    return render_template('lee.html')


# 민수님 개인페이지
@app.route('/minsoo')
def minsoo():
    return render_template('minsoo.html')


# 정훈님 개인페이지
@app.route('/pyo')
def pyo():
    return render_template('pyo.html')


# 성훈님 개인페이지
@app.route('/sung')
def sung():
    return render_template('sung.html')


# 택환님 개인페이지
@app.route('/kimtk')
def tk():
    return render_template('tk.html')


# ----성욱님---
#방명록 기록하기 버튼 클릭시 데이터 받고 db에 입력하는 함수
@app.route("/team4", methods=["POST"])
def team4_post():
    name_receive = request.form['name_give']
    star_receive = request.form['star_give']
    comment_receive = request.form['comment_give']
    randomNum_receive = request.form['randomNum_give']

    count = list(db.teams.find({}, {'_id': False}))
    num = len(count) + 1

    doc = {
        'name':name_receive,
        'star':star_receive,
        'comment':comment_receive,
        'num':num,
        'randomNum':randomNum_receive
    }
    db.teams.insert_one(doc)

    return jsonify({'msg':'기록완료!'})

#방명록 삭제 버튼 클릭시 데이터 받고 db삭제 하는 함수
@app.route("/team4/delete", methods=["POST"])
def team4_delete_post():
    num_receive = request.form['num_give']
    db.teams.delete_one({'num': int(num_receive)})  #선택한num의 db열 삭제

    count = list(db.teams.find({}, {'_id': False})) #db 총 열의 개수 카운트
    num = len(count) + 1

    db.teams.update_one({'num': num}, {'$set': {'num': int(num_receive)}}) #마지막 열에 있는num을 삭제한 num으로 수정

    return jsonify({'msg': '삭제완료!'})

#클라이언트로 데이터 GET 하는 함수
@app.route("/team4", methods=["GET"])
def team4_get():
    teams_list = list(db.teams.find({},{'_id':False}))
    return jsonify({'teams':teams_list})


# -----성욱님 끝---------


# 정훈님---------------
@app.route("/team1/delete", methods=["POST"])
def x():
    x = request.form['del_give']
    db.team1.delete_one({'comment': x})
    return jsonify({'msg': '삭제완료'})


@app.route("/team1", methods=["POST"])
def team1_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {
        'name': name_receive,
        'comment': comment_receive,

    }
    db.team1.insert_one(doc)
    return jsonify({'msg': '댓글 완료~!'})


@app.route("/team1", methods=["GET"])
def team1_get():
    team1_list = list(db.team1.find({}, {'_id': False}))
    # ?
    return jsonify({'team1': team1_list})


# 정훈님끝---------------

# 재관님 ---
@app.route("/lee1", methods=["GET"])
def lee_get():
    all = list(db.lee.find({}, {'_id': False}))
    return jsonify({'lee': all})


# 입력기능
@app.route("/lee1", methods=["POST"])
def bucket_post():
    lee_receive = request.form['lee_give']
    name_receive = request.form['name_give']
    all = list(db.lee.find({}, {'_id': False}))
    count = len(all) + 1;
    doc = {
        'num': count,
        'lee': lee_receive,
        'done': 0,
        'name': name_receive
    }
    db.lee.insert_one(doc)
    return jsonify({'msg': '등록 완료'})


# 삭제 기능
@app.route("/lee1/delete", methods=["POST"])
def delete_bucket():
    del_num = request.form['num_give']

    db.lee.delete_one({'num': int(del_num)})

    return jsonify({'msg': '삭제 완료'})


# ---재관님 끝

# ---민수님
# 개인 소개 페이지에서 방명록 입력 시 insert 하는 구문.
@app.route("/minsoo/insert", methods=["POST"])
def intro_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    count = random.uniform(1, 1000)

    doc = {
        'num': count,
        'name': name_receive,
        'comment': comment_receive
    }

    db.minsoo.insert_one(doc);
    return jsonify({'msg': 'POST 연결 완료!'})


# 개인 소개 페이지에서 방명록 삭제 버튼 클릭 시 삭제 요청을 처리하는 구문.
@app.route("/minsoo/delete", methods=["POST"])
def intro_delete():
    count_receive = request.form['num_give']
    db.minsoo.delete_one({'num': float(count_receive)})

    return jsonify({'msg': '방명록 삭제 완료'})


# 방명록 수정 요청을 처리하는 라우트. 완성본 기준으로는 사용되지 않을 예정.
@app.route("/minsoo/update", methods=["POST"])
def intro_update():
    num_receive = request.form['num_give']
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    print('11111');
    db.minsoo.update_one({'num': float(num_receive)}, {'$set': {'name': name_receive, 'comment': comment_receive}})

    return jsonify({'msg': '방명록 수정 완료'})


# 개인 소개 페이지로 넘어갈 때 get 요청으로 방명록 list 를 제공.
@app.route("/minsoo/getList", methods=["GET"])
def intro_get():
    visitors_list = list(db.minsoo.find({}, {'_id': False}))

    return jsonify({'msg': 'GET 연결 완료!', 'result': visitors_list})


# ---민수님 끝

# ---택환님
@app.route("/tkmark", methods=["POST"])
def tkmark_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    tkmark_list = list(db.tkmark.find({}, {'_id': False}))
    count = len(tkmark_list) + 1

    doc = {
        'num': count,
        'name': name_receive,
        'comment': comment_receive
    }
    db.tkmark.insert_one(doc)
    return jsonify({'msg': '방명록이 등록되었습니다:)'})


@app.route("/tkmark", methods=["GET"])
def tkmark_get():
    comment_list = list(db.tkmark.find({}, {'_id': False}))

    return jsonify({'comments': comment_list})


@app.route("/tkmark/delete", methods=["POST"])
def tkdel():
    del_num = request.form['num_give']
    db.tkmark.delete_one({'num': int(del_num)})
    return jsonify({'msg': '방명록이 삭제되었습니다.'})


# --- 택환님 끝


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

