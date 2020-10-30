from flask import Flask, render_template
from flask_cors import CORS
import requests
import json

app = Flask(__name__, static_folder='../frontend/dist/static', template_folder='../frontend/dist')
CORS(app)

# トップ画面
@app.route('/')
def index():
    return render_template('index.html')

# 機械状態取得API
@app.route("/api/rest/get/operationStatus/")
def get_machine_status():
    # 機械状態取得APIコール
    responce = requests.get(
        'http://localhost:8083/field_api/v3/class/status/instance/status00007/latest')
    jsonData = json.loads(responce.text)
    resData = jsonData['controller_status_number']
    return json.dumps(resData)

@app.route("/api/rest/get/test/")
def test():
    return "ok"

if __name__ == '__main__':
    app.run()
