from flask import Flask, request, jsonify
import series as s  # 套用其他function
import poker as p

app = Flask(__name__)


@app.route('/series')
def getSeries():
    n = int(request.args.get('n'))  # 接收使用者帶進來的參數
    output = s.Func(n)  # 把別的程式直接拿進來用
    return str(output)


@app.route('/poker')
def poker():
    n = int(request.args.get('n'))  # 接收使用者帶進來的參數
    outputDict = p.poker(n)
    return jsonify(outputDict)  # jsonify顯示出json的形式, (寫API傳給前端的人的話必須是json的形式,而不是html的形式)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
