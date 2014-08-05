from flask.ext.restful import Resource
from flask.ext.restful import reqparse
from lib.dao.stat_dao import StatDao
from lib.utils.resultutil import *

stat_dao = StatDao()

class AllStats(Resource):
    """
    API  Resource for the statistics.
    """
    def get(self, parking_id):
        stats = stat_dao.find_by_parking_id(parking_id)
        stats = [stat_dao.get_dict(stat) for stat in stats]
        return returnSucc(stats)

    def post(self, parking_id):
        args = get_stat_args()
        result = StatDao().create(parking_id,
                                  dict(args)['event'])
        return {'result': 'success', 'data': str(result)}

def get_stat_args():
    parking_parser = reqparse.RequestParser()

    parking_parser.add_argument('event', type=str,
        help='The event type of parking. Should be in or out.')

    return parking_parser.parse_args()
