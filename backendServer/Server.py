from flask import Flask, request, jsonify
from flask_cors import CORS
from fileSystem import *
import json

import uuid

app = Flask(__name__)
CORS(app, supports_credentials=True)


# 只接受POST方法访问

@app.route("/login", methods=["POST"])
def login():
    global adminAccount
    result = {'status': 8000, 'data': '服务器响应失败'}  # 默认返回内容
    if request.get_data() is None:  # 判断传入的json数据是否为空
        result = {'status': 5004, 'data': '请求参数为空'}
        return jsonify(result)

    # 获取传入的参数
    get_Data = json.loads(request.get_data())
    # 获取参数信息
    userName = str(get_Data.get('username'))
    passWord = str(get_Data.get('password'))

    if userName not in adminAccount:
        result = {'status': 8001, 'data': '不存在此用户!'}
        return jsonify(result)
    elif userName in adminAccount and adminAccount[userName]['password'] == passWord:  # 管理员登录
        localTempItem = str(uuid.uuid1())
        adminAccount[userName]['token'] = localTempItem
        return jsonify({'status': 200, 'data': '登陆成功', 'token': localTempItem})
    elif adminAccount[userName]['password'] != passWord:
        result = {'status': 8002, 'data': '密码错误!'}
        return jsonify(result)

    return jsonify(result)


@app.route("/checkToken", methods=["POST"])
def checkToken():
    global adminAccount
    result = {'status': 8000, 'data': '服务器响应失败'}  # 默认返回内容
    if request.get_data() is None:  # 判断传入的json数据是否为空
        result = {'status': 5004, 'data': '请求参数为空'}
        return jsonify(result)
    get_Data = json.loads(request.get_data())

    userName = str(get_Data.get('username'))
    token = str(get_Data.get('token'))

    if token == adminAccount[userName]['token']:
        result = {'return_code': 200}
    else:
        result = {'return_code': 404}
    return json.dumps(result, ensure_ascii=False)


@app.route("/commitData", methods=["POST"])
def commitData():
    global adminAccount
    result = {'status': 8000, 'data': '服务器响应失败'}  # 默认返回内容
    if request.get_data() is None:  # 判断传入的json数据是否为空
        result = {'status': 5004, 'data': '请求参数为空'}
        return jsonify(result)
    get_Data = json.loads(request.get_data())

    localMode = str(get_Data.get('mode'))
    data = dict(get_Data.get('data'))
    newFile(localMode, data)
    print('写入完成')
    result = {'status': 200}
    return jsonify(result)


@app.route("/getData", methods=["POST"])
def getData():
    global adminAccount
    result = {'status': 8000, 'data': '服务器响应失败'}  # 默认返回内容
    if request.get_data() is None:  # 判断传入的json数据是否为空
        result = {'status': 5004, 'data': '请求参数为空'}
        return jsonify(result)
    get_Data = json.loads(request.get_data())

    localMode = str(get_Data.get('mode'))
    localData = readFile(localMode)
    print('读取完成')
    result = {'status': 200, 'data':localData}
    return jsonify(result)


if __name__ == "__main__":
    print(' * Server服务开启……')
    adminAccount = {'admin': {'password': '123456', 'token': ''}}
    app.run(host='127.0.0.1', port=5000, debug=False)
