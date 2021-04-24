from flask import Flask

app = Flask(__name__)
#讓使用者可以來訪問我這個接口
@app.route('/')
def helloFlask():
    return 'Hello Flask!'

#宣告一個函數是任何使用者名稱都能輸入/Hello/name
@app.route('/Hello/<username>')
def hello(username):            #定義一個函數，只要使用者請求相應的網址，就執行該函數
    return 'Hello {}'.format(username)

#宣告一個函數是輸入/add/數字/數字,回傳先以數字計算後再轉成字串,因為回傳值必須是字串
@app.route('/add/<x>/<y>')
def add(x, y):
    return str(int(x) + int(y))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)