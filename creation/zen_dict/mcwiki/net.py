from flask import Flask
app = Flask(__name__)

""" 如何做到用户输入某类关键词进入词语界面，输入另一类关键词进入用户界面？ 整个网站的结构是什么样的？   """


@app.route('/')
def welcome():
    return "Welcome to use Online Zen Dict"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
