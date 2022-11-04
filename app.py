from flask import Flask, request
from deepface import DeepFace

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def hello():
    result = {'code': 200, 'msg': 'hello', 'data': None}
    return result


@app.route("/face_verify", methods=['POST', 'GET'])
def face_verify():
    try:
        if request.method == 'POST':
            verify = DeepFace.verify(request.form['img1'], request.form['img2'], 'VGG-Face', 'cosine', None, False,
                                     'opencv', True, False, 'base')
        else:
            verify = DeepFace.verify("1.jpg", "2.jpg", 'VGG-Face', 'cosine', None, False, 'opencv', True, False, 'base')
        result = {'code': 200, 'msg': '识别结果', 'data': verify}
    except Exception as e:
        result = {'code': 500, 'msg': '识别服务异常错误', 'data': str(e)}
    return result
