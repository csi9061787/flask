from flask import Flask

app = Flask(__name__, static_folder='./static', static_url_path='/static')  #定一個路徑跟網址給它
# app = Flask(__name__)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)