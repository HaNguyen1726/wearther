    def display_trending_items(self, frame):
        try:
            self.cursor.execute('''
                SELECT recommendation_outfit_id, name, purchase_link, rec_type, description
                FROM TrendingRecommendations
                ORDER BY recommendation_outfit_id DESC
                LIMIT 6
            ''')
            trending_items = self.cursor.fetchall()

            for i, item in enumerate(trending_items):
                item_frame = ttk.Frame(frame)
                item_frame.grid(row=i // 3, column=i % 3, padx=10, pady=10)
                
                # Display item details
                ttk.Label(item_frame, text=f"#{item[0]} - {item[1]}", font=('Arial', 11, 'bold')).pack()
                ttk.Label(item_frame, text=f"{item[3]}", font=('Arial', 10)).pack()
                ttk.Label(item_frame, text=item[4], font=('Arial', 9)).pack()

                # Load and display image using local path
                image_path = item[2]  
                image = self.load_image_from_url(image_path, (100, 200))
                if image:
                    img_label = tk.Label(item_frame, image=image)
                    img_label.image = image  # Keep a reference to avoid garbage collection
                    img_label.pack()

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error loading trending items: {str(e)}")

    def load_image_from_url(self, url_or_path, size=(100, 200)):
        try:
            if url_or_path.startswith('http'):
                # If the path is a URL, load with headers
                headers = {'User-Agent': 'Mozilla/5.0'}
                request = Request(url_or_path, headers=headers)
                image_bytes = urlopen(request).read()
                data_stream = io.BytesIO(image_bytes)
                pil_image = Image.open(data_stream)
            else:
                # If it's a local path, load directly
                pil_image = Image.open(url_or_path)

            # Resize the image with LANCZOS (high-quality downsampling)
            pil_image = pil_image.resize(size, Image.LANCZOS)
            return ImageTk.PhotoImage(pil_image)
        except Exception as e:
            print(f"Error loading image: {e}")
            return None
