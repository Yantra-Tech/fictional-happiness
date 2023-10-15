from flask import Flask, request, render_template
from whatsapp import WhatsappMessage
from emoji import demojize

from chatengine import ChatEngine

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def index():
    return render_template("index.html")

@app.route("/chatbot", methods = ['GET', 'POST'])
def chatbot():
    if request.method == "GET":
        message = {
            "From" : "Web",
            "Body" : request.args.get("action"),
            "To"   : "Web"
        }
    elif request.method == "POST":
        message = {
            "From" : request.form.get("From"),
            "Body" : demojize(request.form.get("Body")),
            "To"   : request.form.get("To")
        }

        action = ChatEngine.parse(message["Body"])
        output = ChatEngine.execute(action)

        wm = WhatsappMessage(
            src  = message["To"],
            body = output,
            dest = message["From"]
        )
        wm.send()
    
    print(message)

    return "Hello World"
