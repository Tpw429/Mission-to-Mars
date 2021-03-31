from flask import Flask, render_template          # Uses Flask to render a template
from flask_pymongo import PyMongo                 # Uses PyMongo to interact with Mongo Database
import scraping                                   # To use Scraping, Convert from Jupyter Notebook to Python


# How to set up Flask
app = Flask(__name__)


# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Define the route for html page
@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)


# Add the Scraping route
   @app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update({}, mars_data, upsert=True)
   return redirect('/', code=302)


#code to run flask
if __name__ == "__main__":
    app.run()