import tkinter as tk
import random
from PIL import Image, ImageTk


class KeyGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Key Generator")
        self.master.geometry("600x400")

        # Load background image
        image = Image.open("C:/Users/Mvidos/Desktop/Other school works/Hilary/Lab3/image.jpg")
        photo = ImageTk.PhotoImage(image)
        bg_label = tk.Label(self.master, image=photo)
        bg_label.image = photo
        bg_label.place(relwidth=1, relheight=1)

        # Generated key field
        self.generated_key_var = tk.StringVar()
        generated_key_label = tk.Label(self.master, textvariable=self.generated_key_var, font=("Helvetica", 20))
        generated_key_label.place(relx=0.5, rely=0.5, anchor="center")

        # Start button
        start_button = tk.Button(self.master, text="Generate Key", command=self.generate_key, font=("Helvetica", 16))
        start_button.place(relx=0.5, rely=0.7, anchor="center")

    def generate_key(self):
        # Generate key based on the specified format
        key_format = "XXXXX-XXXX-XXXX"
        generated_key = ""

        for char in key_format:
            if char == "X":
                generated_key += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
            else:
                generated_key += char

        # Display the generated key
        self.generated_key_var.set(generated_key)


if __name__ == "__main__":
    root = tk.Tk()
    app = KeyGeneratorApp(root)
    root.mainloop()
