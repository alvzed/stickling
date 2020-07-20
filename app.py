import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)


if os.path.exists("env.py"):
    import env
secret_uri = os.environ.get('secret_uri')

app.config['MONGO_URI'] = secret_uri
mongo = PyMongo(app)


@app.route('/')
def landing_page():
    return render_template('index.html')


@app.route('/propagation_station')
def propagation_station():
    return render_template('propagation_station.html',
                           posts=mongo.db.post.find())


@app.route('/plant_nursery')
def plant_nursery():
    return render_template('plant_nursery.html',
                           posts=mongo.db.post.find())


@app.route('/post/<post_id>')
def view_post(post_id):
    the_post = mongo.db.post.find_one({'_id': ObjectId(post_id)})
    if the_post is None:
        return redirect(url_for('page_not_found'))
    comments = mongo.db.comments.find({'post_id': post_id})
    return render_template('post.html', post=the_post, comments=comments)


@app.route('/new_post')
def new_post():
    return render_template('new_post.html')


@app.route('/create_post', methods=['POST'])
def create_post():
    posts = mongo.db.post
    form = request.form.to_dict()
    posts.insert_one(request.form.to_dict())
    return redirect(url_for(form['feed']))


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


@app.route('/404')
def page_not_found():
    return render_template('404.html')


@app.errorhandler(404)
def error_404(error):
    return page_not_found(), 404


@app.route('/add_comment/<post_id>', methods=['POST'])
def add_comment(post_id):
    comments = mongo.db.comments
    comments.insert_one(request.form.to_dict(),
                        {'$push': {'post_id': ObjectId(post_id),
                                   'comment': request.form.get('comment'),
                                   'username': request.form.get('username')}
                         })
    return view_post(post_id)


@app.route('/delete_comment/<post_id>/<comment_id>')
def delete_comment(post_id, comment_id):
    mongo.db.comments.remove({'_id': ObjectId(comment_id)})
    return view_post(post_id)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
