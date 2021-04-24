from flask import Flask, render_template, request
import poker as p
import model

app = Flask(__name__)

@app.route('/hello')
def hello():
    username = request.args.get('username')
    return render_template('hello.html', username=username)     #第一個參數帶模板,第二個後帶模板裡面有的參數

@app.route('/hello_post', methods=['GET','POST'])
def hello_post():
    request_method = request.method         #需要先宣告兩個會用到的變數
    username = ''                           #因為是給使用者填寫的,先設定為空字串
    if request.method == 'POST':            #變數會在是POST的情況下才會設定進入
        username = request.form.get('username')
    return render_template('hello_post.html', request_method=request_method, username=username)

@app.route('/poker', methods=['GET', 'POST'])
def poker():
    request_method = request.method
    players = 0
    cards = dict()
    if request_method == 'POST':
        players = int(request.form.get('players'))
        cards = p.poker(players)
    return render_template('poker.html', request_method=request_method,
                                         cards=cards)

@app.route('/show_staff')
def hello_google():
    staff_data = model.getStaff()
    column = ['ID', 'Name', 'DeptId', 'Age', 'Gender', 'Salary']
    return render_template('show_staff.html', staff_data=staff_data,
                                              column=column)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)