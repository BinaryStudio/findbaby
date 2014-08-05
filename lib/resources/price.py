from flask.ext.restful import Resource
from flask.ext.restful import reqparse


class Price(Resource):
    """
    API  Resource for the parking.
    """
    def get(self, parking_id):
        #TODO
        return {parking_id: parking_id}

    def post(self, parking_id):
        #TODO
        args = get_parking_args()
        return {'args': str(dict(args))}

    def put(self, parking_id):
        #TODO
        pass

    def patch(self, parking_id):
        #TODO
        pass


def get_parking_args():
    parking_parser = reqparse.RequestParser()
    parking_parser.add_argument('name', type=str,
        help='The name of parking place')
    parking_parser.add_argument('total_pak', type=int,
        help='The number of parking slot,should be int')
    parking_parser.add_argument('info', type=str,
        help='The info of parking place')
    parking_parser.add_argument('uid', type=str,
        help='The info of parking place')
    parking_parser.add_argument('hour', type=float,
        help='The parking price per hour')
    parking_parser.add_argument('day', type=float,
        help='The parking price per day')
    return parking_parser.parse_args()


