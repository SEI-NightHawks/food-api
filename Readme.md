# Django Backend API Documentation

This README provides an overview of the Django backend for a blog application. The provided code includes views, URLs, and serializers for managing user profiles, posts, comments, and likes.

### Team Members
<img src="ReadmeImages/T0351JZQ0-U05JL6LL5A8-0e474603f175-512.png"  width="30" height="30">  Chris Hercules (github: https://github.com/???    )

<img src="ReadmeImages/T0351JZQ0-U05QYAYE86B-1d4a9d9e85cd-72.png"  width="30" height="30">  Elisa Potillo (github: https://github.com/???    )

<img src="ReadmeImages/T0351JZQ0-U05QZ7VBNQG-c4f2d7c7fbf4-512.png"  width="30" height="30">  Jeanpierre Capunay (github: https://github.com/???    )

<img src="ReadmeImages/110782743-2.png"  width="30" height="30">  Manasavi Saluja (github: https://github.com/???    )

<img src="ReadmeImages/T0351JZQ0-U05QZ7WDK6C-868bfc71e1bc-512.png"  width="30" height="30">  Ryan Gelman (github: https://github.com/???    )

<img src="ReadmeImages/T0351JZQ0-U05QN5UN857-7c2e3de4d611-72.jpeg"  width="30" height="30">  Stuart Shapiro (github: https://github.com/sbshap828)

<img src="ReadmeImages/T0351JZQ0-U05QZ7WDK6C-868bfc71e1bc-72.png"  width="30" height="30">  Sara Mejia (github: https://github.com/???8)

<img src="ReadmeImages/T0351JZQ0-U05S5H67CP3-80c403ec2a12-72-2.png"  width="30" height="30">  Titus Hull Faulkner (github: https://github.com/Empairim    )




## Component Hierarchy
![Alt text](<Screenshot 2023-12-11 at 1.45.22 PM.png>)

### Project Schedule
|Day|Deliverable|Status|
| ---- | --------- | ----- |
| Dec 5 | Concept Approval, GitHub Setup, Development of "Team Expectations" document | Complete |
| Dec 6 | Wireframes and Component Structure |
| Dec 7 | Project Approval | Complete |
| Dec 9 | Back End Development |
| Dec 11| Front End and Authentication | Complete |
| Dec 12| Debugging | Complete |
| Dec 13| Testing and Documentation Update| Complete |
| Dec 14| Presentation | Incomplete |





## Endpoints and Paths

### User Routes

- `POST /users/register/`: Register a new user. [Urls.py]
- `POST /users/login/`: Login user and get authentication tokens. [Urls.py]
- `PUT /user/profile/`: Update user profile (requires authentication). [Urls.py]

### User Posts Routes

- `GET /user/posts/<int:user_profile_id>/`: Retrieve all posts by a specific user profile ID. [Urls.py]

### Post Routes

- `GET /posts/`: Retrieve all posts. [Urls.py]
- `POST /posts/`: Create a new post (requires authentication). [Urls.py]
- `GET /posts/<int:pk>/`: Retrieve a specific post by ID. [Urls.py]
- `PUT /posts/<int:pk>/`: Update a specific post by ID (requires authentication). [Urls.py]
- `DELETE /posts/<int:pk>/`: Delete a specific post by ID (requires authentication). [Urls.py]

### Comment Routes

- `GET /comments/`: Retrieve all comments. [Urls.py]
- `POST /comments/`: Create a new comment (requires authentication). [Urls.py]
- `GET /comments/<int:pk>/`: Retrieve a specific comment by ID. [Urls.py]
- `PUT /comments/<int:pk>/`: Update a specific comment by ID (requires authentication). [Urls.py]
- `DELETE /comments/<int:pk>/`: Delete a specific comment by ID (requires authentication). [Urls.py]

### Like Routes

- `GET /likes/`: Retrieve all likes. [Not implemented]
- `POST /likes/`: Create a new like (requires authentication). [Not implemented]
- `GET /likes/<int:pk>/`: Retrieve a specific like by ID. [Not implemented]
- `PUT /likes/<int:pk>/`: Update a specific like by ID (requires authentication). [Not implemented]
- `DELETE /likes/<int:pk>/`: Delete a specific like by ID (requires authentication). [Not implemented]

## Code Structure

### Files and Functions

- `Urls.py`: Contains URL patterns mapping to views.
- `Views.py`: Includes view classes for various API endpoints.
- `Admin.py`: Registers models for Django admin interface.
- `Manage.py`: Django's command-line utility for administrative tasks.

### Usage

To run the Django application, use the `manage.py` script:

1.  Clone
2.  CD into the directory
3.  pipenv install
4.  pip env shell
5.  posql -p create-database
6.  python manage.py migrate
7.  python manage.py makemigtations
8.  python manage.py runserver
9.  This ruuns from localhost 8000

### File Schemas
iuuig