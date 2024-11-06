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
