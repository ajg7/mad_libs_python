from tkinter import *

root = Tk()
root.geometry("350x350")
root.title("Mad Libs Generator")
Label(root, text = "Mad Libs Generator", font = "arial 20 bold").pack()
Label(root, text = "Click to Begin", font = "arial 15 bold").place(x=40, y=30)
Label(root, text = "Once Clicked, Go Back to the Terminal", font = "arial 12 bold").place(x=40, y=60)

def mad_lib():
    animal = input("Enter an Animal: ")
    profession = input("Enter a Profession: ")
    country = input("Enter an Country: ")
    name = input("Enter a Name: ")
    verb = input("Enter a Verb: ")
    food = input("Enter Food: ")
    tv_show = input("Enter a TV Show: ")
    color = input("Enter a Color: ")
    
    print(f"Hello {name}! My {color} {animal} {verb} a lot, while I watch {tv_show} and eat {food}. Meanwhile I am interviewing as a {profession} in {country}")
    
Button(root, text = "My Story", font = "arial 15", command = mad_lib, bg = "ghost white").place(x = 60, y = 120)

root.mainloop()