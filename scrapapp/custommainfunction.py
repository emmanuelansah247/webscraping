import imp
from optparse import Option
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager 
from . import customfunctions as custom
import time
from os import listdir
from os.path import isfile,join
import os

def mainRun():
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        options.add_argument("--headless")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
        driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=options)
        driver.get("https://tympanus.net/codrops/author/crnacura/")

        try: 
            temp_articles = driver.find_elements(By.TAG_NAME,value="article")
            articles = []
            for n in temp_articles:
                if("ct-box" in n.get_attribute("class")):
                    articles.append(n)
            sub_articles = [articles[0]]
            website_data_list = []
            for index,article in enumerate(articles):
                driver.get("https://tympanus.net/codrops/author/crnacura/")
                temp_articles = driver.find_elements(By.TAG_NAME,value="article")
                article = temp_articles[index] 
                _article_date = custom.findArticleDate(article)
                link_to_article_full_website = custom.getLinkToArticleFullWebsite(article)
                driver.get(link_to_article_full_website)
                temp_website_link_article = driver.find_element(By.TAG_NAME, value='article')
                _article_name = custom.findArticleName(temp_website_link_article)
                print(_article_name)
                _article_full_website_link = custom.findArticleFullWebsiteDemoLink(temp_website_link_article)
                _article_github_link = custom.findArticleFullWebsiteGithubLink(temp_website_link_article)
                #navigating to github link to get github stars
                _article_github_stars = None
                if _article_github_link:
                    if "github" in _article_github_link:
                        driver.get(_article_github_link) 
                        _article_github_stars = custom.findArticleFullWebsiteGithubStars(driver)

                
                _website_titles_name_and_body_css = custom.findWebsiteTitleandBodyCss(_article_full_website_link,driver)
                _main_website_previous_links = custom.findMainWebsitePreviousVersions(_article_full_website_link,driver)
                
                temporal_website_data = {
                        '_id': index + 1,
                        "_article_date": _article_date,
                        "_article_name": _article_name,
                        "_article_full_website_link": _article_full_website_link,
                        "_article_github_link": _article_github_link,
                        "_article_github_stars": _article_github_stars,
                        '_website_titles_name_and_body_css': _website_titles_name_and_body_css,
                        '_main_website_previous_links': _main_website_previous_links
                    }

                website_data_list.append(temporal_website_data)
                    
            mypath =  "./static/media"
            demofilename = "demos-" + str(time.time()).replace('.','-') + ".txt"
            with open(join(mypath,demofilename),'w',encoding='utf8',newline='') as f:

                f.write("Main Link" + "\t" + "Project Name" + "\t" + "Time Created" + "\t" + "Github Url" + "\t" + 
                        "Github Stars" + "\n")

                for website in website_data_list:
                    row_data = ""
                    row_data = row_data + website['_article_full_website_link'] + "\t" 
                    row_data = row_data + website['_article_name'] + "\t"
                    row_data = row_data + website['_article_date'] + "\t"
                    row_data = row_data + website['_article_github_link'] + "\t"
                    row_data = row_data + website['_article_github_stars'] + "\t"
                    f.write(row_data + "\n")

            

            version_file_list = []
            versionfilename = "versions-" + str(time.time()).replace('.','-') + ".txt"
            with open(join(mypath,versionfilename),'w',encoding='utf8',newline='') as v:
                file_heading = ["Primary Key","Foreign Key","Website Link",
                "Font 1 Name","Font 1 Size","Font 1 Weight","Font 1 Family","Font 1 Color","Font 1 Background-Color","Font 1 Height","Font 1 Characters",
                "Font 2 Name","Font 2 Size","Font 2 Weight","Font 2 Family","Font 2 Color","Font 2 Background-Color","Font 2 Height","Font 2 Characters",
                "Font 3 Name","Font 3 Size","Font 3 Weight","Font 3 Family","Font 3 Color","Font 3 Background-Color","Font 3 Height","Font 3 Characters",
                "Font 4 Name","Font 4 Size","Font 4 Weight","Font 4 Family","Font 4 Color","Font 4 Background-Color","Font 4 Height","Font 4 Characters",
                "Body Font Size","Body Font Family","Body Background-Color","Body Scroll Height","Screen Height","Screen Width","Screen Depth"
                ]

                temp_file_heading = ""
                for column_name in file_heading:
                    temp_file_heading += column_name + "\t"
                v.write(temp_file_heading + "\n")       
                website_version_file_list = custom.getwebsiteElementsCssAndVersionLinksInList(website_data_list,driver)
                for main_link in website_version_file_list:
                    temp_props = ""
                    for prop_value in main_link.values():
                        temp_props +=  prop_value + "\t"
                    v.write(temp_props + "\n")


        finally:
            driver.quit()
