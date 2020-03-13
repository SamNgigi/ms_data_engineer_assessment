import random
import datetime
import csv
import string
import pandas as pd
import os
from faker import Faker


def csv_dict_write(file_path,data,keys=None):
    if keys:
        data = [{k:v for k,v in element.items() if k in keys} for element in data]
    keys = keys if keys else data[0].keys()
    with open(file_path, 'w') as csvfile:
        dict_writer = csv.DictWriter(csvfile, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)

def create_workbook_from_csvs(xlsfile,csvfiles):
    writer = pd.ExcelWriter(xlsfile)
    for c in csvfiles:
        base_ = os.path.basename(c)
        df = pd.read_csv(c)
        df.to_excel(writer,sheet_name=os.path.splitext(base_)[0])
    writer.save()

def generate_fake_data():
    # generate classes
    start_year=2009
    classes = []
    i=0
    code_tmp="HC_{i}_{start}_{end}"
    while True:
        random.seed()
        sot=datetime.date(start_year,1,1)
        sote = sot+datetime.timedelta(days=197)
        start_date= sot + random.random() * (sote-sot)
        end_date = start_date+datetime.timedelta(weeks=24)
        i += 1
        code=code_tmp.format(i=i,start=start_date.strftime("%Y-%m-%d"),end=end_date.strftime("%Y-%m-%d"))
        classes.append({"name":f"HC_{i}","code":code,"start_date":start_date,"end_date":end_date})
        if start_year != 2020:
            start_year += 1
        else:
            break
    csv_dict_write('data/assessment_2/classes.csv',classes,keys=["name","code"])

    # generate applications
    class_names = [(i["name"],i["start_date"],) for i in classes]
    faker = Faker('en_GB')

    previous_dropped = []
    all_applicants = []
    class_students = {}
    all_emails=[]
    all_phones=[]
    for c,d in class_names:
        names = []
        genders = [] 
        emails = []
        phones = []

        # applications
        applications = []

        for i in range(random.randrange(500,600)):
            name = faker.first_name()+" "+faker.last_name()
            salt=""

            while True:
                email = name.replace(" ","").lower()+salt+random.choice(["@gmail.com","@hotmail.com","@yahoo.com"])
                if email not in all_emails:
                    all_emails.append(email)
                    break
                salt += random.choice(string.ascii_letters+string.digits)

            while True:
                phone = faker.phone_number()
                if phone not in all_phones:
                    all_phones.append(phone)
                    break
            # date
            published_date = d - datetime.timedelta(weeks=5)
            app_date = published_date + random.random() * (d-published_date)

            gender = random.choice(["F","M"])
            names.append(name)
            genders.append(gender)
            emails.append(email)
            phones.append(phone)
            applications.append({
                "name":names[i],
                "email":emails[i],
                "gender":genders[i],
                "phone":phones[i],
                "class":c,
                "date":app_date.strftime("%Y-%m-%d"),
            })

        if previous_dropped:
                for i in random.sample(range(0,len(previous_dropped)),50):
                    a = previous_dropped[i]
                    a["class"]=c
                    published_date = d - datetime.timedelta(weeks=5)
                    app_date = published_date + random.random() * (d-published_date)
                    a["date"]=app_date.strftime("%Y-%m-%d")
                    applications.append(a)

        selected_applications = []
        selected_ids = random.sample(range(0,len(applications)),400)
        for i in selected_ids: 
            selected_applications.append(applications[i])
        class_students[c]=selected_applications
        # dropped
        previous_dropped = []
        for i in range(len(applications)):
            if i not in selected_ids:
                previous_dropped.append(applications[i])
        # introduce duplicates
        applications_copy = []
        to_be_dup = random.sample(range(0,len(applications)),200)
        for i in range(len(applications)):
            applications_copy.append(applications[i])
            if i in to_be_dup:
                for x in range(random.randint(1,10)):
                    applications_copy.append(applications[i])
        all_applicants += applications_copy
        applications_copy = []
    # dump all applicants
    csv_dict_write('data/assessment_2/all_applications.csv',all_applicants)

    # dump accepted
    for k,v in class_students.items():
        csv_dict_write('data/assessment_2/students/%s_students.csv'%k,v,keys=["name","email","phone"])
    # write to workbook
    # csvs = ["data/assessment_2/classes.csv","data/assessment_2/all_applications.csv"]
    # csvs += ['data/assessment_2/students/%s_students.csv'%c for c in class_students.keys()]
    # create_workbook_from_csvs('data/assessment_2/hc_admissions.xlsx',csvs)

    #modules
    modules = c
    graduates ={}
    for k,v in class_students.items():
        students = v
        enrollments={}
        for m in modules:
            enrollments[m]=[]
            next_m_batch = []
            for s in students:
                score = random.randint(50,100)
                attendance = random.randint(65,100)
                _s = {"name":s["name"],"email":s["email"],"phone":s["phone"],"score":score,"attendance":attendance}
                if score >=  60:
                    _s["passed"]=True
                    _s["dropped_reason"]=""
                else:
                    _s["passed"]=False
                    _s["dropped_reason"]="Low score"
                if attendance < 70:
                    _s["passed"]=False
                    _s["dropped_reason"]= "Low attendance" if not _s["dropped_reason"] else _s["dropped_reason"] + " and Low attendance"
                if _s["passed"]:
                    next_m_batch.append(s)
                enrollments[m].append(_s)
            students = next_m_batch
        for m,e in enrollments.items():
            csv_dict_write("data/assessment_2/enrollments/%s_%s.csv"%(k,m),e)
        graduates[k]=students
    # graduates
    for k,v in graduates.items():
        csv_dict_write("data/assessment_2/graduates/%s_Outcomes.csv"%k,v,keys=["name","email","phone"])


if __name__ == "__main__":
    generate_fake_data() 
