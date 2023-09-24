from flask import Flask,render_template
import test
import random
import mysql.connector

app = Flask(__name__)

def connect_db_get_quiz():
    print("퀴즈 가져오기 실행되었음")

    config = {
    'user':'aidencjswo',
    'password':'1234',
    'host':'121.131.135.84',
    'port':'3306',
    'database':'sample'
    }
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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/one')
def one():

    random_number = random.randint(1, 100)
    return render_template('one.html',quizs = connect_db_get_quiz())
if __name__ == '__main__':
    print('server start complete')
    app.run(port=5000)

