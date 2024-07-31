

=======================================

# ProjectTracker

## Introduction

ProjectTracker is a web application designed to help users manage and track their projects efficiently. With a sleek, modern interface and user-friendly features, ProjectTracker aims to streamline project management tasks for individuals and teams.

## Key Features

- **User Authentication**: Secure sign-in system to protect user data and projects.
- **Project Management**: Create, update, and track multiple projects.
- **Responsive Design**: Fully responsive interface that works on desktop and mobile devices.
- **Custom Styling**: Unique color scheme and design elements for a distinctive user experience.

## Technical Stack

- **Backend**: Built with Django, a Python framework.
- **Frontend**: HTML, CSS, Javascript, leveraging Bootstrap Design Libraries
- **Database**: POSTGRESQL hosted on SUPABASE

## Getting Started

To begin using ProjectTracker, simply navigate to the homepage and create an account. Once logged in, you'll have access to all the project management tools at your fingertips.

---
![Responsive Mock](docs/src/Responsive_Design.webp)

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

## Features

### Future Features (out of scope)

- Enhance UX, leverage full capabilities of Django's message framework for a seamless User Experience
- Comments Section, enable commenting on public projects. Generating insight for project creators.
- More colors do distinguish more clearly the state of a project, is it a Draft? or maybe it's already Finished?

## Design

Rather simple but clear design patterns.

### **Fonts**

* Montserrat <br>

        A sans-serif font used for headings and emphasis. Applied with weights 600 (semi-bold) and 700 (bold).

* Roboto  <br>
        
        A clean, modern sans-serif font used for body text and general content. Applied with weights 300 (light), 400 (regular), and 700 (bold).



### **Colors**

| Used for Background gradient| Highlight buttons on hover|Theme color for footer| Highlight correct answer|Highlight incorrect answer|
|----------------------------------------|---------------------------------------------|-------------|----------|--------|
|![Deep navy](assets/media/doc/colors/00c3ff.webp)|![Accent blue](assets/media/doc/colors/0077ff.webp)|![footer dark](assets/media/doc/colors/303030.webp)|![highlight lightgreen](assets/media/doc/colors/90ee90.webp)|![highlight lightcoral](assets/media/doc/colors/f08080.webp)|

## Technologies, Libraries & Sources

## Deployment

This project is a Django application. The required dependencies are listed in `requirements.txt`. All sensitive information and settings are stored in an `env.py` file for local development, and as config vars for production deployments like Heroku.

### Requirements

- Python 3.12.4
- Dependencies listed in `requirements.txt`:
    - asgiref==3.7.2
    - certifi==2024.7.4
    - Django==5.0.7
    - djangorestframework==3.15.2
    - python-decouple==3.8
    - gunicorn==20.1.0
    - psycopg2==2.9.9
    - supabase==2.5.3
    - whitenoise==6.0.0
    - cloudinary==1.40.0

### Local Development Setup

#### Mac (VS Code)

1. Clone the repository:
'''bash
$ git clone <repository-url>
'''

2. Change into the project directory:
'''bash
$ cd ProjectTracker
'''

3. Create a virtual environment:
$ python3 -m venv venv

4. Activate the virtual environment:
$ source venv/bin/activate

5. Install the required dependencies:
$ pip install -r requirements.txt

6. Run the development server:
$ python manage.py runserver

7. Access the application in your browser at http://localhost:8000/

8

```




### **Technologies**

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [OOP](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object-oriented_programming) - Concept of Object-Oriented Programming

### **Libraries & Sources**

- [Git](https://git-scm.com/) - For version control.
- [GitHub](https://github.com/) - Deployment of the website and storing the files online.
- [Google Fonts](https://fonts.google.com/) - Imported main fonts for the website.
- [Am I Responsive](https://ui.dev/amiresponsive) - Mockup responsive image for the README file.
- [W3C Javascript](https://www.w3schools.com/js/js_callback.asp) - Guide on Callbacks, Async/Await functionality.
- [GeeksForGeeks](https://www.geeksforgeeks.org/css-gradients/) - Guide on CSS Gradients and pulse animations.

## Frameworks, Software & Hardware

### **Frameworks**

No Frameworks were used; *vanilla* JavaScript is the key to this project.

### **Software**

- **Visual Studio Code** as IDE with the following Extensions:
  <details>
  <summary>Extensions:</summary>
  <img src="assets/media/doc/VisualCodeExtensions.webp" alt="Visual Studio Code Extensions">
  </details>
  
- **CodeAnywhere** as IDE, switched in favor of VSCode due to restrictions in CodeAnywhere.
- **QuickTime Player** in combination with **VB Cable** for creating the recordings for the audio files and trimming them to the correct length.
- **Google Chrome** for the main development.
- **Chrome Dev Tools** for the main development, debugging, and logging.
- **Slack** for interaction with my cohort and mentor.

### **Hardware**

**Used for development:**

- MacBook Pro M1 (2020)

**Used for Testing:**

- MacBook Pro M1 (2020)
- Redmi 11S
- iPhone SE (2022)
- iPhone 13 Pro
- iPhone 14 Pro Max

## Manual Testing

The website was tested on both Android and iOS devices. Desktop and various browsers mentioned in the [Browser Compatibility](#browser-compatibility) section.

### Features Testing

The testing was split into visuals and logic.

#### **Visuals**

| Action                                 | Expected Reaction                           | Test Result |
|----------------------------------------|---------------------------------------------|-------------|
| Navbar: Hover                          | Enlarged hovered section title              | Success     |
| Section: Hover                         | Shadow appears                              | Success     |
| Audio Button: Hover                    | Enlarged inner text                         | Success     |
| Audio Button: Hover                    | Highlight                                   | Success     |
| Audio Button: Click                    | Displays audio control                      | Success     |
| Audio Button: Click                    | Hides audio button                          | Success     |
| Correct Score: Value Change            | Highlight                                   | Success     |
| Incorrect Score: Value Change          | Highlight                                   | Success     |
| Phrase: User Answers Correctly         | Highlight                                   | Success     |
| Phrase: User Answers Correctly         | Timer is displayed                          | Success     |
| Display of Next Phrase                 | Hint is closed                              | Success     |
| Footer Icon: Hover                     | Icon enlarges                               | Success     |

#### **Logic**

| Action                                | Expected Reaction                           | Test Result |
|---------------------------------------|---------------------------------------------|-------------|
| Navbar: Click                         | Navigates to section                        | Success     |
| Audio Control: Play                   | Audio plays                                 | Success     |
| Audio Control: Play                   | Stops other audio                           | Success     |
| Incorrect Answer: Click               | Incorrect counter increases by 1            | Success     |
| Correct Answer: Click                 | Correct counter increases by 1              | Success     |
| Correct Answer: Click                 | Displays correct phrase                     | Success     |
| Correct Answer: Click                 | Disables answer buttons after timeout       | Success     |
| Hint: Click                           | Toggles display of hint section             | Success     |
| All Answers Correct                   | Displays "New game?" alert                  | Success     |
| From 2nd Game Onwards                 | Resets result to 0                          | Success     |

### Lighthouse Performance

#### **Mobile**

Almost perfect score:
<br>
![Mobile result](assets/media/doc/validator/lighthouse_mobile_small.webp).
<br>
You can also view the full [report!](https://dashdothub.github.io/Guess-The-Phrase/assets/media/doc/validator/lighthouse_mobile.html)

#### **Desktop**

Perfect score!
<br>
![Desktop result](assets/media/doc/validator/lighthouse_desktop_small.webp).
<br>
You can also view the full [report!](https://dashdothub.github.io/Guess-The-Phrase/assets/media/doc/validator/lighthouse_desktop.html)

### Validator Testing

There are three validators that were used to analyse the code.

#### **HTML - W3C - Markup Validation Service**

No Errors found, trailing slashes from special tags like '<meta>' were removed for not having any 'INFO' messages in the validator.
<details>
<summary>Validation result:</summary>
<img src="assets/media/doc/validator/w3c_html_result.webp" alt="HTML Validation result">
</details>

#### **CSS - W3C - CSS Validation Service**

No Errors found, warnings were displayed. Imported Fonts could not be checked. CSS variables are currently not statically checked.
<details>
<summary>Validation result:</summary>
<img src="assets/media/doc/validator/w3c_css_result.webp" alt="CSS Validation result">
</details>

#### **JS Validation**

No Errors found, two warnings. Async functions are only available with jshint from ES8
<details>
<summary>Validation result:</summary>
<img src="assets/media/doc/validator/jshint_result.webp" alt="JS Validation result">
</details>

### Browser Compatibility

## Browsers support

| [<img src="https://raw.githubusercontent.com/alrra/browser-logos/master/src/edge/edge_48x48.png" alt="IE / Edge" width="24px" height="24px" />](http://godban.github.io/browsers-support-badges/)<br/>IE / Edge | [<img src="https://raw.githubusercontent.com/alrra/browser-logos/master/src/firefox/firefox_48x48.png" alt="Firefox" width="24px" height="24px" />](http://godban.github.io/browsers-support-badges/)<br/>Firefox | [<img src="https://raw.githubusercontent.com/alrra/browser-logos/master/src/chrome/chrome_48x48.png" alt="Chrome" width="24px" height="24px" />](http://godban.github.io/browsers-support-badges/)<br/>Chrome | [<img src="https://raw.githubusercontent.com/alrra/browser-logos/master/src/safari/safari_48x48.png" alt="Safari" width="24px" height="24px" />](http://godban.github.io/browsers-support-badges/)<br/>Safari | [<img src="https://raw.githubusercontent.com/alrra/browser-logos/master/src/safari-ios/safari-ios_48x48.png" alt="iOS Safari" width="24px" height="24px" />](http://godban.github.io/browsers-support-badges/)<br/>iOS Safari | [<img src="https://raw.githubusercontent.com/alrra/browser-logos/master/src/opera/opera_48x48.png" alt="Opera" width="24px" height="24px" />](http://godban.github.io/browsers-support-badges/)<br/>Opera |
| --------- | --------- | --------- | --------- | --------- | --------- |
| IE11, Edge| last 2 versions| last 2 versions| last 2 versions| last 2 versions| last 2 versions

### Screen size responsiveness

Responsiveness

### Bugs resolved and unresolved

On game end. After all phrases were asked the hint will be overwritten only when a new game will be started. <br> <i>Fixed on 01.11.2023</i>

In the console one error keeps popping out.
![Console Error](assets/media/doc/bugs/ConsoleError.webp)<br>
The error does not hinder any functionality of the webapp or dose have any other influence on the project.

## Deployment

### **GitHub Pages**

1. Log in to GitHub and locate [GitHub Repository Guess The Phrase](https://github.com/DaSHdotHub/Guess-the-phrase)
2. At the navigation bar of the repository tab find "Settings", click.
3. At the left side under the "Code and automation" section, click on "Pages".
4. Next locate the "Source" and set it to "Deploy from a branch", branch should be "main", folder set to "root" and then click on the "Save" button.
5. Head back to the [Project Repository](https://github.com/DaSHdotHub/Guess-the-phrase) and on the right side click on [Deployments](https://github.com/DaSHdotHub/Guess-the-phrase/deployments) and under the "Active deployments" section is the freshly deployed project: [Guess The Phrase](https://dashdothub.github.io/Guess-The-Phrase/)

### **Local run**

- In your favourite IDE clone the project, e.g. following the GitHub instructions unter the button <br>
![Code Button](assets/media/doc/GitHubCode.webp).
- Make sure python3 is installed.<br>
- Inside or outside an IDE run following command from the root directory of the project:<br>
  <code>phyton3 -m http.server</code>

## Credits

### **Inspirations**

For this project, my assigned mentor encouraged me to go for a quiz game, after a short use of search engines I found this website <br>
<https://www.ef.co.uk/english-resources/english-quotes/famous/> (Link was last checked checked on 01.11.2023) <br>
Therefore my idea was born to make a game of guessing the correct phrases.

All design patterns were created by myself.

### **Resources**

#### Media

* [ChatGPT](https://chat.openai.com/) <br>The texts for introduction, howto and rules were written down by myself, afterwards they were altered by ChatGPT v4 to have a specific appealing language.
- [NaturalReaders](https://www.naturalreaders.com/online/)<br>
Audio was created with the help of this website.
- [Convertio.co](https://convertio.co/)<br>
Images and Screenshots were converted by this webservice
- [Godban@GitHub](https://godban.github.io/browsers-support-badges/)<br> Browser compatibility table for this readme.
- [FontAwesome.com](https://fontawesome.com/)<br> For the icons used in the footer.
- [FavIcon.io](https://favicon.io)<br>
Created the favicon

### **Also**

- Big thanks to my wife and my child who are always supporting me at their best :-)
