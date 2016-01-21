# Project 1, Part 1

* Assigned: 1/21
* Due: 2/4 beginning of class, hard copy
* worth 25% of overall Project 1 grade

In part 1 of the project, you will propose an interesting web application of your choosing,
that will be the basis of the rest of Project 1.  You will also design the ER diagram and 
schema of the database, as setup for part 2 of the project.  

This document is pretty long, but please read it all, it should answer most of your questions.

**Important note**: If you observe Jewish or other religious holidays that overlap with this part of the project, please email the instructor to arrange for alternative deadlines.

* [FAQs](#frequently-asked-questions)
* [Project overview: YOU SHOULD READ](http://github.com/w4111/proj1)


* each team should sign up for a slot to meet with the TA (Meeting Signup Link is pending)


# Overview 

This assignment consists of multiple steps.  At a high level, you will

1. Pick a team mate -- go make new friends!

1. Pick an application and write a short proposal about it

1. Meet with a course staff member to go over the proposal and get feedback

1. Revise your proposal based on the feedback, create the ER-diagram and schema of the database.


If you're having trouble thinking of an application, take a look
at any social website (e.g., instagram, reddit, twitter), 
shopping website (e.g., overstock, etsy amazon), or interest website
(e.g., bandcamp, new york times) .  They all have a similar
themes and can be reduced to an appropriate scope for the project.  
For example, shopping websites usually have products, users, orders, shopping carts etc.
You can ignore most "security"-related issues (e.g., user authentication, encryption) in your application,
however you need to protect against SQL injection attacks (for part 3).

You will ultimately submit the following as hard-copies:

1. **Required** Application Proposal

    * You will describe the general "domain" of your application, construct an Entity-Relationship
    diagram for the database, and map it to a relational schema using the mapping technique 
    that we will cover in class. 
    * Try to pick an application with a schema that is relatively substantial, but not too large. 
        * E/R design should have ~5-10 entity sets and a similar number of relationship sets. 
      You will get a sense if your design is too simple or too complex. Please talk with a TA 
      during office hours if you are in doubt about this.
        * Try to make your application interesting, including a variety of different kinds of attribute 
    domains (e.g., strings, integers, etc.) and relationships (i.e., with different key and 
    participation constraints). 
    * It is important that you include as many relevant constraints for your application from the 
      real world as possible in your E/R diagram.
 


<a name="contingency"></a>
1. **Optional but strongly recommended** Contingency plan for two-person teams: 

  * Since students may drop classes, and to prevent last-minute surprises, we suggest that you 
    also include in your submission a "contingency plan" in case a team-mate drops the class 
    later in the semester. 

  * This contingency plan should indicate how you will "downgrade" the project to a simpler 
    one in such a case --including in Part 3, if you follow the Expanded-Design Option--, 
    so that it is appropriate for a single person to complete. 

  * As general guidelines, your E/R design for a one-person project should have around five 
    entity sets and a similar number of relationship sets. This is a ballpark figure only: 
    something in the 3-to-7 range should be fine. 

  * If your team-mate drops the class, rather than finding a new team-mate,
    you will complete the "downgraded" version of your original project. 

  * **if you choose not to submit it when you 
    submit Part 1 and your team-mate drops the class later, you will have to complete the original 
    project as planned, and no exceptions will be made at that point**.



## Step 1: Prepare for meeting with course staff

1. Find a team-mate. There's no need to notify us of this; you will simply indicate who your team-mate is when you submit Part 1.

1. You will work on, and deploy your project on the Azure virtual machines.   
    If your team doesn't have a machine that can `ssh` to Azure, get a CS account.

1. Decide on an application for your project and:
 
  * Write an informal one-paragraph description of the application (less than 20 lines).
    Highlight interesting and challenging parts.  
    The more concrete your written description, the more efficient 
    and useful the meeting with the class staff will be (see below). This paragraph should include:

    1. A high-level description of the general domain of the application. 

    1. Examples of entities and relationship sets, attributes and constraints you will have.
      This does not be finalized, but will make your meeting with the staff substantially better and is strongly
      encouraged.

    1. An idea of what data you will use to populate your database later on.

  * If you chose Option 3a, provide specific details about how users will interact with the site. 
    For example, if your website is based on the Internet Movie Database, 
    your description might describe the general "entities" that are involved, 
    and what types of operations users can perform (e.g.,  find the actors for a movie,
    add new movies, etc).
 
  * If you chose Option 3.b: write an informal one-paragraph description of how to expand your design in Part 3 (<20 lines).

      * It should augment your project --in terms of the number of entity sets, relationship sets, and overall "complexity" of the design-- roughly by 50%. 
      * The extension should be substantial: rather than just adding a few entity sets and relationship sets that are overly similar to those in Part 1 of the project, you are expected to add a truly novel and significant component to your database (following the above "50% increase in complexity" guidelines). 
      * _You do not need an ER diagram for your Part 1 submission_
      * For example, if your Part 1 database follows some variant of the Amazon web shopping site, a substantial expansion for Part 3 could be the addition of a sophisticated "subsystem" for product reviews and ratings, as well as for allowing users to vote on the usefulness of the reviews from other customers, etc. 
       
  * Write a short description of your contingency plan (see above).
 
 
# Step 2: Revise and complete Part 1
 
1. Meet with a TA or the instructor during the week of **TBA** to discuss your design and make sure that it is appropriate (i.e., challenging enough, but not unrealistically so). 
    * This meeting is required and should last about ten minutes. 
    * We will have expanded office hours during that week.  We will not take appointments, so  show up  during office hours.  
    * Both team members should attend the meeting together. 
    * Bring two copies of the written materials for yourself and the staff.
    * **It is a good idea to come earlier in the week.**  If you choose to come later and it is too crowded, then you will be unhappy.

1. After a TA or the instructor has OKed your proposal
    * Modify description based on the feedback
    * Write the ER diagram, specify as many of the real-world constraints for your application as possible. 
    
1. Map your E/R diagram into a relational schema in SQL, preserve the ER constraints

1. Submit a hard copy of the following on the due date
    a. revised one-paragraph description of the application
    b. E/R diagram, 
    c. resulting SQL schema, 
    d. revised one-paragraph description of your expansion plans if Option 3.b
    e. revised contingency plan (optional)
 
1. Keep a copy of all these materials for yourselves, since you will need them for Parts 2 and 3 of the project.




# Grading

Your grade will be split as follows:

* Meeting with class staff: 7 points.

  * If you come to the meeting prepared with your written description, you can expect to get all points, even if you are asked to make changes or revisions to your proposal.

* Quality of final one-paragraph description of your application: 6 points.

   * We will evaluate the overall quality of your final hard-copy one-paragraph description of your application, including how thoroughly you incorporated any revisions suggested during your meeting with the staff.

* Quality of E/R diagram: 6 points.

    * We will evaluate how well your E/R diagram models your proposed application, including how well you modeled any relevant real-world constraints.

* Quality of your SQL schema: 6 points.

    * We will evaluate how well you mapped your E/R diagram, including constraints, into a SQL schema using the technique that we covered in class.


# Frequently-Asked Questions
<a name="faq"></a>

* I have an idea that requires that I work alone. Can I?
    * No.  Please modify your project idea so that it becomes appropriate for a two-person team.

* Can my team have 3 (or 4, or 12) students?
    * No. Your team has to have exactly two students.

* Can I use my favorite DBMS instead of PostgreSQL?
    * No, sorry.  We would like to be more flexible but don't have the staff to handle several diverse systems and platforms. 

* Can I use Ada (or something that's not Python) for Option 3.a?
    * Please see the answer to the previous question.
