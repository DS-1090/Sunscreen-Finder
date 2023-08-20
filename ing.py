import pandas as pd
import tkinter as tk
from tkinter import Label, Entry, Frame
 
def find():
    need=(e.get())
    s=0
    if(need.isdigit()):
        for i in range(len(pf)):
            if need in pf[i]:
                l=Label(r,text=f"\nPlease Order: {nam[i]}",bg="#F9F9F9", font=("Helvetica", 9))
                l.pack()
                s=1
    else:
        for i in range(len(ing)):
            if need in ing[i]:
                l=Label(r,text=f"\nPlease Order: {nam[i]}",bg="#F9F9F9", font=("Helvetica", 9))
                l.pack()
                s=1

    if s!=1:
        l=Label(r,text="\nNo Matches Found", bg="#F9F9F9",font=("Helvetica", 9))
        l.pack()
    

r = tk.Tk()
data = pd.read_csv('sun - Sheet1.csv')
r.title("Sunscreen Finder")
r.geometry("1000x500")
r.configure(bg="#F9F9F9")

header_frame = Frame(r, bg="#FC6600")
header_frame.pack(fill="x")

header_label = Label(header_frame, text="Find Your Perfect Sunscreen", bg="#FC6600", fg="white", font=("Helvetica", 17, "bold"))
header_label.pack(pady=10)

input_frame = Frame(r, bg="#F9F9F9")
input_frame.pack(fill="x", padx=50, pady=10)

ing = data['Ingredients'].str.lower()
nam = data['Name']
pf = data['SPF'].astype('str')

l1 = Label(r, text="Enter Ingredients (seperated by spaces) or SPF:",bg="#F9F9F9",font=("Helvetica", 9))  
l1.pack()

e = Entry(r,font=("Helvetica", 9))
e.pack(pady=10, ipadx=10, ipady=7)

b=tk.Button(r,text="Find",command=find,bg="#FC6600", fg="white", font=("Helvetica", 9, "bold"), activebackground="#FFD700")
b.pack()

r.mainloop()