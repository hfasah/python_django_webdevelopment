# python_django_webdevelopment
''' 
 NJANGO

njango is a framework for making websites
Slight changes and our website is ready in a go.

'''

''' Build a weather application that fetches weather data from a public API and
 displays it to the user. 
 Store user preferences in a JSON file. 
 '''
 Django commands/Steps

pip install django ( download the django )
django-admin startproject project_name

init file - init file connect all other file and treat every file as a single code.

Asgi & wsgi file - this file is for deployment, means when you made up your project so these files will help you to upload project to server.

Setting file - its important file, it has installed apps list, templates ( to keep all html files inside template folder ), database ( by default sqlite )

Url file - its used to open a website page depending upon the url entered

Manage.py - this file is very important and is used to run your project.

Cd - ( change directory ) go forward into folder
Ls - ( list out all files names ) 
Cd .. - ( go outside the folder ) go backward

 py manage.py runserver ( run the project )
 To show any html template
1. Open setting file and go to template code line
2. Set 'DIRS': [BASE_DIR, 'template'],
3. Create html file inside template folder
4. Import render ( from django.shortcuts import render )
5. Use render to show up your html file in function
