from lib.utils.ext import db
from datetime import datetime

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    sex = db.Column(db.String(10))
    photo = db.Column(db.String(100))
    height = db.Column(db.Float)
    weight = db.Column(db.Float)
    desc = db.Column(db.Text)

    def __repr__(self):
        return u"""
        Person {}:
            name: {}
            age: {}
            sex: {}
            photo: {}
            height: {}
            weight: {}
        """.format(self.id, self.age)

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


class clue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500))
    content = db.Column(db.Text)
    def __repr__(self):
        return u"""
        Clue {}:
            title: {}
            content: {}
        """.format(self.id, self.title, self.content)

    def __init__(self, title, content):
        self.title = title
        self.content = content


class findrequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500))
    content = db.Column(db.Text)
    validTime = db.Column(db.DateTime)
    def __repr__(self):
        return u"""
            request {}:
                title: {}
                content: {}
        """.format(self.id, self.title, self.content)

    def __init__(self, title, content, validTime):
        self.title = title
        self.content = content
        self.validTime = validTime


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
