import pandas as pd

from flask_apps.models.Applications import ApplicationsSql
from flask_apps.models.Outcomes import OutcomesSql
from flask_apps.models.Classes import ClassesSql
from flask_apps.models.Admissions import AdmissionsSql
from flask_apps.models.People import PeopleSql
from flask_apps.models.Modules import ModulesSql
from flask_apps.models.Enrollments import EnrollmentsSql

# Initializations
application_sql = ApplicationsSql()
people_sql = PeopleSql()
classes_sql = ClassesSql()
admissions_sql = AdmissionsSql()
outcomes_sql = OutcomesSql()
modules_sql = ModulesSql()
enrollments_sql = EnrollmentsSql()


# Loading the data
applications_df = application_sql.get_df()
peoples_df = people_sql.get_df()
classes_df = classes_sql.get_df()
admissions_df = admissions_sql.get_df()
outcomes_df = outcomes_sql.get_df()
modules_df = modules_sql.get_df()
enrollment_df = enrollments_sql.get_df()


gapminder = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')


# * APPLICATIONS
# Converting date string to datetime object
applications_df['date'] = pd.to_datetime(applications_df['date'])
# Extracting year
applications_df['year'] = applications_df['date'].dt.year
applications_df.rename(columns={'date': 'applied_date'}, inplace=True)

# *CLASSES
# Converting to datetime
classes_df['start_date'] = pd.to_datetime(classes_df['start_date'])
classes_df['end_date'] = pd.to_datetime(classes_df['end_date'])
# renaming class id to class_id
classes_df.rename(columns={'id': 'class_id'}, inplace=True)

# *PEOPLE
# Mapping gender to applications, admissions & graduates
peoples_df.rename(columns={'id': 'person_id'}, inplace=True)
peoples_df.head()

# *MODULES
modules_df.rename(columns={"id":"module_id"}, inplace=True)
modules_df

# *Import this
class_applications = pd.merge(
    applications_df, classes_df.drop('code', axis=1), how='inner', on='class_id')
class_applications = pd.merge(class_applications, peoples_df[[
                              'person_id', 'gender']], how='inner', on='person_id')


class_cols = ['class_id', 'class_name', 'end_date']

# *Import this
graduates = pd.merge(
    outcomes_df, classes_df[class_cols], how='inner', on='class_id')
graduates = pd.merge(
    graduates, peoples_df[['person_id', 'gender']], how='inner', on='person_id')
graduates.head()
graduate_persons = pd.merge(graduates, peoples_df[['person_id', 'first_name', 'last_name', 'email']],
                            how='inner', on='person_id').drop(['class_id', 'end_date', 'id'], axis=1)

# *Graduates with personal information                            
graduate_persons = graduate_persons[[
    'first_name', 'last_name', 'email', 'class_name', 'gender']]


# *Import this to dboard
admitted_students = pd.merge(admissions_df, classes_df[[
                             'class_id', 'class_name']], how='inner', on='class_id')
admitted_students = pd.merge(admitted_students, peoples_df[[
                             'person_id', 'gender']], how='inner', on='person_id')


# *Applicant name with class applied to
app_include = ["person_id", "class_name", "gender", "year"]
people_include = ["person_id", "first_name", "last_name", "phone", "email"]
people_class = pd.merge(
    peoples_df[people_include], class_applications[app_include], how='inner', on='person_id')

# *ENROLLMENTS merged with class_name, module and person
people_enrolled = pd.merge(enrollment_df, modules_df[[
                           "module_id", "module_name"]], how="inner", on="module_id").drop("module_id", axis=1)
people_enrolled = pd.merge(people_enrolled, classes_df[[
                           "class_id", "class_name"]], how="inner", on="class_id").drop("class_id", axis=1)
people_enrolled = pd.merge(
    people_enrolled, peoples_df[people_include], how="inner", on="person_id").drop("person_id", axis=1)

people_enrolled_col_order = ["id", "first_name", "last_name", "phone", "email",
                             "class_name", "module_name", "score", "attendance", "passed", "dropped_reason"]
people_enrolled_final = people_enrolled[people_enrolled_col_order]


modulebyClass = people_enrolled_final.groupby(
    ['class_name', 'module_name']).size().to_frame(name="mod_count").reset_index()
modulebyClass = pd.merge(modulebyClass, classes_df[[
                         "class_id", "class_name"]], how="inner", on="class_name")
modulebyClass = pd.merge(modulebyClass, modules_df[["module_id", "module_name"]], how="inner", on="module_name")
modulebyClass.sort_values(['class_id', 'module_id'], inplace=True)




