from flask import Flask,render_template
import test
import random
import mysql.connector

app = Flask(__name__)

config = {
'user':'aidencjswo',
'password':'1234',
'host':'121.131.135.84',
'port':'3306',
'database':'sample'
}
def connect_db_get_quiz():
    print("퀴즈 가져오기 실행되었음")

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
    print('ㅇ')
    connection = mysql.connector.connect(**config)
    query = "select cnt from sample.achievement_rate where seq1 = 'test';"
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result[0][0]
    


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/one')
def one():
    return render_template('one.html',quizs = connect_db_get_quiz())

@app.route('/two')
def two():
    return render_template('two.html',cnt = get_achivement())

@app.route('/three')
def three():
    return render_template('three.html')

if __name__ == '__main__':
    print('server start complete')
    app.run(port=5000)

