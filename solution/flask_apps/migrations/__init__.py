from .add_classes_table_001 import CreateClassTable
from .add_modules_table_002 import CreateModulesTable
from .add_people_table_003 import CreatePeoplesTable
from .add_applications_table_004 import CreateApplicationsTable
from .add_admissions_table_005 import CreateAdmissionsTable
from .add_enrollments_table_006 import CreateEnrollmentsTable
from .add_outcomes_table_007 import CreateOutcomesTable

MIGRATIONS = [
    CreateClassTable,
    CreateModulesTable,
    CreatePeoplesTable,
    CreateApplicationsTable,
    CreateAdmissionsTable,
    CreateEnrollmentsTable,
    CreateOutcomesTable
]

def create_migrations_table(db_handler):
    sql = """ 
    CREATE TABLE IF NOT EXISTS migrations(
        id serial PRIMARY KEY,
        number INTEGER UNIQUE,
        name TEXT
    );
    """
    db_handler.execute_sql(sql)
    return True
