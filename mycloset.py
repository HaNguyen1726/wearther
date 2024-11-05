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
