# WEARTHER Project

## Overview
The Fashion Recommender System is a desktop application designed to help users manage their personal wardrobe and receive personalized outfit recommendations based on their style preferences, weather conditions, and dress code requirements. The application also features trending fashion recommendations for users to explore popular items.

The project is developed using Python with tkinter for the user interface and SQLite as the database.

## Table of Contents
[Features](#features)

[Database Design](#database-design)

[Setup Instructions](#

Git Commits

Demo Video

## Key Files and Directories
main.py: Contains the main code for running the application, initializing the tkinter window, setting up the database connection, and implementing the main features.
README.md: Project description, setup instructions, and any relevant details about running the project.
database/fashion_db.sqlite: The SQLite database file where user, clothing, and trending item data are stored.
images/: Stores images for trending items, organized here to keep the main code directory clean.
scripts/db_setup.py: (Optional) Script to initialize or reset the database by creating tables and populating data.

## Features
1. Account Creation
Users can create an account with a username, material preference, and color preference.
The account creation feature adds a new user entry in the SQLite User table.
2. My Closet
Users can add clothing items to their personal closet, specifying details such as item name, color, material, category, weather suitability, and dress code.
The closet items are stored in the Clothing table and are associated with the user account.
3. Trending Recommendations
The "Home" tab displays trending fashion items, including images, names, categories, and descriptions.
These items are stored in the TrendingRecommendations table and displayed with images from the images/ folder.
4. Outfit Recommendations
Users can select weather and dress code preferences, and the application will suggest an outfit from the items saved in the user's closet.
The suggestions are displayed directly on the "Get Recommendations" page, updating each time the user requests a recommendation.
If no items match the criteria, the application suggests adding more items to the closet.


## Database Design
The application uses an SQLite database with three main tables:

1. User Table
uid: Primary key, auto-incremented integer.
username: Unique text field for the username.
material_preference: Text field for storing material preference.
color_preference: Text field for storing color preference.
2. Clothing Table
item_id: Primary key, auto-incremented integer.
uid: Foreign key that references User(uid).
item_name: Text field for the item name.
category: Text field (limited to 'top', 'bottom', 'outerwear', 'shoes').
material: Text field for the material type.
color: Text field for the color.
weather_type: Text field (limited to 'cold', 'mild', 'hot').
dress_code: Text field (limited to 'casual', 'business casual', 'formal').
3. TrendingRecommendations Table
recommendation_outfit_id: Primary key, auto-incremented integer.
name: Text field for the item name.
purchase_link: Text field for the image path.
rec_type: Text field to categorize trending items.
description: Text field for the item description.


## Setup Instructions
Clone the Repository:

bash
Copy code
git clone <repository-url>
cd FashionRecommenderSystem
Install Dependencies:

Ensure you have Python installed. Install any required packages from requirements.txt:
''' bash
Copy code
pip install -r requirements.txt
'''
Run the Application:
'''
Start the application by running main.py:
bash
Copy code
python main.py
''' 

Database Initialization:

The application will automatically create the required database tables if they do not exist. If you need to reset the database, you can use scripts/db_setup.py to drop and recreate tables.
Using the Application:

Create an account in the "Create Account" tab.
Add items to your closet in the "My Closet" tab.
View trending items in the "Home" tab.
Get outfit recommendations in the "Get Recommendations" tab.

## Git Commits
This section outlines the major commits made during the project, detailing the purpose and changes introduced at each stage.

### Initial Commit – Project Setup and Initial Directory Structure
- Set up the foundational project structure to organize the application files and assets effectively.

- Created main files such as main.py for application logic, README.md for project documentation, and a database directory for SQLite database files.

- Added folders for images (for storing item images) and scripts (for any helper scripts), establishing a clear and scalable file structure.

### Database Setup – Creating Tables and Database Initialization
- Configured the SQLite database to store user accounts, clothing items, and trending recommendations.
- Created three main tables:

    - User table: Stores user account information with fields for username, material preference, and color preference.

    - Clothing table: Stores clothing items associated with each user, including fields for item name, category, material, color, weather type, and dress code.

    - PersoanlRecommendations table: Holds items and the details of the items that match users' perferences.

   - TrendingRecommendations table: Holds trending fashion items to be displayed on the homepage, including fields for item name, description, and image path.

- Added code in main.py to initialize tables if they do not already exist, ensuring a consistent database setup for every user.

### UI Setup – Building the Core UI Layout
- Designed the basic user interface using tkinter, setting up primary tabs for the main functionalities:

    - "Create Account" tab for user registration.
  
     - "My Closet" tab for managing and viewing personal clothing items.
  
    - "Get Recommendations" tab for outfit suggestions based on weather and dress code.
  
    - "Home" tab for displaying trending recommendations.
  
- Established a clean layout with a ttk.Notebook widget to make the app intuitive and easy to navigate, laying the foundation for additional functionality in each tab.

### Added Account Creation Feature – User Registration and Validation

- Implemented the user registration functionality within the "Create Account" tab.

- Added form fields to capture username, material preference, and color preference.

- Integrated SQLite commands to insert new user data into the User table.
  
- Added validation to ensure unique usernames and prevent duplicate entries, displaying error messages if a username already exists.
  
- Enabled saving the new user ID (uid) to self.current_user to identify the logged-in user, establishing the user session for future interactions.
  
### Closet Item Addition and Display – My Closet Tab Functionality

- Implemented the "My Closet" tab, allowing users to add clothing items with attributes such as item name, category, material, color, weather suitability, and dress code.
- Integrated form fields for input and linked these to the Clothing table, storing each item with a foreign key reference to the current user’s uid.
- Added functionality to retrieve and display all items in the user's closet, enhancing the user experience by visually confirming saved items.
  
### Trending Recommendations Display – Home Tab with Image Integration
- Developed the "Home" tab to display trending fashion items from the TrendingRecommendations table.
- Integrated item images stored locally in the images folder to simulate product visuals, enhancing the visual appeal of the app.
- Added display elements such as labels to show each item's name, category, and description.
- Utilized a grid layout for trending items, creating a user-friendly interface where users can browse trending fashion recommendations.
  
### Outfit Recommendation Feature – Personalized Suggestions
- Built the outfit recommendation feature in the "Get Recommendations" tab to suggest outfits based on weather and dress code preferences.
- Added drop-down menus for users to select the current weather and desired dress code.
- Implemented a function to query the Clothing table, filtering items that match the selected weather and dress code.
- Displayed recommended outfits directly on the "Get Recommendations" page, with clear messages when no suitable items are found, encouraging users to add more items to their closet.
  
### Error Handling and Bug Fixes – Improving Application Stability
- Fixed issues related to SQLite connection handling and improved error handling throughout the application.
- Added exception handling for database operations to catch potential issues (e.g., missing items, invalid entries).
- Resolved UI responsiveness issues to ensure that all tabs load properly and that the application remains stable during data entry and retrieval.
- Enhanced data validation and ensured the app does not crash due to unexpected inputs, making the application more robust.
  
### Final UI Adjustments and Styling – User Interface Enhancements
- Refined UI elements across all tabs, focusing on alignment, padding, and font styling for a polished look.
- Improved the layout of form fields and buttons, ensuring a cohesive design that is intuitive and visually appealing.
- Adjusted the display of outfit recommendations and closet items to make the information easy to read and navigate.
- Added a "Close Tab" button to dynamically generated tabs, allowing users to close tabs like "Your Closet" for a more seamless experience.
  
### Documentation and Comments – Code Readability and Project Documentation
- Added detailed comments throughout the codebase to explain key functions, parameters, and the purpose of each section.
- Updated README.md with setup instructions, usage information, and detailed descriptions of each feature.
- Created project.md to provide a comprehensive overview of the project, including the Git commit history and demo video link.
- Organized code into logical sections for better readability, making it easier for future developers or reviewers to understand and navigate the code.

## Demo Video
Link to the project demo video: YouTube Demo Video



