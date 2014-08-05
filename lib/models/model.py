from lib.utils.ext import db
from datetime import datetime

class Stat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    parking_id = db.Column(db.Integer)
    event_time = db.Column(db.DateTime)
    event = db.Column(db.String(10))

    def __init__(self, parking_id, event):
        self.parking_id = parking_id
        self.event = event
        time_tuple = datetime.now().timetuple()
        self.event_time = datetime(time_tuple[0],
                                   time_tuple[1],
                                   time_tuple[2],
                                   time_tuple[3],
                                   time_tuple[4],
                                   0)

class Price(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    parking_id = db.Column(db.Integer)
    hour = db.Column(db.Float)
    day = db.Column(db.Float)

    def __init__(self, parking_id, hour, day):
        self.parking_id = parking_id
        self.hour = hour
        self.day = day


class BasicInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    uid = db.Column(db.String(40))
    total_pak = db.Column(db.Integer)
    info = db.Column(db.Text)

    def __init__(self, json_dic):
        self.name = json_dic['name']
        self.uid = json_dic['uid']
        self.total_pak = json_dic['total_pak']
        self.info = ';'.join(json_dic['info'])
