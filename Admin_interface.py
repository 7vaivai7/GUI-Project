from tkinter import *
import sqlite3
from PIL import ImageTk
from tkinter import filedialog
from tkinter import messagebox

############################ UPLOAD PIC FUNCTION #######
def upload():
    global b
    b= StringVar()
    b="NULL"
    filename = filedialog.askopenfile(initialdir="C:/Users/vaish/Desktop/original/online")
    f = str(filename).split("'")
    print(f)
    i=0
    for v in f:
        i=i+1
        if i == 2:
            b=v

    if b != 'NULL':
        messagebox.showinfo("MSG","SUCCESFULLY UPLOADED")

########################### HANDELING PART START###########
def add():
    global add_root
    add_root = Toplevel(root)
    add_root.geometry("+700+100")

    img_label = Label(add_root, image=bg_img)
    img_label.pack()

    the_frame = Frame(add_root, bg="#18214d")
    the_frame.place(x=50, y=100)

    global price
    global title
    global rate
    global catagory


    label = Label(the_frame, text="ENTRY COLUMN", font=("comic sans ms", 10, "bold"), bg="#098dba")
    label.grid(row=0, column=0, columnspan=2,pady=5)

    pic = Button(the_frame, text="UPLOAD", command=upload, font=("comic sans ms", 10, "bold"), fg="white", bg="black")
    pic.grid(row=1, column=1)

    price = Entry(the_frame, width=40)
    price.grid(row=2, column=1,padx=5)
    title = Entry(the_frame, width=40)
    title.grid(row=3, column=1,padx=5)
    catagory = Entry(the_frame, width=40)
    catagory.grid(row=4, column=1,padx=5)
    rate = Entry(the_frame, width=40)
    rate.grid(row=5, column=1,padx=5)

    pic_label = Label(the_frame, text="PICTURE", width=15, pady=5, bg="#18214d", fg="white",font=("comic sans ms", 10, "bold"))
    pic_label.grid(row=1, column=0)
    price_label = Label(the_frame, text="PRICE", width=15, pady=5, bg="#18214d", fg="white",font=("comic sans ms", 10, "bold"))
    price_label.grid(row=2, column=0)
    t_label = Label(the_frame, text="TITLE", width=15, pady=5, bg="#18214d", fg="white",font=("comic sans ms", 10, "bold"))
    t_label.grid(row=3, column=0)
    cata_label = Label(the_frame, text="CATEGORY", width=15, pady=5, bg="#18214d", fg="white",font=("comic sans ms", 10, "bold"))
    cata_label.grid(row=4, column=0)
    rate_label = Label(the_frame, text="RATE", width=15, pady=5, bg="#18214d", fg="white",font=("comic sans ms", 10, "bold"))
    rate_label.grid(row=5, column=0)
    submit_btn = Button(the_frame, command=submit, text="ADD", width=10,font=("comic sans ms", 10, "bold"), fg="white", bg="black")
    submit_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
###
def submit():
    conn = sqlite3.connect('B&G.db')
    c = conn.cursor()


    c.execute("INSERT INTO PRODUCTS VALUES (:pic, :price, :name, :catagory, :rate)",
              {
                  'pic': b,
                  'price': price.get(),
                  'name': title.get(),
                  'catagory': catagory.get(),
                  'rate': rate.get()
              }
              )

    conn.commit()
    conn.close()


    price.delete(0, END)
    title.delete(0, END)
    catagory.delete(0, END)
    rate.delete(0, END)
    messagebox.showinfo("MSG", "SUCCESFULLY ADDED")
    add_root.destroy()
###
def dele():
    global dele_root
    dele_root = Toplevel(root,bg="#18214d")
    dele_root.geometry("+700+100")
    global del_e
    del_label = Label(dele_root, text="DEL ID", font=("comic sans ms", 10, "bold"), bg="#18214d")
    del_label.grid(row=0, column=0)
    del_e = Entry(dele_root, width=30)
    del_e.grid(row=0, column=1)
    btn2 = Button(dele_root, command=delete, text="DEL", width=10,font=("comic sans ms", 10, "bold"), fg="white", bg="black")
    btn2.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
###
def delete():
    conn = sqlite3.connect('B&G.db')
    c = conn.cursor()
    c.execute("DELETE FROM PRODUCTS WHERE oid= " + del_e.get())
    conn.commit()
    conn.close()
    del_e.delete(0, END)
    messagebox.showinfo("MSG", "SUCCESFULLY DELETED")
    dele_root.destroy()
###
def edit():
    global edit_root
    edit_root = Toplevel(root)
    edit_root.geometry("+700+100")
    img_label = Label(edit_root, image=bg_img).pack()

    the_frame = Frame(edit_root, bg="#18214d")
    the_frame.place(x=50, y=50)
    global pic1
    global price1
    global title1
    global catagory1
    global rate1
    global edit_e

    label = Label(the_frame, text="EDIT COLUMN", font=("comic sans ms", 10, "bold"), bg="#098dba")
    label.grid(row=0, column=0, columnspan=2)

    pic1 = Entry(the_frame, width=40)
    pic1.grid(row=1, column=1,padx=5)
    price1 = Entry(the_frame, width=40)
    price1.grid(row=2, column=1,padx=5)
    title1 = Entry(the_frame, width=40)
    title1.grid(row=3, column=1,padx=5)
    catagory1 = Entry(the_frame, width=40)
    catagory1.grid(row=4, column=1,padx=5)
    rate1 = Entry(the_frame, width=40)
    rate1.grid(row=5, column=1,padx=5)

    pic_label = Label(the_frame, text="PICTURE", width=15, pady=5, bg="#18214d", fg="white",font=("comic sans ms", 10, "bold"))
    pic_label.grid(row=1, column=0)
    price_label = Label(the_frame, text="PRICE", width=15, pady=5, bg="#18214d", fg="white",font=("comic sans ms", 10, "bold"))
    price_label.grid(row=2, column=0)
    t_label = Label(the_frame, text="TITLE", width=15, pady=5, bg="#18214d", fg="white",font=("comic sans ms", 10, "bold"))
    t_label.grid(row=3, column=0)
    cata_label = Label(the_frame, text="CATOGORY", width=15, pady=5, bg="#18214d", fg="white",font=("comic sans ms", 10, "bold"))
    cata_label.grid(row=4 ,column=0)
    rate_label = Label(the_frame, text="RATE", width=15, pady=5, bg="#18214d", fg="white",font=("comic sans ms", 10, "bold"))
    rate_label.grid(row=5, column=0)
    save_btn = Button(the_frame, command=save, text="EDIT", width=10,font=("comic sans ms", 10, "bold"), fg="white", bg="black")
    save_btn.grid(row=6, column=1, columnspan=2, padx=10, pady=10)

    edit_label = Label(the_frame, text="EDIT ID", font=("comic sans ms", 10, "bold"), bg="#098dba")
    edit_label.grid(row=7, column=0)
    edit_e = Entry(the_frame, width=30)
    edit_e.grid(row=7, column=1)
    btn_edit = Button(the_frame, command=update, text="UPDATE", width=10,font=("comic sans ms", 10, "bold"), fg="white", bg="black")
    btn_edit.grid(row=8, column=1, columnspan=2, padx=10, pady=10)
###
def update():
    conn = sqlite3.connect('B&G.db')
    c = conn.cursor()

    c.execute("SELECT * FROM PRODUCTS WHERE oid=" + edit_e.get())
    records = c.fetchall()

    for record in records:
        pic1.insert(0, record[0])
        price1.insert(0, record[1])
        title1.insert(0, record[2])
        catagory1.insert(0, record[3])
        rate1.insert(0, record[4])

    conn.commit()
    conn.close()
def save():
    conn = sqlite3.connect('B&G.db')
    c = conn.cursor()

    c.execute("""UPDATE PRODUCTS SET
                pic = :photo,
                price = :cost,
                name = :dis,
                catagory= :catagory,
                rate = :rate
                WHERE oid = :oid""",
              {
                  'photo': pic1.get(),
                  'cost': price1.get(),
                  'dis': title1.get(),
                  'catagory': catagory1.get(),
                  'rate': rate1.get(),
                  'oid': edit_e.get()

              })

    conn.commit()
    conn.close()

    pic1.delete(0, END)
    price1.delete(0, END)
    title1.delete(0, END)
    catagory1.delete(0, END)
    rate1.delete(0, END)
    edit_e.delete(0, END)
###
def show():
    show_root = Toplevel(root)
    show_root.geometry("+700+100")
    img_label = Label(show_root, image=bg_img).pack()

    the_frame = Frame(show_root, bg="#18214d")
    the_frame.place(x=50, y=150)

    conn = sqlite3.connect('B&G.db')
    c = conn.cursor()

    c.execute("SELECT *,oid FROM PRODUCTS")
    records = c.fetchall()

    print_rec = ' '
    for record in records:
        print_rec += str(record[5]) + "  Price:- " + str(record[1]) + "  Title:- " + str(record[2]) + "   Category:- " + str(record[3]) + "   Rating:- " + str(record[4]) +"\n"

    query_label = Label(the_frame, text=print_rec, bg="#18214d", fg="white", font=("comic sans ms", 10, "bold"))
    query_label.pack()

    conn.commit()
    conn.close()
########################## HANDELING PART END ###########


# main root
root = Tk()
# setting the screens size and title
root.geometry("700x400+0+100")
root.resizable(False, False)
root.title("DATA BASE")

bg_img = ImageTk.PhotoImage(file="C:/Users/vaish/OneDrive/Desktop/nee/bg_forest.jpg")

img_label = Label(root, image=bg_img)
img_label.pack()

the_frame = Frame(root, bg="#18214d")
the_frame.place(x=200, y=225)

add_btn = Button(the_frame, text="ADD ENTRY", width=15, font=("comic sans ms", 10, "bold"), fg="white", bg="black",command=add)
add_btn.grid(row=0, column=0, padx=10, pady=10)
del_btn = Button(the_frame, text="DELETE ENTRY", width=15, font=("comic sans ms", 10, "bold"), fg="white", bg="black",command=dele)
del_btn.grid(row=0, column=1, padx=10, pady=10)
edit_btn = Button(the_frame, text="EDIT ENTRY", width=15, font=("comic sans ms", 10, "bold"), fg="white", bg="black",command=edit)
edit_btn.grid(row=1, column=0, padx=10, pady=10)
show_btn = Button(the_frame, text="SHOW ENTRY", width=15, font=("comic sans ms", 10, "bold"), fg="white", bg="black",command=show)
show_btn.grid(row=1, column=1, padx=10, pady=10)

root.mainloop()