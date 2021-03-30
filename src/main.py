# インストールしたパッケージのインポート
from flask import Flask

# appという名前でFlaskのインスタンスを作成
app = Flask(__name__)

@app.route('/')
def hello_world():

    message = "Hello Flask"

    return message

if __name__ == '__main__':
    app.run(host='0.0.0.0')
