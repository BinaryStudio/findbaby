from lib.utils.ext import db
from lib.models.model import BasicInfo

class BasicInfoDao(object):
    
    def find_by_id(self, id):
        basic_info = BasicInfo.query.filter_by(id=id).first()
        if basic_info:
            return self.get_parking_dict(basic_info)
        else:
            return {}

    def find_via_uid(self, uid):
        basic_info = BasicInfo.query.filter_by(uid=uid).first()
        if basic_info:
            return self.get_parking_dict(basic_info)
        else:
            return {}

    def update(self, basic_info):
        _basic_info = self.find_by_id(basic_info.id)
        _basic_info.name = basic_info.name
        _basic_info.uid = basic_info.uid
        _basic_info.total_pak = basic_info.total_pak
        _basic_info.info = basic_info.info
        db.session.save()
        return _basic_info

    def delete(self, id):
        basic_info = self.find_by_id(id)
        db.session.delete(basic_info)
        db.session.commit()

    def create(self, basic_info):
        print basic_info
        db.session.add(basic_info)
        db.session.commit()
        return basic_info

    def create_via_dict(self, json_dict):
        basic_info = BasicInfo(json_dict)
        self.create(basic_info)
        return basic_info

    def get_parking_dict(self, parking):
        parking_dict = {}
        
        parking_dict['id'] = parking.id
        parking_dict['name'] = parking.name
        parking_dict['uid'] = parking.uid
        parking_dict['total_pak'] = parking.total_pak
        parking_dict['info'] = parking.info

        return parking_dict
