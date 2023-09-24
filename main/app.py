from flask import Flask,render_template
import test

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('test.html')
if __name__ == '__main__':
    print('server start complete')
    app.run(port=5000,host='0.0.0.0')