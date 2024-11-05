import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from PIL import Image, ImageTk
from urllib.request import urlopen
import io
import os

class FashionRecommenderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fashion Recommender System")
        self.root.geometry("800x600")
        
        # Database connection
        self.conn = sqlite3.connect('fashion_db.sqlite')
        self.cursor = self.conn.cursor()
        
        # Create tables if they don't exist
        self.create_tables()
        
        # Initialize UI
        self.create_notebook()
        self.current_user = None

    def create_tables(self):
        # User table
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS User (
            uid INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            material_preference TEXT,
            color_preference TEXT
        )
        ''')

        # Clothing table with category specification
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Clothing (
            item_id INTEGER PRIMARY KEY AUTOINCREMENT,
            uid INTEGER,
            item_name TEXT NOT NULL,
            category TEXT CHECK(category IN ('top', 'bottom', 'outerwear', 'shoes')),
            material TEXT,
            color TEXT,
            weather_type TEXT CHECK(weather_type IN ('cold', 'mild', 'hot')),
            dress_code TEXT CHECK(dress_code IN ('casual', 'business casual', 'formal')),
            FOREIGN KEY (uid) REFERENCES User(uid)
        )
        ''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS TrendingRecommendations (
            recommendation_outfit_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            purchase_link TEXT,
            rec_type TEXT,
            description TEXT
        )
        ''')

        # Insert data into TrendingRecommendations table if empty
        self.cursor.execute("SELECT COUNT(*) FROM TrendingRecommendations")
        if self.cursor.fetchone()[0] == 0:
            self.cursor.executemany('''
                INSERT INTO TrendingRecommendations (name, purchase_link, rec_type, description)
                VALUES (?, ?, ?, ?)
            ''', [
                ('Tailored Linen Shorts', 'images\white_shorts.png', 'Top Picks', 'Top Picks for Fall'),
                ('Cream Wide Leg Pants', 'images\white_shorts.png', 'Must Haves', 'Autumn Ready-To-Wear'),
                ('Evronna Dress', 'images\white_shorts.png', 'Trending', 'In Demand Boots'),
                ('Midi Dress', 'images\white_shorts.png', 'Top Picks', 'Seasonal Chart Topper'),
                ('Cashmere Sweater', 'images\white_shorts.png', 'Weather Choice', 'Staff Faves for the Season'),
                 ('Cropped Sweater', 'images\white_shorts.png', 'Must Haves', 'Fall Tops Essentials')
            ])
        self.conn.commit()

    def create_notebook(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill='both', padx=10, pady=5)
        self.create_home_page()
        self.create_user_page()
        self.create_closet_page()
        self.create_outfit_generator_page()
