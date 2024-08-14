
from flask import Flask, request, jsonify
# from flask_cors import CORS, cross_origin
# from logging.config import dictConfig
from http import HTTPStatus

import app.services
from app.services import *


app = Flask(__name__)

services = Services()

stories = [ {
'id': 'A',
'title': 'First Day of School',
'text': 'स्कूल पहला दन...'
}, {
'id': 'B',
'title': 'My Friends',
'text': 'मेरे दोस्त...'
}, {
'id': 'C',
'title': 'The Mango Tree',
'text': 'आम का पेड़...'
}
]

@app.route('/stories', methods=['GET'])
def get_stories():
    return jsonify({'data': stories})

@app.route("/storyA", methods=["GET"])
def just_storyA() -> str:
    story_db = services.show_doc_db('A')
    return story_db

@app.route("/storyB", methods=["GET"])
def just_storyB() -> str:
    story_db = services.show_doc_db('B')
    return story_db

@app.route("/storyC", methods=["GET"])
def just_storyC() -> str:
    story_db = services.show_doc_db('C')
    return story_db

@app.route('/stories/<string:story_id>', methods=['GET'])
def get_story(story_id):
    story = services.show_doc_db(story_id)
    if story:
        return jsonify(story)
    return jsonify({'message': 'story not found'}), HTTPStatus.NOT_FOUND


# @app.route('/stories/<int:story_id>', methods=['GET'])
# def get_story(story_id):
#     story = next((story for story in stories if story['id'] == story_id), None)
#     if story:
#         return jsonify(story)
#     return jsonify({'message': 'story not found'}), HTTPStatus.NOT_FOUND


#Using HTML form:
@app.route('/')
def doc() -> str:
    with open("app/doc.html", "r", encoding="utf-8") as f:
        return f.read()


@app.route("/translate", methods=["POST"])
def translate_word():
    data = request.get_json()
    word_json = services.show_dev_trans(data.get('word')).data
    return word_json


@app.route("/display", methods=["POST"])
def display_story():
    data = request.get_json()
    story_json = services.show_doc_db(data.get('document'))
    return story_json


if __name__ == "__main__":
    app.run(host='0.0.0.0')
