import pandas as pd

from flask_apps.models.Applications import ApplicationsSql
from flask_apps.models.Outcomes import OutcomesSql
from flask_apps.models.Classes import ClassesSql

# Initializations
applicationsSql = ApplicationsSql()
outcomesSql = OutcomesSql()
classesSql = ClassesSql()


# Loading the data
applications_df = applicationsSql.get_df()
outcomes_df = outcomesSql.get_df()
classes_df = classesSql.get_df()

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

# *Import this
class_applications = pd.merge(
    applications_df, classes_df.drop('code', axis=1), how='inner', on='class_id')

class_cols = ['class_id', 'class_name', 'end_date']

# *Import this
graduates = pd.merge(
    outcomes_df, classes_df[class_cols], how='inner', on='class_id')








