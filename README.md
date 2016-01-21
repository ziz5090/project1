# Overview of Project 1

In Project 1, you will build a substantial real-world database application of your choice. 
This project is split into three parts:

* [Part 1](./part1.md): come up with a web application and design the database on paper using ER-modeling.
* Part 2: implement your database by translating your model into a database schema and example data.
* Part 3: implement an application that accesses and modifies your database.

Pick an application that you will enjoy working with, because you will be working on it for a substantial part of the semester! 
A suggestion is that you build a database about something that you are interested in
-- a hobby, a favorite web site, material from another course, a research project, etc. 

It's nice if you pick an application where you can populate your database using real data, although it is not necessary.
As the project progresses, you'll end up creating a database of at least dozens of entities/relationships. 
If you can get real data to populate your database, it does help a bit, but again it is not needed. 


# Summary of Deadlines

* **9/16**: Find team-mate in class or on Piazza to find one. (no deliverable, but last lecture to find a partner in class!)
* **9/21-25**: Meet with TA or instructor to discuss your application and design (details below).  This is a required meeting.
* **9/28**: Submit Part 1 
* **10/19**: Submit Part 2
* **11/16**: Submit Part 3

<!--
* **9/28**: Submit a hard-copy with your final project description (details below).
-->

Note: you can only use late days for the project description submisson, not for finding a teammate nor for meeting with the TA/instructor.Important note: Please check the Project Lateness Policy carefully. 


# Getting Help

We _strongly suggest_ you use the following heuristic when you encounter bugs.  It's pretty much the
heuristic you would take in any software job, so it's good practicie.

1. Use Google or StackOverflow by searching for the error message 
1. Look for previous answers on Piazza 
1. Ask on Piazza include:
  * what you're trying to do
  * describe the approach you took
  * the error message
  * what solutions you've tried
1. Ask the staff
  
        
Remember: the internet is your friend! 


# Teams

You will carry out this project in teams of two. If you can't find a team-mate, please follow these steps:

* Post a message in the class discussion board on CourseWorks asking for a team mate - the best way.
* Send email to Pranay right away (and definitely before Wed Jan 25 at 5 p.m.) asking him to pair you up with another student without a team-mate. 
  Pranay will do his best to find you a team-mate.
* You do not need to notify us of your team composition. 
  Instead, when you submit the first part of your project you should indicate in your submission your team composition.
* See [part 1](http://www.github.com/w4111/proj1part1#contingency) for a contingency plan to protect yourself in case your team mate drops the class.

### Important notes:

* If you decide to drop the class, or are even remotely considering doing so, please be considerate and notify your team-mate immediately.
* On a related note, do not wait until the day before the deadline to start working on the project, just to realize then that your team-mate has dropped the class or moved to another planet. It is your responsibility to start working on the project and spot any problems with your team-mate early on.
* Please check the Collaboration Policy web page for important information of what kinds of collaboration are allowed for projects.



# Setup and Technologies

We ask you to use some cloud-based technologies for the projects, and many of the instructions are written
assuming their use.  If you are strongly opposed to using the technology, please let us know and we can
try to come up with an alternative, however we *strongly* prefer the use of the following.

### Microsoft Azure machine setup

The staff has worked to setup Microsoft Azure credits for you, so you get experience working
with cloud infrastructure that many modern companies such as Pixar and Apple iCloud.

[Click here and follow the instructions for setup (HW0)](https://github.com/w4111/hw0)


### GitHub

One drawback of using a cloud computing platform is that it is difficult to open GUI text editors
such as notepad or sublime to write your code.  We recommend setting up a version control system, 
such as git on [GitHub](http://www.github.com), so that your team can share your code together.  
This way, you can code on your desktop, commit your changes, and pull the updated changes on your 
cloud virtual machine.

### Flask Python Webserver (For part 3)

We will use the [Flask Python webserver](http://flask.pocoo.org/) in this course.
It is a lightweight webserver that requires a minimal amount of understanding of how the webserver framework is implemented (as compared to other frameworks).
In the class github website, we have included a dummy webserver with an example of how to connect to the database.


To use it, go to your EC2 machine and first install the webserver package:

        pip install Flask

Then type the following and follow the instructions:

        git clone https://github.com/w4111/proj1part3.git
        cd proj1part3/webserver
        python server.py

We strongly recommend reading the following documentations:

* [General Flask Documentation](http://flask.pocoo.org/)
* [Jinja Templates](http://jinja.pocoo.org/docs/dev/templates/): this makes it easy to send data (e.g., arrays, dictionaries) 
  to your HTML code and dynamically render them.



### Computer Accounts

If you would like to use Columbia's unix machines for this course, you will
need a CS account.  You can open one from on the [CRF webpage](https://www.cs.columbia.edu/~crf/accounts/cs.html):
and choose the appropriate "student" category as the _account type_

There is a $50 charge to open a CS account. 
Please refer to CRF's homepage for details on infrastructure and policies of the CS department.
