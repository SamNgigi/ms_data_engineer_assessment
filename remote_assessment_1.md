# Remote assessment 1
## Background
Melon University Of Technology wants to do an analysis of tech jobs in the kenyan market. You have been tasked to create a tool that will scrape this jobs from specific job providers, persist them and create a dashboard to show basic insights such as no. of jobs etc.

## Description

**Your task is to write an ETL pipeline to fetch the data fro 3 job providers, clean & process the data, store it in a relational database and create a simple dashboard to visualize the data.**

### Scrape
First scrape **tech/it** jobs from the following providers
1. Ihub
2. Brighter Monday
3. Pigiame

### Parse and Persist
Process the scraped data and store it in a relational database.

Use the abstract model below to know what information to look for and how the database could look like. Feel free to add more columns and tables.

- Table: Jobs
    - id serial
    - provider text
    - job_url text
    - title text
    - description text
    - company text
    - posted datetime/timestamp
    - deadline datetime/timestamp
    - type text e.g full time / part time 
    - experience text e.f junior / seniour / mid level
    - location text e.g nairobi / mombasa
    - technologies array/text e.g [C++,python,django,react,machine learning] here are more examples, [technologies](./technologies.txt).

You can process the scraped jobs to the expected format using any technology of your choice including machine learning  as long as the parsing/processing stage is part of your code.

You should also be able to tell similar jobs from the same provider.

Use a relational database of your own choice e.g postgresql,mysql etc. **NB** Use of an ORM is not allowed you will need to use SQL for this assessment.

### Analysis
 
Create a dashboard using a tool of your choice e.g power bi, google data studio or even your own deployed webapp. The dashboard should be accessible online and have a real time connection to your database.

#### Dashboard specs
Use graphs,tables, charts etc to show the following 

1. List of jobs from each provider
    - fields: `title`, `company`,`link to job`,`posted`,`deadline`,`type`,`location`
    - filterable by `technology`,`location`,`posted`
2. monthly distribution of job postings in the last 4 months.
3. Jobs per provider.
4. Distribution of jobs in different technologies

Feel free to add more insights to your dashboard.

## Note
- Code quality will be tested, write good modular code and if possible follow SOLID principles.
- You can use a language of your choice.
- Use of an ORM is not permitted, you will need to write SQL.
- Going beyond what is expected will be advantageous.

