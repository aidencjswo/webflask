from flask import Flask,render_template,jsonify,request,abort
import test
import random
import mysql.connector
import datetime
import time

app = Flask(__name__, static_folder='static')

config = {
'user':'aidencjswo',
'password':'1234',
'host':'121.131.135.84',
'port':'3306',
'database':'sample'
}
def connect_db_get_quiz():
    connection = mysql.connector.connect(**config)
    query = "select * from quiz"
    #커서 생성
    cursor = connection.cursor()
    #쿼리 실행
    cursor.execute(query)
    #테이블 조회
    result = cursor.fetchall()
    #랜덤번호 출력
    i = random.randint(0,len(result)-1)
    #랜덤 로우 출력
    connection.close()

    return result

def get_achivement():
    connection = mysql.connector.connect(**config)
    query = "select cnt from sample.achievement_rate where seq1 = 'test';"
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result[0][0]
    

def connect_db_get_number_game_score():
    connection = mysql.connector.connect(**config)
    query = "select n.score, case when n.player is null then '익명의 사나이' when replace(n.player,' ','') = '' then '익명의 사나이' else n.player end as player ,n.rownumber from(select @rownum := @rownum + 1 rownumber, n.* from sample.numgame n,(select @rownum := 0) rownum order by score) n where rownumber <= 5;"
    #커서 생성
    cursor = connection.cursor()
    #쿼리 실행
    cursor.execute(query)
    #테이블 조회
    result = cursor.fetchall()
    #랜덤번호 출력
    connection.close()

    temp_obj = {
        "score1":result[0][0],
        "player1":result[0][1],
        "score2":result[1][0],
        "player2":result[1][1],
        "score3":result[2][0],
        "player3":result[2][1],
        "score4":result[3][0],
        "player4":result[3][1],
        "score5":result[4][0],
        "player5":result[4][1]
    }

    return temp_obj

def insert_db_number_game_score(player,score):
    connection = mysql.connector.connect(**config)
    date = time.localtime()
    date_str = str(date.tm_year)+"/"+str(date.tm_mon)+"/"+str(date.tm_mday)
    data_to_insert = (score['score'],player,date_str)
    cursor = connection.cursor()
    query = "insert into sample.numgame (score,player,play_date) values (%s,%s,%s);"
    cursor.execute(query,data_to_insert)
    connection.commit()
    cursor.close()
    connection.close()
    
def select_db_get_achive_fruits():
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    query = "select f_name from sample.fruits;"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result
    
blocked_ips = ["167.94.138.125","43.129.39.176","205.210.31.68","46.101.88.175","128.14.237.9"]

@app.before_request
def block_ip():
    client_ip = request.remote_addr
    if client_ip in blocked_ips:
        # 차단된 IP 주소에서의 요청을 거부
        abort(403)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/one')
def one():
    return render_template('one.html',password_correct=False ,quizs = connect_db_get_quiz())

@app.route('/two')
def two():
    return render_template('two.html',cnt = get_achivement(), fruits = select_db_get_achive_fruits())

@app.route('/three')
def three():
    return render_template('three.html')

@app.route('/four')
def four():
    return render_template('four.html',score = connect_db_get_number_game_score())


@app.route('/number/update', methods=['POST'])
def number_update():
    best_score = connect_db_get_number_game_score()
    current_score = request.json  # JSON 형식의 요청 데이터를 가져옵니다.
    insert_db_number_game_score(current_score['player'],current_score)

    if float(current_score['score']) < float(best_score['score1']):
        # 요청 데이터에서 필요한 작업을 수행합니다.
        data = {"message":"신기록입니다!"}
        return jsonify(data)
    else:
        data = {"message":"다시 도전하세요!"}
        return jsonify(data)



if __name__ == '__main__':
    print('server start complete')
    app.run(port=5000,host='0.0.0.0')

