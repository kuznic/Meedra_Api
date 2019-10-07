from AOM_MODELS.AOM_tables import db
import sqlalchemy


class AOM_PROCEDURES():

    #This class defines the sp_tbl_terminal_summary
    def get_terminal_summary(_terminal_id,_time_from,_time_to):
        result = db.engine.execute(sqlalchemy.text("CALL sp_terminal_health_summary(:param1,:param2,:param3)"),param1=AOM_PROCEDURES.get_value(_terminal_id),param2=AOM_PROCEDURES.get_value(_time_from),param3=AOM_PROCEDURES.get_value(_time_to))
        summary = result.fetchall()
        return summary


    def get_terminal_support_events(_terminal_id):
        result = db.engine.execute(sqlalchemy.text("CALL sp_terminal_events(:param1)"),param1=AOM_PROCEDURES.get_value(_terminal_id))
        summary = result.fetchall()
        return summary


    def get_value(value):
        return value


