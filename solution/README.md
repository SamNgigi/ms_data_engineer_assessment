#  Hogwarts Assessment(WIP)
- This is my working solution for the technical assesment for the Moringa data engineer role

Link to the current dashboard. [Hogwarts Dashboard](https://ds-eng.herokuapp.com/ deployed to Heroku)

## TODO
- [x] Fetch google spread sheet resources
    - A bit about WSGI
    - views and routing
    - running the development server(with debug mode)
- [x] Templates (jinja)
    - rendering template and passing context to template
    - tags
    - control flow(condition and loops)
    - macros
    - template inheritances
- [x] Project structure using Blueprints
- [x] Deploying to production(Heroku)
    - gunicorn as our WSGI production server
- [x] Extensions and CLI
    - Flask Script for commands like `runserver` and `shell`
- [x] Databases (Relational) with Postgres
    - CRUD
    - Relationships
    - SQLAlchemy models and relationships (ORM)
    - DB Migrations using alembic
- [x] Authentication with Flask-Login
- [ ] Testing our Flask app
- [ ] Misc
    - Sending Mails
    - CSRF protection
    - Flask Restful


## Setup 
- Use python3
### Clone
`t`
### Create virtual
There are many ways to create a virtual env i use:
```bash
python3 -m venv virtual
```
Activate virtual and install requirements
```bash
# for unix users
source virtual/bin/activate
pip install - requirements.txt
```
### run server
- Development server `python manage.py`
- Production server `gunicorn "manage:app"`


##  Resources
**N/B** I may not have looked at many of this resources, so if some contain incorrect/outdated info am not to blame, you should refer to multiple sources.
### Flask
- [Official Flask Documentation](https://flask.palletsprojects.com/)
- [Miguel blog](https://blog.miguelgrinberg.com/category/Flask)
    - [https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)