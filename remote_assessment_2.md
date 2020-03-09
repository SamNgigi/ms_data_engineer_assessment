# Remote assessment 2 
## Background
Hogwarts School of Magic has been storing data about their courses and students in spreadsheet, they need a data engineer to transfer this to a relational database and create a dashboard for them with basic insights such as total students, dropouts etc. There are things Dumbledore's magic wand can't fix.

## Description

**Your task is to write an ETL pipeline to fetch the data from google sheets, clean & process, store it in a relational database and create a simple dashboard to visualize the data.**

You have been provided with 3 spreadsheets

1. [hogwarts_admissions](https://docs.google.com/spreadsheets/d/1lKrQ4NKwogywiDqnNuwva4zDVNi18x2BClQ6ugFU7SQ/edit?usp=sharing)
    - list of classes and their respective code in the form `HC_{class}_{start_date}_{end_date}`
    - list of all applications
    - list of students admitted to their respective classes

2. [hogwarts_enrollments](https://docs.google.com/spreadsheets/d/1uHpQQUBf5UNw9Qm18HPq7jKY0pBpiUIpCBH8GRTP3_c/edit?usp=sharing)
    - hogwarts has 4 modules `["charms","Dark Arts","Flying","Potions"]` which ran for 24 weeks in, see `modules` tab
    - a list of enrollments for each `module` per class including scores and whether the student was dropped or continued to the next module.

3. [hogwarts_outcomes](https://docs.google.com/spreadsheets/d/1dzgZHo2HOPRwJWZ35zfseBk-nqB7MMwzen_llZkerew/edit?usp=sharing)
    - list of graduated students per class.

Link to drive: [https://drive.google.com/open?id=1WCZ1h6tgAnxADOfByk-2XJ1N7r0d_oNl](https://drive.google.com/open?id=1WCZ1h6tgAnxADOfByk-2XJ1N7r0d_oNl)


### T1: Fetch data
Make a copy of all spreadsheets to your personal drive. Using [google spreadsheets api](https://developers.google.com/sheets) write fetcher(s) to pull this data from the spreadsheets.

### T2: Cleaning & Persisting data
Clean the data where necessary and persist it in a relational database, you can refer to the following abstract model but feel free to add more columns

```
classes:
    name varchar
    code varchar
    start_date timestamp
    end_date timestamp

modules:
    name varchar
    position integer
    weeks integer

people:
    first_name varchar
    last_name varchar
    phone varchar
    email varchar
    gender varchar

applications:
    person_id FK people
    class_id FK classes
    date timestamp

admissions:
    person_id FK people
    class_id FK classes

enrollments:
    person_id FK people
    class_id FK classes
    module_id FK modules
    score integer
    attendance integer
    passed bool
    dropped_reason text

outcomes:
    person_id FK people
    class_id FK classes
```

Data from the spreadsheets is not clean you will need to clean this data before persisting it as part of the assessement.

Use a relational database of your own choice e.g postgresql,mysql etc. **NB** Use of an ORM is not allowed you will need to use SQL for this assessment.

### T3: Create a dashboard

Create a dashboard using a tool of your choice e.g power bi, google data studio or even your own deployed webapp. The dashboard should be accessible online and have a real time connection to your database.

#### Specs
Use graphs, charts, tables etc to visualize the following(not limited to)
- Show totals
    - total applicants and graduates
    - total applicants,graduates per class.
    - no of students admitted per class.
    - total applications and graduates based on gender.

- List of applicants filterable class.
- List of students filterable by class and module.
- List of graduates filterable by class.
- Drop outs and drop out rate between modules in a class.


Feel free to add more insights to your dashboard.

## Note
- Code quality will be tested, write good modular code and if possible follow SOLID principles.
- You can use a language of your choice.
- Use of an ORM is not permitted, you will need to write SQL.
- Going beyond what is expected will be advantageous.

