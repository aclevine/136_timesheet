__author__ = 'csullivan'

from flask.ext import restful
from flask import jsonify
from flask.ext.restful import reqparse
from flask_restful.utils import cors
from gopher.models import *
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound

class States(restful.Resource):

    @cors.crossdomain(origin='*')
    def get(self):

        states = DBSession.query(State).all()
        states = [state.to_dict() for state in states]

        return jsonify(states=states)
