import tkinter as tk
from tkinter import Button
import mysql.connector as mycon
from PIL import Image, ImageTk
import tkinter.messagebox as msg_box


def add_recipe():
    recipe_name = lbl_btn_add.get()
    recipe_text = text_recipe.get("1.0",tk.END)

    con1 = mycon.connect(host="localhost", user="root", password="root", database="RECIPE_DB")
    if con1.is_connected():
        print("connection established")
    mycur = con1.cursor()
    sql = "INSERT INTO RECIPE (NAME, METHOD) VALUES (%s, %s)"
    val = (recipe_name, recipe_text)
    mycur.execute(sql,val)
    con1.commit()
    msg_box.showinfo("Add Recipe", "CONGRATULATIONS!!! RECIPE ENTERED SUCCESSFULLY IN THE DATABASE :)")
    text_recipe.delete("1.0",tk.END)
    #text_recipe.insert("1.0","CONGRATULATIONS!!! BELOW RECIPE ENTERED SUCCESSFULLY IN THE DATABASE :)\n\n")


    #Let's get the new name list & adding in list_recipe.
    sql1 = "select NAME from RECIPE;"

    mycur.execute(sql1)
    rs = mycur.fetchall()

    list_recipe.delete("1.0",tk.END)
    c = 1
    for i in rs:
        print(i)
        b = '\n'
        new = str(c) + '.' + ' ' + ''.join(i + (b,))
        test_str = str(c) + ".0"
        list_recipe.insert(test_str, new)
        c = c + 1


def view_recipe():
    recipe_view = lbl_btn_view.get()
    con1 = mycon.connect(host="localhost", user="root", password="root", database="RECIPE_DB")
    if con1.is_connected():
        print("connection established")
    sl = "Select * from RECIPE WHERE NAME = " + "'" + recipe_view + "';"
    mycur = con1.cursor()
    mycur.execute(sl)
    rs = mycur.fetchall()
    print(rs)
    if len(rs)==0:
        text_recipe.delete("1.0",tk.END)
        msg_box.showinfo("View Recipe", "The entered recipe does not exist in the DATABASE :(")
        #text_recipe.insert("1.0","The entered recipe does not exist in the DATABASE :(")
    else:
        for i in rs:
            print(i[1])
            text_recipe.delete("1.0",tk.END)
            text_recipe.insert("1.0",i[1])

def delete_recipe():
    recipe_delete=lbl_btn_remove.get()
    print(recipe_delete)
    con1 = mycon.connect(host="localhost", user="root", password="root", database="RECIPE_DB")

    # Checking whether Recipe exist in the database or not.
    sl = "Select * from RECIPE WHERE NAME = " + "'" + recipe_delete + "';"
    mycur = con1.cursor()
    mycur.execute(sl)
    rs = mycur.fetchall()
    if len(rs) == 0:
        text_recipe.delete("1.0", tk.END)
        msg_box.showinfo("Delete Recipe", "The recipe that you want to delete does not exist in the DATABASE :(")
        #text_recipe.insert("1.0", "The recipe that you want to delete does not exist in the DATABASE :(")
    else:
        sl = "DELETE FROM RECIPE WHERE NAME = " + "'" + recipe_delete + "';"
        print(sl)
        mycur = con1.cursor()
        mycur.execute(sl)
        con1.commit()
        text_recipe.delete("1.0",tk.END)
        comm =  "Recipe " + recipe_delete + " successfully deleted from the DATABASE :)"
        msg_box.showinfo("Delete Recipe", comm)
        #text_recipe.insert("1.0",comm)

        #Getting the updated RECIPE NAMES after deletion.
        sql1 = "select NAME from RECIPE;"
        mycur.execute(sql1)
        rs = mycur.fetchall()
        print(rs)

        # Adding the updated RECIPE NAMES in the textbox.
        if len(rs) != 0:
            c = 1
            list_recipe.delete("1.0",tk.END)
            for i in rs:
                b = '\n'
                new = str(c) + '.' + ' ' + ''.join(i + (b,))
                test_str = str(c) + ".0"
                list_recipe.insert(test_str, new)
                c = c + 1
        else:
            list_recipe.delete("1.0",tk.END)

#FRAME FOR THE APPLICATION.
window = tk.Tk()
window.title("Recipe Management App - Talha Faizan, Gaurav Yadav, Sanket Makode, Salil Tigga")

window.rowconfigure(0, minsize=500, weight=0)
window.columnconfigure(1, minsize=200, weight=0)
window.resizable(width=True, height=True)

# Frame 1:
frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)

# Button1 and text
lbl_btn_add = tk.Entry(master=frm_buttons, width=10)
btn_add = tk.Button(frm_buttons, text="Add Recipe", command=add_recipe)

# Button2 and text
lbl_btn_view = tk.Entry(master=frm_buttons, width=10)
btn_view: Button = tk.Button(frm_buttons, text="View Recipe",command=view_recipe)

# Button3 and text
lbl_btn_remove = tk.Entry(master=frm_buttons, width=10 )
btn_remove = tk.Button(frm_buttons, text="Remove Recipe",command=delete_recipe)

# Create a photoimage object of the image in the path
image1 = Image.open(r"D:\Python project/school logo.png")
resize_image = image1.resize((100, 100))
test = ImageTk.PhotoImage(resize_image)
label_image = tk.Label(master=frm_buttons, image=test)
label_image.image = test

# Frame 2:
frm_recipe_list = tk.Frame(master=window)
frm_recipe_list.rowconfigure(0, weight=1)
frm_recipe_list.columnconfigure(1, weight=1)
list_recipe_heading = tk.Label(master=frm_recipe_list, text=" Available Recipes ", height=1, fg="Black", bg="White",
                                         borderwidth=2, relief="solid", font=("Helvetica", 15))
list_recipe = tk.Text(master=frm_recipe_list, width=30, height=30, borderwidth=2, relief="solid")

# Frame 3:
frm_recipe_text = tk.Frame(window)
frm_recipe_text.rowconfigure(0, weight=1)
frm_recipe_text.columnconfigure(1, weight=1)
text_recipe_heading = tk.Label(master=frm_recipe_text, text="Add/View Recipe Below", height=0, fg="Black", bg="GREEN",
                               borderwidth=2, relief="solid", font=("Arial Rounded MT Bold", 20))
text_recipe = tk.Text(master=frm_recipe_text, borderwidth=2, relief="solid")

# Frame 4:
frm_copyright = tk.Frame(master=window)
copyright_heading = tk.Label(master=frm_copyright, text=" Class XII CS Project under the guidance of Meenakshi Ma'am ",
                             height=1, fg="Black", bg="White",borderwidth=2, relief="raised",
                             font=("Times New Roman Baltic", 13))

# Placing buttons in Frame 1 (button frame):
label_image.grid(row=0, column=0, columnspan=2, sticky="ew", padx=20, pady=20)
lbl_btn_add.grid(row=1, column=0, sticky="ew", padx=10, pady=20)
btn_add.grid(row=1, column=1, sticky="ew", padx=20, pady=20)
lbl_btn_view.grid(row=2, column=0, sticky="ew", padx=10, pady=20)
btn_view.grid(row=2, column=1, sticky="ew", padx=20)
lbl_btn_remove.grid(row=3, column=0, sticky="ew", padx=10, pady=20)
btn_remove.grid(row=3, column=1, sticky="ew", padx=20)

# Placing recipe text in Frame 2:
list_recipe_heading.grid(row=0, column=0, sticky="ns", pady=5)
list_recipe.grid(row=1, column=0, sticky="ns", pady=20)

# Placing recipe list in Frame 3:
text_recipe_heading.grid(row=0, column=0, sticky="nsew", pady=20)
text_recipe.grid(row=1, column=0, sticky="nsew", pady=20)

# Placing Copyright Statement in Frame 4:
copyright_heading.grid(row=0, column=1, sticky="nsew", pady=20)

# Placing the frames in main window frame
frm_buttons.grid(row=0, column=0, sticky="ns", rowspan=2)
frm_recipe_list.grid(row=0, column=1, sticky="ns", padx=20, pady=10)
frm_recipe_text.grid(row=0, column=2, sticky="nsew", padx=40, pady=10)
frm_copyright.grid(row=1, column=2, sticky="nsew", padx=40, pady=1, columnspan=2)



# ADDING THE NAMES OF THE RECIPE FROM THE BATABASE FOR INITIAL VIEWING.

con1 = mycon.connect(host="localhost", user="root", password="root", database="RECIPE_DB")
if con1.is_connected():
    print("connection established")
mycur = con1.cursor()
sql = "select NAME from RECIPE;"
mycur.execute(sql)
rs = mycur.fetchall()
print(rs)
if len(rs) !=0:
    c = 1
    for i in rs:
        b = '\n'
        new = str(c) + '.' + ' ' + ''.join(i + (b,))
        test_str = str(c) + ".0"
        list_recipe.insert(test_str, new)
        c = c + 1

window.mainloop()