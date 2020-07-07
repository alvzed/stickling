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
def get_posts():
    return render_template('index.html', posts=mongo.db.post.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
