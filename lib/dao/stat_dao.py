import time
from lib.utils.ext import db
from lib.models.model import Stat

class StatDao(object):
    
    def find_by_parking_id(self, parking_id):
        stats = Stat.query.filter_by(parking_id=parking_id).all()
        return stats

    def create(self, parking_id, event):
        stat = Stat(int(parking_id), event)
        db.session.add(stat)
        db.session.commit()
        return stat

    def get_dict(self, stat):
        dict_stat = {}
        dict_stat['parking_id'] = stat.parking_id
        dict_stat['event'] = stat.event
        dict_stat['timestamp'] = int(time.mktime(stat.event_time.timetuple()))
        dict_stat['id'] = stat.id
        return dict_stat