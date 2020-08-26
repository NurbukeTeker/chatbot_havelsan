from flask import Flask, render_template, request, jsonify
import re
import finiteState as fs

app = Flask(__name__, static_url_path="/static")


@app.route('/message', methods = ['POST'])
def reply():
    global refresh
    question = request.form["msg"]      
    answer = fs.getAnswer(question)    
    print("answer: ", answer)
    return jsonify( { 'text': answer, 'reload' : False }) 
     

@app.route('/postmethod', methods = ['POST']) 
def post_javascript_data():       
   return ''
    
global refresh
refresh = False


@app.route("/")
def index():
    global refresh
    refresh = True
    answer = fs.getAnswer("refresh")
    return render_template("index.html")

if (__name__ == "__main__"):         
    app.run(host="localhost", port = 5000)

