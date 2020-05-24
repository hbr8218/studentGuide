# StudentGuide
This is a webapp that will assist students to look up themselves by getting an intuition of how to prepare for exam, what area should be given priority to so as to be better in upcoming semester/exams. This webapp will show analysiss(analyses) of performance of past student based on subjects and other activites like game, love affairs, etc. There is contextual chatbot that make the user comfortable to chat with so that it could try its best to assist the user.
## Install all required library
`python install -r requirements.txt`
## Heroku Setup
Although, this webapp is not for production but the project covers complete setup to deploy on a cloud server for production purpose. Add a file called Profile to the project's root directory and write the following code
`web: gunicorn app:app`
Here the app before colon tells it's a name of a python module and the app after the colon representd the instance of Flask class that will run over time.
