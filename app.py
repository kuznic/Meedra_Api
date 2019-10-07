from flask import  jsonify, request, Response, json
from functools import wraps
from settings import *
from AOM_MODELS import AOM_procedures as SP,AOM_tables as T
from flask_restplus import Resource, Api, fields, reqparse

#creates an instance of the Api class from the flask_restplus extension
api = Api(app,vRecursion='1.0', title='This Is WEMA AOM Swagger Documentations', 
          description='WEMA AOM')



#this returns information about all the terminals existing in the AOM database
@api.route('/terminals', endpoint='terminals') #this is a route decorator
@api.doc(params={})
class Get_Terminals(Resource):
    def get(self):
        return jsonify({'Terminals':T.AOM_TABLES.get_all_terminals()})



#this returns information about a specific terminal as identified by the supplied terminal_id
@api.route('/terminals/<string:terminal_id>')
@api.doc(params={'terminal_id': 'This is a unique alpha-numeric identification number for each terminal'})
class Get_Terminal_By_Terminal_Id(Resource):
    def get(self,terminal_id):
        try:
            return_value = T.AOM_TABLES.get_terminal(terminal_id)
            return jsonify(return_value)
        except AttributeError as error:
            return jsonify({'Terminal':str(terminal_id) + ' deos not exist'})


#returns terminal health history for a specific durartion
@api.route('/terminals/<string:terminal_id>/<string:from_time>/<string:to_time>',methods=['GET'])
class Get_Terminal_Health_Summary(Resource):
    def get(self,terminal_id,from_time,to_time):
        return_value = SP.AOM_PROCEDURES.get_terminal_summary(terminal_id,from_time,to_time)
        return jsonify([dict(row) for row in return_value])


#gets terminal support events
@api.route('/terminal/events/<string:terminal_id>',methods=['GET'])
class Get_Terminal_Events(Resource):
    def get(self,terminal_id):
        return_value = SP.AOM_PROCEDURES.get_terminal_support_events(terminal_id)
        return jsonify([dict(row) for row in return_value])

if __name__ == '__main__':
    app.run(port=4326)


