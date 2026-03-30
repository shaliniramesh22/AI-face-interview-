import csv
import os
import shutil
import time
from tkinter import Tk, messagebox, ttk
from tkinter import *
from tkinter.ttk import Treeview

import cv2
from PIL import Image,ImageTk

import speech_recognition as sr
from PIL import ImageTk
import ar_master

from tkinter_video_voice_input import DomainOperations


mm = ar_master.master_flask_code()


# mm = ar_master.master_flask_code()


class tk_master:
    care_taker = ''
    user = ''
    emotion = ''
    company = ''
    job_list=[]
    job_id=''
    job_name=''
    job_company=''
    job_skills=''

    def __init__(self):
        self.master = 'ar_master'
        self.title = 'FACE INTERVIEW'
        self.titlec = 'FACE INTERVIEW'
        self.backround_color = '#2F4F4F'
        self.text_color = '#FFF'
        # self.text_color = '#c0c0c0'
        self.backround_image = 'images/background_hd1.jpg'

    def get_title(self):
        return self.title

    def get_titlec(self):
        return self.titlec

    def get_backround_color(self):
        return self.backround_color


    def get_text_color(self):
        return self.text_color

    def get_backround_image(self):
        return self.backround_image

    def admin_login(self):
        admin_login_root = Toplevel()
        admin_login_root.attributes('-topmost', 'true')
        get_data = tk_master()
        w = 780
        h = 500
        ws = admin_login_root.winfo_screenwidth()
        hs = admin_login_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        admin_login_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        image = Image.open('images/background_hd1.jpg')
        img = image.resize((w, h))
        my_img = ImageTk.PhotoImage(img)
        admin_login_root.resizable(False, False)
        canvas1 = Canvas(admin_login_root, width=200, height=300)
        canvas1.create_image(0, 0, image=my_img, anchor=NW)
        canvas1.pack(fill="both", expand=True)
        canvas1.create_text(390, 20, text=get_data.get_titlec(), font=("Times New Roman", 24),
                            fill=get_data.get_text_color())
        ##
        admin_id2 = canvas1.create_text(390, 100, text="ADMIN LOGIN", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(300, 200, text="Username", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(300, 300, text="Password", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        e1 = Entry(canvas1, font=('times', 15, ' bold '))
        canvas1.create_window(470, 200, window=e1)
        e2 = Entry(canvas1, font=('times', 15, ' bold '), show="*")
        canvas1.create_window(470, 300, window=e2)

        def exit_program():
            a = e1.get()
            b = e2.get()
            if (a == ""):
                messagebox.showinfo(title="Alert", message="Enter Username", parent=admin_login_root)
            elif (b == ""):
                messagebox.showinfo(title="Alert", message="Enter Password", parent=admin_login_root)
            elif ((a == "admin") and (b == "admin")):
                messagebox.showinfo("Result", "Login Success", parent=admin_login_root)
                admin_login_root.destroy()
                tt = tk_master()
                # tt.admin_home()
                tt.company_home()
            else:
                messagebox.showinfo("Result", "Login Failed", parent=admin_login_root)

        b1 = Button(canvas1, text="Login", command=exit_program, font=('times', 15, ' bold '))
        canvas1.create_window(470, 400, window=b1)
        admin_login_root.mainloop()

    def admin_home(self):
        admin_home_root = Toplevel()

        admin_home_root.attributes('-topmost', 'true')
        get_data = tk_master()
        w = 780
        h = 500
        ws = admin_home_root.winfo_screenwidth()
        hs = admin_home_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        admin_home_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        image = Image.open('images/background_hd1.jpg')
        img = image.resize((w, h))
        my_img = ImageTk.PhotoImage(img)
        admin_home_root.resizable(False, False)
        canvas1 = Canvas(admin_home_root, width=200, height=300)
        canvas1.create_image(0, 0, image=my_img, anchor=NW)
        canvas1.pack(fill="both", expand=True)
        canvas1.create_text(390, 20, text=get_data.get_titlec(), font=("Times New Roman", 24),
                            fill=get_data.get_text_color())
        ##
        admin_id2 = canvas1.create_text(390, 100, text="ADMIN HOME", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        def user_details():
            user_details_root = Toplevel()

            user_details_root.attributes('-topmost', 'true')
            w = 650
            h = 350
            ws = user_details_root.winfo_screenwidth()
            hs = user_details_root.winfo_screenheight()
            x = (ws / 2) - (w / 2)
            y = (hs / 2) - (h / 2)
            user_details_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
            self.bg = ImageTk.PhotoImage(file='images/background_hd.jpg')
            user_details_root.title(get_data.get_titlec())
            user_details_root.resizable(False, False)
            bg = ImageTk.PhotoImage(file='images/background_hd1.jpg')
            canvas = Canvas(user_details_root, width=200, height=300)
            canvas.pack(fill="both", expand=True)
            canvas.create_image(0, 0, image=bg, anchor=NW)
            admin_id2 = canvas.create_text(310, 70, text="User Details", font=("Times New Roman", 24),
                                           fill=get_data.get_text_color())
            fram = Frame(canvas)
            fram.place(x=60, y=100, width=550, height=230)
            scrollbarx = Scrollbar(fram, orient=HORIZONTAL)
            scrollbary = Scrollbar(fram, orient=VERTICAL)
            tree = Treeview(fram, columns=("name", "contact", "email", "address"),
                            yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
            scrollbarx.config(command=tree.xview)
            scrollbarx.pack(side=BOTTOM, fill=X)
            scrollbary.config(command=tree.yview)
            scrollbary.pack(side=RIGHT, fill=Y)
            tree.heading('name', text="name", anchor=W)
            tree.heading('contact', text="contact", anchor=W)
            tree.heading('email', text="email", anchor=W)
            tree.heading('address', text="address", anchor=W)


            tree.column('#0', width=0)
            tree.column('#1', width=100)
            tree.column('#2', width=100)
            tree.column('#3', width=100)

            tree.pack()
            d1 = mm.select_direct_query("select * from user_details")
            for data in d1:
                tree.insert("", 0, values=data)

            user_details_root.mainloop()



        b1 = Button(canvas1, text="User Details", command=user_details, font=('times', 15, ' bold '))
        canvas1.create_window(200,150, window=b1)
        def company_details():
            company_details_root = Toplevel()

            company_details_root.attributes('-topmost', 'true')
            w = 650
            h = 350
            ws = company_details_root.winfo_screenwidth()
            hs = company_details_root.winfo_screenheight()
            x = (ws / 2) - (w / 2)
            y = (hs / 2) - (h / 2)
            company_details_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
            self.bg = ImageTk.PhotoImage(file='images/background_hd.jpg')
            company_details_root.title(get_data.get_titlec())
            company_details_root.resizable(False, False)
            bg = ImageTk.PhotoImage(file='images/background_hd1.jpg')
            canvas = Canvas(company_details_root, width=200, height=300)
            canvas.pack(fill="both", expand=True)
            canvas.create_image(0, 0, image=bg, anchor=NW)
            admin_id2 = canvas.create_text(310, 70, text="Company Details", font=("Times New Roman", 24),
                                           fill=get_data.get_text_color())
            fram = Frame(canvas)
            fram.place(x=60, y=100, width=550, height=230)
            scrollbarx = Scrollbar(fram, orient=HORIZONTAL)
            scrollbary = Scrollbar(fram, orient=VERTICAL)
            tree = Treeview(fram, columns=("name", "contact", "email", "address"),
                            yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
            scrollbarx.config(command=tree.xview)
            scrollbarx.pack(side=BOTTOM, fill=X)
            scrollbary.config(command=tree.yview)
            scrollbary.pack(side=RIGHT, fill=Y)
            tree.heading('name', text="name", anchor=W)
            tree.heading('contact', text="contact", anchor=W)
            tree.heading('email', text="email", anchor=W)
            tree.heading('address', text="address", anchor=W)

            tree.column('#0', width=0)
            tree.column('#1', width=100)
            tree.column('#2', width=100)
            tree.column('#3', width=100)

            tree.pack()
            d1 = mm.select_direct_query("select * from user_details")
            for data in d1:
                tree.insert("", 0, values=data)

            company_details_root.mainloop()

        b2 = Button(canvas1, text="Company Details", command=company_details, font=('times', 15, ' bold '))
        canvas1.create_window(200, 250, window=b2)
        def logout():
            tt = tk_master()
            tt.company_registration()

        b3 = Button(canvas1, text="Add Company", command=logout, font=('times', 15, ' bold '))
        canvas1.create_window(430, 150, window=b3)

        def add_question():
            add_question_root = Toplevel()
            add_question_root.attributes('-topmost', 'true')
            get_data = tk_master()
            w = 780
            h = 500
            ws = add_question_root.winfo_screenwidth()
            hs = add_question_root.winfo_screenheight()
            x = (ws / 2) - (w / 2)
            y = (hs / 2) - (h / 2)
            add_question_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
            image = Image.open('images/background_hd1.jpg')
            img = image.resize((w, h))
            my_img = ImageTk.PhotoImage(img)
            add_question_root.resizable(False, False)
            canvas1 = Canvas(add_question_root, width=200, height=300)
            canvas1.create_image(0, 0, image=my_img, anchor=NW)
            canvas1.pack(fill="both", expand=True)
            canvas1.create_text(390, 20, text=get_data.get_titlec(), font=("Times New Roman", 24),
                                fill=get_data.get_text_color())
            ##
            admin_id2 = canvas1.create_text(390, 100, text="ADD QUESTION", font=("Times New Roman", 20),
                                            fill=get_data.get_text_color())
            admin_id2 = canvas1.create_text(200, 200, text="Company", font=("Times New Roman", 20),
                                            fill=get_data.get_text_color())
            admin_id2 = canvas1.create_text(200, 250, text="Job Title", font=("Times New Roman", 20),
                                            fill=get_data.get_text_color())
            admin_id2 = canvas1.create_text(200, 300, text="Question", font=("Times New Roman", 20),
                                            fill=get_data.get_text_color())
            admin_id2 = canvas1.create_text(200, 350, text="Answer", font=("Times New Roman", 20),
                                            fill=get_data.get_text_color())

            def write_dataset(company, job, question, answer):
                file = 'dataset.csv'
                pr_chk = 0
                # with open(file) as f:
                #     reader = csv.DictReader(f, delimiter=',')
                #     for row in reader:
                #         t1 = row['company']
                #         a, b = (t1), (company)
                #         if a == b:
                #             pr_chk += 1
                if pr_chk == 0:
                    file1 = 'dataset1.csv'
                    with open(file) as f, open('dataset1.csv', 'w', encoding='utf-8', newline='')as csvfile:
                        reader = csv.DictReader(f, delimiter=',')
                        filewriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                        filewriter.writerow(
                            ['company', 'job', 'question', 'answer'])
                        for row in reader:
                            t1 = row['company']
                            t2 = row['job']
                            t3 = row['question']
                            t4 = row['answer']
                            filewriter.writerow([t1, t2, t3, t4])
                        filewriter.writerow([company, job, question, answer])
                    shutil.copy('dataset1.csv', file)
                    os.remove(file1)
                #     messagebox.showinfo(title="info", message="Success", parent=add_question_root)
                # else:
                #     messagebox.showinfo(title="info", message="Already Trained", parent=add_question_root)

            aa = tk_master.company
            # print(aa)
            e1 = Entry(canvas1, font=('times', 15, ' bold '), text=aa)
            canvas1.create_window(470, 200, window=e1)
            e1.delete(0, END)
            e1.insert(0, aa)

            # e2 = Entry(canvas1, font=('times', 15, ' bold '))
            # canvas1.create_window(470, 250, window=e2)

            tk_master.job_list = mm.select_direct_query("select * from job_details where company='" + str(aa) + "'")
            # print(tk_master.job_list)
            job_title = []
            for x in tk_master.job_list:
                job_title.append(x[2])
            # print(job_title)

            combo = ttk.Combobox(canvas1, state="readonly", font=('times', 14, ' bold '), values=job_title)
            # combo.place(x=50, y=50)
            canvas1.create_window(470, 250, window=combo)

            e3 = Entry(canvas1, font=('times', 15, ' bold '))
            canvas1.create_window(470, 300, window=e3)

            e4 = Entry(canvas1, font=('times', 15, ' bold '))
            canvas1.create_window(470, 350, window=e4)

            def exit_program():
                company = tk_master.company
                a = e1.get()
                b = combo.get()
                c = e3.get()
                d = e4.get()

                if (a == ""):
                    messagebox.showinfo(title="Alert", message="Enter Company", parent=add_question_root)
                elif (b == ""):
                    messagebox.showinfo(title="Alert", message="Select Job Title", parent=add_question_root)
                elif (c == ""):
                    messagebox.showinfo(title="Alert", message="Enter Question", parent=add_question_root)
                elif (d == ""):
                    messagebox.showinfo(title="Alert", message="Enter Answer", parent=add_question_root)
                else:
                    # maxin = mm.find_max_id("job_details")
                    # qry = ("insert into job_details values('" + str(maxin) + "','" + str(company) + "','" + str(a) + "','" + str(b) + "','" + str(c) + "','" + str(d) + "','0','0')")
                    # result = mm.insert_query(qry)
                    write_dataset(str(a), str(b), str(c), str(d))
                    messagebox.showinfo(title="Alert", message="Success", parent=add_question_root)
                    add_question_root.destroy()

            b1 = Button(canvas1, text="ADD JOB", command=exit_program, font=('times', 15, ' bold '))
            canvas1.create_window(470, 450, window=b1)
            add_question_root.mainloop()
        b4 = Button(canvas1, text="Add Question", command=add_question, font=('times', 15, ' bold '))
        canvas1.create_window(430, 250, window=b4)

        admin_home_root.mainloop()


    def set_window_design(self):
        root = Tk()
        w = 780
        h = 500
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.bg = ImageTk.PhotoImage(file='images/background_hd1.jpg')
        root.title(self.title)
        root.resizable(False, False)
        bg = ImageTk.PhotoImage(file=self.backround_image)
        canvas = Canvas(root, width=200, height=300)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor=NW)
        canvas.create_text(390, 20, text=self.title, font=("Times New Roman", 24), fill=self.text_color)

        ###
        def clickHandler(event):
            tt = tk_master
            tt.admin_login(event)

        image = Image.open('images/admin.png')
        img = image.resize((125, 125))
        my_img = ImageTk.PhotoImage(img)
        image_id = canvas.create_image(250, 120, image=my_img)
        canvas.tag_bind(image_id, "<1>", clickHandler)

        ###
        def clickHandler1(event):
            tt = tk_master
            tt.user_login(event)

        image1 = Image.open('images/studentss.png')
        img1 = image1.resize((125, 125))
        my_img1 = ImageTk.PhotoImage(img1)
        image_id1 = canvas.create_image(250, 300, image=my_img1)
        canvas.tag_bind(image_id1, "<1>", clickHandler1)

        ##
        # def clickHandler2(event):
        #     tt = tk_master
        #     tt.company_login(event)
        #
        # image2 = Image.open('images/company.png')
        # img2 = image2.resize((125, 125))
        # my_img11 = ImageTk.PhotoImage(img2)
        # image_id2 = canvas.create_image(250, 400, image=my_img11)
        # canvas.tag_bind(image_id2, "<1>", clickHandler2)

        ###
        admin_id = canvas.create_text(420, 120, text="Admin", font=("Times New Roman", 24), fill=self.text_color)
        canvas.tag_bind(admin_id, "<1>", clickHandler)
        ###
        admin_id1 = canvas.create_text(420, 300, text="User", font=("Times New Roman", 24), fill=self.text_color)
        canvas.tag_bind(admin_id1, "<1>", clickHandler1)
        ###
        # company1 = canvas.create_text(420, 400, text="Company", font=("Times New Roman", 24), fill=self.text_color)
        # canvas.tag_bind(company1, "<1>", clickHandler2)
        root.mainloop()

    def company_login(self):
        company_login_root =Toplevel()
        company_login_root.attributes('-topmost', 'true')
        get_data=tk_master()
        w = 780
        h = 500
        ws = company_login_root.winfo_screenwidth()
        hs = company_login_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        company_login_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        image = Image.open('images/background_hd1.jpg')
        img = image.resize((w, h))
        my_img = ImageTk.PhotoImage(img)
        company_login_root.resizable(False, False)
        canvas1 = Canvas(company_login_root, width=200, height=300)
        canvas1.create_image(0, 0, image=my_img, anchor=NW)
        canvas1.pack(fill="both", expand=True)
        canvas1.create_text(390, 20, text=get_data.get_titlec(), font=("Times New Roman", 24), fill=get_data.get_text_color())
        ##
        admin_id2 = canvas1.create_text(390, 100, text="COMPANY LOGIN", font=("Times New Roman", 24), fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(300, 200, text="Username", font=("Times New Roman", 24), fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(300, 300, text="Password", font=("Times New Roman", 24), fill=get_data.get_text_color())
        def clickHandler1(event):
            tt = tk_master()
            tt.company_registration()
        new_register_id = canvas1.create_text(440, 450, text="New Registration Here...", font=("Times New Roman", 24),fill=get_data.get_text_color())
        canvas1.tag_bind(new_register_id, "<1>", clickHandler1)
        e1 = Entry(canvas1,font=('times', 15, ' bold '))
        canvas1.create_window(470, 200, window=e1)
        e2 = Entry(canvas1, font=('times', 15, ' bold '),show="*")
        canvas1.create_window(470, 300, window=e2)
        def exit_program():
            a=e1.get()
            b=e2.get()
            if (a == ""):
                messagebox.showinfo(title="Alert", message="Enter Username", parent=company_login_root)
            elif (b == ""):
                messagebox.showinfo(title="Alert", message="Enter Password", parent=company_login_root)
            else:
                tk_master.company=a
                qry = "SELECT * from company_details where username='" +str(a)+ "' and password='"+ str(b)+ "'"
                result = mm.select_login(qry)
                if result == "no":
                    messagebox.showinfo("Result","Login Failed", parent=company_login_root)
                else:

                    tt = tk_master()

                    tt.care_taker=str(a)
                    messagebox.showinfo("Result","Login Success", parent=company_login_root)
                    company_login_root.destroy()
                    tt = tk_master()
                    tt.company_home()

        b1=Button(canvas1, text="Login", command=exit_program, font=('times', 15, ' bold '))
        canvas1.create_window(470, 400, window=b1)
        company_login_root.mainloop()
    def company_registration(self):
        company_registration_root = Toplevel()
        company_registration_root.attributes('-topmost', 'true')
        get_data = tk_master()
        w = 780
        h = 500
        ws = company_registration_root.winfo_screenwidth()
        hs = company_registration_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        company_registration_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        image = Image.open('images/background_hd1.jpg')
        img = image.resize((w, h))
        my_img = ImageTk.PhotoImage(img)
        company_registration_root.resizable(False, False)
        canvas1 = Canvas(company_registration_root, width=200, height=300)
        canvas1.create_image(0, 0, image=my_img, anchor=NW)
        canvas1.pack(fill="both", expand=True)
        # canvas1.create_text(390, 20, text=get_data.get_title(), font=("Times New Roman", 24),
        #                     fill=get_data.get_text_color())
        ##
        admin_id2 = canvas1.create_text(390, 20, text="COMPANY REGISTRATION", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(300, 70, text="Name", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(300, 120, text="Contact", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(300, 170, text="Email", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(300, 220, text="Address", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(300, 270, text="Username", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(300, 320, text="Password", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())

        e1 = Entry(canvas1, font=('times', 15, ' bold '))
        canvas1.create_window(480, 70, window=e1)
        e2 = Entry(canvas1, font=('times', 15, ' bold '))
        canvas1.create_window(480, 120, window=e2)
        e3 = Entry(canvas1, font=('times', 15, ' bold '))
        canvas1.create_window(480, 170, window=e3)
        e4 = Entry(canvas1, font=('times', 15, ' bold '))
        canvas1.create_window(480, 220, window=e4)
        e5 = Entry(canvas1, font=('times', 15, ' bold '))
        canvas1.create_window(480, 270, window=e5)
        e6 = Entry(canvas1, font=('times', 15, ' bold '))
        canvas1.create_window(480, 320, window=e6)

        def exit_program():
            name = e1.get()
            contact = e2.get()
            email = e3.get()
            address = e4.get()
            username = e5.get()
            password = e6.get()
            if (name == ""):
                messagebox.showinfo(title="Alert", message="Enter Name", parent=company_registration_root)
            elif (contact == ""):
                messagebox.showinfo(title="Alert", message="Enter Contact", parent=company_registration_root)
            elif (email == ""):
                messagebox.showinfo(title="Alert", message="Enter Email", parent=company_registration_root)
            elif (address == ""):
                messagebox.showinfo(title="Alert", message="Enter Address", parent=company_registration_root)
            elif (username == ""):
                messagebox.showinfo(title="Alert", message="Enter Username", parent=company_registration_root)
            elif (password == ""):
                messagebox.showinfo(title="Alert", message="Enter Password", parent=company_registration_root)
            else:
                maxin = mm.find_max_id("company_details")
                qry = ("insert into company_details values('" + str(maxin) + "','" + str(name) + "','" + str(
                    contact) + "','" + str(email) + "','" + str(address) + "','" + str(username) + "','" + str(
                    password) + "','0','0')")
                result = mm.insert_query(qry)
                messagebox.showinfo(title="Alert", message="Registration Success", parent=company_registration_root)
                company_registration_root.destroy()
        b1 = Button(canvas1, text="Register", command=exit_program, font=('times', 15, ' bold '))
        canvas1.create_window(470, 400, window=b1)
        company_registration_root.mainloop()

    def user_login(self):
        user_login_root =Toplevel()
        user_login_root.attributes('-topmost', 'true')
        get_data=tk_master()
        w = 780
        h = 500
        ws = user_login_root.winfo_screenwidth()
        hs = user_login_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        user_login_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        image = Image.open('images/background_hd1.jpg')
        img = image.resize((w, h))
        my_img = ImageTk.PhotoImage(img)
        user_login_root.resizable(False, False)
        canvas1 = Canvas(user_login_root, width=200, height=300)
        canvas1.create_image(0, 0, image=my_img, anchor=NW)
        canvas1.pack(fill="both", expand=True)
        canvas1.create_text(390, 20, text=get_data.get_titlec(), font=("Times New Roman", 24), fill=get_data.get_text_color())
        ##
        admin_id2 = canvas1.create_text(390, 100, text="USER LOGIN", font=("Times New Roman", 24), fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(300, 200, text="Username", font=("Times New Roman", 24), fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(300, 300, text="Password", font=("Times New Roman", 24), fill=get_data.get_text_color())
        def clickHandler1(event):
            tt = tk_master()
            tt.user_registration()
        new_register_id = canvas1.create_text(440, 450, text="New Registration Here...", font=("Times New Roman", 24),fill=get_data.get_text_color())
        canvas1.tag_bind(new_register_id, "<1>", clickHandler1)
        e1 = Entry(canvas1,font=('times', 15, ' bold '))
        canvas1.create_window(470, 200, window=e1)
        e2 = Entry(canvas1, font=('times', 15, ' bold '),show="*")
        canvas1.create_window(470, 300, window=e2)
        def exit_program():
            a=e1.get()
            b=e2.get()
            if (a == ""):
                messagebox.showinfo(title="Alert", message="Enter Username", parent=user_login_root)
            elif (b == ""):
                messagebox.showinfo(title="Alert", message="Enter Password", parent=user_login_root)
            else:
                tk_master.user=a
                qry = "SELECT * from user_details where username='" +str(a)+ "' and password='"+ str(b)+ "'"
                result = mm.select_login(qry)
                if result == "no":
                    messagebox.showinfo("Result","Login Failed", parent=user_login_root)
                else:
                    tt = tk_master()
                    tt.care_taker=str(a)
                    messagebox.showinfo("Result","Login Success", parent=user_login_root)
                    user_login_root.destroy()

                    tt.user_home()
                    # d = DomainOperations()
                    # d.run()

        b1=Button(canvas1, text="Login", command=exit_program, font=('times', 15, ' bold '))
        canvas1.create_window(470, 400, window=b1)
        user_login_root.mainloop()
    def user_registration(self):
        user_registration_root = Toplevel()
        user_registration_root.attributes('-topmost', 'true')
        get_data = tk_master()
        w = 780
        h = 500
        ws = user_registration_root.winfo_screenwidth()
        hs = user_registration_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        user_registration_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        image = Image.open('images/background_hd1.jpg')
        img = image.resize((w, h))
        my_img = ImageTk.PhotoImage(img)
        user_registration_root.resizable(False, False)
        canvas1 = Canvas(user_registration_root, width=200, height=300)
        canvas1.create_image(0, 0, image=my_img, anchor=NW)
        canvas1.pack(fill="both", expand=True)
        # canvas1.create_text(390, 20, text=get_data.get_title(), font=("Times New Roman", 24),
        #                     fill=get_data.get_text_color())
        ##
        admin_id2 = canvas1.create_text(390, 20, text="USER REGISTRATION", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(300, 70, text="Name", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(300, 120, text="Contact", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(300, 170, text="Email", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(300, 220, text="Address", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(300, 270, text="Username", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(300, 320, text="Password", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())

        e1 = Entry(canvas1, font=('times', 15, ' bold '))
        canvas1.create_window(480, 70, window=e1)
        e2 = Entry(canvas1, font=('times', 15, ' bold '))
        canvas1.create_window(480, 120, window=e2)
        e3 = Entry(canvas1, font=('times', 15, ' bold '))
        canvas1.create_window(480, 170, window=e3)
        e4 = Entry(canvas1, font=('times', 15, ' bold '))
        canvas1.create_window(480, 220, window=e4)
        e5 = Entry(canvas1, font=('times', 15, ' bold '))
        canvas1.create_window(480, 270, window=e5)
        e6 = Entry(canvas1, font=('times', 15, ' bold '))
        canvas1.create_window(480, 320, window=e6)

        def exit_program():
            name = e1.get()
            contact = e2.get()
            email = e3.get()
            address = e4.get()
            username = e5.get()
            password = e6.get()
            if (name == ""):
                messagebox.showinfo(title="Alert", message="Enter Name", parent=user_registration_root)
            elif (contact == ""):
                messagebox.showinfo(title="Alert", message="Enter Contact", parent=user_registration_root)
            elif (email == ""):
                messagebox.showinfo(title="Alert", message="Enter Email", parent=user_registration_root)
            elif (address == ""):
                messagebox.showinfo(title="Alert", message="Enter Address", parent=user_registration_root)
            elif (username == ""):
                messagebox.showinfo(title="Alert", message="Enter Username", parent=user_registration_root)
            elif (password == ""):
                messagebox.showinfo(title="Alert", message="Enter Password", parent=user_registration_root)
            else:
                maxin = mm.find_max_id("user_details")
                qry = ("insert into user_details values('" + str(maxin) + "','" + str(name) + "','" + str(
                    contact) + "','" + str(email) + "','" + str(address) + "','" + str(username) + "','" + str(
                    password) + "','0','0')")
                result = mm.insert_query(qry)
                messagebox.showinfo(title="Alert", message="Registration Success", parent=user_registration_root)
                user_registration_root.destroy()
        b1 = Button(canvas1, text="Register", command=exit_program, font=('times', 15, ' bold '))
        canvas1.create_window(470, 400, window=b1)
        user_registration_root.mainloop()
    def user_home(self):
        user_home_root = Toplevel()
        user_home_root.attributes('-topmost', 'true')
        get_data = tk_master()
        w = 780
        h = 500
        ws = user_home_root.winfo_screenwidth()
        hs = user_home_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        user_home_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        image = Image.open('images/background_hd1.jpg')
        img = image.resize((w, h))
        my_img = ImageTk.PhotoImage(img)
        user_home_root.resizable(False, False)
        canvas1 = Canvas(user_home_root, width=200, height=300)
        canvas1.create_image(0, 0, image=my_img, anchor=NW)
        canvas1.pack(fill="both", expand=True)

        admin_id2 = canvas1.create_text(390, 20, text="USER HOME", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())

        def job_search():

            job_search_root = Toplevel()

            def view_data():
                def selectItem(a):
                    curItem = tree.focus()
                    data = (tree.item(curItem))
                    data1 = (data['values'])


                    tk_master.job_id = data1[0]
                    tk_master.job_name = data1[1]
                    tk_master.job_company = data1[2]
                    # tk_master.job_skills = data1[3]

                    import exam_data
                    exam_data.exam_demo.job_name = data1[1]
                    exam_data.exam_demo.job_company = data1[2]


                    # print(file_name)
                    job_search_root.destroy()
                    tt = tk_master()
                    tt.job_search_1()
                date_list = []
                id = e1.get()
                data = mm.select_direct_query("select id,job_title,skills from job_details where job_title='" + str(id) + "' or skills='"+str(id)+"' and status='0'")
                for x in data:
                    date_list.append(x)

                print(date_list)
                TableMargin = Frame(job_search_root, width=600)
                TableMargin.place(x=50, y=150, width=600, height=400)
                scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
                scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
                tree = ttk.Treeview(TableMargin, columns=("id", "job_title", "skills"), height=400,
                                    selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
                scrollbary.config(command=tree.yview)
                scrollbary.pack(side=RIGHT, fill=Y)
                scrollbarx.config(command=tree.xview)
                scrollbarx.pack(side=BOTTOM, fill=X)
                tree.heading('id', text="id", anchor=W)
                # tree.heading('company', text="company", anchor=W)
                tree.heading('job_title', text="job_title", anchor=W)
                tree.heading('skills', text="skills", anchor=W)
                tree.bind('<ButtonRelease-1>', selectItem)
                tree.column('#0', stretch=NO, minwidth=0, width=0)
                tree.column('#1', stretch=NO, minwidth=0, width=200)
                tree.column('#2', stretch=NO, minwidth=0, width=200)
                # tree.column('#3', stretch=NO, minwidth=0, width=200)
                tree.pack()




                tree.pack()
                for x in date_list:
                    tree.insert("", 0, values=(x))

            job_search_root.attributes('-topmost', 'true')
            get_data = tk_master()
            w = 880
            h = 600
            ws = job_search_root.winfo_screenwidth()
            hs = job_search_root.winfo_screenheight()
            x = (ws / 2) - (w / 2)
            y = (hs / 2) - (h / 2)
            job_search_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
            image = Image.open('images/background_hd.jpg')
            img = image.resize((w, h))
            my_img = ImageTk.PhotoImage(img)
            job_search_root.resizable(False, False)
            canvas1 = Canvas(job_search_root, width=200, height=300)
            canvas1.create_image(0, 0, image=my_img, anchor=NW)
            canvas1.pack(fill="both", expand=True)
            # canvas1.create_text(390, 20, text=get_data.get_title(), font=("Times New Roman", 30),
            #                     fill=get_data.get_text_color())
            ##
            admin_id2 = canvas1.create_text(390, 20, text="JOB SEARCH", font=("Times New Roman", 24),
                                            fill=get_data.get_text_color())
            admin_id2 = canvas1.create_text(100, 100, text="Job Title", font=("Times New Roman", 24),
                                            fill=get_data.get_text_color())
            e1 = Entry(canvas1, font=('times', 15, ' bold '))
            canvas1.create_window(280, 100, window=e1)

            b1 = Button(canvas1, text="Search", command=view_data, font=('times', 15, ' bold '))
            canvas1.create_window(490, 100, window=b1)
            job_search_root.mainloop()
        def dd2():
            dd=0
        b1 = Button(canvas1, text="Job Search", command=job_search, font=('times', 15, ' bold '))
        canvas1.create_window(420, 150, window=b1)
        ###
        b2 = Button(canvas1, text="Logout", command=dd2, font=('times', 15, ' bold '))
        canvas1.create_window(420, 200, window=b2)
        ###
        # b3 = Button(canvas1, text="Received", command=dd3, font=('times', 15, ' bold '))
        # canvas1.create_window(420,
        # .250, window=b3)

        user_home_root.mainloop()
    def job_search_1(self):
        job_search_1_root = Toplevel()
        job_search_1_root.attributes('-topmost', 'true')
        get_data = tk_master()
        w = 780
        h = 500
        ws = job_search_1_root.winfo_screenwidth()
        hs = job_search_1_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        job_search_1_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        image = Image.open('images/background_hd1.jpg')
        img = image.resize((w, h))
        my_img = ImageTk.PhotoImage(img)
        job_search_1_root.resizable(False, False)
        canvas1 = Canvas(job_search_1_root, width=200, height=300)
        canvas1.create_image(0, 0, image=my_img, anchor=NW)
        canvas1.pack(fill="both", expand=True)
        canvas1.create_text(390, 20, text=get_data.get_titlec(), font=("Times New Roman", 24),
                            fill=get_data.get_text_color())
        ##
        admin_id2 = canvas1.create_text(390, 100, text="Start Interview", font=("Times New Roman", 20),
                                        fill=get_data.get_text_color())

        admin_id2 = canvas1.create_text(200, 200, text="Job Title", font=("Times New Roman", 20),
                                        fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(200, 250, text="Skills", font=("Times New Roman", 20),
                                        fill=get_data.get_text_color())
        # admin_id2 = canvas1.create_text(200, 300, text="Skills", font=("Times New Roman", 20),
        #                                 fill=get_data.get_text_color())

        admin_id2 = canvas1.create_text(470, 200, text=tk_master.job_name, font=("Times New Roman", 20),fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(470, 250, text=tk_master.job_company, font=("Times New Roman", 20),fill=get_data.get_text_color())
        admin_id2 = canvas1.create_text(470, 300, text=tk_master.job_skills, font=("Times New Roman", 20),fill=get_data.get_text_color())

        def exit_program():
            # print('ddd')
            job_search_1_root.destroy()
            d = DomainOperations()
            d.run()


        b1 = Button(canvas1, text="START", command=exit_program, font=('times', 15, ' bold '))
        canvas1.create_window(470, 450, window=b1)
        job_search_1_root.mainloop()


    def user_voice(self):
        global name, message
        name = ''
        message = ''
        user_voice_root = Toplevel()
        user_voice_root.attributes('-topmost', 'true')
        get_data = tk_master()
        w = 780
        h = 500
        ws = user_voice_root.winfo_screenwidth()
        hs = user_voice_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        user_voice_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        image = Image.open('images/background_hd1.jpg')
        img = image.resize((w, h))
        my_img = ImageTk.PhotoImage(img)
        user_voice_root.resizable(False, False)
        canvas1 = Canvas(user_voice_root, width=200, height=300)
        canvas1.create_image(0, 0, image=my_img, anchor=NW)
        canvas1.pack(fill="both", expand=True)
        canvas1.create_text(390, 20, text=get_data.get_titlec(), font=("Times New Roman", 24),
                            fill=get_data.get_text_color())
        ##
        admin_id2 = canvas1.create_text(390, 100, text="Voice Input", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())

        def clickHandler():
            print("call")
            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio_data = r.record(source, duration=4)
                text = r.recognize_google(audio_data)
                print(text)
                user_voice_root.name = text
                canvas1.itemconfig(amount_view, text=str(text))

        global amount_view
        amount_view = canvas1.create_text(380, 150, text="-", font=("Times New Roman", 30),
                                          fill=get_data.get_text_color())
        bb1 = Button(canvas1, font=('times', 15, ' bold '), text='INPUT', command=clickHandler)
        canvas1.create_window(150, 150, window=bb1)

        ##############################################
        def clickHandler1():
            print("call")
            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio_data = r.record(source, duration=4)
                text = r.recognize_google(audio_data)
                print(text)
                user_voice_root.message = text
                canvas1.itemconfig(amount_view1, text=str(text))

        global amount_view1
        amount_view1 = canvas1.create_text(380, 200, text="-", font=("Times New Roman", 30),
                                           fill=get_data.get_text_color())
        bb2 = Button(canvas1, font=('times', 15, ' bold '), text='Message', command=clickHandler1)
        canvas1.create_window(150, 200, window=bb2)

        def exit_program():
            user_voice_root.destroy()

        b1 = Button(canvas1, text="SEND", command=exit_program, font=('times', 15, ' bold '))
        canvas1.create_window(470, 250, window=b1)
        user_voice_root.mainloop()

    def company_home(self):
        company_home_root = Toplevel()

        company_home_root.attributes('-topmost', 'true')
        get_data = tk_master()
        w = 780
        h = 500
        ws = company_home_root.winfo_screenwidth()
        hs = company_home_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        company_home_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        image = Image.open('images/background_hd1.jpg')
        img = image.resize((w, h))
        my_img = ImageTk.PhotoImage(img)
        company_home_root.resizable(False, False)
        canvas1 = Canvas(company_home_root, width=200, height=300)
        canvas1.create_image(0, 0, image=my_img, anchor=NW)
        canvas1.pack(fill="both", expand=True)
        canvas1.create_text(390, 20, text=get_data.get_titlec(), font=("Times New Roman", 24),
                            fill=get_data.get_text_color())
        ##
        admin_id2 = canvas1.create_text(390, 100, text="COMPANY HOME", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        def add_keyword():
            admin_add_keyword_root = Toplevel()
            admin_add_keyword_root.attributes('-topmost', 'true')
            get_data = tk_master()
            w = 780
            h = 500
            ws = admin_add_keyword_root.winfo_screenwidth()
            hs = admin_add_keyword_root.winfo_screenheight()
            x = (ws / 2) - (w / 2)
            y = (hs / 2) - (h / 2)
            admin_add_keyword_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
            image = Image.open('images/background_hd1.jpg')
            img = image.resize((w, h))
            my_img = ImageTk.PhotoImage(img)
            admin_add_keyword_root.resizable(False, False)
            canvas1 = Canvas(admin_add_keyword_root, width=200, height=300)
            canvas1.create_image(0, 0, image=my_img, anchor=NW)
            canvas1.pack(fill="both", expand=True)
            canvas1.create_text(390, 20, text=get_data.get_titlec(), font=("Times New Roman", 24),
                                fill=get_data.get_text_color())
            ##
            admin_id2 = canvas1.create_text(390, 100, text="ADD JOB", font=("Times New Roman", 20),fill=get_data.get_text_color())
            admin_id2 = canvas1.create_text(200, 200, text="Job Title", font=("Times New Roman", 20),fill=get_data.get_text_color())
            admin_id2 = canvas1.create_text(200, 250, text="Skils Required", font=("Times New Roman", 20),fill=get_data.get_text_color())
            admin_id2 = canvas1.create_text(200, 300, text="Salary", font=("Times New Roman", 20),fill=get_data.get_text_color())
            admin_id2 = canvas1.create_text(200, 350, text="Description", font=("Times New Roman", 20),fill=get_data.get_text_color())

            def write_dataset(company, job, question, answer):
                file = 'dataset.csv'
                pr_chk = 0
                # with open(file) as f:
                #     reader = csv.DictReader(f, delimiter=',')
                #     for row in reader:
                #         t1 = row['company']
                #         a, b = (t1), (company)
                #         if a == b:
                #             pr_chk += 1
                if pr_chk == 0:
                    file1 = 'dataset1.csv'
                    with open(file) as f, open('dataset1.csv', 'w', encoding='utf-8', newline='')as csvfile:
                        reader = csv.DictReader(f, delimiter=',')
                        filewriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                        filewriter.writerow(
                            ['company', 'job', 'question', 'answer'])
                        for row in reader:
                            t1 = row['company']
                            t2 = row['job']
                            t3 = row['question']
                            t4 = row['answer']
                            filewriter.writerow([t1, t2, t3, t4])
                        filewriter.writerow([company, job, question, answer])
                    shutil.copy('dataset1.csv', file)
                    os.remove(file1)
                    messagebox.showinfo(title="info", message="Success", parent=admin_add_keyword_root)
                else:
                    messagebox.showinfo(title="info", message="Already Trained", parent=admin_add_keyword_root)

            e1 = Entry(canvas1, font=('times', 15, ' bold '))
            canvas1.create_window(470, 200, window=e1)

            e2 = Entry(canvas1, font=('times', 15, ' bold '))
            canvas1.create_window(470, 250, window=e2)

            e3 = Entry(canvas1, font=('times', 15, ' bold '))
            canvas1.create_window(470, 300, window=e3)

            e4 = Entry(canvas1, font=('times', 15, ' bold '))
            canvas1.create_window(470, 350, window=e4)

            def exit_program():
                company=tk_master.company
                a = e1.get()
                b = e2.get()
                c = e3.get()
                d = e4.get()

                if (a == ""):
                    messagebox.showinfo(title="Alert", message="Enter Job Title", parent=admin_add_keyword_root)
                elif (b == ""):
                    messagebox.showinfo(title="Alert", message="Enter skills", parent=admin_add_keyword_root)
                elif (c == ""):
                    messagebox.showinfo(title="Alert", message="Enter Salary", parent=admin_add_keyword_root)
                elif (d == ""):
                    messagebox.showinfo(title="Alert", message="Enter Description", parent=admin_add_keyword_root)
                else:
                    maxin = mm.find_max_id("job_details")
                    qry = ("insert into job_details values('" + str(maxin) + "','" + str(company) + "','" + str(a) + "','" + str(b) + "','" + str(c) + "','" + str(d) + "','0','0')")
                    result = mm.insert_query(qry)
                    # write_dataset(str(a), str(b), str(c), str(d))
                    messagebox.showinfo(title="Alert", message="Success", parent=admin_add_keyword_root)
                    admin_add_keyword_root.destroy()


            b1 = Button(canvas1, text="ADD JOB", command=exit_program, font=('times', 15, ' bold '))
            canvas1.create_window(470, 450, window=b1)
            admin_add_keyword_root.mainloop()
        def add_question():
            add_question_root = Toplevel()
            add_question_root.attributes('-topmost', 'true')
            get_data = tk_master()
            w = 780
            h = 500
            ws = add_question_root.winfo_screenwidth()
            hs = add_question_root.winfo_screenheight()
            x = (ws / 2) - (w / 2)
            y = (hs / 2) - (h / 2)
            add_question_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
            image = Image.open('images/background_hd1.jpg')
            img = image.resize((w, h))
            my_img = ImageTk.PhotoImage(img)
            add_question_root.resizable(False, False)
            canvas1 = Canvas(add_question_root, width=200, height=300)
            canvas1.create_image(0, 0, image=my_img, anchor=NW)
            canvas1.pack(fill="both", expand=True)
            canvas1.create_text(390, 20, text=get_data.get_titlec(), font=("Times New Roman", 24),
                                fill=get_data.get_text_color())
            ##
            admin_id2 = canvas1.create_text(390, 100, text="ADD QUESTION", font=("Times New Roman", 20),fill=get_data.get_text_color())
            admin_id2 = canvas1.create_text(200, 200, text="Company", font=("Times New Roman", 20),fill=get_data.get_text_color())
            admin_id2 = canvas1.create_text(200, 250, text="Job Title", font=("Times New Roman", 20),fill=get_data.get_text_color())
            admin_id2 = canvas1.create_text(200, 300, text="Question", font=("Times New Roman", 20),fill=get_data.get_text_color())
            admin_id2 = canvas1.create_text(200, 350, text="Answer", font=("Times New Roman", 20),fill=get_data.get_text_color())

            def write_dataset(company, job, question, answer):
                file = 'dataset.csv'
                pr_chk = 0
                # with open(file) as f:
                #     reader = csv.DictReader(f, delimiter=',')
                #     for row in reader:
                #         t1 = row['company']
                #         a, b = (t1), (company)
                #         if a == b:
                #             pr_chk += 1
                if pr_chk == 0:
                    file1 = 'dataset1.csv'
                    with open(file) as f, open('dataset1.csv', 'w', encoding='utf-8', newline='')as csvfile:
                        reader = csv.DictReader(f, delimiter=',')
                        filewriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                        filewriter.writerow(
                            ['company', 'job', 'question', 'answer'])
                        for row in reader:
                            t1 = row['company']
                            t2 = row['job']
                            t3 = row['question']
                            t4 = row['answer']
                            filewriter.writerow([t1, t2, t3, t4])
                        filewriter.writerow([company, job, question, answer])
                    shutil.copy('dataset1.csv', file)
                    os.remove(file1)
                #     messagebox.showinfo(title="info", message="Success", parent=add_question_root)
                # else:
                #     messagebox.showinfo(title="info", message="Already Trained", parent=add_question_root)

            aa = tk_master.company
            # print(aa)
            e1 = Entry(canvas1, font=('times', 15, ' bold '),text=aa)
            canvas1.create_window(470, 200, window=e1)
            e1.delete(0, END)
            e1.insert(0, aa)

            # e2 = Entry(canvas1, font=('times', 15, ' bold '))
            # canvas1.create_window(470, 250, window=e2)

            tk_master.job_list = mm.select_direct_query("select * from job_details where company='" + str(aa) + "'")
            # print(tk_master.job_list)
            job_title=[]
            for x in tk_master.job_list:
                job_title.append(x[2])
            # print(job_title)

            combo = ttk.Combobox(canvas1,state="readonly", font=('times', 14, ' bold '),values=job_title)
            # combo.place(x=50, y=50)
            canvas1.create_window(470, 250, window=combo)


            e3 = Entry(canvas1, font=('times', 15, ' bold '))
            canvas1.create_window(470, 300, window=e3)

            e4 = Entry(canvas1, font=('times', 15, ' bold '))
            canvas1.create_window(470, 350, window=e4)

            def exit_program():
                company=tk_master.company
                a = e1.get()
                b = combo.get()
                c = e3.get()
                d = e4.get()

                if (a == ""):
                    messagebox.showinfo(title="Alert", message="Enter Company", parent=add_question_root)
                elif (b == ""):
                    messagebox.showinfo(title="Alert", message="Select Job Title", parent=add_question_root)
                elif (c == ""):
                    messagebox.showinfo(title="Alert", message="Enter Question", parent=add_question_root)
                elif (d == ""):
                    messagebox.showinfo(title="Alert", message="Enter Answer", parent=add_question_root)
                else:
                    # maxin = mm.find_max_id("job_details")
                    # qry = ("insert into job_details values('" + str(maxin) + "','" + str(company) + "','" + str(a) + "','" + str(b) + "','" + str(c) + "','" + str(d) + "','0','0')")
                    # result = mm.insert_query(qry)
                    write_dataset(str(a), str(b), str(c), str(d))
                    messagebox.showinfo(title="Alert", message="Success", parent=add_question_root)
                    add_question_root.destroy()


            b1 = Button(canvas1, text="ADD JOB", command=exit_program, font=('times', 15, ' bold '))
            canvas1.create_window(470, 450, window=b1)
            add_question_root.mainloop()



        b1 = Button(canvas1, text="Add Job Details", command=add_keyword, font=('times', 15, ' bold '))
        canvas1.create_window(370,150, window=b1)

        b2 = Button(canvas1, text="Add Question", command=add_question, font=('times', 15, ' bold '))
        canvas1.create_window(370, 200, window=b2)
        def user_details():
            user_details_root = Toplevel()

            user_details_root.attributes('-topmost', 'true')
            w = 650
            h = 350
            ws = user_details_root.winfo_screenwidth()
            hs = user_details_root.winfo_screenheight()
            x = (ws / 2) - (w / 2)
            y = (hs / 2) - (h / 2)
            user_details_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
            self.bg = ImageTk.PhotoImage(file='images/background_hd.jpg')
            user_details_root.title(get_data.get_titlec())
            user_details_root.resizable(False, False)
            bg = ImageTk.PhotoImage(file='images/background_hd1.jpg')
            canvas = Canvas(user_details_root, width=200, height=300)
            canvas.pack(fill="both", expand=True)
            canvas.create_image(0, 0, image=bg, anchor=NW)
            admin_id2 = canvas.create_text(310, 70, text="User Details", font=("Times New Roman", 24),
                                           fill=get_data.get_text_color())
            fram = Frame(canvas)
            fram.place(x=60, y=100, width=550, height=230)
            scrollbarx = Scrollbar(fram, orient=HORIZONTAL)
            scrollbary = Scrollbar(fram, orient=VERTICAL)
            tree = Treeview(fram, columns=("name", "contact", "email", "address"),
                            yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
            scrollbarx.config(command=tree.xview)
            scrollbarx.pack(side=BOTTOM, fill=X)
            scrollbary.config(command=tree.yview)
            scrollbary.pack(side=RIGHT, fill=Y)
            tree.heading('name', text="name", anchor=W)
            tree.heading('contact', text="contact", anchor=W)
            tree.heading('email', text="email", anchor=W)
            tree.heading('address', text="address", anchor=W)


            tree.column('#0', width=0)
            tree.column('#1', width=100)
            tree.column('#2', width=100)
            tree.column('#3', width=100)

            tree.pack()
            d1 = mm.select_direct_query("select * from user_details")
            for data in d1:
                tree.insert("", 0, values=data)

            user_details_root.mainloop()



        b1 = Button(canvas1, text="User Details", command=user_details, font=('times', 15, ' bold '))
        canvas1.create_window(370,250, window=b1)
        company_home_root.mainloop()



ar = tk_master()
root = ar.set_window_design()

