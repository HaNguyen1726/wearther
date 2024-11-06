def create_outfit_generator_page(self):
        generator_frame = ttk.Frame(self.notebook)
        self.notebook.add(generator_frame, text='Get Recommendations')

        self.weather_var = tk.StringVar()
        self.weather_combo = ttk.Combobox(generator_frame, values=['cold', 'mild', 'hot'], textvariable=self.weather_var)
        self.weather_combo.grid(row=1, column=1, pady=5, padx=5)

        self.dress_code_var = tk.StringVar()
        self.dress_code_combo = ttk.Combobox(generator_frame, values=['casual', 'business casual', 'formal'], textvariable=self.dress_code_var)
        self.dress_code_combo.grid(row=2, column=1, pady=5, padx=5)

        ttk.Button(generator_frame, text="Recommend Outfit", command=self.generate_outfit).grid(row=3, column=0, columnspan=2, pady=20)


def generate_outfit(self):

        weather = self.weather_var.get()
        dress_code = self.dress_code_var.get()

        if not weather or not dress_code:
            messagebox.showerror("Error", "Please select both weather and dress code!")
            return

        categories = ['top', 'bottom', 'outerwear', 'shoes']
        outfit = {}
        for category in categories:
            if category == 'outerwear' and weather == 'hot':
                continue

            self.cursor.execute('''
                SELECT item_name, color, material
                FROM Clothing
                WHERE uid = ? AND category = ? AND weather_type = ? AND dress_code = ?
            ''', (self.current_user, category, weather, dress_code))
            item = self.cursor.fetchone()
            if item:
                outfit[category] = item

        if outfit:
            for category, item in outfit.items():
                print(f"{category.capitalize()}: {item[0]} ({item[1]}, {item[2]})")
        else:
            messagebox.showinfo("No Matches", "No outfit matches your criteria.")

            
