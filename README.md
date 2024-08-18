Inspiration: 
In Sec 3 I took part in the Swift App Design Challenge and I designed a study organization app with my groupmates that ended up being showcased at SUTD and I really enjoyed designing it so I wanted to create a working version using the skills I have now

What It Does:
After logging in/registering, the web app allows you to book venues to study in, keep track of what topics/subjects you study and for how long, gives you an overview of what you have studied so far and allows you to set a target for how long you want to study for. The app also allows you to make a simple to-do list and lets you track your grades

How It's Built:
I built the app on Replit using Flask. The Login page uses a database containing the username and passwords and the study hours and grades are kept on a csv file. I used Javascript to make a dropdown option in the To-Do List and to make a simple timer

Challenges Encountered:
The CSS looks slightly different on different devices, especially on mobile, causing some of the assets to be off centre and I was unable to make them all display consistently on multiple devices. I also struggled with the javascript as I had to learn about the syntax and I found it difficult to change the html using javascript. Using "GET" and "POST" were also a bit of a challenge as I needed some of the information being sent to remain on the page and not be cleared and it was challenging to understand how session worked. I also struggled a little with connecting the sql database and setting up and deploying the website on PythonAnywhere was difficult as some of my code had to be changed.

Accomplishments that I'm Proud of:
I'm proud of learning some basic Javascript and being able to set up the timer. Although I was unable to send the time recorded from the timer directly to the study_log.csv, I am happy I was able to set up the start, stop and reset buttons. I'm also proud of having a functional login and registration function and of being able to use input type checkbox to create a to-do list.

What I learnt:
I learnt about Javascript and the similarities and differences in syntax with Python and I learnt how to connect an SQL Database to my flask app. I also learnt how to use input type checkbox and I learnt creative ways to use css to style divs into creating a progress bar. I also became more comfortable with using Jinja and using GET and POST methods

Whats next for StudyPal?
I want to learn more Javascript and implement a calendar and schedule system for people to insert important events like examination dates and to have a countdown timer for these important dates. I would also like to use an sql database instead of csv to make it so that the time studied and the tasks in the to-do list can be linked together so you do not have to manually enter in how long you've studied and the information will go directly to the database from the timer and so that the to-do list will be completed automatically. I want to make a user profile system where you can set information about yourself such as what subjects you take and how long you've studied for and see the profiles of others. I want to create a leaderboard to display who has studied the most to encourage users to continue using the app and I want to expand on the venue booking system to allow users to book for consultations too.

