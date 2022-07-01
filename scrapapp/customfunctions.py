
from lib2to3.pgen2 import driver
from logging import exception
import math
from typing import final
from selenium import webdriver
from selenium.webdriver.support.color import Color
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def findArticleDate(article):
        ct_subline = article.find_element(By.CSS_SELECTOR, value = "p[class='ct-subline']")
        article_date = ct_subline.find_element(By.TAG_NAME,value='time').text
        return article_date

def getLinkToArticleFullWebsite(article):
        finding_demo_link_div_a= article.find_element(By.CSS_SELECTOR, value = "div[class='ct-latest-right-side']").find_element(By.TAG_NAME,value='a')
        link_to_article_full_website = finding_demo_link_div_a.get_attribute('href')
        return link_to_article_full_website

def findArticleName(temp_demo_link_article):
        article_name = temp_demo_link_article.find_element(By.TAG_NAME,value='header').find_element(By.TAG_NAME,value='h1').text
        return article_name

def findArticleFullWebsiteDemoLink(temp_demo_link_article):
        temp_demo_link_article_anchors = temp_demo_link_article.find_elements(By.XPATH, value="//a[contains(@class,'ct-demo-link')]")
        article_demo_link = None
        if temp_demo_link_article_anchors:
            article_demo_link = temp_demo_link_article_anchors[0].get_attribute('href')
        return article_demo_link

def findArticleFullWebsiteGithubLink(temp_demo_link_article):
        temp_demo_link_article_anchors = temp_demo_link_article.find_elements(By.XPATH, value="//a[contains(@class,'ct-demo-link')]")
        article_github_link = None
        if temp_demo_link_article_anchors:
            article_github_link = temp_demo_link_article_anchors[1].get_attribute('href')
        return article_github_link

def findArticleFullWebsiteGithubStars(driver):
        article_github_link_stars = driver.find_element(By.ID,value='repo-stars-counter-star').text
        return article_github_link_stars
        
def getWebsiteTitles(driver):
        website_titles = driver.find_elements(By.XPATH, value="//h1 | //h2 | //h3 | //h4")
        if len(website_titles) < 4:
            span_anchor_list = driver.find_elements(By.XPATH, value="//span | //a")
            for sp_el in span_anchor_list:
                if(len(sp_el.text) > 0):
                    website_titles.append(sp_el)

        if len(website_titles) > 4:
            website_titles = [website_titles[0],website_titles[1],website_titles[2],website_titles[3]]

        return website_titles


# get css properties of elements

def getFormattedNeededCssProperties(all_css_of_element,css_properties_filters):
        title_css = []
        for css_property_filter in css_properties_filters:
            property_value = all_css_of_element[css_property_filter["name"]]
            if "color" in css_property_filter["name"]:
                property_value = Color.from_string(all_css_of_element[css_property_filter["name"]]).hex
            title_css.append({"name":css_property_filter["caption"] , "value": property_value})
        return title_css

    
def getNamesOfCssPropertiesYouNeedToFilter():
        css_filter = [
            {'name':'font-size','caption':'fontsize'},
            {'name':'font-weight','caption':'fontweight'},
            {'name':'font-family','caption':'fontfamily'},
            {'name':'color','caption':'color'},
            {'name':'background-color','caption':'backgroundcolor'},
            {'name':'height','caption':'height'},
            {'name':'element-length','caption':'elementlength'}
            ]
        return css_filter

def getBodyCssPropertiesYouNeedToFilter():
        css_filter = [
            {'name':'font-size','caption':'fontsize'},
            {'name':'font-family','caption':'fontfamily'},
            {'name':'background-color','caption':'backgroundcolor'},
            {'name':'scroll-height','caption':'scrollheight'},
            {'name':'screen-height','caption':'screenheight'},
            {'name':'screen-width','caption':'screenwidth'},
            {'name':'screen-depth','caption':'screendepth'}
            ]
        return css_filter

def getElementCssPropertiesFromJavascript(element,driver):
        styles =  driver.execute_script('var items = {};' +
                            'var compsty = getComputedStyle(arguments[0]);' +
                            'var len = compsty.length;' + 
                            'for (index = 0; index < len; index++)' +
                            '{items [compsty[index]] = compsty.getPropertyValue(compsty[index])};' +
                            'items["element-length"] = String((arguments[0].innerText).length);' +
                            'items["scroll-height"] = String(arguments[0].scrollHeight) + "px";' +
                            'items["screen-height"] = String(screen.height) + "px";' +
                            'items["height"] = String(arguments[0].scrollHeight) + "px";' +
                            'items["screen-width"] = String(screen.width) + "px";' +
                            'items["screen-depth"] = String(Math.ceil(parseFloat(arguments[0].scrollHeight) / parseFloat(screen.height)));' +
                            'return items;', element)
        return styles

def findMainWebsitePreviousVersions(article_full_website_link,driver):
        demo_versions = []
        correct_nav = None
        navs = driver.find_elements(By.TAG_NAME,value='nav')
        temp_nav = []
        try:
            temp_nav = driver.find_element(By.CSS_SELECTOR, value = "div[class='demos']")            
            navs.append(temp_nav)
        except:
            temp_nav = []
        nav_anchor_tags = []
        for nav in navs:
            nav_classes = nav.get_attribute('class')
            if nav_classes:
                for nav_class in nav_classes:
                    if "link" or "demo" in nav_class:
                        if "menu" not in nav_class:
                            nav_anchor_tags = nav.find_elements(By.TAG_NAME,value='a')
                            if nav_anchor_tags is not None:
                                for anchor in nav_anchor_tags:
                                        try:
                                            if "#" not in anchor.get_attribute('href'):
                                                correct_nav = nav
                                        except:
                                            correct_nav = []
                    
        if correct_nav:
            nav_anchor_tags = correct_nav.find_elements(By.TAG_NAME,value='a')
            for anchor in nav_anchor_tags:
                anchor_href = anchor.get_attribute('href') 
                if anchor_href != None:
                    if "http" not in anchor_href:
                        anchor_href = article_full_website_link  + "/" + anchor_href
                    if "github.com" not in anchor_href:
                         if "codrops" not in anchor_href:
                            temp_item = {
                                "name": anchor.text,
                                "link": anchor_href
                            }
                            demo_versions.append(temp_item)
        
        for index,demo in enumerate(demo_versions):
            demo_versions[index]["_version_titles_name_and_body_css"] = findWebsiteTitleandBodyCss(demo["link"],driver)

        return demo_versions



def findWebsiteTitleandBodyCss(website_full_link,driver):
        
        driver.get(website_full_link)
        height = getElementCssPropertiesFromJavascript(driver.find_element(By.TAG_NAME,value='body'),driver)["height"]
        
        #getting the titles and big heading on the website
        website_titles = getWebsiteTitles(driver)
        css_properties_to_filter = getNamesOfCssPropertiesYouNeedToFilter()
        _website_titles_name_and_body_css = []
        for website_title in website_titles:
            all_css_of_element = getElementCssPropertiesFromJavascript(website_title,driver)
            
            
            if(website_title.tag_name == "span" or website_title.tag_name == "a"):
                all_css_of_element["height"] = all_css_of_element["font-size"]
                
            formatted_css = getFormattedNeededCssProperties(all_css_of_element,css_properties_to_filter)
                
            _website_titles_name_and_body_css.append({"element": website_title.tag_name,"elementtext": website_title.text,"height":height,"css_properties":formatted_css })

        return _website_titles_name_and_body_css


def checkIfDemoExist(length,list,index):
        if length > index:
            return list[index]["link"]
        else:
            return ""

def getwebsiteElementsCssAndVersionLinksInList(website_data_list,driver):
        version_file_list = []
        page_body_height = 0
        screenheight = 0
        website_counter = 0
        for website in website_data_list:
            temp_version_file_list = {}
            website_counter += 1
            temp_version_file_list["primarykey"] = str(website_counter)
            temp_version_file_list["foreignkey"] = " "
            temp_version_file_list["main-link"] = website['_article_full_website_link']
            for index,props in enumerate(website["_website_titles_name_and_body_css"]):
                temp_version_file_list["font-name" + str(index + 1)] = props["element"]
                page_body_height = props["height"]
                for prop in props["css_properties"]:
                    temp_version_file_list[prop["name"] + str(index + 1)] = prop["value"]
            
            
            driver.get(website['_article_full_website_link'])
            body_css_unformatted = getElementCssPropertiesFromJavascript(driver.find_element(By.TAG_NAME,value='body'),driver)
            body_css_formatted = getFormattedNeededCssProperties(body_css_unformatted,getBodyCssPropertiesYouNeedToFilter())
            
            for body_prop in body_css_formatted:
                if body_prop["name"] == "scrollheight":
                   body_prop["value"] = str(page_body_height)
                if body_prop["name"] == "screenheight":
                    screenheight = body_prop["value"]
                if body_prop["name"]  == "screendepth":
                    page_body_height = str(page_body_height).replace("px","")
                    page_body_height = float(page_body_height)
                    screenheight = str(screenheight).replace("px","")
                    screenheight = float(screenheight)
                    if screenheight > 0:
                        body_prop["value"] = str(math.ceil(page_body_height/screenheight))

                temp_version_file_list["body-" + body_prop["name"]] = body_prop["value"]
            version_file_list.append(temp_version_file_list)
            primarykeycounter = website_counter
            version_page_body_height = 0
            version_screenheight = 0
            for vl_index,version_link in enumerate(website["_main_website_previous_links"]):
                temp_version_file_list = {}
                website_counter += 1
                temp_version_file_list["primarykey"] = str(website_counter)
                temp_version_file_list["foreignkey"] = str(primarykeycounter)
                temp_version_file_list[version_link["name"]] = version_link["link"]
                for v_index,version_css in enumerate(version_link["_version_titles_name_and_body_css"]):
                    temp_version_file_list["v" + str(v_index) + str(vl_index)] = version_css["element"]
                    version_page_body_height  = version_css["height"]
                    for element_css_prop in version_css["css_properties"]:
                        temp_version_file_list["v" + element_css_prop["name"] + str(v_index)] = element_css_prop["value"]

                driver.get(version_link["link"])
                version_body_css_unformatted = getElementCssPropertiesFromJavascript(driver.find_element(By.TAG_NAME,value='body'),driver)
                version_body_css_formatted = getFormattedNeededCssProperties(version_body_css_unformatted,getBodyCssPropertiesYouNeedToFilter())
                
                for version_body_prop in version_body_css_formatted:
                    if version_body_prop["name"] == "scrollheight":
                        version_body_prop["value"] = str(version_page_body_height)
                    if version_body_prop["name"] == "screenheight":
                        version_screenheight = version_body_prop["value"]
                    if version_body_prop["name"]  == "screendepth":
                        version_page_body_height = str(version_page_body_height).replace("px","")
                        version_page_body_height = float(version_page_body_height)
                        version_screenheight = str(version_screenheight).replace("px","")
                        version_screenheight = float(version_screenheight)
                        if screenheight > 0:
                            version_body_prop["value"] = str(math.ceil(version_page_body_height/version_screenheight))
                    
                    temp_version_file_list["body-" + version_body_prop["name"]] = version_body_prop["value"]

                version_file_list.append(temp_version_file_list)
        # version_file_list = sorted(version_file_list,key=lambda d:d["elementlength1"],reverse=True)
        return version_file_list
        
        