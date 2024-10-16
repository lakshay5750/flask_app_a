from flask import Flask
from flask import request


app=Flask(__name__)

@app.route('/')
def test1():
    return "<h1>hello world!</h2>"
@app.route('/test')
def test2():
    return "<h1>hello world2</h2>"
@app.route('/fa')
def test3():
    return "<h1>hello world3</h2>"
@app.route('/lakshay')
def test4():
    a=5+6
    return "this is lakshay varshney...I am currently persuaing btech {}" .format(a)
@app.route('/test4')
def test5():
   data= request.args.get('x')
   return "this is input url {}" .format(data) 
if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True,port=8080)

