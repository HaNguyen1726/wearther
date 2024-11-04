# Wearther Introduction
This repo is for my project called Wearther which aims to help users select their outfits using weather data and their events.

## Value Proposition
An average person takes more than 12 minutes daily to select their outfits and only makes the selection from 20% of the clothes they own. This is a huge waste of resources.

Wearther is an effort to help streamline this process.

## Database Design
There are 4 tables in this database: **User, Clothing, PersonalRecommendation,** TrendingRecommedations

The first table **User** contains uid, username, material_preference, color_preference. This table stores users' data and their preferences. 

The second table, **Clothing** has item_id, item_name, category, material, color, image_link. This acts as the digital closet for the users. 

The third table, **PersonalRecommendation** has item_id, uid, weather, dress_code. This table is holds the recommedation for users based on the weather and the dress_code. When the button is activated, it will show the recommendations to users.

The last table is **TrendingRecommedation**. It is intended as the main monetization mechanism of this app/ business where the most trendy items are recommended and users are encouraged to purchase these. It includes recommendation_outfit_id, purchase_link, rec_type, description. rec_type includes values such as 'Must haves', 'Fall Favorites', etc.

## CRUD Execution


## App Functionalites

## Git Repo's Commit Explanation
o List of git commits done.
o (IMPORTANT) the link to your project’s demo video (3 – 5 minutes, unlisted on YouTube).
Please explain the following points in your video:
 General description of your database, including the choice of DB software (e.g., SQLite)
 A running demo of your application.
 An overview of your GitHub repo’s commits
