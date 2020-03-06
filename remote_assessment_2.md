# Remote assessment 2 (WIP)
## Background
Hogwarts School of Magic has been storing data about their courses and students in spreadsheet, they need a data engineer to store this information in a relational database and create a dashboard for them with basic insights such as total students, dropouts etc. There are things a magic wand can't fix.

## Description
The datasets provided has the following information:

    - Curriculum (the course modVules)
    - Classes with their start and end dates
    - applications
    - students enrollments (students in each module)

Hogwarts has only one course `Core` which runs for a period of 24 weeks every year.

The classes are named in the format `HC_{class}_{start_date}_{end_date}` for example `HC_1_2009-04-15_2009-09-30`.
