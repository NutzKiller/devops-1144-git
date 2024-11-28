from flask import Flask, render_template
import requests
import json
from pymongo import MongoClient
import os
app = Flask(__name__)

# MongoDB Configuration
app.config["MONGO_URI"] = "mongodb://mongo:27017/dog_images_db"
mongo = PyMongo(app)

@app.route('/')
def home():
    # Fetch a random dog image
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    data = response.json()
    image_url = data['message']
    
    # Check if the image already exists in the database
    existing_image = mongo.db.images.find_one({"image_url": image_url})
    if not existing_image:
        # Save the image to the database if not already present
        mongo.db.images.insert_one({"image_url": image_url})
    
    # Get all saved images from the database
    saved_images = list(mongo.db.images.find({}, {"_id": 0, "image_url": 1}))
    saved_images = [img["image_url"] for img in saved_images]
    
    return render_template('index.html', image_url=image_url, saved_images=saved_images)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
