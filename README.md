# Your Project's Name

**stickling** is a platform for finding, buying, selling and trading plants, as well as seeking help for the plants you have and love. Houseplants are a fantastiv way of brightening up your day-to-day life, and **stickling** aims to open up this world for as many people as possible in an easy manner. 

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

These three images above match what are the three main features of stickling. All they are meant to separate the different types of posts that stickling focuses on. 

![Mobile view desktop](/wireframes/mobile_view.png)

As you can see these is only one wireframe for the mobile view, it is this way because it was used more to represent the general ratio the content would have on the mobile view compared to the desktop view.


## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.

The minimal viable product of this project is based around the CRUD functionality of the posts and comments. The user authentication was deemed as not essential at this point due to the complexity that it would entail. You can read more about this in the features left to implement section. 
 
### Existing Features

- Propagation Station - allows users to view posts of plants for sale or trade, as well as posts requesting to buy certain plants. 
- Plant Nursery - allows users to view posts made by users asking for help with their plants. 

- Create new posts - allows users to create new posts for both Propagation Station and Plant nursery by filling out the necessary information such as email for contact, a photo for the post, etc. 
    - Note that the photos are currently based on Url instead of uploading them, this is due to the limited database size that this project currently has. 
- View posts - allows users to see all the data relating to the post on a focus page for individual posts. It also displays contact, edit, and delete buttons on this page.
- Edit posts - Allows users to update the data of the posts by first clicking the edit button and then entering new information into the fields on the page. 
- Detete posts - allows users to remove a post comletely by entering a posts focus page and pressing the delete button. 

- Create comments - allows users to leave a comment on specific posts by filling out username and the comment text.
- Delete comments - allows users to remove a comment by clicking the delete button on the comment. 

- Contact user - Allows the user to contect the poster by clicking the Contact button. It then opens up an email ith the email and subject fields filled in. The user then only has to fill out the text field to inquire about the post. 
    - This feature is only available on posts on the Propagation Station feed. 

### Features Left to Implement
- User authentication - will allow a user to create an account that will store their contact information, username and more to prepopulate some fields of posts and comments to relate these to the specific user. This would also solve issues of users editing or deleting other users posts. 
- Userpage - will allow users to see all their data on one page as well as their all their posts. It would also allow other users to see all this. 
- Notifications - will alert users when others interact with their posts. 


- Greenhouse - this will be a feed with the focus being on the social aspects compared to the other feeds that exist in this project. 

- Likes - This feature would mainly be used on the Greenhouse, it would append a list of users that have liked the post and show a total number of likes on the post. 

- Upload photos - this will allow users to upload an image instead of using a url when making a new post. 

- Messages - this will allow users to contact each other directly on the site instead of contacting each other through email. 

- Edit comments -this would allow users to update the posts to correct spelling errors and the like. It would also store the previous edits for all users to access to avoid users using this feature maliciously. 

- Server side validation for forms - the new post and new comment functions currently have no server side validation to avoid any misuse, implementing this will resolve possible issues with the functions. 

- Search - will allow users to display posts that match keywords they have entered into the search bar. 

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


In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

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
As you can see the main difference between these and the wireframe is that the photo is now on the left side of the post instead of the top. This is because I opted for a title on the posts since it brings more context to the post which I felt was needed due to the nature of these two feeds. 

The deployed version also has a a 'focus' page which looks like this: 
![The posts](/wireframes/post_focus.png)
This was implemented so that users can add longer descrition on the posts. These are not present on the feed due to them cluttering up the feeds. 

## Deployment

This project is hosted on Heroku, specifically with the heroku CLI for python. 
First make sure that you've install heroku on your device, if not the install it. 

Login to heroku through the terminal by typing heroku login and pressing enter. 
Push the project to heroku with your preferred method. 
Set up all the environment variables you need in the settings of your project (For this project it is IP set to 0.0.0.0, PORT set to 5000 and a variable called secret_uri that contains the URI needed to connect to the MongoDB database). 

Make sure to have a procfile and requirements.txt so the webapp sets up properly. 

Then launch the site with the command heroku ps:scale web=1. 
A complete guide to deployment process can be found [here](https://devcenter.heroku.com/articles/getting-started-with-python)

**The main difference** between the deployed app and the development app can be found on the very top of app.py, you can see the line 'if os.path.exists("env.py"): import env'. This is because there is a .gitignore file that targets the file env.py. In the development version this contains the variable secret_uri that we don't pushed to github for security reasons. This variable is of course stored in the config vars in Heroku. 


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X