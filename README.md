# StudentGuide
This is a webapp that will assist students to look up themselves by getting an intuition of how to prepare for exam, what area should be given priority to so as to be better in upcoming semester/exams. This webapp will show analysiss(analyses) of performance of past student based on subjects and other activites like game, love affairs, etc. There is contextual chatbot that make the user comfortable to chat with so that it could try its best to assist the user.
## Install all required library
`python install -r requirements.txt`
## Heroku Setup
Although, this webapp is not for production but the project covers complete setup to deploy on a cloud server for production purpose. Add a file called Profile to the project's root directory and write the following code <br />
`web: gunicorn app:app` <br />
Here the app before colon tells it's a name of a python module and the app after the colon representd the instance of Flask class that will run over time.
#### Create Heroku apps
There are two heroku apps, one for staging and another for production using the following command:- <br />
`heroku create studentguide-pro` <br />
`heroku create studentguide-stage`
#### Add Heroku apps to git remote
`git remote add pro https://git.heroku.com/studentguide-pro.git` <br />
`git remote add stage https://git.heroku.com/studentguide-stage.git` <br />
Further, we will able to push our apps live to heroku. <br />
- For staging: git push stage master
- For production: git push pro master
## Config Setting
### Local Setting
To set up our application with environment variables, we’re going to use autoenv. This program allows us to set commands that will run every time we cd into our directory. In order to use it, we will need to install it globally. First, exit out of your virtual environment in the terminal, install autoenv, then and add a .env file and the following: <br />
`source your_virtual_env_path/bin/activate` <br />
`export APP_SETTING="Config.DevelopmentConfig"`
### Heroku Setting
Similarly, Set environment variables on Heroku. <br />
- For Staging: heroku config:set APP_SETTINGS=config.StagingConfig --remote stage
- For Production: heroku config:set APP_SETTINGS=config.ProductionConfig --remote pro
## Setting up Database(Postgresql)
Since Heroku use postgresql.
To get started, install postgersql if you don't have already so that it would be easier for us to deploy on heroku. Create a database named studentguidedb with following tables:- <br />
1. Registration table
2. Login table
#### Local Migration
We are going to use Alembic, which is part of Flask-Migrate, to manage database migrations to update a database’s schema. <br />
To create the migrations folder in the project's root directory:- <br />
`python manage.py db init` <br />
To manage database migration:- <br />
`python manage.py db migrate` <br />
To commit detected changes:- <br />
`python manage.py db upgrade` <br />
#### Remote Migration 
Let's apply the migration on the databases on Heroku. <br />
- Add a postgress addon to the staging server <br />
`heroku addons:create heroku-postgresql:hobby-dev --app studentguide-stage` <br />
- Add a postgress addon to the production server <br />
`heroku addons:create heroku-postgresql:hobby-dev --app studentguide-pro` <br />
Note: hobby-dev is the free tier of the Heroku postgres addon. <br />