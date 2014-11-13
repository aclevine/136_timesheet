__author__ = 'csullivan'

from flask.ext import restful
from flask import jsonify
from flask.ext.restful import reqparse
from flask_restful.utils import cors
from gopher.models import *
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound

class StateClubs(restful.Resource):

    @cors.crossdomain(origin='*')
    def get(self, state_id):

        state = DBSession.query(State).filter(State.id == state_id).one()

        clubs = [club.to_dict() for club in state.clubs]
        
        return jsonify(clubs=clubs)
