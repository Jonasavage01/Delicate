
# Delicate Web Application


## Description:
Delicate is a long-term project aiming to establish an online presence for our family-owned organic soap business, "Delicate." Specializing in organic soap production, our website serves as a platform for customers to learn about who we are, our products, and the values we uphold. The project originated from the need to create an accessible space for our customers to connect with our brand, stay informed, and eventually make purchases.

## Project Purpose:
The primary goals of the Delicate web application are as follows:

- **Informative Platform:**
  - Provide visitors with insights into our family business, highlighting our mission, values, and commitment to organic soap production.

- **Product Showcase:**
  - Display our range of organic soap products, allowing customers to explore and learn about each item.

- **Educational Blog:**
  - Offer valuable content through our blog, providing educational information about organic products, ingredients, and sustainable practices.

- **Newsletter Subscription:**
  - Allow users to subscribe to our newsletter for regular updates, promotions, and relevant content.

- **User Accounts:**
  - Enable users to create accounts, log in, and eventually access features like online shopping and favoriting products.

- **Help and Contact Section:**
  - Provide a direct messaging feature for users to contact us with inquiries or feedback.

## Project Development Choices:
The decision to embark on this project was driven by our desire to:

- **Connect with Customers:**
  - Establish an online presence to connect with our audience and share the story behind our products.

- **Expand Functionality Over Time:**
  - The project is designed for scalability, allowing the addition of new features and functionalities as the business grows.

- **Provide a Seamless User Experience:**
  - The website layout and design aim to offer a seamless and visually appealing experience for visitors.

## Future Enhancements:

- **Search Functionality:**
  - Although the search bar is currently non-functional, future updates will implement a robust search feature.

- **User Account Features:**
  - Once completed, user accounts will provide additional functionalities such as favoriting products and making purchases.

 - **Responsive Design:**
  - Responsive design functionality has not been implemented yet but is planned for future updates.



## Project Structure:
The project is organized as follows:

- **`templates/`**
  - `index.html`: Home page.
  - `contact.html`: Contact page.
  - `blog.html`, `blog-page1.html`, `blog-page2.html`, `blog-page3.html`: Blog pages.
  - `log-in.html`, `exitoso.html`, `register.html`: User authentication pages.
  - `shop.html`: Product catalog page.
  - Product pages: `product1.html`, `product2.html`, ..., `product8.html`.

- **`static/`**
  - **CSS:**
    - `index.css`, `shop.css`, `blog.css`, `contact.css`, `about-us.css`, `blog-pages.css`.
    - `log-in.css`, `register.css`, `exitoso.css`.

  - **Images:**
    - Folder containing images for various sections.

- **`app.py`**: Contains the main application logic and routes.

- **`final-project.db`**: Database file.

- **Readme.md**: Documentation file.



# Analysis of the `index.html` Template

Let's incorporate the requested additional sections and explain the functionality of the newsletter subscription area.

## Updated Structure

### Header (`<head>`):
- Includes metadata, links to Bootstrap, and local style files.
- Sets the page title and site icon.

### Body (`<body>`):
- Begins with a header (`<header>`), containing a search bar, icons, and the page logo.
- Navigation bar (`<nav>`) with links to key sections and a contact icon.
- Banner (`<div class="breadcrumbs">`):
  - Displays the current location with a banner background and a prominent button to explore the store.
- Main Images Section (`<section class="main-images">`):
  - Presents attractive images with promotional text.
  - Includes a "Shop" button with a visible shopping cart.
- Benefits Section (`<section>`):
  - Highlights key benefits with icons and descriptive text.
  - Communicates important aspects like "100% organic," "24/7 Customer Support," and "100% secure payment."
- Featured Products (`<section class="featured-products">`):
  - Showcases a selection of featured products with links to individual pages for more details.
- Newsletter Subscription (`<section class="call-to-action">`):
  - Invites users to subscribe to the newsletter to receive the latest posts, products, and exclusive photos.
  - Includes a subscription form with an email input field and a "Subscribe" button.
  - Functionality is supported by JavaScript scripts that handle email entry and verification.
- Blog Updates (`<section class="blog-updates">`):
  - Displays the latest blog updates, each with a title and a link to the full blog page.

### Footer (`<footer>`):
- Contains copyright information ("Copyright © 2023 | Delicaté").

## Key Functionalities

### Featured Products Section:
- Allows visitors to explore some featured products directly from the home page.

### Newsletter Subscription:
- Invites users to subscribe to receive updates and exclusive news.
- The form is validated with scripts to ensure the entry of a valid email.

### Blog Updates:
- Provides quick links to the latest blog posts, encouraging exploration of the content.

### Subscription Logic (Flask):
- The /subscribe endpoint handles server logic to process newsletter subscriptions.
- Data is sent as JSON, and email validation is performed before insertion into the database.



# Delicate Web Application - Contact Page

## Description

The Contact page of the Delicate web application serves as a crucial point of interaction between the business and its customers. This page provides users with various means to get in touch, whether it's for inquiries, assistance, or simply to say hello. The page is designed to be user-friendly, encouraging visitors to engage with the brand in a personalized manner.

## Page Purpose

### Contact Information
Display the business's contact details, including the physical address, email addresses, and phone numbers. This information is essential for users who prefer traditional means of communication.

### Contact Form
Offer a user-friendly contact form that allows visitors to send messages directly from the website. The form includes fields for the subject, greeting, email, and name. The form encourages users to start their messages with a friendly greeting, creating a warm and approachable communication environment.

### Send Message Button
The "Send Message" button triggers the process of sending the user's input to the server. The server-side logic, implemented in the Flask backend, handles the submission and processing of user messages.

## Page Structure

### Contact Information Section
The section includes details such as the business's physical address, represented by a map pin icon, and email addresses. The information is presented in a clean and organized layout, making it easy for users to find and use.

### Contact Form Section
The contact form is designed with simplicity and clarity in mind. Each input field is labeled, and there's a clear prompt encouraging users to start with a friendly greeting. The form includes fields for the subject, greeting, email, and name.

### Send Message Button
The "Send Message" button is prominently displayed below the contact form. It triggers the client-side script that collects user input and sends it to the server for further processing.

### Script for Form Validation
The script includes a function (isValidEmail) for validating the format of the email entered by the user. This ensures that users provide a valid email address before submitting the form.

### Script for Sending Message
The sendMessage function collects input from the form, validates the email, and then uses the Fetch API to send the data to the server at the /contact endpoint. Upon receiving a response from the server, the user is alerted with a message indicating the success or failure of the message submission.

## Flask Backend Code

The Flask backend code for processing the contact form is implemented in the /contact endpoint. When a POST request is made to this endpoint, the server extracts the JSON data from the request, including the subject, greeting, email, and name. It then inserts this data into a database table named contact_messages for future reference.

## User Interaction

- Users can fill out the contact form with their message, subject, and contact details.
- The form includes a prompt to encourage users to start their messages with a friendly greeting.
- Clicking the "Send Message" button triggers a validation process and sends the user's input to the server for further processing.
- Upon successful submission, users receive an alert with a success message. If there are issues with the submission, users are alerted with an appropriate error message.

## Conclusion

The Contact page of the Delicate web application plays a crucial role in fostering communication between the business and its customers. With a well-designed contact form and clear presentation of contact information, users are encouraged to reach out, making the overall user experience more engaging and interactive.



# Delicate Web Application - Blog Page

## Description

The Blog page of the Delicate web application is a treasure trove of information, providing readers with insightful articles on skincare, natural ingredients, and healthy living. This page aims to engage visitors and keep them informed about the benefits of organic products, encouraging them to make informed choices for their skin.

## Page Purpose

### Blog Articles
The primary goal is to present captivating blog articles that cover various topics related to skincare. Each article is thoughtfully crafted to provide valuable information and insights.

### Visual Appeal
The page uses visually appealing images to enhance the reading experience. Images related to the blog content create a visually engaging layout.

### Navigation
The navigation menu allows users to explore different sections of the website, including the blog, shop, contact, and about us.

## Page Structure

### Header
- **Title:** "Descubre los mejores jabones orgánicos para tu piel"
- **Search Bar:** Users can easily search for specific topics within the blog.

### Navigation Menu
- **Home:** Navigate to the home page.
- **Tienda (Shop):** Visit the shop section.
- **Blog:** Explore the blog articles (current page).
- **Contacto (Contact):** Access the contact page.
- **Sobre nosotros (About Us):** Learn more about the business.

### Banner
A visually appealing banner section with breadcrumbs, providing a sense of location within the website.

### Featured Blog Articles
1. **Secretos del coco y la avena**
   - Date: Diciembre 12, 2023
   - Image: A captivating image of coconut and oat soap.
   - Brief Description: Introduction to the blog topic, enticing readers to explore the article.

2. **Caléndula. La Flor que Cuida tu Piel**
   - Date: Diciembre 12, 2023
   - Image: An image showcasing the calendula flower.
   - Brief Description: Teaser about the benefits of calendula for skin care.

3. **8 increíbles Beneficios del café**
   - Date: Diciembre 12, 2023
   - Image: Coffee beans or a coffee cup image.
   - Brief Description: Highlighting the surprising benefits of coffee for the skin.

4. **Zumo para tu Piel**
   - Date: Diciembre 12, 2023
   - Image: Image of fresh orange juice or oranges.
   - Brief Description: Exploring how oranges contribute to healthy skin.

### Call-to-Action (Newsletter)
Encouraging visitors to subscribe to the newsletter for the latest updates, products, and exclusive content.

## JavaScript Functions
- **clearExampleEmail():** Clears the example email in the input field on focus.
- **restoreExampleEmail():** Restores the example email if the field is left empty.
- **isValidEmail(email):** Validates the email format.
- **subscribe():** Handles the subscription process, including email validation and confirmation.


# Delicate Web Application - Shop Page

## Description

The "shop.html" page of the Delicate web application is dedicated to providing users with a unique and pleasant shopping experience. This report outlines the structure and functionality of the page to offer a clear understanding of its purpose and features.

## Page Purpose

### Product Catalog
The primary function of the page is to showcase a product catalog, highlighting the variety of organic soaps available for skincare. Each product is accompanied by a detailed description to inform users about its benefits and properties.

### Shopping Experience
The goal is to provide visitors with an easy and enjoyable shopping experience. Users can explore different categories, view product details, and add items to their cart seamlessly.

## Page Structure

### Header
- **Title:** "Explore Organic Soap Collection"
- **Search Bar:** Users can easily search for specific soap types or ingredients within the shop.

### Navigation Menu
- **Home:** Navigate to the home page.
- **Tienda (Shop):** Explore the product catalog (current page).
- **Blog:** Read insightful articles on skincare.
- **Contacto (Contact):** Access the contact page.
- **Sobre nosotros (About Us):** Learn more about the business.


### Individual Product Listings
1. **Coconut & Oat Soap**
   - Price: $
   - Image: ![Coconut & Oat Soap](images/coconut_oat_soap.jpg)
   - Brief Description: Gently exfoliating soap for smooth and radiant skin.

2. **Calendula Bliss Soap**
   - Price: $
   - Image: ![Calendula Bliss Soap](images/calendula_bliss_soap.jpg)
   - Brief Description: Nourishing soap enriched with the goodness of calendula.

3. **Coffee Delight Soap**
   - Price: $
   - Image: ![Coffee Delight Soap](images/coffee_delight_soap.jpg)
   - Brief Description: Invigorating coffee-infused soap for a refreshing bath.




# Delicate Web Application - Register Page

## Description

The "register.html" page of the Delicate web application is dedicated to allowing users to create an account on the platform. This section provides a detailed description of the page's structure, functionalities, and the corresponding Flask backend code.

## Page Structure

### Create an Account Section
- **Title:** "Create Account"
- **Form (`signupForm`):**
  - **Email Input Field:** Allows users to enter their email address.
    - Uses the "email" input type with pattern validation to ensure a valid email format.
    - Required field.
  - **Password Input Field:** Enables users to set their account password.
    - Uses the "password" input type with a minimum length requirement of 8 characters.
    - Required field.
  - **Confirm Password Input Field:** Ensures users re-enter the password for confirmation.
    - Uses the "password" input type with a minimum length requirement of 8 characters.
    - Required field.
  - **Create Account Button:** Submits the form for account creation.

### JavaScript Functions
- **validateAndSubmit():**
  - Validates that the entered passwords match.
  - Submits the form if all validations are successful.

### "Already have an account" Section
- **Text:** "Already have an account"
- **Login Link (`login`):** Redirects users to the login page using the Flask `url_for` function.

## Flask Backend Code

### Routes
- **/register (GET):**
  - Renders the "register.html" page, displaying the account creation form.
- **/register (POST):**
  - Handles form submission for account creation.
  - Obtains user input (email, password, confirm_password) from the form.
  - Validates password matching and displays an error message if needed.
  - Hashes the password using a secure hashing function.
  - Inserts the user into the database.
  - Redirects to the registration success page upon successful registration.

### Functions
- **validate_password(password, confirm_password):**
  - Validates that the entered password and confirm password match.
- **hash_password(password):**
  - Hashes the password using a secure hashing algorithm.
- **insert_user(email, hashed_password):**
  - Inserts the user's email and hashed password into the database.

## User Interaction

1. Users access the "Create Account" section on the register page.
2. They enter their email address, set a password, and confirm the password.
3. Upon clicking the "Create Account" button, the form is submitted.
4. The Flask backend validates the form data, ensuring password match and other criteria.
5. If successful, the user's information is securely stored in the database, and they are redirected to the registration success page.
6. If there are issues with the form submission, error messages are displayed, and the user is redirected to the homepage.

## Conclusion

The register page serves as a critical component for user account creation in the Delicate web application. With client-side validation using JavaScript and secure server-side handling using Flask, the page ensures a seamless and secure registration process for users. The integration of Flask routes and functions facilitates the storage of user information in the database and enhances the overall user experience.

---

# Delicate Web Application - Login Page

## Description

The "log-in.html" page of the Delicate web application allows users to log in to their accounts. This section provides a detailed description of the page's structure, functionalities, and the corresponding Flask backend code.

## Page Structure

### Sign-In Section
- **Title:** "Iniciar sesión"
- **Form (method="post" action="{{ url_for('login') }}"):**
  - **Email Input Field:** Allows users to enter their email address.
    - Uses the "email" input type.
    - Required field.
  - **Password Input Field:** Enables users to enter their account password.
    - Uses the "password" input type.
    - Required field.
  - **Remember Me Option:**
    - A checkbox allowing users to choose whether to be remembered.
  - **"Iniciar sesión" Button:** Submits the form for user login.

### JavaScript Functions
- **validateForm():**
  - Validates the format of the entered email address using a regular expression.
  - Additional validations can be added as needed.
  - Submits the form if all validations are successful.

### "Already have an account" Section
- **Text:** "Ya tiene una cuenta"
- **Register Link (`register`):** Redirects users to the register page using the Flask `url_for` function.

## Flask Backend Code

### Routes
- **/login (POST):**
  - Handles form submission for user login.
  - Obtains user input (email, password) from the form.
  - Validates user credentials using a separate function (`validate_login`).
  - If successful, sets the user's session and redirects to the homepage.
  - Displays an error message and redirects to the login page if the credentials are invalid.
- **/login2 (GET):**
  - Renders the "log-in.html" page, displaying the login form.

### Functions
- **validate_login(email, password):**
  - Validates user login credentials against the database.
- **get_user_id(email):**
  - Retrieves the user ID based on their email address.

## User Interaction

1. Users access the "Iniciar sesión" section on the login page.
2. They enter their email address and password.
3. Upon clicking the "Iniciar sesión" button, the form is submitted.
4. The Flask backend validates the form data, checking the user's credentials.
5. If the credentials are valid, the user's session is established, and they are redirected to the homepage.
6. If there are issues with the form submission or invalid credentials, error messages are displayed, and the user is redirected to the login page.

## Conclusion

The login page is a crucial component for user authentication in the Delicate web application. With client-side validation using JavaScript and secure server-side handling using Flask, the page ensures a seamless and secure login process for users. The integration of Flask routes and functions facilitates the validation of user credentials against the database, enhancing the overall user experience.


# Flask Web Application Documentation

## Configuration and Database Connection

The database configuration is done through an instance of the cs50 SQL class, facilitating interaction with SQL databases. The connection is established with an SQLite database named final-project.db, indicating the use of SQLite as the database engine.

## Session Management

Session configuration indicates it's not permanent (`app.config["SESSION_PERMANENT"] = False`) and is stored in the filesystem (`app.config["SESSION_TYPE"] = "filesystem"`). Sessions do not persist beyond the application's duration and are stored in files on the server's filesystem. The `session` object is used to store user information between requests.

## Routes and Template Rendering

The application defines various routes to handle HTTP requests, including static pages like the home page (`/home`), the "About Us" page (`/Aboutus`), the contact page (`/Contact`), and dynamic pages for blogs and store products. Functions associated with these routes use `render_template` to generate dynamic HTML responses, providing a modular and scalable structure for web content.

## User Registration and Login

The application manages user registration and login with routes like `/register` and `/login`. Passwords are validated during registration, hashed before storing in the database, and users are redirected to a success page (`/success`). Login involves credential validation and establishes a session for the authenticated user.

## Utility Functions

- `validate_password`: Ensures password consistency.
- `hash_password`: Applies a secure hash to passwords.
- `insert_user`: Facilitates the insertion of new users into the database.

## Error Handling

The `handle_exception` function handles any exceptions that may arise during application execution and returns an error message with an HTTP status code of 500. This is crucial for security and user experience, providing a controlled response in case of errors.

## Handling POST Requests

Routes like `/contact` and `/subscribe` handle POST requests to process forms. These routes receive JSON data, perform operations in the database, and return JSON responses, demonstrating the application's ability to handle asynchronous interactions.

## Logic for Dynamic Pages

Routes like `/read_more`, `/read_more2`, etc., demonstrate the ability to dynamically generate content based on URL parameters. This is valuable for applications presenting diverse content, such as blogs or product pages.

## Debugging and Development

The application runs in debug mode (`app.run(debug=True)`), providing detailed information about errors and facilitating development during the construction and testing phase.

## Profile and Session Pages

The application includes routes related to user profiles and sessions. The logic for the profile page (`/profile`) demonstrates the ability to customize the user experience based on their authentication status.

## Imports

- `os`: Module for interacting with the operating system.
- `Flask`: Main Flask class used to create the web application.
- `flash`: Module for displaying temporary messages.
- `render_template`: Flask function for rendering HTML templates.
- `request`: Object representing the client's request.
- `session`: Object for storing user information between requests.
- `url_for`: Function for dynamically building URLs.
- `Session`: Extension for session management in Flask.
- `SQL`: Class provided by cs50 for interacting with SQL databases.
- `check_password_hash` and `generate_password_hash`: Functions for securely handling passwords.
- `abort` and `jsonify`: `abort` is used to interrupt execution and generate HTTP errors. `jsonify` converts Python objects to JSON responses, commonly used to return structured data in HTTP responses.

## Application Configuration

The Flask instance named `app` is configured to use Flask-Session, and the database configuration is set. The connection to the SQLite database is established using the `SQL` class from cs50.

## Utility Functions

- `validate_password`, `hash_password`, and `insert_user` are utility functions for password validation, password hashing, and user insertion into the database, respectively.

## Routes

The file defines numerous routes to handle different HTTP requests, providing a structured routing system for the application. HTML templates with `render_template` are used to generate dynamic HTML responses based on the routes.

## Business Logic

Routes like `/contact` and `/subscribe` handle POST requests, perform operations in the database, and return JSON responses. Routes `/register` and `/login` are related to user registration and login.

## Error Handling

The `handle_exception` function handles exceptions and returns error messages with a 500 status code, providing a controlled response in case of errors.

Collectively, these features and components make `app.py` a comprehensive and well-structured script for a Flask web application, covering aspects such as database interaction, session management, routing, and dynamic information presentation.


## Conclusion

In conclusion, the `app.py` file serves as the backbone of a well-organized Flask web application. Its modular organization, session handling, interaction with the database, and dynamic content generation make it an essential script for both functionality and user experience in the web application.

The file encapsulates crucial aspects of web development, including user registration and login, session management, database interactions, error handling, and dynamic content rendering. The use of utility functions enhances code reusability, and the routing structure provides a clear and scalable approach to handling various HTTP requests.

Understanding and maintaining `app.py` is vital for developers working on the project, as it dictates the application's behavior and responsiveness. The integration of Flask features, such as session management and template rendering, showcases best practices in web development.

As the central hub of the Flask application, `app.py` not only orchestrates different components but also represents a comprehensive blueprint for building robust and maintainable web applications. Its clear structure, combined with well-defined routes and utility functions, contributes to the reliability and extensibility of the entire project.

## Final Conclusion

# Summary of the Delicate Web Application
"""
The Delicate web application is a meticulously crafted project, aiming to establish a digital presence for a family-owned organic soap business. Through informative content, product showcasing, educational blogs, and interactive features, the app aims to connect with customers, providing a platform for exploration, learning, and engagement.
"""

# Development Choices
"""
The project reflects a commitment to scalability, user experience, and future enhancements. The pending responsive design implementation underscores adaptability across various devices.
"""

# Documentation Overview
"""
The documentation explores key pages (home, contact, blog, shop, register, login) detailing each page's purpose, structure, JavaScript functions, Flask backend code, and user interaction.
"""

# app.py Overview
"""
The app.py file is a well-organized and pivotal script, showcasing best practices in web development. Its modular design, Flask integration, utility functions, error handling, and routing structure serve as a comprehensive blueprint for a robust web application.
"""

# Essence of the Delicate Web Application
"""
Delicate is more than a digital storefront; it's a platform fostering connections, providing valuable information, and delivering a delightful user experience. The current structure and features position it for future growth and enhancement.
"""












