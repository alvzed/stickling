import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)


if os.path.exists("env.py"):
    import env
secret_key = os.environ.get('secret_key')

app.config['MONGO_DBNAME'] = 'sticklingDB'
app.config['MONGO_URI'] = 'mongodb+srv://alvzed:%s@sticklingcluster.vbm1p.mongodb.net/sticklingDB?retryWrites=true&w=majority' % secret_key
mongo = PyMongo(app)


@app.route('/')
@app.route('/propagation_station')
def propagation_station():
    return render_template('propagation_station.html',
                           posts=mongo.db.post.find())


@app.route('/greenhouse')
def greenhouse():
    return render_template('greenhouse.html',
                           posts=mongo.db.post.find())


@app.route('/plant_nursery')
def plant_nursery():
    return render_template('plant_nursery.html',
                           posts=mongo.db.post.find())


@app.route('/new_post')
def new_post():
    return render_template('new_post.html')


# @app.route('/create_post')
# def create_post():


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
