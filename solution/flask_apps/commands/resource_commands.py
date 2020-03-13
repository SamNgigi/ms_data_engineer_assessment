from flask_script import Command
from ..services.resources.gspread_service import GspreadService
from ..services.resources.abstract_resource import AbstractSpreadSheetResource

from ..services.resources.admissions.ApplicationsRes import AllApplicationsResource
from ..services.resources.admissions.ClassRes import ClassResource
from ..services.resources.admissions.StudentsClassRes import StudentsClassResource

from ..services.resources.enrollments.ModulesRes import ModulesResource 
from ..services.resources.enrollments.BaseClassByModuleRes import BaseClassByModuleRes

from ..services.resources.outcomes.OutcomesRes import OutcomesResource



class MapResources(Command):
    
    def run(self):  # pylint: disable=E0202
        gsheet_resources = [
            # AllApplicationsResource(),
            ClassResource(),
            # StudentsClassResource(),
            # ModulesResource(),
            # BaseClassByModuleRes(),
            # OutcomesResource()
        ]

        for gsheet_res in gsheet_resources:

            gsheet_res.fetch()
            gsheet_res.process()
            gsheet_res.store()
