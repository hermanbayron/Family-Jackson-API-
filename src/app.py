"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person
# from models import db, Familiar

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def get_all_members():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()

    response_body = {
        "hello": "members obtenido",
        "family": members
    }
    return jsonify(response_body), 200

@app.route('/members', methods=['POST'])
def add_member():
    # this is how you can use the Family datastructure by calling its methods
    
    body = request.get_json()

    # if query_members is None:
        #guardar datos recibidos a la tabla Members
    new_member = {
        "id":body["id"],
        "first_name":body["first_name"],
        "age":body["age"],
        "lucky_numbers":body["lucky_numbers"]

    }
    members = jackson_family.add_member(new_member)
    response_body = {
                "family": members
            }

    return jsonify(response_body), 200

@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):  #pongo un 
    # this is how you can use the Family datastructure by calling its methods
    
    body = request.get_json()
    members = jackson_family.delete_member(member_id)

    if member_id == id:
        response_body = {
                    "family": members
                }

        return jsonify(response_body), 200

    elif member_id != id:
        response_body = {
            "msg": "it does not exist, it cannot delet"
        }
        return jsonify(response_body), 400

    else: 
        response_body = {
            "msg": "Error of the Servidor 500"
        }
    return jsonify(response_body), 500


#     if query_familiar is None:
#         #guardar datos recibidos a la tabla Familiar




#     response_body = {
#             "msg": "existed familiar"
#         }
#     return jsonify(response_body), 400


@app.route('/members/<int:member_id>', methods=['GET'])
def get_miembro(member_id):

    # this is how you can use the Family datastructure by calling its methods
    member = jackson_family.get_member(member_id)

    # response_body = {
    #     "hello": "member obtenido",
    #     "family": members
    # }
    return jsonify(member), 200


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
