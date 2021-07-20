from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import sqlite3
import numpy as np
from tkinter import messagebox

def mens():
    #########################################################################
    main_frame = Frame(main_root, bg="white")
    main_frame.place(x=300, y=50, width=1000, height=700)

    ####################################################################################
    # create canvas
    my_canvas = Canvas(main_frame, bg="#18214d")
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    # add a scrool bar
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    # config canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    # second frame
    second_frame = Frame(my_canvas, bg="#18214d")

    # add window
    my_canvas.create_window((180, 70), window=second_frame, anchor=NW)

    #########################################################################

    label = Label(second_frame, text="MENS COLLECTIONS", font=("comic sans ms", 20, "bold"), fg="#18214d", width=65)
    label.grid(row=0, column=0, columnspan=4)

    conn = sqlite3.connect('B&G.db')
    c = conn.cursor()

    c.execute("SELECT *,oid FROM PRODUCTS WHERE catagory='MENS'")
    records = c.fetchall()
    global arr
    arr = np.empty(100, dtype=object)
    a = 0
    i = 1
    j = 0
    for record in records:

        arr[a] = ImageTk.PhotoImage(Image.open(record[0]))

        button = Button(second_frame, image=arr[a], bd=0, command=click)
        button.grid(row=i, column=j, pady=5, padx=5)

        btn = Button(second_frame, text=record[2], bd=0, font=("comic sans ms", 18, "bold"), command=click, fg="white",bg="#18214d")
        btn.grid(row=i + 1, column=j)

        btn1 = Button(second_frame, text="RS. " + str(record[1]) + "    code: " + str(record[5]), bd=0, fg="green",font=("comic sans ms", 10, "bold"), bg="#18214d", command=click)
        btn1.grid(row=i + 2, column=j)

        j = j + 1
        a = a + 1
        if j > 2:
            i = i + 3
            j = 0

    conn.commit()
    conn.close()
def womens():
    #########################################################################
    main_frame = Frame(main_root, bg="white")
    main_frame.place(x=300, y=50, width=1000, height=700)

    ####################################################################################
    # create canvas
    my_canvas = Canvas(main_frame, bg="#18214d")
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    # add a scrool bar
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    # config canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    # second frame
    second_frame = Frame(my_canvas, bg="#18214d")

    # add window
    my_canvas.create_window((180, 70), window=second_frame, anchor=NW)

    #########################################################################

    label = Label(second_frame, text="WOMENS COLLECTIONS", font=("comic sans ms", 20, "bold"), fg="#18214d", width=65)
    label.grid(row=0, column=0, columnspan=4)

    conn = sqlite3.connect('B&G.db')
    c = conn.cursor()

    c.execute("SELECT *,oid FROM PRODUCTS WHERE catagory='WOMENS'")
    records = c.fetchall()
    global arr
    arr = np.empty(100, dtype=object)
    a = 0
    i = 1
    j = 0
    for record in records:

        arr[a] = ImageTk.PhotoImage(Image.open(record[0]))

        button = Button(second_frame, image=arr[a], bd=0, command=click)
        button.grid(row=i, column=j, pady=5, padx=5)

        btn = Button(second_frame, text=record[2], bd=0, font=("comic sans ms", 18, "bold"), command=click, fg="white",
                     bg="#18214d")
        btn.grid(row=i + 1, column=j)

        btn1 = Button(second_frame, text="RS. " + str(record[1]) + "    code: " + str(record[5]), bd=0, fg="green",
                      font=("comic sans ms", 10, "bold"), bg="#18214d", command=click)
        btn1.grid(row=i + 2, column=j)

        j = j + 1
        a = a + 1
        if j > 2:
            i = i + 3
            j = 0

    conn.commit()
    conn.close()
def kids():
    #########################################################################
    main_frame = Frame(main_root, bg="white")
    main_frame.place(x=300, y=50, width=1000, height=700)

    ####################################################################################
    # create canvas
    my_canvas = Canvas(main_frame, bg="#18214d")
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    # add a scrool bar
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    # config canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    # second frame
    second_frame = Frame(my_canvas, bg="#18214d")

    # add window
    my_canvas.create_window((180, 70), window=second_frame, anchor=NW)

    #########################################################################

    label = Label(second_frame, text="KIDS COLLECTION", font=("comic sans ms", 20, "bold"), fg="#18214d", width=65)
    label.grid(row=0, column=0, columnspan=4)

    conn = sqlite3.connect('B&G.db')
    c = conn.cursor()

    c.execute("SELECT *,oid FROM PRODUCTS WHERE catagory='KIDS'")
    records = c.fetchall()
    global arr
    arr = np.empty(100, dtype=object)
    a = 0
    i = 1
    j = 0
    for record in records:

        arr[a] = ImageTk.PhotoImage(Image.open(record[0]))

        button = Button(second_frame, image=arr[a], bd=0, command=click)
        button.grid(row=i, column=j, pady=5, padx=5)

        btn = Button(second_frame, text=record[2], bd=0, font=("comic sans ms", 18, "bold"), command=click, fg="white",
                     bg="#18214d")
        btn.grid(row=i + 1, column=j)

        btn1 = Button(second_frame, text="RS. " + str(record[1]) + "    code: " + str(record[5]), bd=0, fg="green",
                      font=("comic sans ms", 10, "bold"), bg="#18214d", command=click)
        btn1.grid(row=i + 2, column=j)

        j = j + 1
        a = a + 1
        if j > 2:
            i = i + 3
            j = 0

    conn.commit()
    conn.close()
def shoes():
    #########################################################################
    main_frame = Frame(main_root, bg="white")
    main_frame.place(x=300, y=50, width=1000, height=700)

    ####################################################################################
    # create canvas
    my_canvas = Canvas(main_frame, bg="#18214d")
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    # add a scrool bar
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    # config canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    # second frame
    second_frame = Frame(my_canvas, bg="#18214d")

    # add window
    my_canvas.create_window((180, 70), window=second_frame, anchor=NW)

    #########################################################################

    label = Label(second_frame, text="SHOES COLLECTIONS", font=("comic sans ms", 20, "bold"), fg="#18214d", width=65)
    label.grid(row=0, column=0, columnspan=4)

    conn = sqlite3.connect('B&G.db')
    c = conn.cursor()

    c.execute("SELECT *,oid FROM PRODUCTS WHERE catagory='SHOES'")
    records = c.fetchall()
    global arr
    arr = np.empty(100, dtype=object)
    a = 0
    i = 1
    j = 0
    for record in records:

        arr[a] = ImageTk.PhotoImage(Image.open(record[0]))

        button = Button(second_frame, image=arr[a], bd=0, command=click)
        button.grid(row=i, column=j, pady=5, padx=5)

        btn = Button(second_frame, text=record[2], bd=0, font=("comic sans ms", 18, "bold"), command=click, fg="white",
                     bg="#18214d")
        btn.grid(row=i + 1, column=j)

        btn1 = Button(second_frame, text="RS. " + str(record[1]) + "    code: " + str(record[5]), bd=0, fg="green",
                      font=("comic sans ms", 10, "bold"), bg="#18214d", command=click)
        btn1.grid(row=i + 2, column=j)

        j = j + 1
        a = a + 1
        if j > 2:
            i = i + 3
            j = 0

    conn.commit()
    conn.close()
def other():
    #########################################################################
    main_frame = Frame(main_root, bg="white")
    main_frame.place(x=300, y=50, width=1000, height=700)

    ####################################################################################
    # create canvas
    my_canvas = Canvas(main_frame, bg="#18214d")
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    # add a scrool bar
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    # config canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    # second frame
    second_frame = Frame(my_canvas, bg="#18214d")

    # add window
    my_canvas.create_window((180, 70), window=second_frame, anchor=NW)

    #########################################################################

    label = Label(second_frame, text="OTHERS COLLECTIONS", font=("comic sans ms", 20, "bold"), fg="#18214d", width=65)
    label.grid(row=0, column=0, columnspan=4)

    conn = sqlite3.connect('B&G.db')
    c = conn.cursor()

    c.execute("SELECT *,oid FROM PRODUCTS WHERE catagory='OTHERS'")
    records = c.fetchall()
    global arr
    arr = np.empty(100, dtype=object)
    a = 0
    i = 1
    j = 0
    for record in records:

        arr[a] = ImageTk.PhotoImage(Image.open(record[0]))

        button = Button(second_frame, image=arr[a], bd=0, command=click)
        button.grid(row=i, column=j, pady=5, padx=5)

        btn = Button(second_frame, text=record[2], bd=0, font=("comic sans ms", 18, "bold"), command=click, fg="white",
                     bg="#18214d")
        btn.grid(row=i + 1, column=j)

        btn1 = Button(second_frame, text="RS. " + str(record[1]) + "    code: " + str(record[5]), bd=0, fg="green",
                      font=("comic sans ms", 10, "bold"), bg="#18214d", command=click)
        btn1.grid(row=i + 2, column=j)

        j = j + 1
        a = a + 1
        if j > 2:
            i = i + 3
            j = 0

    conn.commit()
    conn.close()

def register():
    global reg_root
    reg_root = Toplevel(root)
    reg_root.title("REGISTER")

    img_label = Label(reg_root, image=bg_img)
    img_label.pack()

    global entry_user
    global entry_pass
    global f_name
    global l_name
    global num
    global address

    the_frame = Frame(reg_root, bg="white")
    the_frame.place(x=50, y=30)

    label3 = Label(the_frame, text="FILL IN THE REQUIRED INFO", font=("comic sans ms", 10, "bold"), bg="white")
    label3.grid(row=0, column=0, columnspan=2)
    label4 = Label(the_frame, text="Username", font=("comic sans ms", 10, "bold"), bg="white")
    label4.grid(row=1, column=1)
    entry_user = Entry(the_frame)
    entry_user.grid(row=2, column=1)
    label2 = Label(the_frame, image=reg_logo, bd=0)
    label2.grid(row=1, column=0, pady=10, rowspan=2)
    label5 = Label(the_frame, text="Password", font=("comic sans ms", 10, "bold"), bg="white")
    label5.grid(row=3, column=1)
    entry_pass = Entry(the_frame)
    entry_pass.grid(row=4, column=1)
    label20 = Label(the_frame, image=passs, bd=0)
    label20.grid(row=3, column=0, pady=10, rowspan=2)
    label6 = Label(the_frame, text="First Name", font=("comic sans ms", 10, "bold"), bg="white")
    label6.grid(row=5, column=1)
    f_name = Entry(the_frame)
    f_name.grid(row=6, column=1)
    label21 = Label(the_frame,image=names, bd=0)
    label21.grid(row=5, column=0, pady=10, rowspan=4)
    label6 = Label(the_frame, text="Last Name", font=("comic sans ms", 10, "bold"), bg="white")
    label6.grid(row=7, column=1)
    l_name = Entry(the_frame)
    l_name.grid(row=8, column=1)
    label6 = Label(the_frame, text="Mobile No.", font=("comic sans ms", 10, "bold"), bg="white")
    label6.grid(row=9, column=1)
    num = Entry(the_frame)
    num.grid(row=10, column=1)
    label21 = Label(the_frame, image=call, bd=0)
    label21.grid(row=9, column=0, pady=10, rowspan=2)
    label6 = Label(the_frame, text="Address", font=("comic sans ms", 10, "bold"), bg="white")
    label6.grid(row=11, column=1)
    address = Entry(the_frame)
    address.grid(row=12, column=1)
    label21 = Label(the_frame, image=loco, bd=0)
    label21.grid(row=11, column=0, pady=10, rowspan=2)
    myButton3 = Button(the_frame, text="Register", command=register_user, bg="orange")
    myButton3.grid(row=13, column=0, columnspan=2)
def register_user():
    conn = sqlite3.connect('B&G.db')
    c = conn.cursor()

    c.execute("SELECT *,oid FROM ACCOUNT ")
    records = c.fetchall()
    for record in records:
        if str(record[0]) == str(entry_user.get()):
            messagebox.showinfo("MSG", "ID ALREADY USED")
            return

    c.execute("INSERT INTO ACCOUNT VALUES (:ID, :PASS, :f_name, :l_name, :no, :address)",
              {
                  'ID': entry_user.get(),
                  'PASS': entry_pass.get(),
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'no': num.get(),
                  'address': address.get()
              }
              )

    conn.commit()
    conn.close()

    entry_user.delete(0, END)
    entry_pass.delete(0, END)
    f_name.delete(0, END)
    l_name.delete(0, END)
    num.delete(0, END)
    address.delete(0, END)
    messagebox.showinfo("MSG", "REGISTERED SUCSESSFULL")
    reg_root.destroy()

def login():
    global login_root

    login_root = Toplevel(root)
    login_root.geometry("+425+200")
    login_root.title("LOGIN")

    img_label = Label(login_root, image=bg_img)
    img_label.pack()

    global entry_user1
    global entry_pass1

    the_frame1 = Frame(login_root, bg="white")
    the_frame1.place(x=50, y=70)

    label = Label(the_frame1, text="LOGIN", bg="white", font=("comic sans ms", 18, "bold"))
    label.grid(row=0, column=0, columnspan=2)
    label2 = Label(the_frame1, image=login_logo, bd=0)
    label2.grid(row=1, column=0, pady=5, columnspan=2)
    label3 = Label(the_frame1, image=id, bd=0)
    label3.grid(row=2, column=0, pady=5, padx=10)
    label4 = Label(the_frame1, image=passs, bd=0)
    label4.grid(row=3, column=0, pady=5, padx=10)

    entry_user1 = Entry(the_frame1)
    entry_user1.grid(row=2, column=1, pady=10, padx=10)
    entry_user1.insert(0, "Enter User ID")

    entry_pass1 = Entry(the_frame1)
    entry_pass1.grid(row=3, column=1, pady=10, padx=10)
    entry_pass1.insert(0, "Enter Password")


    myButton3 = Button(the_frame1, text="Login", fg="white", bg="orange", font=("comic sans ms", 10, "bold"),command=login_verify)
    myButton3.grid(row=4, columnspan=2)
def login_verify():
    conn = sqlite3.connect('B&G.db')
    c = conn.cursor()

    c.execute("SELECT *,oid FROM ACCOUNT ")
    records = c.fetchall()
    for record in records:
        if str(record[0]) == str(entry_user1.get()):
            if str(record[1]) == str(entry_pass1.get()):
                messagebox.showinfo("MSG","LOGIN SUCSESSFULL")
                main_page()
                return
            else:
                messagebox.showinfo("MSG", "WRONG PASSWORD")
                return
    messagebox.showinfo("MSG", "INCORRECT ID")
    return
    conn.commit()
    conn.close()

def logout():
    main_root.destroy()
    entry_user1.delete(0, END)
    entry_pass1.delete(0, END)

def cart():
    g = entry_user1.get()
    T = (g,)
    global cart_root
    cart_root=Toplevel(root, bg="#18214d")
    cart_root.geometry("+300+100")
    label = Label(cart_root, text="THE CART", font=("comic sans ms", 20, "bold"), bg="grey", fg="white")
    label.grid(row=0, column=0, columnspan=2)

    conn = sqlite3.connect('B&G.db')
    c = conn.cursor()

    c.execute("SELECT *,oid FROM CART WHERE ID=?",T)
    records = c.fetchall()
    global brr
    brr = np.empty(100, dtype=object)
    a = 0
    i = 1

    for record in records:
        brr[a] = ImageTk.PhotoImage(Image.open(record[0]))

        labela = Label(cart_root, image=brr[a], bd=0)
        labela.grid(row=i, column=0, rowspan=2, pady=5)

        lbl = Label(cart_root, text=record[2], bd=0, font=("comic sans ms", 18, "bold"), width=22)
        lbl.grid(row=i, column=1)

        lbl1 = Label(cart_root, text="RS. " + str(record[1]),bg="#18214d", bd=0, fg="green", font=("comic sans ms", 10, "bold"))
        lbl1.grid(row=i + 1, column=1)

        a = a + 1
        i = i + 2
    del_label = Button(cart_root, image=delete, command=dele_c, bg="#18214d")
    del_label.grid(row=i, column=0, columnspan=2)
    conn.commit()
    conn.close()
def order():
    g=entry_user1.get()
    T=(g,)
    global order_root
    order_root = Toplevel(root, bg="#18214d")
    order_root.geometry("+300+100")
    label = Label(order_root, text="THE ORDERS", font=("comic sans ms", 20, "bold"), bg="grey", fg="white")
    label.grid(row=0, column=0, columnspan=2)

    conn = sqlite3.connect('B&G.db')
    c = conn.cursor()

    c.execute("SELECT *,oid FROM ORDERS WHERE ID=?",T)
    records = c.fetchall()
    global crr
    crr = np.empty(100, dtype=object)
    a = 0
    i = 1

    for record in records:
        crr[a] = ImageTk.PhotoImage(Image.open(record[0]))

        labela = Label(order_root, image=crr[a], bd=0)
        labela.grid(row=i, column=0, rowspan=5, pady=5)

        lbl = Label(order_root, text=record[2], bd=0, font=("comic sans ms", 18, "bold"), width=22)
        lbl.grid(row=i, column=1)

        lbl1 = Label(order_root, text="RS. " + str(record[1]), bg="#18214d", bd=0, fg="green",font=("comic sans ms", 10, "bold"))
        lbl1.grid(row=i + 1, column=1)
        lbl2 = Label(order_root, text="DELEVER TO " + str(record[3]) +" "+str(record[4]), bg="#18214d", bd=0, fg="green",font=("comic sans ms", 10, "bold"))
        lbl2.grid(row=i + 2, column=1)
        lbl3 = Label(order_root, text="CONTACT NO." + str(record[5]), bg="#18214d", bd=0, fg="green",font=("comic sans ms", 10, "bold"))
        lbl3.grid(row=i + 3, column=1)
        lbl4 = Label(order_root, text="ADDRESS " + str(record[6]), bg="#18214d", bd=0, fg="green",font=("comic sans ms", 10, "bold"))
        lbl4.grid(row=i + 4, column=1)
        a = a + 1
        i = i + 5
    del_label=Button(order_root, image=delete,command=dele_o, bg="#18214d")
    del_label.grid(row=i,column=0)
    billing_btn=Button(order_root,image=bill,command=billing,bg="#18214d")
    billing_btn.grid(row=i, column=1)
    conn.commit()
    conn.close()

def billing():
    order_root.destroy()
    global bill_root
    g = entry_user1.get()
    T = (g,)
    bill_root = Toplevel(root)
    bill_root.geometry("%dx%d+0+0" % (width_value - 25, height_value - 25))
    img_label = Label(bill_root, image=bg_main).pack()
    first_frame = Frame(bill_root, bg="#18214d")
    first_frame.place(x=250, y=100)
    bill_lable = Label(first_frame, text="BILLING", font=("comic sans ms", 18, "bold"), fg="white", bg="#18214d")
    bill_lable.grid(row=0,column=0,columnspan=3)
    no_lable = Label(first_frame, text="NO.", font=("comic sans ms", 18, "bold"), fg="white", bg="#18214d")
    no_lable.grid(row=1,column=0)
    name_lable = Label(first_frame, text="ITEM", font=("comic sans ms", 18, "bold"), fg="white", bg="#18214d")
    name_lable.grid(row=1, column=1)
    price_lable = Label(first_frame, text="PRICE", font=("comic sans ms", 18, "bold"), fg="white", bg="#18214d")
    price_lable.grid(row=1, column=2)

    conn = sqlite3.connect('B&G.db')
    c = conn.cursor()

    c.execute("SELECT *,oid FROM ORDERS WHERE ID=?", T)
    records = c.fetchall()
    i=1
    total_price=0
    for record in records:
        no_lable1 = Label(first_frame, text=str(i), font=("comic sans ms", 18, "bold"), fg="white", bg="#18214d")
        no_lable1.grid(row=i+1, column=0)
        name_lable1 = Label(first_frame, text=str(record[2]), font=("comic sans ms", 18, "bold"), fg="white", bg="#18214d")
        name_lable1.grid(row=i+1, column=1)
        price_lable1 = Label(first_frame, text=str(record[1]), font=("comic sans ms", 18, "bold"), fg="white", bg="#18214d")
        price_lable1.grid(row=i+1, column=2)
        i=i+1
        total_price=total_price+record[1]
    total_lable1 = Label(first_frame, text="TOTAL", font=("comic sans ms", 18, "bold"), fg="green", bg="#18214d")
    total_lable1.grid(row=i + 1, column=1)
    tprice_lable1 = Label(first_frame, text=str(total_price), font=("comic sans ms", 18, "bold"), fg="green", bg="#18214d")
    tprice_lable1.grid(row=i + 1, column=2)
    pay_btn=Button(first_frame,text="PAY",command=payy, bg="black", fg="white",font=("comic sans ms", 18, "bold"))
    pay_btn.grid(row=i + 2, column=0,columnspan=3)
    conn.commit()
    conn.close()
def payy():
    bill_root.destroy()

def dele_o():
    g = entry_user1.get()
    T = (g,)
    order_root.destroy()
    conn = sqlite3.connect('B&G.db')
    c = conn.cursor()
    c.execute("DELETE FROM ORDERS WHERE ID = ?",T)
    conn.commit()
    conn.close()
def dele_c():
    g = entry_user1.get()
    T = (g,)
    cart_root.destroy()
    conn = sqlite3.connect('B&G.db')
    c = conn.cursor()
    c.execute("DELETE FROM CART WHERE ID= ?",T)
    conn.commit()
    conn.close()
#########################
def main_page():
    global main_root
    main_root = Toplevel(root)
    main_root.geometry("%dx%d+0+0" % (width_value - 25, height_value - 25))

    img_label = Label(main_root, image=bg_main).pack()

    first_frame = Frame(main_root, bg="#18214d")
    first_frame.place(x=25, y=50)

    cata_lable=Label(first_frame,text="CATAGORY", font=("comic sans ms", 18, "bold"),fg="white",bg="#18214d")
    cata_lable.pack(pady=5)
    mens_btn=Button(first_frame,text="MENS", font=("comic sans ms", 10, "bold"),command=mens, width=20, fg="white", bg="black")
    mens_btn.pack(pady=5,padx=2)
    womens_btn = Button(first_frame, text="WOMENS", font=("comic sans ms", 10, "bold"), command=womens, width=20, fg="white", bg="black")
    womens_btn.pack(pady=5,padx=2)
    kids_btn = Button(first_frame, text="KIDS", font=("comic sans ms", 10, "bold"), command=kids, width=20, fg="white", bg="black")
    kids_btn.pack(pady=5,padx=2)
    shoes_btn = Button(first_frame, text="SHOES", font=("comic sans ms", 10, "bold"), command=shoes, width=20, fg="white", bg="black")
    shoes_btn.pack(pady=5,padx=2)
    other_btn = Button(first_frame, text="OTHERS", font=("comic sans ms", 10, "bold"), command=other, width=20, fg="white", bg="black")
    other_btn.pack(pady=5,padx=2)

    third_frame=Frame(main_root, bg="#18214d")
    third_frame.place(x=25,y=350)

    ACC_lable = Label(third_frame, text="ACCOUNTS", font=("comic sans ms", 18, "bold"), fg="white", bg="#18214d")
    ACC_lable.pack(pady=5)
    cart_btn = Button(third_frame, text="CART", font=("comic sans ms", 10, "bold"), command=cart, width=20,fg="white", bg="black")
    cart_btn.pack(pady=5, padx=2)
    order_btn = Button(third_frame, text="ORDERS", font=("comic sans ms", 10, "bold"), command=order,width=20, fg="white", bg="black")
    order_btn.pack(pady=5, padx=2)
    logout_btn = Button(third_frame, text="LOGOUT", font=("comic sans ms", 10, "bold"), command=logout, width=20,fg="white", bg="black")
    logout_btn.pack(pady=5, padx=2)
    #
    #########################################################################
    main_frame = Frame(main_root, bg="white")
    main_frame.place(x=300, y=50, width=1000, height=700)

    ####################################################################################
    # create canvas
    my_canvas = Canvas(main_frame, bg="#18214d")
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    # add a scrool bar
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    # config canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    # second frame
    second_frame = Frame(my_canvas, bg="#18214d")

    # add window
    my_canvas.create_window((180, 70), window=second_frame, anchor=NW)

    #########################################################################

    label = Label(second_frame, text="WELCOME", font=("comic sans ms", 20, "bold"), fg="#18214d", width=65)
    label.grid(row=0, column=0, columnspan=4)

    conn = sqlite3.connect('B&G.db')
    c = conn.cursor()

    c.execute("SELECT *,oid FROM PRODUCTS")
    records = c.fetchall()
    global arr
    arr = np.empty(100, dtype=object)
    a = 0
    i = 1
    j = 0
    for record in records:

        arr[a] = ImageTk.PhotoImage(Image.open(record[0]))

        button = Button(second_frame, image=arr[a], bd=0, command=click)
        button.grid(row=i, column=j, pady=5, padx=5)

        btn = Button(second_frame, text=record[2], bd=0, font=("comic sans ms", 18, "bold"), command=click,fg="white", bg="#18214d")
        btn.grid(row=i + 1, column=j)

        btn1 = Button(second_frame, text="RS. " + str(record[1]) + "    code: " + str(record[5]), bd=0, fg="green",font=("comic sans ms", 10, "bold"), bg="#18214d", command=click)
        btn1.grid(row=i + 2, column=j)

        j = j + 1
        a = a + 1
        if j > 2:
            i = i + 3
            j = 0

    conn.commit()
    conn.close()
#########################
def click():
    global disp_root
    disp_root = Toplevel(root, bg="#18214d")
    disp_root.geometry("+300+97")
    disp_root.title("BUY")
    global entry
    lb = Label(disp_root, text="Enter the product code", font=("comic sans ms", 10, "bold"))
    lb.grid(row=0, column=0, pady=10, columnspan=2)
    entry = Entry(disp_root, width=50)
    entry.grid(row=1, column=0, pady=10)
    btn2 = Button(disp_root, text="OK", command=disp, width=20)
    btn2.grid(row=1, column=1, pady=10)
def disp():
    conn = sqlite3.connect('B&G.db')
    c = conn.cursor()
    global photo
    global money
    global product_name
    global product_catagory
    global product_rate
    global sel_pic

    c.execute("SELECT * FROM PRODUCTS WHERE oid =" +entry.get())
    records = c.fetchall()
    for record in records:

        photo=record[0]
        money=record[1]
        product_name=record[2]
        product_catagory = record[3]
        product_rate = record[4]

        sel_pic = ImageTk.PhotoImage(Image.open(photo))

        label1 = Label(disp_root, image=sel_pic, bd=0)
        label1.grid(row=2, column=0, pady=20, padx=20,rowspan=3)

        label2 = Label(disp_root, text=product_name, bd=0, font=("comic sans ms", 18, "bold"), width=22)
        label2.grid(row=2, column=1)

        label3 = Label(disp_root, text="RS. " + str(money), bd=0, fg="green",font=("comic sans ms", 10, "bold"),bg="#18214d")
        label3.grid(row=3, column=1)

        if product_rate == 1:
            label4 = Label(disp_root, image= star1, bd=0)
            label4.grid(row=4, column=1)
        elif product_rate == 2:
            label4 = Label(disp_root, image= star2, bd=0)
            label4.grid(row=4, column=1)
        elif product_rate == 3:
            label4 = Label(disp_root, image= star3, bd=0)
            label4.grid(row=4, column=1)
        elif product_rate == 4:
            label4 = Label(disp_root, image= star4, bd=0)
            label4.grid(row=4, column=1)
        elif product_rate == 5:
            label4 = Label(disp_root, image= star5, bd=0)
            label4.grid(row=4, column=1)
        else:
            label4 = Label(disp_root, image=invalid_star, bd=0)
            label4.grid(row=4, column=1)

    btn6 = Button(disp_root, image=cart_img, bd=0, command=add_cart, bg="white")
    btn6.grid(row=5, column=0)
    btn7 = Button(disp_root, image=order_img, bd=0, command=buy_now, bg="white")
    btn7.grid(row=5, column=1, padx=5)


    conn.commit()
    conn.close()

def add_cart():
    conn = sqlite3.connect('B&G.db')
    c = conn.cursor()

    c.execute("INSERT INTO CART VALUES (:pic, :price, :name, :ID)",
              {
                  'pic': photo,
                  'price': money,
                  'name': product_name,
                  'ID': entry_user1.get()
              }
              )
    messagebox.showinfo("MSG", "SUCCESFULLY ADDED TO CART")
    conn.commit()
    conn.close()
    disp_root.destroy()
def buy_now():
    g=entry_user1.get()
    T=(g,)
    conn = sqlite3.connect('B&G.db')
    c = conn.cursor()

    c.execute("SELECT * FROM ACCOUNT WHERE ID= ?",T)
    records = c.fetchall()

    for record in records:
        first=record[2]
        last = record[3]
        nooo = record[4]
        addss = record[5]


    c.execute("INSERT INTO ORDERS VALUES (:pic, :price, :name, :f_name, :l_name, :number, :address, :ID)",
              {
                  'pic': photo,
                  'price': money,
                  'name': product_name,
                  'f_name': first,
                  'l_name': last,
                  'number': nooo,
                  'address': addss,
                  'ID': g

              }
              )
    messagebox.showinfo("MSG", "SUCCESFULLY ADDED TO ORDERS")
    conn.commit()
    conn.close()
    disp_root.destroy()

# main root
root = Tk()
root.geometry("+50+100")
root.resizable(False,False)
root.title("ONLINE SHOP")

width_value=root.winfo_screenwidth()
height_value=root.winfo_screenheight()

####### IMPORT PICTURES FROM DEVICE ######################################################
bg_img = ImageTk.PhotoImage(file="C:/Users/vaish/OneDrive/Desktop/nee/bg.png")
reg_logo = ImageTk.PhotoImage(file="C:/Users/vaish/OneDrive/Desktop/nee/reg_logo.jpg")
login_logo = ImageTk.PhotoImage(file="C:/Users/vaish/OneDrive/Desktop/nee/login_logo.jpg")
logo = ImageTk.PhotoImage(file="C:/Users/vaish/OneDrive/Desktop/nee/logo.jpg")
passs = ImageTk.PhotoImage(file="C:/Users/vaish/OneDrive/Desktop/nee/pass.jpg")
loco = ImageTk.PhotoImage(file="C:/Users/vaish/OneDrive/Desktop/nee/address.jpg")
call = ImageTk.PhotoImage(file="C:/Users/vaish/OneDrive/Desktop/nee/call.jpg")
names = ImageTk.PhotoImage(file="C:/Users/vaish/OneDrive/Desktop/nee/name.jpg")
id = ImageTk.PhotoImage(file="C:/Users/vaish/OneDrive/Desktop/nee/id.jpg")
bg_main = ImageTk.PhotoImage(file="C:/Users/vaish/OneDrive/Desktop/nee/bg_main_page.jpg")
cart_img = ImageTk.PhotoImage(file="C:/Users/vaish/OneDrive/Desktop/nee/cart.jpg")
order_img = ImageTk.PhotoImage(file="C:/Users/vaish/OneDrive/Desktop/nee/orders.jpg")
star1 = ImageTk.PhotoImage(file="C:/Users/vaish/OneDrive/Desktop/nee/1_star.jpg")
star2 = ImageTk.PhotoImage(file="C:/Users/vaish/OneDrive/Desktop/nee/2_star.jpg")
star3 = ImageTk.PhotoImage(file="C:/Users/vaish/OneDrive/Desktop/nee/3_star.jpg")
star4 = ImageTk.PhotoImage(file="C:/Users/vaish/OneDrive/Desktop/nee/4_star.jpg")
star5 = ImageTk.PhotoImage(file="C:/Users/vaish/OneDrive/Desktop/nee/5_star.jpg")
invalid_star = ImageTk.PhotoImage(file="C:/Users/vaish/OneDrive/Desktop/nee/invalid_star.jpg")
delete= ImageTk.PhotoImage(file="C:/Users/vaish/OneDrive/Desktop/nee/delete.jpg")
kid = ImageTk.PhotoImage(file="C:/Users/vaish/OneDrive/Desktop/nee/KIDS.jpg")
man = ImageTk.PhotoImage(file="C:/Users/vaish/OneDrive/Desktop/nee/MEN.jpg")
lady = ImageTk.PhotoImage(file="C:/Users/vaish/OneDrive/Desktop/nee/WOMEN.jpg")
shoe = ImageTk.PhotoImage(file="C:/Users/vaish/OneDrive/Desktop/nee/SHOES.jpg")
others = ImageTk.PhotoImage(file="C:/Users/vaish/OneDrive/Desktop/nee/other.jpg")
bill = ImageTk.PhotoImage(file="C:/Users/vaish/OneDrive/Desktop/nee/bill.jpg")
###########################################################################################
back_ground= Label(root,image=bg_img).pack()

label = Label(root, text="WELCOME",bg="black",fg="white", font=("comic sans ms", 18, "bold"),relief=GROOVE)
label.place(x=0,y=0,relwidth=1)

the_frame = Frame(root,bg="white")
the_frame.place(x=90,y=100)

label2 = Label(the_frame,image=logo,bd=0)
label2.grid(row=0,column=0,pady=20,columnspan=2)
label3 = Label(the_frame,image=reg_logo,bd=0)
label3.grid(row=1,column=0,pady=20,padx=10)
label4 = Label(the_frame,image=login_logo,bd=0)
label4.grid(row=2,column=0,pady=20,padx=10)

myButton = Button(the_frame, text="Register", command=register,bg="orange",fg="white",font=("comic sans ms",10,"bold"))
myButton.grid(row=1,column=1,padx=10)

myButton1 = Button(the_frame, text="Login", command=login,bg="orange",fg="white",font=("comic sans ms",10,"bold"))
myButton1.grid(row=2,column=1,padx=10)

root.mainloop()








