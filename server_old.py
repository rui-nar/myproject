from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

Gifts = {
    'Gift1': {'task': 'build an API'},
    'Gift2': {'task': '?????'},
    'Gift3': {'task': 'profit!'},
}


def abort_if_Gift_doesnt_exist(Gift_id):
    if Gift_id not in Gifts:
        abort(404, message="Gift {} doesn't exist".format(Gift_id))

parser = reqparse.RequestParser()
parser.add_argument('task')


# Gift
# shows a single Gift item and lets you delete a Gift item
class Gift(Resource):
    def get(self, Gift_id):
        abort_if_Gift_doesnt_exist(Gift_id)
        return Gifts[Gift_id]

    def delete(self, Gift_id):
        abort_if_Gift_doesnt_exist(Gift_id)
        del Gifts[Gift_id]
        return '', 204

    def put(self, Gift_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        Gifts[Gift_id] = task
        return task, 201


# GiftList
# shows a list of all Gifts, and lets you POST to add new tasks
class GiftList(Resource):
    def get(self):
        return Gifts

    def post(self):
        args = parser.parse_args()
        Gift_id = int(max(Gifts.keys()).lstrip('Gift')) + 1
        Gift_id = 'Gift%i' % Gift_id
        Gifts[Gift_id] = {'task': args['task']}
        return Gifts[Gift_id], 201

##
## Actually setup the Api resource routing here
##
api.add_resource(GiftList, '/Gifts')
api.add_resource(Gift, '/Gifts/<Gift_id>')


if __name__ == '__main__':
    app.run(debug=True)