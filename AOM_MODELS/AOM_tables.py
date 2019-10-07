
import json
from flask import Flask
from  flask_sqlalchemy import SQLAlchemy
from  settings import app

db=SQLAlchemy(app)

class AOM_TABLES():
     


     #defines the tbl_terminal table in the AOM database
    class TERMINALS(db.Model):
        __tablename__ = 'tbl_terminal'
        terminal_id = db.Column(db.Unicode(8), primary_key=True)
        terminal_name = db.Column(db.Unicode(20), nullable=True)
        terminal_location = db.Column(db.Unicode(40), nullable=True)

    class AVG_TERMINAL_WITH_RATE(db.Model):
        __tablename__='tbl_terminal_avg_with_rate'
        terminal_id = db.Column(db.Unicode(8), primary_key=True)
        withdrawal_rate_per_hr = db.Column(db.Integer)
        withdrawal_hr = db.Column(db.Unicode(8))
        withdrawal_day = db.Column(db.Unicode(8))

    class TERMINAL_SUPPORT_EVENTS(db.Model):
        __tablename__ = 'tbl_terminal_support_events'
        terminal_id = db.Column(db.Unicode(8), primary_key=True)
        terminal_name = db.Column(db.Unicode(20), nullable=True)
        event_id = db.Column(db.Unicode(15))
        severity = db.Column(db.Unicode(20))
        date_time = db.Column(db.DateTime, default=db.func.current_timestamp())

    class TERMINAL_MODE(db.Model):
        __tablename__ = 'tbl_terminal_mode'
        terminal_id = db.Column(db.Unicode(8), primary_key=True)
        terminal_mode = db.Column(db.Unicode(15))

    class AVG_TERMINAL_WITH_INFO(db.Model):
        __tablename__='tbl_avg_withdrawal_info'
        terminal_id = db.Column(db.Unicode(8), primary_key=True)
        withdrawal_amount = db.Column(db.Float)
        withdrawal_count_hr = db.Column(db.Integer)
        withdrawal_day = db.Column(db.Unicode(8))
        withdrawal_hr = db.Column(db.Unicode(8))

    class TERMINAL_CASH_INFO(db.Model):
        __tablename__= 'tbl_terminal_cash_info'
        terminal_id = db.Column(db.Unicode(8), primary_key=True)
        terminal_media_combo = db.Column(db.Unicode(100))
        terminal_media_balance = db.Column(db.Float)
        terminal_media_total = db.Column(db.Float)

    class TERMINAL_DOWNTIME(db.Model):
        __tablename__ = 'tbl_terminal_downtime'
        terminal_id = db.Column(db.Unicode(8), primary_key=True)
        date_time = db.Column(db.DateTime, default=db.func.current_timestamp())





    def get_all_terminals():
        return [AOM_TABLES.convert_to_json(terminal_id) for terminal_id in  AOM_TABLES.TERMINALS.query.all()]
   
    def get_terminal(_terminal_id):
        return AOM_TABLES.convert_to_json(AOM_TABLES.TERMINALS.query.filter_by(terminal_id=_terminal_id).first())


         #allows you return the result in friendly manner
    def convert_to_json(self):
        return {'terminal_id':self.terminal_id, 'terminal_name':self.terminal_name, 'term_location':self.terminal_location}


      