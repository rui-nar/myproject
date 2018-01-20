"""Module to manage interface with the users database"""
from flask import Blueprint
from flask import jsonify
#from flask import request

from models.user import Person

USER = Person.objects.create(first_name="Rui")
USER.save()


USER_INTERFACE = Blueprint('USER_INTERFACE', __name__, template_folder='templates')

@USER_INTERFACE.route('/userdb/user', methods=['GET'])
def get_all_users():
    """Return all users"""
    return jsonify({'names': Person.objects.values_list('first_name', flat=True)})

''' @userInterface.route('/userdb/user/<userId>',methods=['GET'])
def getEmp(userId):
    usr = [ user for user in userDB if (user['id'] == userId) ] 
    return jsonify({'user':usr})

@userInterface.route('/userdb/user/<userId>',methods=['PUT'])
def updateEmp(userId):
    em = [ user for user in userDB if (user['id'] == userId) ]
    if 'name' in request.json : 
        em[0]['name'] = request.json['name']
    if 'title' in request.json:
        em[0]['title'] = request.json['title']
    return jsonify({'user':em[0]})

@userInterface.route('/userdb/user',methods=['POST'])
def createEmp():
    dat = {
    'id':request.json['id'],
    'name':request.json['name'],
    'title':request.json['title']
    }
    userDB.append(dat)
    return jsonify(dat)

@userInterface.route('/userdb/user/<userId>',methods=['DELETE'])
def deleteEmp(userId):
    em = [ user for user in userDB if (user['id'] == userId) ]
    if len(em) == 0:
        abort(404)
    userDB.remove(em[0])
    return jsonify({'response':'Success'}) '''