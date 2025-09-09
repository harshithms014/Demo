from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Multi-Stage Docker Build!Created by harshithms014 ths to check and deploy using kubernetes   "

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5006)
