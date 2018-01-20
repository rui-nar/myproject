from flask_restful import reqparse, abort, Api, Resource


def abort_if_Gift_doesnt_exist(Gift_id):
    if Gift_id not in Gifts:
        abort(404, message="Gift {} doesn't exist".format(Gift_id))


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

