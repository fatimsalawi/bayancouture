# bayancouture
This is a repository to my Abaya website using MongoDB and Django 
1.	Use Python 3.12.1
2.	Install Anaconda Navigator then open it Launch Cmd.exe Prompt as a terminal.
3.	The folder is created in the desktop. (you can create it anywhere you want)
4.	opening the terminal using the cd command with the path of the folder created.
For example, cd C:\Users\fatim\OneDrive\Desktop\Django\bayancouture
5.	In the anaconda terminal, create a virtual environment using this command
	conda create --name newEnv django
6.	pip install all requirements
7.	Run the server using this command (python manage.py runserver) in the anaconda terminal
8.	To run the project, copy the URL and paste it in your web browser http://127.0.0.1:8000/
9.	Apply migrations using these commands 
•	python manage.py make migrations. 
•	python manage.py migrate 
•	python manage.py runserver.
10.	In the setting.py file changed the database engine to connect to MongoDB
11.	Home page is a list of view of all the Abayas in the database.
12.	Users are able to create accounts and register.
13.	After logging in, users can create an Abaya by filling out the form, and they can upload their image by providing the URL, and it will be saved in MongoDB.
14.	Accessing into Django Admin site http://127.0.0.1:8000/ admin
15.	I style my HTML page with bootstrap 5 by copying Bootstrap CDN into my HTML pages.

