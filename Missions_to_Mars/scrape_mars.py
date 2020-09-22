# Import our libraries
from bs4 import BeautifulSoup
import requests
from urllib.request import Request, urlopen
import urllib.request
from splinter import Browser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd


def scrape():

# Design function to automate creation of BeautifulSoup objects
    def create_soup(url):
        """Create a BeautifulSoup object by passing a url"""

        # Define path to chromedriver
        executable_path = {'executable_path': 'C:\webdrivers\chromedriver.exe'}
        # Create new browser object
        browser = Browser('chrome', **executable_path, headless=True)
        
        # Extract html
        browser.visit(url)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        
        return soup

    # I. NASA Mars News
    # Scrape NASA Mars News
    mars_url = 'https://mars.nasa.gov/news/'
    mars_source_url = 'https://mars.nasa.gov'

    # Create BeautifulSoup object
    mars_soup = create_soup(mars_url)

    # Loop through soup object to create NASA Mars News dictionary
    results = mars_soup.find_all('li', class_="slide")
    news_json = []
    for result in results:
        title = result.find('div', class_='content_title').a.text.strip()
        description = result.find('div', class_='article_teaser_body').text.strip()
        
        extension = result.a['href']
        article_url = f'{mars_source_url}{extension}'

        news_dict = {
            'title': title,
            'description': description,
            'url': article_url
        }
        
        news_json.append(news_dict)
    
    return news_json

    # #II. Featured image
    # img_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

    # # III. Mars Hemispheres
    # # URLs for scraping photos
    # hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    # base_url = 'http://astrogeology.usgs.gov'

    # # Go on index url and create BeautifulSoup object. Scrape to find URL of hemispheres extension
    # soup_index = create_soup(hemispheres_url)
    # containers = soup_index.find_all('div', class_="item")
    # url_list = [base_url + container.a['href'] for container in containers]

    # # Create a loop that visits all 4 sites, creates BeautifulSoup objects and retrieves img src parsing html
    # hemisphere_image_urls = []

    # for url in url_list:
    #     soup = create_soup(url)
        
    #     title = soup.find('h2', class_='title').text.strip()
    #     title = title.replace(' Enhanced', '')
        
    #     img_container = soup.find('div', class_='downloads')
    #     img_href = img_container.li.a['href']
    #     img_url = f'{base_url}{img_href}'
        
    #     dict_entry = {'title': title,
    #                 'img_url': img_url}
        
    #     hemisphere_image_urls.append(dict_entry)

    #return news_json