from operator import imod
from flask import request
from datetime import date
from .._base_resource import BaseResource
from ...repository import *
from ...repository.interface import *


class AttendanceController(BaseResource):
    def __init__(self):
        super().__init__()

        self.req_parser.add_argument("date", type = str, required = False, default = date.today())
        self.req_parser.add_argument("name", type = str, required = False)

        # repository controller objects
        self.att_interface = AttendanceInterface()

    def get(self):
        if request.endpoint == "date":
            return self.formatter.get(self.att_interface.get_attendance_by_date(self.args["date"]))
        else:
            return self.formatter.get(self.att_interface.get_attendace_by_name(self.args["name"]))
        
