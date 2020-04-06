# Group-Project
COSC 3380 - Database System

**#Database Preparation**  
Install mysql Ver 8.0.19, and Mysql Workbench in your computer  
Reset your mysql password to "rootroot"  
Create a database name "database_project"  
Import the database_project.sql file  

**#Make sure to have python3.7, pip, virtualenv installed in your computer:**  
You can install these in the command line

**#Creating your local Github directory**  
Create an empty directory “project”  
In terminal, cd to “project”  
```mkdir project3380```  
cd to project 3380  
```git init```  
```git remote add project3380 https://github.com/Mifa79/library3380.git```  
```git pull project3380 master```  

**#Set-up virtual environment**  
To create, cd OUTSIDE, next to "project3380" folder and run the following command:  
```python3.7 -m venv ENV```  
ENV is the name you choose for your virtual environment  

**#Activate virtual environment:**  
On Windows:  
```ENV\Scripts\activate.bat```  
On MAC:  
```source ENV/bin/activate```  

**#Install necessary things in the virtual environment, run command:**  
cd inside project3380  
```pip install -r requirements.txt```  
This will install everything in the requirements.txt file  
To see if all the dependencies in requirements.txt are installed, run command:  
```pip freeze```  

**#Import the database**  
```python3.7 manage.py migrate```

**#Run the project**  
CD into project3380/src/  
```python3.7 manage.py runserver```  
Copy the link (similar to this http://127.0.0.1:8000/) and paste in a browser  

  
