# WEARTHER Project

## Overview
The Fashion Recommender System is a desktop application designed to help users manage their personal wardrobe and receive personalized outfit recommendations based on their style preferences, weather conditions, and dress code requirements. The application also features trending fashion recommendations for users to explore popular items.

The project is developed using Python with tkinter for the user interface and SQLite as the database.

## Table of Contents
[Features](#features)

[Database Design](#database-design)

[Setup Instructions](#setup-instructions)

[Git Commits](#git-commits)

[Demo Video](#demo-video)

## Key Files and Directories
**main.py:** Contains the main code for running the application, initializing the tkinter window, setting up the database connection, and implementing the main features.

**README.md:** Project description, setup instructions, and any relevant details about running the project.

**database/fashion_db.sqlite:** The SQLite database file where user, clothing, and trending item data are stored.

**images/:** Stores images for trending items, organized here to keep the main code directory clean.

## Features
**1. Account Creation**

Users can create an account with a username, material preference, and color preference.

The account creation feature adds a new user entry in the SQLite User table.

**2. My Closet**

Users can add clothing items to their personal closet, specifying details such as item name, color, material, category, weather suitability, and dress code.

The closet items are stored in the Clothing table and are associated with the user account.

**3. Trending Recommendations**

The "Home" tab displays trending fashion items, including images, names, categories, and descriptions.

These items are stored in the TrendingRecommendations table and displayed with images from the images/ folder.

**4. Outfit Recommendations**

Users can select weather and dress code preferences, and the application will suggest an outfit from the items saved in the user's closet.

The suggestions are displayed directly on the "Get Recommendations" page, updating each time the user requests a recommendation.

If no items match the criteria, the application suggests adding more items to the closet.


## Database Design
The application uses an SQLite database with three main tables:

**1. User Table**
uid: Primary key, auto-incremented integer.

username: Unique text field for the username.

material_preference: Text field for storing material preference.

color_preference: Text field for storing color preference.

**2. Clothing Table**
item_id: Primary key, auto-incremented integer.

uid: Foreign key that references User(uid).

item_name: Text field for the item name.

category: Text field (limited to 'top', 'bottom', 'outerwear', 'shoes').

material: Text field for the material type.

color: Text field for the color.

weather_type: Text field (limited to 'cold', 'mild', 'hot').

dress_code: Text field (limited to 'casual', 'business casual', 'formal').

**3. TrendingRecommendations Table**
recommendation_outfit_id: Primary key, auto-incremented integer.

name: Text field for the item name.

purchase_link: Text field for the image path.

rec_type: Text field to categorize trending items.

description: Text field for the item description.

**4. PersonalRecommendations Table**
recommend_id: Primary key, auto-incremented integer

uid: foreign key, references the User table

item_id: foreign key, references the Clothing table

weather: text column contains the weather condition of the outfit

dress_code: text column contains the dress code of the generated outfit

feedback: text column contains the like/ dislike feedback of the generated outfit

## Setup Instructions
**1. Clone the Repository:**

    bash
    Copy code
    git clone <repository-url>
    cd wearther


**2. Run the Application:**

Start the application by running main.py:

    bash
    Copy code
    python demo.py
 

**3. Database Initialization:**

The application will automatically create the required database tables if they do not exist. 

**4. Using the Application:**

- Create an account in the "Create Account" tab.
- Add items to your closet in the "My Closet" tab.
- View trending items in the "Home" tab.
- Get outfit recommendations in the "Get Recommendations" tab.

## Git Commits
This section outlines the major commits made during the project, detailing the purpose and changes introduced at each stage.

### Initial Commit – Project Setup and Initial Directory Structure
- Set up the foundational project structure to organize the application files and assets.

- Created main files such as core.py for application basics, README.md for project motivation and milestones, and a project directory for easier collaboration.

- Added folders for images (for storing trending item images) and local URL calling.

### Database Setup – Creating Tables and Database Initialization
- Configured the SQLite database to store user accounts, clothing items, and trending recommendations.
  
- Created four main tables:

    - User table: Stores user account information with fields for username, material preference, and color preference.

    - Clothing table: Stores clothing items associated with each user, including fields for item name, category, material, color, weather type, and dress code.

    - PersonalRecommendations table: Holds items and the details of the items that match users' preferences.

   - TrendingRecommendations table: Holds trending fashion items to be displayed on the homepage, including fields for item name, description, and image path.

- Added code in core.py to initialize tables if they do not already exist, ensuring a consistent database setup for every user.

### UI Setup – Building the Core UI Layout
- Designed the basic user interface using tkinter, setting up primary tabs for the main functionalities:
    - "Home" tab for displaying trending recommendations.

    - "Create Account" tab for user registration.
  
     - "My Closet" tab for managing and viewing personal clothing items.
  
    - "Get Recommendations" tab for outfit suggestions based on weather and dress code.
    
- Established a clean layout with a ttk.Notebook widget to make the app intuitive and easy to navigate, laying the foundation for additional functionality in each tab.

### Added Account Creation Feature – User Registration and Validation

- Implemented the user registration functionality within the "Create Account" tab.
- Added form fields to capture username, material preference, and color preference.
  - Created an Entry box for Username
  - Color Peference Combo box for users to choose from a drop down
  - Material Preference Combo box for users to choose from
- Integrated SQLite commands to insert new user data into the User table.
  - "Create Account" button to save users to User database
- Added validation to ensure unique usernames and prevent duplicate entries, displaying error messages if a username already exists.
- Enabled saving the new user ID (uid) to self.current_user to identify the logged-in user, establishing the user session for future interactions.
  
### Closet Item Addition and Display – My Closet Tab Functionality (mycloset.py)

- Implemented the "My Closet" tab, allowing users to add clothing items with attributes such as item name, category, material, color, weather suitability, and dress code.
  - Created an Entry box for item name
  - Category Combo box to identify if the item is a top, bottom, outerwear, or shoes
  - Material Combo box for users to choose from
  - Color Combo box for users to choose from a dropdown
  - Weather Combo box determines the suitable weather to style this piece
  - Dress code Combo box for suitable events
- Integrated form fields for input and linked these to the Clothing table, storing each item with a foreign key reference to the current user’s uid.
  - "Add Item" button registers the item to the database
- Added functionality to retrieve and display all items in the user's closet, enhancing the user experience by visually confirming saved items.
  - "Show Closet" button allows users to revisit all items they have added
 
### Trending Recommendations Display – Home Tab with Image Integration (homepage.py)
- Developed the "Home" tab to display trending fashion items from the TrendingRecommendations table.
- Integrated item images stored locally in the ***images folder*** enhancing the visual appeal of the app.
- Added display elements such as labels to show each item's name, category, and description.
- Utilized a 3x2 grid layout for trending items, creating a user-friendly interface where users can browse trending fashion recommendations.
  
### Outfit Recommendation Feature – Personalized Suggestions (recommendation.py)
- Built the outfit recommendation feature in the "Get Recommendations" tab to suggest outfits based on weather and dress code preferences.
  - Weather Combo box determines the weather to suggest outfit
  - Dress code Combo box for choosing the event type to make recommendations for
- Implemented a function to query the Clothing table, filtering items that match the selected weather and dress code.
  - "Get Recommendation" button shows the query result
- Displayed recommended outfits directly on the "Get Recommendations" page, with clear messages when no suitable items are found, encouraging users to add more items to their closet.
- Feedback mechanism allows users to choose the outfits that best suit their styles]
  - "Like" button: the outfit will be saved in this table and the same recommendations will be made again when users select the same conditions
  - "Dislike" button: the outfit will be removed from PersonalRecommendations table and another outfit will be generated
  
### Error Handling and Final UI Adjustments – Enhance Application Usability
- Fixed issues related to SQLite connection handling and improved error handling throughout the application.
- Added exception handling for database operations to catch potential issues (e.g., missing items, invalid entries).
- Resolved UI responsiveness issues to ensure that all tabs load properly and that the application remains stable during data entry and retrieval.
- Added a "Close Tab" button to dynamically generated tabs, allowing users to close tabs like "Your Closet" for a more seamless experience.

### Documentation and Comments – Code Readability and Project Documentation
- Created project.md to provide a comprehensive overview of the project, including the Git commit history and demo video link.
- Organized code into logical sections for better readability, making it easier for future developers or reviewers to understand and navigate the code.

## Demo Video
Link to the project demo video: YouTube Demo Video



