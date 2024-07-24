# ProjectTracker

## Features
- **User Registration and Authentication:** Users can sign up, log in, and manage their profiles.
- **Project Management:** Users can create, edit, and delete projects. Projects can transition through different states: draft, ongoing, completed, and cancelled.
- **Task Management:** Within each project, users can create, edit, and delete tasks. Tasks can be associated with specific projects.
- **State Management:** Projects can transition between states: draft, ongoing, completed, and cancelled.

## Wireframes
### Design Wireframes:
* Create wireframes for the main pages of the application (registration, login, dashboard, project management, task management) to guide the frontend development.

## Models
1. **User:** Stores user information and authentication details.
2. **Profile:** Stores additional user information like bio, profile picture.
3. **Project:** Stores details of projects, including title, description, state, and timestamps.
4. **Task:** Stores details of tasks, including title, description, due date, status, and associated project.
5. **Comment:** (Optional) Stores comments on projects or tasks.

## Tech Stack
- **Backend:** Django for API development and user authentication.
- **Frontend:** Plain JavaScript and Bootstrap for the user interface.

## Implementation Outline

### Backend (Django)
1. **Set Up Django Project:**
   - Initialize a new Django project and configure the settings, including the connection to the Supabase database.
2. **Create User Model and Authentication Endpoints:**
   - Implement the user model and endpoints for user registration, login, and profile management using Django REST Framework.
3. **Develop Project Model and Endpoints:**
   - Create the project model with fields for title, description, and state. Implement CRUD endpoints for managing projects.
4. **Develop Task Model and Endpoints:**
   - Create the task model with fields for title, description, due date, status, and associated project. Implement CRUD endpoints for managing tasks.
5. **Develop Comment Model and Endpoints (Optional):**
   - Create a comment model for adding comments to projects or tasks. Implement CRUD endpoints for managing comments.
6. **Test Backend with Postman:**
   - Use Postman to test all API endpoints for user, project, task, and comment management to ensure they function correctly.

### Frontend (Plain JS + Bootstrap)
1. **Set Up Frontend Project:**
   - Initialize a new frontend project using plain JavaScript and configure Bootstrap for styling.
2. **Develop Registration and Login Pages:**
    - Create the registration and login pages with forms for user input and connect them to the backend authentication endpoints.
3. **Develop Dashboard Page:**
    - Implement the dashboard page to display the user's projects, with options to add, edit, delete, and view tasks.
4. **Develop Project Management:**
    - Create forms and functionality to add, edit, and delete projects, and update the project state.
5. **Develop Task Management:**
    - Create forms and functionality to add, edit, and delete tasks within projects.
6. **Implement State Management:**
    - Ensure that projects can transition between draft, ongoing, completed, and cancelled states through the frontend interface.
7. **Integrate Comments (Optional):**
    - Add functionality to view, add, edit, and delete comments on projects and tasks.

### Database and Hosting
1. **Configure Supabase Database:**
    - Set up the Supabase database, create necessary tables and configure Django to connect to it.
2. **Deploy Backend to Heroku:**
    - Deploy the Django backend to Heroku, ensuring that all environment variables and configurations are set up correctly.
3. **Deploy Frontend to Heroku:**
    - Deploy the frontend to Heroku and configure it to communicate with the backend.
4. **Set Up Content Delivery Network (CDN) (Optional):**
    - Consider using a CDN like Cloudinary for storing and serving images to ensure faster load times and handle Heroku’s sleep mode limitations.

### Testing and Optimization
1. **End-to-End Testing:**
    - Perform end-to-end testing of the entire application to ensure all components work together seamlessly.
2. **Optimize Performance:**
    - Optimize the performance of the frontend and backend, ensuring quick load times and efficient API calls.
3. **Prepare for Launch:**
    - Finalize all features, ensure all documentation is complete, and prepare the application for launch.

### User Stories

## Site Users
* As a new user, I'll be informed about the benefits of using the webpage/webapp before signing up.
* As a new user, I want to get a confirmation e-Mail, with a link for activating my account.
* As a user, I can register so that I can create, edit, and delete my projects.
* As a user, I can choose a due date for my project to set a deadline.
* As a user, I can choose a creation date for my project, which is default set to "today" to keep track of when I started the project.
* As a user, I can view all of my projects on a dashboard to manage them efficiently.
* As a user, I have access to my profile and can edit or add data to keep my information up to date.
* As a user, I can mark my project to be public to share it with others.
* (Optional) As a potential user, I can view how many users/requests the website has so that I know if it's a real deal before signing up.
* (Optional) As a potential user, I can view publicly made project histories to understand the types of projects managed on the platform.
* (Optional) As a registered user, I can add comments to a public project to provide feedback or suggestions.
## Mobile Users
* As a mobile user, I have a different view that helps me to scroll through my existing projects easily and efficiently.
* As a mobile user, I can access all the features available to desktop users but in a mobile-optimized layout for a better user experience.
## Admin
* As an administrator, I can access the admin panel so that I can monitor the page and existing users to ensure everything is running smoothly.
* As an administrator, I can manage user accounts, including the ability to deactivate or delete accounts if necessary.
* As an administrator, I can oversee all projects, including the ability to edit or delete any project to maintain the quality and appropriateness of content on the platform.
* As an administrator, I can view and manage comments on public projects to ensure they adhere to community guidelines.