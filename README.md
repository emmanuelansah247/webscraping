# Web Scraping Project
This project scraps the website https://tympanus.net/codrops/author/crnacura/ and stores the information in a file

## Stack

1. Selenium
2. Python
3. Django
4. Html
5. Css

### Setting Up on local Machine (Windows)
1. Download or Clone the repository

    To clone the repository, open your git terminal (you need to install git) and type
    
        git clone https://github.com/emmanuelansah247/webscraping.git
        
2. Install virtual environment (you need to have python and pip installed)

    To install virtual environment, type (in your terminal)
    
       pip install virtualenv
       
3. You can activate the virtual environment (you need to install virtualenv)

    To activate the virtual environment, navigate to the folder of the project and type
    
       venv\scripts\activate
       
4. You need to install the following

    To install Django, type
    
         pip install django
    
    To install Selenium, type
    
        pip install selenium
      
    To install webdriver-manager, typ
      
        pip install webdriver-manager
        
5. When everything is successfully installed, run the following command

       py manage.py runserver
     
     
     Open your browser and navigate to http://127.0.0.1:8000/
     
 
 #### Scraping and Generating the files (The application by default opens with a default file)
 
 Whiles on http://127.0.0.1:8000/, you can click on the button "Generate New Files" to generate two files for you
 (This should take around 4 to 5 minutes)
    
