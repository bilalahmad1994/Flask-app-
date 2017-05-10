from flask import Flask,request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


# @app.route('/name')
# def name():
#     return 'my name is sami'


# @app.route('/method',methods=['GET','POST'])
# def method():
#     if request.method=='POST':
#         return 'You are using Post'
#     else:
#         return 'You are using Get'



# @app.route('/method')
# def methodname():
#     return 'you are using %s'%request.method



# @app.route('/name/<username>')
# def user(username):
#     return '<h1>great<h1>%s'%username



if __name__ == '__main__':
    app.run()