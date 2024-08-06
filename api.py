from flask import Flask, request, jsonify
# from flask_cors import CORS, cross_origin
# from logging.config import dictConfig

import app.services
from app.services import *

# dictConfig({
#     'version': 1,
#     'formatters': {'default': {
#         'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
#     }},
#     'handlers': {'wsgi': {
#         'class': 'logging.StreamHandler',
#         'stream': 'ext://flask.logging.wsgi_errors_stream',
#         'formatter': 'default'
#     }},
#     'root': {
#         'level': 'INFO',
#         'handlers': ['wsgi']
#     }
# })


app = Flask(__name__)
# app.config['CORS_HEADERS'] = 'Content-Type'
# cors = CORS(app, resources={r"/parse": {"origins": "http://localhost:port"}})

services = Services()


@app.route('/')
def doc() -> str:
    # app.logger.info("doc - Got request")
    # return "Hello there"
    with open("app/doc.html", "r") as f:
        return f.read()



@app.route("/translate", methods=["GET"])
def translate_word():
    data = request.get_json()
    services.show_dev_trans(data.get('word'))
    # app.logger.info("/generate - Generated words.")
    return jsonify({"msg": "success"})


@app.route("/display", methods=["POST"])
# @cross_origin(origin='localhost', headers=['Content-Type', 'Authorization'])
def display_story():

    data = request.get_json()
    # app.logger.info(f"/parse - Got request: {data}")
    doc = services.show_doc(data.get('document'))
    # app.logger.info(f"/parse - Output: {doc}")
    return doc
    #return jsonify(doc)


@app.route("/segment", methods=["POST"])
# @cross_origin(origin='localhost', headers=['Content-Type', 'Authorization'])
def segment_word():
    data = request.get_json()
    # app.logger.info(f"/segment - Got request: {data}")
    segments = services.document(data.get ('document'))
    app.logger.info(f"/segment - Output: {segments}")

    return jsonify(segments)


@app.route("/storyA", methods=["GET"])
# @cross_origin(origin='localhost', headers=['Content-Type', 'Authorization'])
def just_storyA() -> str:
    # data = request.form['letter']    # app.logger.info(f"/parse - Got request: {data}")
    # doc = services.show_doc(data)
    # return doc.text
    # #return jsonify(doc)
    return services.show_doc("A")

@app.route("/storyB", methods=["GET"])
# @cross_origin(origin='localhost', headers=['Content-Type', 'Authorization'])
def just_storyB() -> str:
    return services.show_doc("B").text


@app.route("/storyC", methods=["GET"])
# @cross_origin(origin='localhost', headers=['Content-Type', 'Authorization'])
def just_storyC() -> str:
    return services.show_doc("C").text



if __name__ == "__main__":
    app.run(host='0.0.0.0')