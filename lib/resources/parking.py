from flask.ext.restful import Resource
from flask.ext.restful import reqparse
from lib.dao.basic_dao import BasicInfoDao
from lib.dao.price_dao import PriceDao
from lib.dao.ava_dao import AvaDao
from lib.utils.resultutil import *

basic_info_dao = BasicInfoDao()
price_dao = PriceDao()
ava_dao = AvaDao()


class Parkings(Resource):
    """
    API  Resource for the parking.
    """
    def get(self):
        #TODO
        return {parking_id: parking_id}

    def post(self):
        args = get_parking_args()
        print dict(args)['info']
        parking = basic_info_dao.create_via_dict(dict(args))
        price_dao.create(parking.id, dict(args)['hour'], dict(args)['day'])
        ava_dao.create(parking.id, parking.total_pak)
        data = {'id': parking.id}
        return returnSucc(data)


class UidParking(Resource):
    """
    API Resource for get the parking info via uid
    """
    def get(self, uid):
        parking = basic_info_dao.find_via_uid(uid)
        if parking:
            price = price_dao.find_by_parking_id(parking['id'])
            parking.update(price)
        return returnSucc(parking)


class Parking(Resource):
    """
    API  Resource for the parking.
    """
    def get(self, parking_id):
        #TODO
        parking = basic_info_dao.find_by_id(parking_id)
        price = price_dao.find_by_parking_id(parking_id)
        parking.update(price)
        return returnSucc(parking)

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
    parking_parser.add_argument('name',
        help='The name of parking place')
    parking_parser.add_argument('total_pak', type=int,
        help='The number of parking slot,should be int')
    parking_parser.add_argument('info', type=str, action='append',
        help='The info of parking place')
    parking_parser.add_argument('uid', type=str,
        help='The info of parking place')
    parking_parser.add_argument('hour', type=float,
        help='The parking price per hour')
    parking_parser.add_argument('day', type=float,
        help='The parking price per day')
    return parking_parser.parse_args()


