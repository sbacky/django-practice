# **Social Media Project**

The purpose of this project is to build a simple social network that allows user to post short text-based messages. Users will be able to follow other users to see their posts or unfollow them to stop seeing their posts.

A high-level overview of the steps that this project will follow, include: Set up the base project, Extend the django user model, Implement a Post-Save hook.

## **Project Overview**

In the most basic form, a social network needs two things:

1. **User-to-User** Connections that allow people to connect with one another
2. **Content Creation** and display functionality

Additionally, the following steps will be used to build out the necessary functions and features.

* Part 1: Models and Relationships
    * Step 1: Set Up the Base Project
    * Step 2: Extend the Django User Model
    * Step 3: Implement a Post-Save Hook
* Part2: Templates and Front-End Styling
    * Step 4: Create a Base Template with Bulma
    * Step 5: List All User Profiles
    * Step 6: Access Indivisual Profile Pages
* Part 3: Follows and Posts
    * Step 7: Follow and Unfollow other profiles
    * Step 8: Create the Back-End logic for posts
    * Step 9: Display messages on the front end
* Part 4: Forms and Submissions
    * Step 10: Submit posts through Django forms
    * Step 11: Prevent double submissions and handle errors
    * Step 12: Improve the Front-End user Experience 

### **Profiles for User-to-User Connections**

Users will need to form at least the following two connections:

1. Need to have multiple users
2. Each user needs to know about other users

Connections will be implemented using the following assumptions:

* Users will be able to follow or not follow another user.
* If a user follows another user, they will see all of the other users content. If they dont follow the other user, they will not see their content.
* Users can follow a person without being followed back. Relationships can be asymmetrical.
* Users need to be able to see who exists so they know who they can follow.
* Users should be able to see who follows them.
* User functionality will be very basic. Users will not be able to block people or respond to content.

In order to obtain the functionality required, Django's built-in User model will be combined with a custom Profile model that extends the default User model.

|----------|        |------------------------------|
|   User   | -----> |    Profile                   |
|----------|        |------------------------------|
| Built-In |        | User    | OneToOneField (id) |
|----------|        | Follows | ManyToMany (self)  |
                    |------------------------------|

### Text-Based Content

Posts will be the shareable messages that users can create on the social network to share with other users. This content will need three pieces of information:

1. Who wrote it
2. What the message says
3. when the user wrote it

Post messages will connect to the user model through a one to many relationship. This means that one user can have many post messages and each post message belongs to exactly one user.

|------------------------------|        |----------|        |------------------------------|
| Message                      | <----- |   User   | -----> |    Profile                   |
|------------------------------|        |----------|        |------------------------------|
| user       | ForiegnKey (id) |        | Built-In |        | User    | OneToOneField (id) |
| body       | CharField       |        |----------|        | Follows | ManyToMany (self)  |
| created_at | DateTimeField   |                            |------------------------------|
|------------------------------|

>The created_at field will not be editable by the user. This field will be auto set by Django whenever a user submits a new post message.

Users will also need a way to create content and view the content that they and other users in their network have created.

* Provide a form for submitting content
* Create views to handle these submissions
* Build templates to display existing content
* Make it look decent

## Goals

### Part 1: Models and Relationships

Step 1: Set Up the Base Project

1. Activated virtual environment - COMPLETED
2. Created new Django project called myproject - COMPLETED
3. Created Django app called social - COMPLETED
4. Add social to projects INSTALLED_APPS path in settings.py file - COMPLETED
5. Cleaned up admin portal to focus on the essential functionality needed - COMPLETED
6. Created a few users social network - COMPLETED
7. Extended default User model with Profile model - COMPLETED
8. Link User and Profile models with a signal - COMPLETED

Part2: Templates and Front-End Styling

9. Create base.html template to form standard feel of social app - COMPLETED
10. Add template page to display list of all profiles - COMPLETED
11. Add logic to display all profiles minus current logged in user in views.profile_list - COMPLETED
12. Integrate Bulma CSS to style your app - COMPLETED
13. Use template inheritance to reduce repetition - COMPLETED
14. Structure Django templates in a folder hierarchy - COMPLETED
15. Build routing and view functions - COMPLETED
16. Interlink pages of your app using dynamic URLs - COMPLETED