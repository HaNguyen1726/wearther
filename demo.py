import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from PIL import Image, ImageTk
from urllib.request import Request, urlopen
import io
import os

class FashionRecommenderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fashion Recommender System")
        self.root.geometry("800x600")
        
        # Database connection
        self.conn = sqlite3.connect('wearther_db.sqlite')
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

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS PersonalRecommendations (
            recommendation_id INTEGER PRIMARY KEY AUTOINCREMENT,
            uid INTEGER,
            item_id INTEGER,
            weather TEXT,
            dress_code TEXT,
            feedback TEXT,
            FOREIGN KEY (uid) REFERENCES User(uid),
            FOREIGN KEY (item_id) REFERENCES Clothing(item_id)
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
                ('Cream Wide Leg Pants', 'images\wide_pants.png', 'Must Haves', 'Autumn Ready-To-Wear'),
                ('Pullover Hoodie', 'images\pullover.png', 'Trending', 'In Demand Boots'),
                ('Midi Dress', 'images\midi.png', 'Top Picks', 'Seasonal Chart Topper'),
                ('Cashmere Sweater', 'images\cashmere_vest.png', 'Weather Choice', 'Staff Faves for the Season'),
                 ('Cropped Sweater', 'images\cropped_sweatshirt.png', 'Must Haves', 'Fall Tops Essentials')
            ])
        self.conn.commit()

    def create_notebook(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill='both', padx=10, pady=5)
        self.create_home_page()
        self.create_user_page()
        self.create_closet_page()
        self.create_outfit_generator_page()


    def create_home_page(self):
        home_frame = ttk.Frame(self.notebook)
        self.notebook.add(home_frame, text='Home')
        
        # Welcome message
        ttk.Label(home_frame, text="Welcome to Your Personal Stylist!", font=('Arial', 16, 'bold')).pack(pady=20)
        
        # Trending recommendations section
        ttk.Label(home_frame, text="Trending Items", font=('Arial', 14)).pack(pady=10)
        
        # Frame for trending items
        trending_frame = ttk.Frame(home_frame)
        trending_frame.pack(fill='both', expand=True, padx=20)
        
        # Display 5 trending items in a grid
        self.display_trending_items(trending_frame)


#Create a tab/ page called Create Account which adds a new user to the database
    def create_user_page(self):
        user_frame = ttk.Frame(self.notebook)
        self.notebook.add(user_frame, text='Create Account')
        
        #Prompt the user to input their name
        ttk.Label(user_frame, text="Username:").grid(row=1, column=0, pady=5, padx=5)
        self.username_entry = ttk.Entry(user_frame)
        self.username_entry.grid(row=1, column=1, pady=5, padx=5)
        
        #Prompt the user to choose their favorite color from the text box
        ttk.Label(user_frame, text="Color Preference:").grid(row=2, column=0, pady=5, padx=5)
        self.color_var = tk.StringVar()
        self.color_combo = ttk.Combobox(user_frame, values=['Black', 'White', 'Blue', 'Red'], textvariable=self.color_var)
        self.color_combo.grid(row=2, column=1, pady=5, padx=5)

        ttk.Label(user_frame, text="Material Preference:").grid(row=3, column=0, pady=5, padx=5)
        self.material_var = tk.StringVar()
        self.material_combo = ttk.Combobox(user_frame, values=['Cotton', 'Wool', 'Silk', 'Linen'], textvariable=self.material_var)
        self.material_combo.grid(row=3, column=1, pady=5, padx=5)

        ttk.Button(user_frame, text="Create Account", command=self.create_user).grid(row=4, column=0, columnspan=2, pady=20)

    def create_closet_page(self):
        closet_frame = ttk.Frame(self.notebook)
        self.notebook.add(closet_frame, text='My Closet')

        self.closet_entries = {
            'Item Name:': ttk.Entry(closet_frame),
            'Category:': ttk.Combobox(closet_frame, values=['top', 'bottom', 'outerwear', 'shoes']),
            'Weather Type:': ttk.Combobox(closet_frame, values=['cold', 'mild', 'hot']),
            'Dress Code:': ttk.Combobox(closet_frame, values=['casual', 'business casual', 'formal'])
        }

        for i, (label, entry) in enumerate(self.closet_entries.items()):
            ttk.Label(closet_frame, text=label).grid(row=i+1, column=0, pady=5, padx=5)
            entry.grid(row=i+1, column=1, pady=5, padx=5)

        ttk.Button(closet_frame, text="Add Item", command=self.add_clothing_item).grid(row=len(self.closet_entries)+1, column=0, columnspan=2, pady=20)
        ttk.Button(closet_frame, text="Show Closet", command=self.show_clothing_item).grid(row=len(self.closet_entries)+1, column=2, columnspan=2, pady=20)

    def create_outfit_generator_page(self):
        generator_frame = ttk.Frame(self.notebook)
        self.notebook.add(generator_frame, text='Get Recommendations')

        ttk.Label(generator_frame, text="Today's Weather:").grid(row=1, column=0, pady=5, padx=5)
        self.weather_var = tk.StringVar()
        self.weather_combo = ttk.Combobox(generator_frame, values=['cold', 'mild', 'hot'], textvariable=self.weather_var)
        self.weather_combo.grid(row=1, column=1, pady=5, padx=5)

        ttk.Label(generator_frame, text="Today's Weather:").grid(row=2, column=0, pady=5, padx=5)
        self.dress_code_var = tk.StringVar()
        self.dress_code_combo = ttk.Combobox(generator_frame, values=['casual', 'business casual', 'formal'], textvariable=self.dress_code_var)
        self.dress_code_combo.grid(row=2, column=1, pady=5, padx=5)

        ttk.Button(generator_frame, text="Recommend Outfit", command=self.generate_outfit).grid(row=3, column=0, columnspan=2, pady=20)
        

    def create_user(self):
        try:
            username = self.username_entry.get()
            color_pref = self.color_var.get()
            material_pref = self.material_var.get()

            self.cursor.execute('''
                INSERT INTO User (username, color_preference, material_preference)
                VALUES (?, ?, ?)
            ''', (username, color_pref, material_pref))
            self.conn.commit()
            self.current_user = self.cursor.lastrowid
            messagebox.showinfo("Success", "Account created successfully!")
            self.notebook.select(1)

        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already exists!")

    def add_clothing_item(self):
        if not self.current_user:
            messagebox.showerror("Error", "Please create an account first!")
            return

        try:
            values = [entry.get() for entry in self.closet_entries.values()]
            self.cursor.execute('''
                INSERT INTO Clothing (uid, item_name, category, material, color, weather_type, dress_code)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (self.current_user, *values))
            self.conn.commit()
            messagebox.showinfo("Success", "Item added successfully!")

        except sqlite3.Error:
            messagebox.showerror("Error", "Error adding item.")

                
    def show_clothing_item(self):
        if not self.current_user:
            messagebox.showerror("Error", "Please create an account first!")
            return

        try:
            # Retrieve clothing items for the current user
            self.cursor.execute('''
                SELECT item_name, category, material, color, weather_type, dress_code
                FROM Clothing
                WHERE uid = ?
                LIMIT 6
            ''', (self.current_user,))
            items = self.cursor.fetchall()

            if items:
                # Check if the "Your Closet" tab already exists
                for i in range(len(self.notebook.tabs())):
                    if self.notebook.tab(i, "text") == "Your Closet":
                        self.notebook.forget(i)  # Remove existing "Your Closet" tab

                # Create a new "Your Closet" tab
                closet_frame = ttk.Frame(self.notebook)
                self.notebook.add(closet_frame, text="Your Closet")

                # Display each item in the frame
                for i, item in enumerate(items):
                    item_label = f"Item Name: {item[0]}, Category: {item[1]}, Material: {item[2]}, Color: {item[3]}, Weather Type: {item[4]}, Dress Code: {item[5]}"
                    ttk.Label(closet_frame, text=item_label).grid(row=i, column=0, sticky='w', padx=10, pady=5)

                # Add a button to close the "Your Closet" tab
                ttk.Button(closet_frame, text="Close Tab", command=lambda: self.notebook.forget(closet_frame)).grid(row=len(items), column=0, pady=20)

            else:
                messagebox.showinfo("No Items", "Your closet is empty. Please add items first.")

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error retrieving items: {str(e)}")




       def generate_outfit(self):
        if not self.current_user:
            messagebox.showerror("Error", "Please create an account first!")
            return

        weather = self.weather_var.get()
        dress_code = self.dress_code_var.get()

        if not weather or not dress_code:
            messagebox.showerror("Error", "Please select both weather and dress code!")
            return

        # Clear previous recommendations if they exist
        if hasattr(self, 'recommendation_frame'):
            for widget in self.recommendation_frame.winfo_children():
                widget.destroy()
        else:
            # Create a frame to display recommendations if it doesn't exist
            self.recommendation_frame = ttk.Frame(self.notebook.nametowidget(self.notebook.tabs()[-1]))
            self.recommendation_frame.grid(row=4, column=0, columnspan=2, pady=10)

        try:
            # Check for a previously liked outfit for the same weather and dress code
            self.cursor.execute('''
                SELECT c.item_name, c.category, c.material, c.color, pr.recommendation_id
                FROM Clothing c
                JOIN PersonalRecommendations pr ON c.item_id = pr.item_id
                WHERE pr.uid = ? AND pr.weather = ? AND pr.dress_code = ? AND pr.feedback = 'like'
            ''', (self.current_user, weather, dress_code))
            liked_outfit = self.cursor.fetchall()

            if liked_outfit:
                # Display the previously liked outfit
                ttk.Label(self.recommendation_frame, text="Recommended Outfit:", font=('Arial', 12, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)
                for i, item in enumerate(liked_outfit, start=1):
                    item_text = f"{item[1].capitalize()}: {item[0]} ({item[3]}, {item[2]})"
                    ttk.Label(self.recommendation_frame, text=item_text).grid(row=i, column=0, columnspan=2, sticky='w')
            else:
                # Generate a new outfit by fetching items based on weather and dress code
                categories = ['top', 'bottom', 'outerwear', 'shoes']
                outfit = {}

                for category in categories:
                    if category == 'outerwear' and weather == 'hot':
                        continue

                    self.cursor.execute('''
                        SELECT item_id, item_name, color, material
                        FROM Clothing
                        WHERE uid = ? AND category = ? AND weather_type = ? AND dress_code = ?
                        LIMIT 1
                    ''', (self.current_user, category, weather, dress_code))
                    item = self.cursor.fetchone()
                    if item:
                        outfit[category] = item

                # Display the new outfit
                if outfit:
                    ttk.Label(self.recommendation_frame, text="Recommended Outfit:", font=('Arial', 12, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)
                    for i, (category, item) in enumerate(outfit.items(), start=1):
                        item_text = f"{category.capitalize()}: {item[1]} ({item[2]}, {item[3]})"
                        ttk.Label(self.recommendation_frame, text=item_text).grid(row=i, column=0, columnspan=2, sticky='w')
                    
                    # Add Like and Dislike buttons
                    ttk.Button(self.recommendation_frame, text="Like", command=lambda: self.store_recommendation(outfit, 'like')).grid(row=len(outfit)+1, column=0, pady=10)
                    ttk.Button(self.recommendation_frame, text="Dislike", command=self.regenerate_outfit).grid(row=len(outfit)+1, column=1, pady=10)
                else:
                    ttk.Label(self.recommendation_frame, text="No suitable items found. Please add more items to your closet.", font=('Arial', 10)).grid(row=1, column=0, columnspan=2)

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error generating outfit: {str(e)}")

    def store_recommendation(self, outfit, feedback):
        try:
            for category, item in outfit.items():
                self.cursor.execute('''
                    INSERT INTO PersonalRecommendations (uid, item_id, weather, dress_code, feedback)
                    VALUES (?, ?, ?, ?, ?)
                ''', (self.current_user, item[0], self.weather_var.get(), self.dress_code_var.get(), feedback))
            self.conn.commit()
            messagebox.showinfo("Feedback Received", "Your feedback has been saved. We’ll prioritize this outfit for similar conditions!")
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error saving recommendation: {str(e)}")

    def regenerate_outfit(self):
        # Clear any disliked outfit for the current weather and dress code
        try:
            self.cursor.execute('''
                DELETE FROM PersonalRecommendations
                WHERE uid = ? AND weather = ? AND dress_code = ? AND feedback = 'dislike'
            ''', (self.current_user, self.weather_var.get(), self.dress_code_var.get()))
            self.conn.commit()
            # Generate a new outfit
            self.generate_outfit()
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error regenerating outfit: {str(e)}")


    def load_image_from_url(self, url_or_path, size=(100, 100)):
        try:
            # Detect if the path is a URL or a local file
            if url_or_path.startswith('http'):
                # Load image from URL with headers
                headers = {'User-Agent': 'Mozilla/5.0'}
                request = Request(url_or_path, headers=headers)
                image_bytes = urlopen(request).read()
                data_stream = io.BytesIO(image_bytes)
                pil_image = Image.open(data_stream)
            else:
                # Load image from a local file
                pil_image = Image.open(os.path.normpath(url_or_path))

            # Resize the image
            pil_image = pil_image.resize(size, Image.LANCZOS)
            return ImageTk.PhotoImage(pil_image)
        except Exception as e:
            print(f"Error loading image: {e}")
            return None



if __name__ == "__main__":
    root = tk.Tk()
    app = FashionRecommenderApp(root)
    root.mainloop()
