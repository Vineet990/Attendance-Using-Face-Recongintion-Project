from app.main.models.attendance_model import Attendance

class AttendanceInterface:

    def get_attendace_by_name(self,name:str):
        query = [row.__to_dict__() for row in Attendance.query.filter_by(Name = name).all()]

        return query

    def get_attendance_by_date(self,date:str):
        query = [row.__to_dict__() for row in Attendance.query.filter_by(DOA = date).all()]

        return query

