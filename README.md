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
 
 Whiles on http://127.0.0.1:8000/, you can click on the button "Generate New Files" to generate two files for you i.e the Demo File or Version File.
 Demo files stores the information relating to the main website link. 
 Version File stores the information relating the main link and sub links
 (This should take around 4 to 5 minutes)
 
 #### Description of Files
 
 Demo File
 
    Main Link - The link to the original website
    
    Project Name - The name of the project/Website
    
    Time Created - The time the website was created
    
    Github Url - Github url to the website 
    
    Github Stars - Github stars on the website
    
 Version File
    Primary Key - A unique identifier of each website link
    
    Foreign Key - A reference to the primary key (Main link will have sub website links. Main link without sub links will have this column to be empty)
    
    Website Link - The website in reference link
                
    Font Name  - Name of the specified html element (it can be h1,h2,h3, span or any title element)
    
    Font Size - Size of the html element
    
    Font Weight - Font weight of the html element 
    
    Font Family - Font Family of the html element
    
    Font Color - Font color of the html element
    
    Font Background-Color - Background color of the html element
    
    Font Height - Height of the element
    
    Font Characters - The length of the letters in the html element
    
    Body Font Size - Font size of the body element (Body tag)
    
    Body Font Family - Font family of the body element
 
    Body Background-Color - Background color of the body element
    
    Body Scroll Height - Scroll Height of the body element
    
    Screen Height - Screen height of the laptop/computer using for the web scrapping
    
    Screen Width - screen width of the laptop/computer using for the web scrapping
    
    Screen Depth - screen depth (how many times you will downwards from till you get to the bottom) of the laptop/computer using for the web scrapping
