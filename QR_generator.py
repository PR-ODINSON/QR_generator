#!/usr/bin/env python
# coding: utf-8

# In[7]:


import qrcode
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


# Function to generate QR Code
def generate_qr():
    data = entry_data.get()
    if not data:
        messagebox.showerror("Error", "Please enter data to generate QR code.")
        return

    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR Code, with version 1 being the smallest
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrcode.png")

    # Display the QR Code in the app
    img_tk = ImageTk.PhotoImage(Image.open("qrcode.png"))
    qr_label.config(image=img_tk)
    qr_label.image = img_tk
    messagebox.showinfo("Success", "QR Code generated and saved as 'qrcode.png'")


# GUI setup
root = Tk()
root.title("QR Code Generator")

# Input label and entry
Label(root, text="Enter Data for QR Code:", font=("Arial", 14)).pack(pady=10)
entry_data = Entry(root, font=("Arial", 14), width=30)
entry_data.pack(pady=10)

# Generate button
Button(root, text="Generate QR Code", font=("Arial", 14), command=generate_qr).pack(pady=10)

# Placeholder for QR code display
qr_label = Label(root)
qr_label.pack(pady=10)

root.geometry("400x500")
root.mainloop()


# In[ ]:




