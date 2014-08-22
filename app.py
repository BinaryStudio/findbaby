import sys
from flask import Flask, render_template
from flask.ext.restful import Api
from lib.resources.parking import Parking, Parkings, UidParking
from lib.resources.slot import SlotInc, SlotDes, UpdateSlot, Slot
from lib.resources.stat import AllStats
from lib.utils.ext import db
from lib.ctrl.main import main

def create_app():
    app = Flask("parkplace")
    app.config.from_pyfile('app.config.' + sys.argv[1] + '.cfg', silent=True)
    
    app.register_blueprint(main)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    api = Api(app)

    api.add_resource(Parking, '/rest/parkings/<string:parking_id>')
    api.add_resource(Parkings, '/rest/parkings')
    api.add_resource(UidParking, '/rest/parkings/uid/<string:uid>')

    api.add_resource(SlotInc, '/rest/slots/inc/<string:parking_id>')
    api.add_resource(SlotDes, '/rest/slots/des/<string:parking_id>')
    api.add_resource(UpdateSlot, '/rest/slots/update/<string:parking_id>')
    api.add_resource(Slot, '/rest/slots')

    api.add_resource(AllStats, '/rest/stats/<string:parking_id>')

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'])
