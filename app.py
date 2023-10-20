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
        if not request.args.get("Body"):
            return "No input provided"
        
        message = {
            "From" : "Web",
            "Body" : request.args.get("Body"),
            "To"   : "Web"
        }
    elif request.method == "POST":
        message = {
            "From" : request.form.get("From"),
            "Body" : request.form.get("Body"),
            "To"   : request.form.get("To")
        }

    action = ChatEngine.parse(message["Body"])
    output = ChatEngine.execute(action)

    if "whatsapp" in message["From"] and "whatsapp" in message["To"]:
        wm = WhatsappMessage(
            src  = message["To"],
            body = output,
            dest = message["From"]
        )
        output = wm.respond()
    # print(wm)
    # print(output)
    return output

@app.route("/errors", methods = ["GET", "POST"])
def errors():
    print(request)
    return ""
