<h3 align="center">Accidento</h3>

### What it does
<p> Accidento is a web application, where people from all over the world can have an insight, where the accident occurred recently.</p>
<ul>
 <li>It displays the accidents occurred in major places</li>
 <li>It insist to lay speed breakers in the accident-prone areas.</li>
 <li>It insist us to be aware of the signboards.</li>

### Approach
![](https://github.com/Techipeeyon/Images/raw/main/icons/Untitled%20Diagram.jpg)

### Installation Instructions
The portal is primarily a django based application, and to set it up we require to have 
python environment with django and other project dependencies installed. Though one can
work with the project without an virtual environment,  it is recommended to use one so 
as to avoid conflicts with other projects.

0. Make sure that you have `Python 3`, `python-3-devel`, `gcc`, `virtualenv`, and `pip` installed.     
1. Clone the repository

 ```
        $ git clone https://github.com/TechieNK/Defender.git
        $ cd Defender
 ```
2. Create a python 3 virtualenv, and activate the environment.
 ```bash
        $ virtualenv -p python3
        $ source bin/activate
 ```   
3. Install the project dependencies
 ```
        $ pip install -r requirements.txt
 ```
### After Setting Up
From now when you start your work, run ``source bin/activate`` inside the project repository and you can work with the django application as usual - 

* `python manage.py migrate` - set up database
* `python manage.py createsuperuser` - create admin user
* `python manage.py runserver`  - run the project locally

### Build With: 
<img align="left" alt="Bootstrap Studio" width="auto" height="100px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Bootstrap_Studio_Logo.png/240px-Bootstrap_Studio_Logo.png" />
<img align="left" alt="Django" width="auto" height="70px" style="margin-top:10px" src="https://www.djangoproject.com/m/img/logos/django-logo-negative.png" />

        
