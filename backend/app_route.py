from database import db
from flask import Flask, redirect,request, Blueprint


rout_api = Blueprint('rout_api', __name__)

@rout_api.route('/createworkflow/<name>',methods = ['POST'])
def create_workflow(name):
	try:
  		return {'result': 'correct'}
	except:
  		return {'error_code': '500','message': 'internal error'}

@rout_api.route('/createstatus/<name>/<worklow_id>',methods = ['POST'])
def create_status(name, worklow_id):
	try:
  		return {'result': 'correct'}
	except:
  		return {'error_code': '500','message': 'internal error'}
  
@rout_api.route('/createimage/<name>/<status_id>',methods = ['POST'])
def create_image(name, status_id):
	try:
  		return {'result': 'correct'}
	except:
  		return {'code': '500','message': 'internal error'}

@rout_api.route('/changeimagestatus/<status_id>/<image_id>',methods = ['PUT'])
def change_image_status(status_id,image_id):
	try:
  		return {'result': 'correct'}
	except:
  		return {'code': '500','message': 'internal error'}

@rout_api.route('/listimageinsidestatus/<status_id>',methods = ['GET'])
def list_image_inside_status(status_id):
	try:
  		return {'result': 'correct'}
	except:
  		return {'code': '500','message': 'internal error'}

@rout_api.route('/listworkflowstatus/<worklow_id>',methods = ['GET'])
def list_workflow_status(worklow_id):
	try:
  		return {'result': 'correct'}
	except:
  		return {'code': '500','message': 'internal error'}

@rout_api.route('/deletestatus/<status_id>',methods = ['DELETE'])
def delete_status(status_id):
	try:
  		return {'result': 'correct'}
	except:
  		return {'code': '500','message': 'internal error'}

