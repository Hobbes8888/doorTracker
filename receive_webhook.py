from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        html = f"<h1>Deployed with Zeet!!</h1>"
        print(request.json)
    return html, request.json




if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000)