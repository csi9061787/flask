from flask import Flask, request

app = Flask(__name__)

@app.route('/hello_get')
def hello_get():
    username = request.args.get('username')  #?後的參數用args
    userage = request.args.get('userage')
    return '<h1>Hello {}, you are {} years old.</h1>'.format(username, userage)     #回傳要是html的字串

@app.route('/hello_post', methods=['GET','POST'])
def hello_post():  #action 使用的是相對路徑
    outStr ="""
    <form action="/hello_post" method="POST">         
        <input type="textbox" name="username">
        <button type="submit">SUBMIT</button>
    </form>
    """
    #如果形式是post的話,要去接收get的username,並回傳outStr加上一串字顯上在畫面
    if request.method == 'POST':
        username = request.form.get('username')  #表單接收參數用form
        outStr += """<div>Hello {}</div>""".format(username)
    return outStr

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)          #debug只能在python上使用,可以讓網頁不需關閉再重啟

