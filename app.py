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


@app.route('/post/<post_id>')
def view_post(post_id):
    the_post = mongo.db.post.find_one({'_id': ObjectId(post_id)})
    return render_template('post.html', post=the_post)


@app.route('/new_post')
def new_post():
    return render_template('new_post.html')


@app.route('/create_post', methods=['POST'])
def create_post():
    posts = mongo.db.post
    posts.insert_one(request.form.to_dict())
    return redirect(url_for('propagation_station'))


@app.route('/edit_post/<post_id>')
def edit_post(post_id):
    the_post = mongo.db.post.find_one({'_id': ObjectId(post_id)})
    return render_template('edit_post.html', post=the_post)


@app.route('/update_post/<post_id>', methods=['POST'])
def update_post(post_id):
    posts = mongo.db.post
    posts.update({'_id': ObjectId(post_id)},
                 {
                    'title': request.form.get('title'),
                    'picture': request.form.get('picture'),
                    'location': request.form.get('location'),
                    'barter': request.form.get('barter'),
                    'description': request.form.get('description')
                 })
    return redirect(url_for('propagation_station'))


@app.route('/delete_post/<post_id>')
def delete_post(post_id):
    mongo.db.post.remove({'_id': ObjectId(post_id)})
    return redirect(url_for('propagation_station'))


@app.route('/add_comment/<post_id>', methods=['POST'])
def add_comment(post_id):
    post = mongo.db.post
    post.update({'_id': ObjectId(post_id)},
                {'$push': {'comments': {'comment': request.form.get('comment'),
                           'username': request.form.get('username')}}
                 }, upsert=True)
    return redirect(url_for('propagation_station'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
