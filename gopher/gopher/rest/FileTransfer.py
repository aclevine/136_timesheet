__author__ = 'csullivan'
import base64
from flask.ext import restful
from flask import jsonify
from flask import request
from flask.ext.restful import reqparse
from flask_restful.utils import cors
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
from application import logger

class FileTransfer(restful.Resource):

    # @cors.crossdomain(origin='*')
    def post(self):
        # print request
        # print request.files
        # print request.data
        # print request.form
        # print request.json
        data = request.data
        # data = base64.b64decode(request.form.get("data")[22:])
        with open("wav_file.wav", 'wb') as audio:
        	audio.write(data)
        return jsonify({"message": "received"})
