from flask.ext.restful import reqparse
from flask.ext.restful import Resource
from lib.dao.ava_dao import AvaDao
from lib.dao.basic_dao import BasicInfoDao
from lib.utils.resultutil import *


class SlotInc(Resource):
    """
    API Resource for Increasing the parking slot.
    """
    def get(self, parking_id):
        AvaDao().incn(parking_id, 1)
        return returnSucc(1)

    def post(self, parking_id):
        args = get_slot_args()
        AvaDao().incn(parking_id, args.number)
        return returnSucc(args.number)


class SlotDes(Resource):
    """
    API  Resource for Decreasing the parking slot.
    """
    def get(self, parking_id):
        AvaDao().decn(parking_id, 1)
        return returnSucc(1)

    def post(self, parking_id):
        args = get_slot_args()
        AvaDao().decn(parking_id, args.number)
        return returnSucc(args.number)


class UpdateSlot(Resource):
    """
    API Resource for update the parking slot.
    """
    def put(self, parking_id):
        args = get_slot_args()
        AvaDao().update(parking_id, args.number)
        return returnSucc(args.number)

    def patch(self, parking_id):
        return self.put(parking_id)


class Slot(Resource):
    """
    API to show the slot.
    """
    def get(self, parking_id):
        slotnumber = int(AvaDao().get(parking_id))
        return returnSucc(slotnumber)


def get_slot_args():
    parking_parser = reqparse.RequestParser()
    parking_parser.add_argument('number', type=int,
        help='The number of changed slots')
    return parking_parser.parse_args()




