from flask import Flask
from flask import render_template  # 实现前后端分离
from flask import request
from baiduSpider import getBaiduMessage


app = Flask(__name__)

# 装饰器，给函数新增功能
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/s')
def search():
    # 获取用户输入的关键字
    keyWord = request.args.get('wd')
    pageNumber = request.args.get('pn')
    html = getBaiduMessage(keyWord,pageNumber)
    return html

@app.route('/python')
def index1():
    return 'hello python world'

# 这里的if判断是为了防止外部调用
if __name__ == '__main__':
    # 修改端口号 port
    app.run(debug=True,port = 8000)