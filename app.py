from flask import Flask, request
app = Flask(__name__)

@app.route("/chatbot", methods = ['GET', 'POST'])
def index():
    if request.method == "GET":
        action = request.args.get("action")
        if action == "convert":
            print("Calling Unitconverter")
        else:
            print("Calling some other function")
            

    return "Hello World"
