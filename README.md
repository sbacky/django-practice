# **Social Media Project**

The purpose of this project is to build a simple social network that allows the user to post short text-based messages. Users will be able to follow other users to see their posts or unfollow them to stop seeing their posts.

A high-level overview of the steps that this project, include: Set up the base project, Extend the django user model, Implement a Post-Save hook.

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

At the end of this part, Django admin interface will be able to be used to create users and this will automatically generate a profile for each new user and set up the necessary connection between user and profile models.

1. Implement one-to-one and many-to-many relationships between Django models - COMPLETED
2. Extend the Django user model with a custom Profile model - COMPLETED
3. Customize the Django admin interface - COMPLETED

Step 2: Templates and Front-End Styling

At the end of this part, detail pages and the profile list page will be accessible and can navigate between them. Bulma will also be used to style the pages.

4. Integrate Bulma CSS and style your app - COMPLETED
5. Use template inheritance to reduce repetition - COMPLETED
6. Structure Django templates in a folder hierarchy - COMPLETED
7. Build routing and view functions - COMPLETED
8. Interlink pages of your app using dynamic URLs - COMPLETED

Step 3: Follows and Posts

At the end of this part, basic pages will be built out, and can create posts on the back end and display them on the front end. Users will be able to discover and follow other users and read the contents of the profiles that they follow. They’ll also be able to click a button that sends an HTTP POST request handled by Django to unfollow a profile if they want to stop reading a certain user’s content.

9. Create the front-end interface to let users follow and unfollow profiles - COMPLETED
10. Submit and handle a POST request in Django using buttons - COMPLETED
11. Set up the model for your text-based content - COMPLETED
12. Build styled templates to display content on the front end - COMPLETED
13. Use intricate model relationships in template code - COMPLETED

Step 4: Forms and Submissions

In the fourth part, use Django forms on top of an Messages model to setup form for creating a Message. Build back-end to handle more HTTP POST request submissions so that users can post their text-based messages.

14. Create and render Django forms from your Messages model - COMPLETED
15. Prevent double submissions and display helpful error messages - COMPLETED
16. Interlink pages of your app using dynamic URLs - COMPLETED
17. Refactor a view function - COMPLETED
18. Use QuerySet field lookups to filter your data on the back end - COMPLETED
