import pandas as pd

from flask_apps.models.Applications import ApplicationsSql
from flask_apps.models.Outcomes import OutcomesSql
from flask_apps.models.Classes import ClassesSql
from flask_apps.models.Admissions import AdmissionsSql
from flask_apps.models.People import PeopleSql

# Initializations
applicationsSql = ApplicationsSql()
outcomesSql = OutcomesSql()
classesSql = ClassesSql()
admissionsSql = AdmissionsSql()
peoples_sql = PeopleSql()


# Loading the data
applications_df = applicationsSql.get_df()
outcomes_df = outcomesSql.get_df()
classes_df = classesSql.get_df()
admissions_df = admissionsSql.get_df()
peoples_df = peoples_sql.get_df()


gapminder = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')


# Converting date string to datetime object
applications_df['date'] = pd.to_datetime(applications_df['date'])
# Extracting year
applications_df['year'] = applications_df['date'].dt.year
applications_df.rename(columns={'date': 'applied_date'}, inplace=True)

# Converting to datetime
classes_df['start_date'] = pd.to_datetime(classes_df['start_date'])
classes_df['end_date'] = pd.to_datetime(classes_df['end_date'])
# renaming class id to class_id
classes_df.rename(columns={'id': 'class_id'}, inplace=True)

# Mapping gender to applications, admissions & graduates
peoples_df.rename(columns={'id': 'person_id'}, inplace=True)
peoples_df.head()

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
# people_class.head()







