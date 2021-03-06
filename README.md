# Stickling

**Stickling** is a platform for finding, buying, selling and trading plants, as well as seeking help for the plants you have and love. Houseplants are a fantastic way of brightening up your day-to-day life, and **Stickling** aims to open up this world to as many people as possible in an easy manner. 

## UX
 
Use this section to provide insight into your UX process, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

#### User stories
- As Emma, I want to buy a new cactus for my living room. 

- As Sanna, I have a monstera I want to trade for a tomato plant. 

- As John, I have a cactus I want to sell since I'm moving abroad and can't take it with me.

- As Elton, I want to rescue my dying plant by seeking advice on how to treat it properly. 

- As Gus, I want to share my knowledge with other people and help them with their plants. 

- As Amund I like to share my plant journey online with other people, both for inspiration and for fun. 


#### Wireframes

All the wireframes were made using balsamiq and were a general approximation for how to layout would actually look. The UI has changed quite a bit since this step in the process.

![Sign up page desktop](/wireframes/signup_desktop.png)

![Login page desktop](/wireframes/login_desktop.png)

The sign up and login pages were designed to be quite simple, and to look quite similar. 

![Propagation station view desktop](/wireframes/propagation_station_desktop.png)

![Plant nursery view desktop](/wireframes/plant_nursery_desktop.png)

![Greenhouse view desktop](/wireframes/greenhouse_desktop.png)

These three images above match what are the three main features of Stickling. They are meant to separate the different types of posts that Stickling focuses on. 

![Mobile view desktop](/wireframes/mobile_view.png)

As you can see there is only one wireframe for the mobile view. It is this way because it was used more to represent the general ratio of the content on the mobile view compared to the desktop view.


## Features

The minimal viable product of this project is based around the CRUD functionality of the posts and comments. The user authentication was deemed as not essential at this point due to the complexity that it would entail. You can read more about this in the features left to implement section. 
 
### Existing Features

- Propagation Station - allows users to view posts of plants for sale or trade, as well as posts requesting to buy certain plants. 
- Plant Nursery - allows users to view posts made by users asking for help with their plants. 

- Create new posts - allows users to create new posts for both Propagation Station and Plant nursery by filling out the necessary information such as email for contact, a photo for the post, etc. 
    - Note that the photos are currently based on Url instead of uploading them, this is due to the limited database size that this project currently has. 
- View posts - allows users to see all the data relating to the post on a focus page for individual posts. It also displays contact, edit, and delete buttons on this page.
- Edit posts - allows users to update the data of the posts by first clicking the edit button and then entering new information into the fields on the page. 
- Delete posts - allows users to remove a post completely by entering a post's focus page and pressing the delete button. 

- Create comments - allows users to leave a comment on specific posts by filling out username and the comment fields.
- Delete comments - allows users to remove a comment by clicking the delete button on the comment. 

- Contact user - allows the user to contect the poster by clicking the Contact button. It then opens up an email with the email address and subject fields filled in. The user only has to fill out the text field and send it. 
    - This feature is only available on posts on the Propagation Station feed. 

### Features Left to Implement
- User authentication - will allow a user to create an account that will store their contact information, username, and more, to prepopulate some fields of posts and comments to relate these to the specific user. This would also solve issues of any user editing or deleting other users' posts. 
- Userpage - will allow users to see all their data on one page as well as their posts. It would also allow ursers to see other users profiles. 
- Notifications - will alert users when others interact with their posts. 

- Greenhouse - this will be a feed with the focus on social aspects, compared to the other feeds that exist in this project. 

- Likes - this feature would mainly be used on the Greenhouse, it would append a list of users that have liked the post and show a total number of likes on the post. 

- Upload photos - this will allow users to upload an image instead of using a url when making a new post. 

- Messages - this will allow users to contact each other directly on the site instead of contacting each other through email. 

- Edit comments -this would allow users to update the posts to correct spelling errors and the like. It would also store the previous edits for all users to access to avoid users using this feature maliciously. 

- Server side validation for forms - the 'new post' and 'new comment' functions currently have no server side validation to avoid any misuse, implementing this will resolve possible issues with the functions. 

- Search - will allow users to display posts that match keywords they have entered into the search bar. 

- Time stamp - will put a timestamp on all posts, which will be used to sort the feeds.


## Technologies Used

- [Flask 1.1.2](https://flask.palletsprojects.com/en/1.1.x/)
    - The project uses **Flask** for all back end functions in the project.

- [Flask PyMongo](https://flask-pymongo.readthedocs.io/en/latest/)
    - The project uses **Flask PyMongo** to communicate with MongoDB.

- [Bootstrap](https://getbootstrap.com/)
    - The project uses **Bootstrap** to speed up the design process and for its grid system.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation, especially on the new post page.


## Testing

This project was put through manual testing. Both by myself and by other people. The things that needed the testing were mainly the CRUD functionality for the posts and the comments, these were put through the following steps.

1. Create posts:
    1. Go to one of the feeds
    2. Click the plus button 
    3. Try to submit the form and verify that it doesn't submit and sends an error message
    4. Repeat step 3 for all the fields (except for the location fields as it isn't required)

**Bugs that appeared** during this test was the fact that any user can go in and remove the required tag of any field and submit the form. This will be fixed in the future when server side validation is added.

*This next step ties into the first test, it can be seen as a continuation of it.*

2. Read posts:
    1. Go to create a post
    2. Fill out all the required fields and press submit, with the feed checkbox set to Propagation Station
    3. Check the feed if the new post has appeared
    4. Return to step 1
    5. Follow step 2 with the feed checkbox set to Plant Nursery and click submit
    6. Check if the new post has appeared on the feed

3. Edit the post:
    1. Click the 'view post' button on the post you want to edit
    2. Check if all the fields are already filled in with the data from the original post
    3. Change some data in any of the fields
    4. Click submit 
    5. Check to see if the update has passed correctly

**Bugs that appeared** during this test was that the edit would remove the feed and emailaddress values from the database and the post would no longer be shown. This has since been fixed.

4. Delete the post
    1. Click the 'view post' button on the post you want to delete
    2. Click the delete button
    3. Check if the post has been removed 

The comments went through similar testing, though it was much simpler since it doesn't require as much testing of the form and the edit function has not been implemented yet. 

1. Create comments
    1. Try to Submit an empty form, see if it shows an error message.
    2. Try to Submit with only one of the fields filled in, see if it shows an error message. Repeat this step, switching which field is filled in. 
    3. Finally submit a filled out form and see if the the comment has now appeared on the post. 

2. Delete a comment
    1. Go to the comment you wish to delete
    2. Click the delete button
    3. Check if the comment has been removed. 

1. Contact a user 
    1. Go to a post on the Propagation Station
    2. Click the 'View Post' button
    3. Click the contact button
    4. Check that an email opens up
    5. Check if the email and subject fields are filled in 

This feature comes with some big security flaws, so it will be replaced with a message board as soon as user authentication is implemented. 


#### How this ties up with user stories

- As Emma, I want to buy a new cactus for my living room. 

Emma can quite easily go onto the Propagation Station and look through the posts if anyone has posted about selling a cactus. If this is the case then she can click 'view post' and then 'contact' to send an email to the seller. 

If there are no posts mentioning a cactus she can make a new post with the about wanting to buy a cactus. 

This user story ties together with John, who was looking to sell a cactus, and he can follow the same steps and then communicate with Emma about selling his cactus to her. 

- As Sanna, I have a monstera I want to trade for a tomato plant. 
Just like Emma, Sanna can look through the Propagation Station if anyone has a tomato plant they want to trade. If not, Sanna can create a new post set to Want to trade saying that she has a monstera and specifying what she'd like  to trade it for.

- As Elton, I want to rescue my dying plant by seeking advice on how to treat it properly. 
- As Gus, I want to share my knowledge with other people and help them with their plants. 

These two stories work together on the Plant Nursery feed. 
Elton can make a post about his dying plant by clicking new post and setting the checkbox to plant nursery. After posting this Gus can look at the post and leave comments to give John advice on how to save his plant. 

- As Amund I like to share my plant journey online with other people, both for inspiration and for fun.

This user story will be solved in the future when user authentication, likes, and the Greenhouse feed has been implemented. 


## MongoDB Schema

The database has two collections: post and comments. The main collection is the post one, as all the comments collection has a one to many relationship with the post collection. 

The post collection looks like this:

![mongodb post collection](/wireframes/datastructure_posts.png)

Note that the indestructible value is only here now to keep the database from being wiped and was entered manually. This value prevents the edit and delete buttons from appearing on the posts. 
It is a fairly simple collection without any nested objects or lists in it. The reason for this will be explained with the structure of the comments collection as seen below: 

![mongodb comments collection](/wireframes/datastructure_comments.png)

As you can see it has two id's in it, the top one is the ObjectId generated by MongoDB and is used for delete comment function. The second id value is the ObjectId of the post it is relating to. It is a separate collection to make deleting and editing comments much easier. 

##### The site now

Due to differences in the scope and the minimal viable product the site ended up with some differences, specifically for the landing page which now looks like this: 

![The deployed landing page](/wireframes/stickling_index.png)
![The deployed landing page for phone](/wireframes/stickling_index_phone.png)

This is mainly because this version doesn't have user authentication as of yet, so the login and sign up pages were not necessary.

The two different feeds that made it to the final version are the Propagation Station and Plant Nursery. Images below. 

![Deployed Propagation Station](/wireframes/prop_stat_index.png)
![Deployed Propagation Station for phone](/wireframes/prop_stat_phone.png)
![The deployed Plant Nursery](/wireframes/plant_nursery.png)
![The deployed Plant Nursery for phone](/wireframes/plant_nursery_phone.png)

As you can see the main difference between these and the wireframes are that the photos are now on the left side of the posts instead of the top. This is because I opted for a title on the posts since it brings more context to them. I felt this was needed due to the nature of the two feeds that have been implement. 

The deployed version also has a 'focus' page which looks like this: 

![The posts](/wireframes/post_focus.png)

This was implemented so that users can add longer description on the posts. These are not present on the feed due to them cluttering up the feeds. 

## Deployment
Below is a short summary of how to deploy a site on Heroku, I do not give as good of an explanation as you can find [on their site](https://devcenter.heroku.com/articles/getting-started-with-python). Please go to this site for a much better explanation.

This project is hosted on Heroku, specifically with the Heroku CLI for python. 
First make sure that you've installed Heroku on your device, if not then install it. 

Login to Heroku through the terminal by typing Heroku login and pressing enter. 
Push the project to Heroku with your preferred method. 
Set up all the config vars you need in the settings of your project (For this project it is IP set to 0.0.0.0, PORT set to 5000 and a variable called secret_uri that contains the URI needed to connect to the MongoDB database). 

Make sure to have a Procfile and requirements.txt so the webapp sets up properly. 

Then launch the site with the command Heroku ps:scale web=1. 
A complete guide to the deployment process can be found [here](https://devcenter.heroku.com/articles/getting-started-with-python).

**The main difference** between the deployed app and the development app can be found on the very top of app.py, you can see the line 'if os.path.exists("env.py"): import env'. This is because there is a .gitignore file that targets the file env.py. In the development version this contains the variable secret_uri that we don't push to github for security reasons. This variable is of course stored in the config vars in Heroku. 


## Credits
A big thank you to Emma and Sanna for giving me feedback on the project during the early stages, and to Vendela, Elvira, Emma (again), and Sanna (again) for helping me with testing. 

Another big thank you to Lovina the cat for providing me with several usernames during testing.


### Content
- The content on this site was made by yours truly and the testers mentioned above.

### Media
- The photos on this site are mainly from [unsplash](https://unsplash.com/s/photos/houseplant).

### Acknowledgements

- I received inspiration for this project from my dying tomato plant, which I seem to be completely unable to save.  