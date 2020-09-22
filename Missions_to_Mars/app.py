from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import scrape_mars


app = Flask(__name__)

# Create flask_pymongo to set up connection to database
#Engine and a location
app.config['MONGO_URI'] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route('/')
def index():

    news = mongo.db.nasa_news.find_one()
    return render_template("index.html", news=news)

@app.route('/news')
def scrape_news():
    """Returns a JSON list of the most recent news available on Nasa's Mars website """
    recent_news = scrape_mars.scrape()

    #total_results = len(recent_news)
    nasa_news_dict = {"articles": [news for news in recent_news]}
    return jsonify(nasa_news_dict)

@app.route('/scrape')
def scrape():
    """Calls scrape.py and updates MongoDB collections for 'mars_app' database"""

    # Query Mongo database and find latest article
    nasa_news = mongo.db.nasa_news
    news_data = scrape_mars.scrape()
    latest_news = news_data[0]
    nasa_news.update({}, latest_news, upsert=True)

    #Call scrape function
    #latest_news = mongo.db.latest_news
    #mars_data = scrape_mars.scrape()
    #news.update({}, mars_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)


