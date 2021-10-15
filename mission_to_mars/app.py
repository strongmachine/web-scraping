import sys
from flask import Flask, render_template, jsonify, redirect
import pymongo
import scrape_mars


app = Flask(__name__)

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.mars_db
collection = db.mars_facts


@app.route('/scrape')
def scrape():
   # db.collection.remove()
    mars = scrape_mars.scrape()
    print("\n\n\n")

    db.mars_facts.insert_one(mars)
    return "Some scrapped data"



@app.route("/")
def home():
    mars = db.mars_facts.find_one()
    # mars = {"mars_facts_data": news_title}
    print(mars)
    return render_template("index.html", mars = mars)
 

if __name__ == "__main__":
    app.run(debug=True)
