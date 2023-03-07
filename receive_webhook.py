from flask import Flask, request, abort
import json

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    html = "<h1>Webhook Received</h1>"
    html += "<p>Request JSON:</p>"
    html += "<pre>" + json.dumps(request.json, indent=4) + "</pre>"
    return html




if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000)