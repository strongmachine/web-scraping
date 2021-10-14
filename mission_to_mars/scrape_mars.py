# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
from urllib.parse import urlsplit
from bs4 import BeautifulSoup as bs
from splinter import Browser
import os
import pandas as pd
import time
from webdriver_manager.chrome import ChromeDriverManager


# -
def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=False)


def scrape():
    browser = init_browser()
    mars_facts_data = {}

    url = "https://redplanetscience.com/"
    browser.visit(url)
    time.sleep(2)


    html = browser.html
    soup = bs(html, "html.parser")

# +
    news_title = soup.find("div", class_="content_title").text
    news_p = soup.find("div", class_="article_teaser_body").text
    print(f"Title:{ news_title}")
    print(f"Paragraph:{news_p}")


# -

    url_image = 'https://www.spaceimages-mars.com'
    browser.visit(url_image)


# +
# https://www.spaceimages-mars.com/image/featured/mars2.jpg

    featured_image_url = "https://www.spaceimages-mars.com/image/featured/mars2.jpg"
# /html/body/div[8]/div/div/div/div/img element xpath

# -

    url_mars_facts = "https://galaxyfacts-mars.com"

    tables = pd.read_html(url_mars_facts)
    tables[0]

# +
# Scrape table in Mars Facts website

    df_facts = tables[0]
    df_facts.columns = ["Parameters", "Values_Mars", "Values_Earth"]
    df_facts.set_index(["Parameters"])
# -

# save images to html table string
    mars_html = df_facts.to_html()
    mars_html = mars_html.replace("\n", "")
    mars_html


# +
# Mars Hemispheres
# -

# Visit hemispheres website
    url_hemispheres = "https://marshemispheres.com/"
    browser.visit(url_hemispheres)

# +
# xpath to grab
#import urlsplit
    xpath = "//*[@id='product-section']/div[2]/div[1]"

# Base Url
    hemisphere_base_url = '{0.scheme}://{0.netloc}/'.format(
    urlsplit(url_hemispheres))
    print(hemisphere_base_url)

# +
# start grabbing imgs

# Cerberus Hemisphere Enhanced
    hemisphere_img_urls = []
    results = browser.find_by_xpath(
    "//*[@id='product-section']/div[2]/div[1]/a/img").click()
    time.sleep(2)
    cerberus_open_click = browser.find_by_xpath(
    "//*[@id='wide-image-toggle']").click()
    time.sleep(1)
    cerberus_image = browser.html
    soup = bs(cerberus_image, "html.parser")
    cerberus_url = soup.find("img", class_="wide-image")["src"]
    cerberus_img_url = hemisphere_base_url + cerberus_url
    print(cerberus_img_url)
    cerberus_title = soup.find("h2", class_="title").text
    print(cerberus_title)
    back_button = browser.find_by_xpath(
    "//*[@id='results']/div[1]/div/div[4]/a/h3").click()
    cerberus = {"image title": cerberus_title, "image url": cerberus_img_url}
    hemisphere_img_urls.append(cerberus)


# +
# Schiaparelli Hemisphere Enhanced

    results1 = browser.find_by_xpath(
    "//*[@id='product-section']/div[2]/div[2]/a/img").click()
    time.sleep(2)
    schiaparelli_open_click = browser.find_by_xpath(
    "//*[@id='wide-image-toggle']").click()
    time.sleep(1)
    schiaparelli_image = browser.html
    soup = bs(schiaparelli_image, "html.parser")
    schiaparelli_url = soup.find("img", class_="wide-image")["src"]
    schiaparelli_img_url = hemisphere_base_url + schiaparelli_url
    print(schiaparelli_img_url)
    schiaparelli_title = soup.find("h2", class_="title").text
    print(schiaparelli_title)
    back_button = browser.find_by_xpath(
    "//*[@id='results']/div[1]/div/div[4]/a/h3").click()
    schiaparelli = {"image title": schiaparelli_title,
                "image url": schiaparelli_img_url}
    hemisphere_img_urls.append(schiaparelli)

# +
# Syrtis Major Hemisphere Enhanced

    results1 = browser.find_by_xpath(
    "//*[@id='product-section']/div[2]/div[3]/a/img").click()
    time.sleep(2)
    syrtis_major_open_click = browser.find_by_xpath(
    "//*[@id='wide-image-toggle']").click()
    time.sleep(1)
    syrtis_major_image = browser.html
    soup = bs(syrtis_major_image, "html.parser")
    syrtis_major_url = soup.find("img", class_="wide-image")["src"]
    syrtis_major_img_url = hemisphere_base_url + syrtis_major_url
    print(syrtis_major_img_url)
    syrtis_major_title = soup.find("h2", class_="title").text
    print(syrtis_major_title)
    back_button = browser.find_by_xpath(
    "//*[@id='results']/div[1]/div/div[4]/a/h3").click()
    syrtis_major = {"image title": syrtis_major_title,
                "image url": syrtis_major_img_url}
    hemisphere_img_urls.append(syrtis_major)

# +
# Valles Marineris Hemisphere Enhanced


    results1 = browser.find_by_xpath(
    "//*[@id='product-section']/div[2]/div[4]/a/img").click()
    time.sleep(2)
    valles_marineris_open_click = browser.find_by_xpath(
    "//*[@id='wide-image-toggle']").click()
    time.sleep(1)
    valles_marineris_image = browser.html
    soup = bs(valles_marineris_image, "html.parser")
    valles_marineris_url = soup.find("img", class_="wide-image")["src"]
    valles_marineris_img_url = hemisphere_base_url + syrtis_major_url
    print(valles_marineris_img_url)
    valles_marineris_title = soup.find("h2", class_="title").text
    print(valles_marineris_title)
    back_button = browser.find_by_xpath(
    "//*[@id='results']/div[1]/div/div[4]/a/h3").click()
    valles_marineris = {"image title": valles_marineris_title,
                    "image url": valles_marineris_img_url}
    hemisphere_img_urls.append(valles_marineris)
# -

# list of dictionaries
# hemisphere_img_urls

    mars_facts_data["hemisphere_img_url"] = hemisphere_img_urls


    return mars_facts_data
