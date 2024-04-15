from tkinter import *
from matplotlib import pyplot as plt
from PIL import ImageTk,Image
import sqlite3
conn = sqlite3.connect('manage.db')
c = conn.cursor()
obj1 = Tk()
obj1.title("Faculty Performance Information")
obj1.geometry("800x800")
obj1.configure(bg='black')
Label(obj1,text="Faculty Performance Information",width=30,bg='black',fg='white',font="Times 45 bold").grid(row=3,column=0)
Label(obj1,text="About Us ",bg='black',fg='white',font="Times 30 bold").grid(row=5,column=0)
Label(obj1,text="This site helps navigate through different aspects of Faculty Performance Information in an convenient manner.\n We provide options like personal and professional data along with statistical data to make it easier to analyse them.",bg='black',fg='white',font="Times 15 ").grid(row=6,column=0)
Label(obj1,text="Search",bg='black',width=30,fg='white',font="Times 30 bold").grid(row=9,column=0)
Label(obj1,text="It provides two filters to display only the information required.\n It has two options: to search by year or the profeesional parameter.",bg='black',fg='white',font="Times 15").grid(row=10,column=0)
Label(obj1,text="Information",bg='black',width=30,fg='white',font="Times 30 bold").grid(row=7,column=0)
Label(obj1,text="This displays the detailed personal and professional information of a particular Faculty.",bg='black',fg='white',font="Times 15").grid(row=8,column=0)
Label(obj1,text="Statistical Data",bg='black',width=30,fg='white',font="Times 30 bold").grid(row=11,column=0)
Label(obj1,text="This displays analytical data in a visually appealing manner ",bg='black',fg='white',font="Times 15").grid(row=12,column=0)

path="back2.png"
img=ImageTk.PhotoImage(Image.open(path))
l=Label(obj1,image=img).grid(row=14)
def n(p):
    t=Toplevel()
    print(p)
    t.title("Personal Information -> Prof. Nishee Shelat")
    t.geometry("500x500")
    t.configure(bg='black')
    path="female.png"
    img=ImageTk.PhotoImage(Image.open(path))
    l=Label(t,image=img)
    l.grid(row=0,column=1)
    r1=15
    c1=1
    x=c.execute("Select faculty_name from faculty where faculty_id='101'")
    Label(t,text='Name : ',bg='black',fg='white',font='30').grid(row=r1,column=0)
    for row in x.fetchall():
        for i in range(0,1):
            Label(t, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
        r1=r1+1
    x=c.execute("Select faculty_age from faculty where faculty_id='101'")
    Label(t,text='Age :',bg='black',fg='white',font='30').grid(column=0)
    for row in x.fetchall():
        for i in range(0,1):
            Label(t, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
        r1=r1+1
    x=c.execute("Select experience from faculty where faculty_id='101'")
    Label(t,text='Experience(years) :',bg='black',fg='white',font='30').grid(column=0)
    for row in x.fetchall():
        for i in range(0,1):
            Label(t, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
        r1=r1+1
    x=c.execute("Select address from faculty where faculty_id='101'")
    Label(t,text='Address :',bg='black',fg='white',font='30').grid(column=0)
    for row in x.fetchall():
        for i in range(0,1):
            Label(t, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
        r1=r1+1
    x=c.execute("Select email_id from faculty where faculty_id='101'")
    Label(t,text='Email :',bg='black',fg='white',font='30').grid(column=0)
    for row in x.fetchall():
        for i in range(0,1):
            Label(t, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
        r1=r1+1
    t.mainloop()
def ys():
    t=Toplevel()
    t.title("Personal Information -> Prof. Yashesh Sorathia")
    t.geometry("500x500")
    t.configure(bg='black')
    path="male.png"
    img=ImageTk.PhotoImage(Image.open(path))
    l=Label(t,image=img)
    l.grid(row=0,column=1)
    r1=15
    c1=1
    x=c.execute("Select faculty_name from faculty where faculty_id='103'")
    Label(t,text='Name : ',bg='black',fg='white',font='30').grid(row=r1,column=0)
    for row in x.fetchall():
        for i in range(0,1):
            Label(t, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
        r1=r1+1
    x=c.execute("Select faculty_age from faculty where faculty_id='103'")
    Label(t,text='Age :',bg='black',fg='white',font='30').grid(column=0)
    for row in x.fetchall():
        for i in range(0,1):
            Label(t, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
        r1=r1+1
    x=c.execute("Select experience from faculty where faculty_id='103'")
    Label(t,text='Experience(years) :',bg='black',fg='white',font='30').grid(column=0)
    for row in x.fetchall():
        for i in range(0,1):
            Label(t, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
        r1=r1+1
    x=c.execute("Select address from faculty where faculty_id='103'")
    Label(t,text='Address :',bg='black',fg='white',font='30').grid(column=0)
    for row in x.fetchall():
        for i in range(0,1):
            Label(t, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
        r1=r1+1
    x=c.execute("Select email_id from faculty where faculty_id='103'")
    Label(t,text='Email :',bg='black',fg='white',font='30').grid(column=0)
    for row in x.fetchall():
        for i in range(0,1):
            Label(t, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
        r1=r1+1
    t.mainloop()
def d():
    t=Toplevel()
    t.title("Personal Information -> Prof. Dhwani Shah")
    t.geometry("500x500")
    t.configure(bg='black')
    path="female.png"
    img=ImageTk.PhotoImage(Image.open(path))
    l=Label(t,image=img)
    l.grid(row=0,column=1)
    r1=15
    c1=1
    x=c.execute("Select faculty_name from faculty where faculty_id='102'")
    Label(t,text='Name : ',bg='black',fg='white',font='30').grid(row=r1,column=0)
    for row in x.fetchall():
        for i in range(0,1):
            Label(t, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
        r1=r1+1
    x=c.execute("Select faculty_age from faculty where faculty_id='102'")
    Label(t,text='Age :',bg='black',fg='white',font='30').grid(column=0)
    for row in x.fetchall():
        for i in range(0,1):
            Label(t, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
        r1=r1+1
    x=c.execute("Select experience from faculty where faculty_id='102'")
    Label(t,text='Experience(years) :',bg='black',fg='white',font='30').grid(column=0)
    for row in x.fetchall():
        for i in range(0,1):
            Label(t, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
        r1=r1+1
    x=c.execute("Select address from faculty where faculty_id='102'")
    Label(t,text='Address :',bg='black',fg='white',font='30').grid(column=0)
    for row in x.fetchall():
        for i in range(0,1):
            Label(t, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
        r1=r1+1
    x=c.execute("Select email_id from faculty where faculty_id='102'")
    Label(t,text='Email :',bg='black',fg='white',font='30').grid(column=0)
    for row in x.fetchall():
        for i in range(0,1):
            Label(t, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
        r1=r1+1
    t.mainloop()
def k():
    t=Toplevel()
    t.title("Personal Information -> Prof. Kiara Sharma")
    t.geometry("500x500")
    t.configure(bg='black')
    path="female.png"
    img=ImageTk.PhotoImage(Image.open(path))
    l=Label(t,image=img)
    l.grid(row=0,column=1)
    r1=15
    c1=1
    x=c.execute("Select faculty_name from faculty where faculty_id='104'")
    Label(t,text='Name : ',bg='black',fg='white',font='30').grid(row=r1,column=0)
    for row in x.fetchall():
        for i in range(0,1):
            Label(t, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
        r1=r1+1
    x=c.execute("Select faculty_age from faculty where faculty_id='104'")
    Label(t,text='Age :',bg='black',fg='white',font='30').grid(column=0)
    for row in x.fetchall():
        for i in range(0,1):
            Label(t, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
        r1=r1+1
    x=c.execute("Select experience from faculty where faculty_id='104'")
    Label(t,text='Experience(years) :',bg='black',fg='white',font='30').grid(column=0)
    for row in x.fetchall():
        for i in range(0,1):
            Label(t, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
        r1=r1+1
    x=c.execute("Select address from faculty where faculty_id='104'")
    Label(t,text='Address :',bg='black',fg='white',font='30').grid(column=0)
    for row in x.fetchall():
        for i in range(0,1):
            Label(t, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
        r1=r1+1
    x=c.execute("Select email_id from faculty where faculty_id='104'")
    Label(t,text='Email :',bg='black',fg='white',font='30').grid(column=0)
    for row in x.fetchall():
        for i in range(0,1):
            Label(t, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
        r1=r1+1
    t.mainloop()
def kp():
    t=Toplevel()
    t.geometry("500x500")
    t.title("Personal Information -> Prof. Kavya Patel")
    t.configure(bg='black')
    path="female.png"
    img=ImageTk.PhotoImage(Image.open(path))
    l=Label(t,image=img)
    l.grid(row=0,column=1)
    r1=15
    c1=1
    x=c.execute("Select faculty_name from faculty where faculty_id='105'")
    Label(t,text='Name : ',bg='black',fg='white',font='30').grid(row=r1,column=0)
    for row in x.fetchall():
        for i in range(0,1):
            Label(t, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
        r1=r1+1
    x=c.execute("Select faculty_age from faculty where faculty_id='105'")
    Label(t,text='Age :',bg='black',fg='white',font='30').grid(column=0)
    for row in x.fetchall():
        for i in range(0,1):
            Label(t, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
        r1=r1+1
    x=c.execute("Select experience from faculty where faculty_id='105'")
    Label(t,text='Experience(years) :',bg='black',fg='white',font='30').grid(column=0)
    for row in x.fetchall():
        for i in range(0,1):
            Label(t, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
        r1=r1+1
    x=c.execute("Select address from faculty where faculty_id='105'")
    Label(t,text='Address :',bg='black',fg='white',font='30').grid(column=0)
    for row in x.fetchall():
        for i in range(0,1):
            Label(t, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
        r1=r1+1
    x=c.execute("Select email_id from faculty where faculty_id='105'")
    Label(t,text='Email :',bg='black',fg='white',font='30').grid(column=0)
    for row in x.fetchall():
        for i in range(0,1):
            Label(t, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
        r1=r1+1
    t.mainloop()
def s():
    t=Toplevel()
    t.geometry("500x500")
    t.title("Personal Information -> Prof. Sakshi Singhvi")
    t.configure(bg='black')
    path="female.png"
    img=ImageTk.PhotoImage(Image.open(path))
    l=Label(t,image=img)
    l.grid(row=0,column=1)
    r1=15
    c1=1
    x=c.execute("Select faculty_name from faculty where faculty_id='106'")
    Label(t,text='Name : ',bg='black',fg='white',font='30').grid(row=r1,column=0)
    for row in x.fetchall():
        for i in range(0,1):
            Label(t, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
        r1=r1+1
    x=c.execute("Select faculty_age from faculty where faculty_id='106'")
    Label(t,text='Age :',bg='black',fg='white',font='30').grid(column=0)
    for row in x.fetchall():
        for i in range(0,1):
            Label(t, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
        r1=r1+1
    x=c.execute("Select experience from faculty where faculty_id='106'")
    Label(t,text='Experience(years) :',bg='black',fg='white',font='30').grid(column=0)
    for row in x.fetchall():
        for i in range(0,1):
            Label(t, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
        r1=r1+1
    x=c.execute("Select address from faculty where faculty_id='106'")
    Label(t,text='Address :',bg='black',fg='white',font='30').grid(column=0)
    for row in x.fetchall():
        for i in range(0,1):
            Label(t, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
        r1=r1+1
    x=c.execute("Select email_id from faculty where faculty_id='106'")
    Label(t,text='Email :',bg='black',fg='white',font='30').grid(column=0)
    for row in x.fetchall():
        for i in range(0,1):
            Label(t, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
        r1=r1+1
    t.mainloop()
def a():
    t=Toplevel()
    t.title("Personal Information -> Prof. Ananya Singh")
    t.geometry("500x500")
    t.configure(bg='black')
    path="female.png"
    img=ImageTk.PhotoImage(Image.open(path))
    l=Label(t,image=img)
    l.grid(row=0,column=1)
    r1=15
    c1=1
    x=c.execute("Select faculty_name from faculty where faculty_id='107'")
    Label(t,text='Name : ',bg='black',fg='white',font='30').grid(row=r1,column=0)
    for row in x.fetchall():
        for i in range(0,1):
            Label(t, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
        r1=r1+1
    x=c.execute("Select faculty_age from faculty where faculty_id='107'")
    Label(t,text='Age :',bg='black',fg='white',font='30').grid(column=0)
    for row in x.fetchall():
        for i in range(0,1):
            Label(t, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
        r1=r1+1
    x=c.execute("Select experience from faculty where faculty_id='107'")
    Label(t,text='Experience(years) :',bg='black',fg='white',font='30').grid(column=0)
    for row in x.fetchall():
        for i in range(0,1):
            Label(t, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
        r1=r1+1
    x=c.execute("Select address from faculty where faculty_id='107'")
    Label(t,text='Address :',bg='black',fg='white',font='30').grid(column=0)
    for row in x.fetchall():
        for i in range(0,1):
            Label(t, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
        r1=r1+1
    x=c.execute("Select email_id from faculty where faculty_id='107'")
    Label(t,text='Email :',bg='black',fg='white',font='30').grid(column=0)
    for row in x.fetchall():
        for i in range(0,1):
            Label(t, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
        r1=r1+1
    t.mainloop()
def p():
    t=Toplevel()
    t.title("Personal Information -> Prof. Prachi Shiveshwar")
    t.geometry("500x500")
    t.configure(bg='black')
    path="female.png"
    img=ImageTk.PhotoImage(Image.open(path))
    l=Label(t,image=img)
    l.grid(row=0,column=1)
    r1=15
    c1=1
    x=c.execute("Select faculty_name from faculty where faculty_id='108'")
    Label(t,text='Name : ',bg='black',fg='white',font='30').grid(row=r1,column=0)
    for row in x.fetchall():
        for i in range(0,1):
            Label(t, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
        r1=r1+1
    x=c.execute("Select faculty_age from faculty where faculty_id='108'")
    Label(t,text='Age :',bg='black',fg='white',font='30').grid(column=0)
    for row in x.fetchall():
        for i in range(0,1):
            Label(t, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
        r1=r1+1
    x=c.execute("Select experience from faculty where faculty_id='108'")
    Label(t,text='Experience(years) :',bg='black',fg='white',font='30').grid(column=0)
    for row in x.fetchall():
        for i in range(0,1):
            Label(t, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
        r1=r1+1
    x=c.execute("Select address from faculty where faculty_id='108'")
    Label(t,text='Address :',bg='black',fg='white',font='30').grid(column=0)
    for row in x.fetchall():
        for i in range(0,1):
            Label(t, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
        r1=r1+1
    x=c.execute("Select email_id from faculty where faculty_id='108'")
    Label(t,text='Email :',bg='black',fg='white',font='30').grid(column=0)
    for row in x.fetchall():
        for i in range(0,1):
            Label(t, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
        r1=r1+1
    t.mainloop()
    
def open_n():
    t=Toplevel()
    t.title("Professional Information -> Prof. Nishee Shelat")
    t.geometry("300x300")
    t.config(bg='black')
    count=0
    count1=0
    count2=0
    count3=0
    count4=0
    count5=0
    count6=0
    Label(t,text='Prof. Nishee shelat',bg='black',fg='white',font='30').grid()
    r1=2
    c1=1
    x=c.execute("Select * from article_international where faculty_id='101'")
    for row in x.fetchall():
        count=count+1
    x=c.execute("Select * from article_national where faculty_id='101'")
    for row in x.fetchall():
        count=count+1
    x=c.execute("Select * from book_chapter where faculty_id='101'")
    for row in x.fetchall():
        count1=count1+1
    x=c.execute("Select * from case_study where faculty_id='101'")
    for row in x.fetchall():
        count2=count2+1
    x=c.execute("Select * from conference_international_attended where faculty_id='101'")
    for row in x.fetchall():
        count3=count3+1
    x=c.execute("Select * from conference_international_organised where faculty_id='101'")
    for row in x.fetchall():
        count3=count3+1
    x=c.execute("Select * from conference_national_attended where faculty_id='101'")
    for row in x.fetchall():
        count3=count3+1
    x=c.execute("Select * from paper_national where faculty_id='101'")
    for row in x.fetchall():
        count4=count4+1
    x=c.execute("Select * from patent where faculty_id='101'")
    for row in x.fetchall():
        count5=count5+1
    x=c.execute("Select * from events where faculty_id='101'")
    for row in x.fetchall():
        count6=count6+1
    Label(t,text='Article',bg='black',fg='white',font='30').grid(row=r1,column=0)
    Label(t,text=count,bg='black',fg='white',font='30').grid(row=r1,column=c1)
    r1=r1+1
    Label(t,text='Book',bg='black',fg='white',font='30').grid(row=r1,column=0)
    Label(t,text=count1,bg='black',fg='white',font='30').grid(row=r1,column=c1)
    r1=r1+1
    Label(t,text='Case',bg='black',fg='white',font='30').grid(row=r1,column=0)
    Label(t,text=count2,bg='black',fg='white',font='30').grid(row=r1,column=c1)
    r1=r1+1
    Label(t,text='Conference',bg='black',fg='white',font='30').grid(row=r1,column=0)
    Label(t,text=count3,bg='black',fg='white',font='30').grid(row=r1,column=c1)
    r1=r1+1
    Label(t,text='Paper',bg='black',fg='white',font='30').grid(row=r1,column=0)
    Label(t,text=count4,bg='black',fg='white',font='30').grid(row=r1,column=c1)
    r1=r1+1
    Label(t,text='Patent',bg='black',fg='white',font='30').grid(row=r1,column=0)
    Label(t,text=count5,bg='black',fg='white',font='30').grid(row=r1,column=c1)
    r1=r1+1
    Label(t,text='Events',bg='black',fg='white',font='30').grid(row=r1,column=0)
    Label(t,text=count6,bg='black',fg='white',font='30').grid(row=r1,column=c1)
def open_d():
    t=Toplevel()
    t.title("Professional Information -> Prof. Dhwani Shah")
    t.geometry("300x300")
    t.config(bg='black')
    count=0
    count1=0
    count2=0
    count3=0
    Label(t,text='Prof. Dhwani Shah',bg='black',fg='white',font='30').grid()
    r1=2
    c1=1
    x=c.execute("Select * from case_study where faculty_id='102'")
    for row in x.fetchall():
        count=count+1
    x=c.execute("Select * from conference_national_attended where faculty_id='102'")
    for row in x.fetchall():
        count1=count1+1
    x=c.execute("Select * from conference_national_organised where faculty_id='102'")
    for row in x.fetchall():
        count1=count1+1
    x=c.execute("Select * from paper_international where faculty_id='102'")
    for row in x.fetchall():
        count2=count2+1
    x=c.execute("Select * from paper_national where faculty_id='102'")
    for row in x.fetchall():
        count2=count2+1
    x=c.execute("Select * from project_consult where faculty_id='102'")
    for row in x.fetchall():
        count3=count3+1
    Label(t,text='Case Study',bg='black',fg='white',font='30').grid(row=r1,column=0)
    Label(t,text=count,bg='black',fg='white',font='30').grid(row=r1,column=c1)
    r1=r1+1
    Label(t,text='Conference',bg='black',fg='white',font='30').grid(row=r1,column=0)
    Label(t,text=count1,bg='black',fg='white',font='30').grid(row=r1,column=c1)
    r1=r1+1
    Label(t,text='Paper',bg='black',fg='white',font='30').grid(row=r1,column=0)
    Label(t,text=count2,bg='black',fg='white',font='30').grid(row=r1,column=c1)
    r1=r1+1
    Label(t,text='Project',bg='black',fg='white',font='30').grid(row=r1,column=0)
    Label(t,text=count3,bg='black',fg='white',font='30').grid(row=r1,column=c1)
def open_ys():
    t=Toplevel()
    t.title("Professional Information -> Prof. Yashesh Sorathia")
    t.geometry("300x300")
    t.config(bg='black')
    count=0
    count1=0
    count2=0
    count3=0
    Label(t,text='Prof. Yashesh Sorathia',bg='black',fg='white',font='30').grid()
    r1=2
    c1=1
    x=c.execute("Select * from article_national where faculty_id='103'")
    for row in x.fetchall():
        count=count+1
    x=c.execute("Select * from conference_international_organised where faculty_id='103'")
    for row in x.fetchall():
        count1=count1+1
    x=c.execute("Select * from paper_international where faculty_id='103'")
    for row in x.fetchall():
        count2=count2+1
    x=c.execute("Select * from project_consult where faculty_id='103'")
    for row in x.fetchall():
        count3=count3+1
    x=c.execute("Select * from project_research where faculty_id='103'")
    for row in x.fetchall():
        count3=count3+1
    Label(t,text='Article',bg='black',fg='white',font='30').grid(row=r1,column=0)
    Label(t,text=count,bg='black',fg='white',font='30').grid(row=r1,column=c1)
    r1=r1+1
    Label(t,text='Conference',bg='black',fg='white',font='30').grid(row=r1,column=0)
    Label(t,text=count1,bg='black',fg='white',font='30').grid(row=r1,column=c1)
    r1=r1+1
    Label(t,text='Paper',bg='black',fg='white',font='30').grid(row=r1,column=0)
    Label(t,text=count2,bg='black',fg='white',font='30').grid(row=r1,column=c1)
    r1=r1+1
    Label(t,text='Project',bg='black',fg='white',font='30').grid(row=r1,column=0)
    Label(t,text=count3,bg='black',fg='white',font='30').grid(row=r1,column=c1)
def open_k():
    t=Toplevel()
    t.title("Professional Information -> Prof. Kiara Sharma")
    t.geometry("300x300")
    t.config(bg='black')
    count=0
    count1=0
    count2=0
    count3=0
    Label(t,text='Prof. Kiara Sharma',bg='black',fg='white',font='30').grid()
    r1=2
    c1=1
    count4=0
    x=c.execute("Select * from Workshop where faculty_id='104'")
    for row in x.fetchall():
        count=count+1
    x=c.execute("Select * from article_national where faculty_id='104'")
    for row in x.fetchall():
        count1=count1+1
    x=c.execute("Select * from book_complete where faculty_id='104'")
    for row in x.fetchall():
        count2=count2+1
    x=c.execute("Select * from conference_international_attended where faculty_id='104'")
    for row in x.fetchall():
        count3=count3+1
    x=c.execute("Select * from project_research where faculty_id='104'")
    for row in x.fetchall():
        count4=count4+1
    Label(t,text='Workshop',bg='black',fg='white',font='30').grid(row=r1,column=0)
    Label(t,text=count,bg='black',fg='white',font='30').grid(row=r1,column=c1)
    r1=r1+1
    Label(t,text='Article',bg='black',fg='white',font='30').grid(row=r1,column=0)
    Label(t,text=count1,bg='black',fg='white',font='30').grid(row=r1,column=c1)
    r1=r1+1
    Label(t,text='Book',bg='black',fg='white',font='30').grid(row=r1,column=0)
    Label(t,text=count2,bg='black',fg='white',font='30').grid(row=r1,column=c1)
    r1=r1+1
    Label(t,text='Conference',bg='black',fg='white',font='30').grid(row=r1,column=0)
    Label(t,text=count3,bg='black',fg='white',font='30').grid(row=r1,column=c1)
    r1=r1+1
    Label(t,text='Project',bg='black',fg='white',font='30').grid(row=r1,column=0)
    Label(t,text=count4,bg='black',fg='white',font='30').grid(row=r1,column=c1)
def open_kp():
    t=Toplevel()
    t.title("Professional Information -> Prof. Kavya Patel")
    t.geometry("300x300")
    t.config(bg='black')
    count=0
    count1=0
    count2=0
    count3=0
    Label(t,text='Prof. Kavya Patel',bg='black',fg='white',font='30').grid()
    r1=2
    c1=1
    x=c.execute("Select * from article_international where faculty_id='105'")
    for row in x.fetchall():
        count=count+1
    x=c.execute("Select * from book_chapter where faculty_id='105'")
    for row in x.fetchall():
        count1=count1+1
    x=c.execute("Select * from events where faculty_id='105'")
    for row in x.fetchall():
        count2=count2+1
    x=c.execute("Select * from patent where faculty_id='105'")
    for row in x.fetchall():
        count3=count3+1
    Label(t,text='Article',bg='black',fg='white',font='30').grid(row=r1,column=0)
    Label(t,text=count,bg='black',fg='white',font='30').grid(row=r1,column=c1)
    r1=r1+1
    Label(t,text='Book',bg='black',fg='white',font='30').grid(row=r1,column=0)
    Label(t,text=count1,bg='black',fg='white',font='30').grid(row=r1,column=c1)
    r1=r1+1
    Label(t,text='Event',bg='black',fg='white',font='30').grid(row=r1,column=0)
    Label(t,text=count2,bg='black',fg='white',font='30').grid(row=r1,column=c1)
    r1=r1+1
    Label(t,text='Patent',bg='black',fg='white',font='30').grid(row=r1,column=0)
    Label(t,text=count3,bg='black',fg='white',font='30').grid(row=r1,column=c1)
def open_s():
    t=Toplevel()
    t.title("Professional Information -> Prof. Sakshi Singhvi")
    t.geometry("300x300")
    t.config(bg='black')
    count=0
    count1=0
    count2=0
    Label(t,text='Prof. Sakshi Singhvi',bg='black',fg='white',font='30').grid()
    r1=2
    c1=1
    x=c.execute("Select * from article_international where faculty_id='106'")
    for row in x.fetchall():
        count=count+1
    x=c.execute("Select * from book_chapter where faculty_id='106'")
    for row in x.fetchall():
        count1=count1+1
    x=c.execute("Select * from project_consult where faculty_id='106'")
    for row in x.fetchall():
        count2=count2+1
    Label(t,text='Article',bg='black',fg='white',font='30').grid(row=r1,column=0)
    Label(t,text=count,bg='black',fg='white',font='30').grid(row=r1,column=c1)
    r1=r1+1
    Label(t,text='Book',bg='black',fg='white',font='30').grid(row=r1,column=0)
    Label(t,text=count1,bg='black',fg='white',font='30').grid(row=r1,column=c1)
    r1=r1+1
    Label(t,text='Project',bg='black',fg='white',font='30').grid(row=r1,column=0)
    Label(t,text=count2,bg='black',fg='white',font='30').grid(row=r1,column=c1)
def open_a():
    t=Toplevel()
    t.title("Professional Information -> Prof. Ananya Singh")
    t.geometry("300x300")
    t.config(bg='black')
    count=0
    count1=0
    count2=0
    Label(t,text='Prof. Ananya Singh',bg='black',fg='white',font='30').grid()
    r1=2
    c1=1
    x=c.execute("Select * from events where faculty_id='107'")
    for row in x.fetchall():
        count=count+1
    x=c.execute("Select * from paper_national where faculty_id='107'")
    for row in x.fetchall():
        count1=count1+1
    x=c.execute("Select * from patent where faculty_id='107'")
    for row in x.fetchall():
        count2=count2+1
    Label(t,text='Event',bg='black',fg='white',font='30').grid(row=r1,column=0)
    Label(t,text=count,bg='black',fg='white',font='30').grid(row=r1,column=c1)
    r1=r1+1
    Label(t,text='Paper',bg='black',fg='white',font='30').grid(row=r1,column=0)
    Label(t,text=count1,bg='black',fg='white',font='30').grid(row=r1,column=c1)
    r1=r1+1
    Label(t,text='Patent',bg='black',fg='white',font='30').grid(row=r1,column=0)
    Label(t,text=count2,bg='black',fg='white',font='30').grid(row=r1,column=c1)
def open_p():
    t=Toplevel()
    t.title("Professional Information -> Prof. Prachi Shiveshwar")
    t.geometry("300x300")
    t.config(bg='black')
    count=0
    count1=0
    count2=0
    Label(t,text='Prof. Prachi Shiveshwar',bg='black',fg='white',font='30').grid()
    r1=2
    c1=1
    count3=0
    x=c.execute("Select * from Workshop where faculty_id='108'")
    for row in x.fetchall():
        count=count+1
    x=c.execute("Select * from book_complete where faculty_id='108'")
    for row in x.fetchall():
        count1=count1+1
    x=c.execute("Select * from conference_national_organised where faculty_id='108'")
    for row in x.fetchall():
        count2=count2+1
    x=c.execute("Select * from paper_international where faculty_id='108'")
    for row in x.fetchall():
        count3=count3+1
    Label(t,text='Workshop',bg='black',fg='white',font='30').grid(row=r1,column=0)
    Label(t,text=count,bg='black',fg='white',font='30').grid(row=r1,column=c1)
    r1=r1+1
    Label(t,text='Book',bg='black',fg='white',font='30').grid(row=r1,column=0)
    Label(t,text=count1,bg='black',fg='white',font='30').grid(row=r1,column=c1)
    r1=r1+1
    Label(t,text='Conference',bg='black',fg='white',font='30').grid(row=r1,column=0)
    Label(t,text=count2,bg='black',fg='white',font='30').grid(row=r1,column=c1)
    r1=r1+1
    Label(t,text='Paper',bg='black',fg='white',font='30').grid(row=r1,column=0)
    Label(t,text=count3,bg='black',fg='white',font='30').grid(row=r1,column=c1)
    
def y():
    obj1 = Toplevel()
    obj1.title("Search by Year")
    obj1.config(bg='black')
    obj1.geometry("200x200")
    global year
    year=IntVar()
    Label(obj1,text='Year',bg='black',fg='white',font='30',padx=10).grid( row=0, column=0)
    Entry(obj1, textvariable=year).grid(row=0, column=1)
    Button(obj1, text="Submit", width=10, height=1, command=y1).grid(row=4, column=0, columnspan=2, pady=2)
    
def y1():
    root=Tk()
    root.title("Search by Year -> Information")
    root.config(bg='black')
    countrow=0
   
    global year1
    year1=year.get()
    t=[]
    print(year1) 
    t.append(year1)
    r1=1
    c1=0
    x=c.execute("SELECT * FROM book_chapter natural join Faculty where book_year=?",t)
    for row in x.fetchall():
        countrow+=1
    if(countrow>0):
        Label(root,text="BOOK(Chapter) :  ",bg='black',fg='white',font='30').grid(row=r1,column=0)
        r1=r1+1
        x=c.execute("SELECT faculty_name,book_name FROM book_chapter natural join Faculty where book_year=?",t)
        for row in x.fetchall():
             for i in range(0,2):
                 Label(root, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
                 c1=c1+1
             c1=0
             r1=r1+1
        countrow=0

    x=c.execute("SELECT * FROM book_complete natural join Faculty where book_year=?",t)
    for row in x.fetchall():
        countrow+=1
    if(countrow>0):
        Label(root,text="BOOK(Complete) :  ",bg='black',fg='white',font='30').grid(row=r1,column=0)
        r1=r1+1
        x=c.execute("SELECT faculty_name,book_name FROM book_complete natural join Faculty where book_year=?",t)
        for row in x.fetchall():
            for i in range(0,2):
                 Label(root, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
                 c1=c1+1
            c1=0
            r1=r1+1
    countrow=0


    x=c.execute("SELECT * FROM conference_international_attended natural join Faculty where conference_year=?",t)
    for row in x.fetchall():
        countrow+=1
    if(countrow>0):
        Label(root,text="INTERNATIONAL CONFERENCE(Attended) :  ",bg='black',fg='white',font='30').grid(row=r1,column=0)
        r1=r1+1
        x=c.execute("SELECT faculty_name,conference_name FROM conference_international_attended natural join Faculty where conference_year=?",t)
        for row in x.fetchall():
            for i in range(0,2):
                 Label(root, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
                 c1=c1+1
            c1=0
            r1=r1+1
        countrow=0


    x=c.execute("SELECT * FROM conference_international_organised natural join Faculty where conference_year=?",t)
    for row in x.fetchall():
        countrow+=1
    if(countrow>0):
        Label(root,text="INTERNATIONAL CONFERENCE(Organised) :  ",bg='black',fg='white',font='30').grid(row=r1,column=0)
        r1=r1+1
        x=c.execute("SELECT faculty_name,conference_name FROM conference_international_organised natural join Faculty where conference_year=?",t)
        for row in x.fetchall():
            for i in range(0,2):
                 Label(root, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
                 c1=c1+1
            c1=0
            r1=r1+1
    countrow=0


    x=c.execute("SELECT * FROM conference_national_organised natural join Faculty where conference_year=?",t)
    for row in x.fetchall():
        countrow+=1
    if(countrow>0):
        Label(root,text="NATIONAL CONFERENCE(Organised) :  ",bg='black',fg='white',font='30').grid(row=r1,column=0)
        r1=r1+1
        x=c.execute("SELECT faculty_name,conference_name FROM conference_national_organised natural join Faculty where conference_year=?",t)
        for row in x.fetchall():
            for i in range(0,2):
                Label(root, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
                c1=c1+1
            c1=0
            r1=r1+1
    countrow=0
    
    x=c.execute("SELECT * FROM conference_national_attended natural join Faculty where conference_year=?",t)
    for row in x.fetchall():
        countrow+=1
    if(countrow>0):
        Label(root,text="NATIONAL CONFERENCE(Attended) :  ",bg='black',fg='white',font='30').grid(row=r1,column=0)
        r1=r1+1
        x=c.execute("SELECT faculty_name,conference_name FROM conference_national_attended natural join Faculty where conference_year=?",t)
        for row in x.fetchall():
            for i in range(0,2):
                Label(root, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
                c1=c1+1
            c1=0
            r1=r1+1
    countrow=0
          


    x=c.execute("SELECT * FROM paper_national natural join Faculty where publish_year=?",t)
    for row in x.fetchall():
        countrow+=1
    if(countrow>0):
        Label(root,text="NATIONAL PAPER :  ",bg='black',fg='white',font='30').grid(row=r1,column=0)
        r1=r1+1
        x=c.execute("SELECT faculty_name,paper_name FROM paper_national natural join Faculty where publish_year=?",t)
        for row in x.fetchall():
            for i in range(0,2):
                Label(root, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
                c1=c1+1
            c1=0
            r1=r1+1
    countrow=0


    x=c.execute("SELECT * FROM paper_international natural join Faculty where publish_year=?",t)
    for row in x.fetchall():
        countrow+=1
    if(countrow>0):
        Label(root,text="INTERNATIONAL PAPER :  ",bg='black',fg='white',font='30').grid(row=r1,column=0)
        r1=r1+1
        x=c.execute("SELECT faculty_name,paper_name FROM paper_international natural join Faculty where publish_year=?",t)
        for row in x.fetchall():
            for i in range(0,2):
                Label(root, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
                c1=c1+1
            c1=0
            r1=r1+1
    countrow=0

    x=c.execute("SELECT * FROM patent natural join Faculty where patent_year=?",t)
    for row in x.fetchall():
        countrow+=1
    if(countrow>0):
        Label(root,text="PATENT :  ",bg='black',fg='white',font='30').grid(row=r1,column=0)
        r1=r1+1
        x=c.execute("SELECT faculty_name,patent_name FROM patent natural join Faculty where patent_year=?",t)
        for row in x.fetchall():
            for i in range(0,2):
                Label(root, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
                c1=c1+1
            c1=0
            r1=r1+1
            
    countrow=0


    x=c.execute("SELECT * FROM project_consult natural join Faculty where year=?",t)
    for row in x.fetchall():
        countrow+=1
    if(countrow>0):
        Label(root,text="CONSULTING PROJECT :  ",bg='black',fg='white',font='30').grid(row=r1,column=0)
        r1=r1+1
        x=c.execute("SELECT faculty_name,project_name FROM project_consult natural join Faculty where year=?",t)
        for row in x.fetchall():
            for i in range(0,2):
                Label(root, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
                c1=c1+1
            c1=0
            r1=r1+1
    countrow=0
    
    x=c.execute("SELECT * FROM project_research natural join Faculty where year=?",t)
    for row in x.fetchall():
        countrow+=1
    if(countrow>0):
        Label(root,text="RESEARCH PROJECT :  ",bg='black',fg='white',font='30').grid(row=r1,column=0)
        r1=r1+1
        x=c.execute("SELECT faculty_name,project_name FROM project_research natural join Faculty where year=?",t)
        for row in x.fetchall():
            for i in range(0,2):
                Label(root, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
                c1=c1+1
            c1=0
            r1=r1+1
    countrow=0


    x=c.execute("SELECT * FROM Workshop natural join Faculty where wk_year=?",t)
    for row in x.fetchall():
        countrow+=1
    if(countrow>0):
        Label(root,text="WORKSHOP :  ",bg='black',fg='white',font='30').grid(row=r1,column=0)
        r1=r1+1
        x=c.execute("SELECT faculty_name,wk_name FROM Workshop natural join Faculty where wk_year=?",t)
        for row in x.fetchall():
            for i in range(0,2):
                Label(root, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
                c1=c1+1
            c1=0
            r1=r1+1
    countrow=0

    
    x=c.execute("SELECT * FROM events natural join Faculty where event_year=?",t)
    for row in x.fetchall():
        countrow+=1
    if(countrow>0):
        Label(root,text="EVENTS :  ",bg='black',fg='white',font='30').grid(row=r1,column=0)
        r1=r1+1
        x=c.execute("SELECT faculty_name,event_name FROM events natural join Faculty where event_year=?",t)
        for row in x.fetchall():
            for i in range(0,2):
                Label(root, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
                c1=c1+1
            c1=0
            r1=r1+1
    countrow=0
    

    x=c.execute("SELECT * FROM article_international natural join Faculty where article_year=?",t)
    for row in x.fetchall():
        countrow+=1
    if(countrow>0):
        Label(root,text="ARTICLE INTERNATIONAL :  ",bg='black',fg='white',font='30').grid(row=r1,column=0)
        r1=r1+1
        x=c.execute("SELECT faculty_name,article_title FROM article_international natural join Faculty where article_year=?",t)
        for row in x.fetchall():
            for i in range(0,2):
                Label(root, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
                c1=c1+1
            c1=0
            r1=r1+1
    countrow=0

    
    x=c.execute("SELECT * FROM article_national natural join Faculty where article_year=?",t)
    for row in x.fetchall():
        countrow+=1
    if(countrow>0):
        Label(root,text="ARTICLE NATIONAL :  ",bg='black',fg='white',font='30').grid(row=r1,column=0)
        r1=r1+1
        x=c.execute("SELECT faculty_name,article_title FROM article_national natural join Faculty where article_year=?",t)
        for row in x.fetchall():
            for i in range(0,2):
                Label(root, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
                c1=c1+1
            c1=0
            r1=r1+1
    countrow=0


    x=c.execute("SELECT * FROM case_study natural join Faculty where case_year=?",t)
    for row in x.fetchall():
        countrow+=1
    if(countrow>0):
        Label(root,text="CASE STUDY :  ",bg='black',fg='white',font='30').grid(row=r1,column=0)
        r1=r1+1
        x=c.execute("SELECT faculty_name,case_title FROM case_study natural join Faculty where case_year=?",t)
        for row in x.fetchall():
            for i in range(0,2):
                Label(root, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
                c1=c1+1
            c1=0
            r1=r1+1
    countrow=0

    root.mainloop()
    
def prof_parameter():
    global v
    v=IntVar()
    top=Toplevel()
    top.title("Search by Professional Parameter")
    top.config(bg='black')
    Label(top,text="Choose any of the following attributes: ",bg='black',fg='white',font='30',padx=20,pady=2).pack()
    
    Radiobutton(top,text="Patent",variable=v,value=1,bg='black',fg='white',font='30').pack()
    Radiobutton(top,text="Case Study",variable=v,value=2,bg='black',fg='white',font='30').pack()
    Radiobutton(top,text="Article",variable=v,value=3,bg='black',fg='white',font='30').pack()
    Radiobutton(top,text="Book",variable=v,value=4,bg='black',fg='white',font='30').pack()
    Radiobutton(top,text="Conference",variable=v,value=5,bg='black',fg='white',font='30').pack()
    Radiobutton(top,text="Workshop",variable=v,value=6,bg='black',fg='white',font='30').pack()
    Radiobutton(top,text="Events",variable=v,value=7,bg='black',fg='white',font='30').pack()
    Radiobutton(top,text="Paper",variable=v,value=9,bg='black',fg='white',font='30').pack()
    Radiobutton(top,text="Project",variable=v,value=10,bg='black',fg='white',font='30').pack()

    Button(top, text="Submit", width=10, height=1,command=disp).pack()

def disp():
    r1=1
    c1=0
    global v1;
    top=Toplevel()
    top.title("Search by Professional Parameter -> Information")
    top.config(bg='black')
    v1=v.get()
    if (v1==1):
         x=c.execute("SELECT * FROM patent natural join Faculty")
         for row in x.fetchall():
             for i in range(0,10):
                 Label(top, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
                 c1=c1+1
             c1=0
             r1=r1+1
    elif(v1==2):
         x=c.execute("SELECT * FROM case_study natural join Faculty")
         for row in x.fetchall():
             for i in range(0,10):
                 Label(top, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
                 c1=c1+1
             c1=0
             r1=r1+1
    elif(v1==3):
         Label(top, text="National articles:",bg='black',fg='white',font='30').grid()
         x=c.execute("SELECT * FROM faculty natural join article_national natural join article_national_city")
         for row in x.fetchall():
             for i in range(0,11):
                 Label(top, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
                 c1=c1+1
             c1=0
             r1=r1+1
         Label(top, text="International articles:",bg='black',fg='white',font='30').grid(row=r1+1)
         r1+=2
         x=c.execute("SELECT * FROM faculty natural join article_international natural join article_international_country")
         for row in x.fetchall():
             for i in range(0,11):
                 Label(top, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
                 c1=c1+1
             c1=0
             r1=r1+1
    elif(v1==4):
         Label(top, text="Complete book:",bg='black',fg='white',font='30').grid()        
         x=c.execute("SELECT * FROM faculty natural join book_complete")
         for row in x.fetchall():
             for i in range(0,11):
                 Label(top, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
                 c1=c1+1
             c1=0
             r1=r1+1
         Label(top, text="Chapter of Book:",bg='black',fg='white',font='30').grid(row=r1+1)
         r1+=2
         x=c.execute("select * from faculty natural join book_chapter")
         for row in x.fetchall():
             for i in range(0,11):
                 Label(top, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
                 c1=c1+1
             c1=0
             r1=r1+1
    elif(v1==5):
         Label(top, text="National conference attended:",bg='black',fg='white',font='30').grid()
         x=c.execute("SELECT * FROM faculty natural join conference_national_attended")
         for row in x.fetchall():
             for i in range(0,11):
                 Label(top, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
                 c1=c1+1
             c1=0
             r1=r1+1
         Label(top, text="National conference organised:",bg='black',fg='white',font='30').grid(row=r1+1)
         r1+=2
         x=c.execute("SELECT * FROM faculty natural join conference_national_organised")
         for row in x.fetchall():
             for i in range(0,10):
                 Label(top, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
                 c1=c1+1
             c1=0
             r1=r1+1
         Label(top, text="International conference attended:",bg='black',fg='white',font='30').grid(row=r1+1)
         r1+=2
         x=c.execute("select * from faculty natural join conference_international_attended")
         for row in x.fetchall():
             for i in range(0,11):
                 Label(top, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
                 c1=c1+1
             c1=0
             r1=r1+1
         Label(top, text="International conference organised:",bg='black',fg='white',font='30').grid(row=r1+1)
         r1+=2
         x=c.execute("select * from faculty natural join conference_international_organised")
         for row in x.fetchall():
             for i in range(0,10):
                 Label(top, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
                 c1=c1+1
             c1=0
             r1=r1+1
    elif(v1==6):
         x=c.execute("SELECT * FROM workshop natural join Faculty")
         for row in x.fetchall():
             for i in range(0,10):
                 Label(top, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
                 c1=c1+1
             c1=0
             r1=r1+1
    elif(v1==7):
         x=c.execute("SELECT * FROM events natural join Faculty")
         for row in x.fetchall():
             for i in range(0,10):
                 Label(top, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
                 c1=c1+1
             c1=0
             r1=r1+1
    elif(v1==9):
         Label(top, text="National Paper:",bg='black',fg='white',font='30').grid()
         x=c.execute("SELECT * FROM faculty natural join paper_national")
         for row in x.fetchall():
             for i in range(0,10):
                 Label(top, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
                 c1=c1+1
             c1=0
             r1=r1+1
         Label(top, text="International Paper:",bg='black',fg='white',font='30').grid(row=r1+1)
         r1+=2
         x=c.execute("select * from faculty natural join paper_international")
         for row in x.fetchall():
             for i in range(0,10):
                 Label(top, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
                 c1=c1+1
             c1=0
             r1=r1+1
    elif(v1==10):
         Label(top, text="Research Project:",bg='black',fg='white',font='30').grid()
         x=c.execute("SELECT * FROM faculty natural join project_research natural join project_sponsor")
         for row in x.fetchall():
             for i in range(0,11):
                 Label(top, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
                 c1=c1+1
             c1=0
             r1=r1+1
         Label(top, text="Consulting Project:",bg='black',fg='white',font='30').grid(row=r1+1)
         r1+=2
         x=c.execute("select * from faculty natural join project_consult")
         for row in x.fetchall():
             for i in range(0,11):
                 Label(top, text=row[i],bg='black',fg='white',font='30').grid(row=r1,column=c1)
                 c1=c1+1
             c1=0
             r1=r1+1
    else:
        print(v1)

    for row in x.fetchall():
             Label(top, text=row,bg='black',fg='white',font='30').grid()

def nishee():
    plt.style.use('dark_background')
    count=0
    count1=0
    count2=0
    count3=0
    count4=0
    count5=0
    count6=0
    x=c.execute("Select * from article_international where faculty_id='101'")
    for row in x.fetchall():
        count=count+1
    x=c.execute("Select * from article_national where faculty_id='101'")
    for row in x.fetchall():
        count=count+1
    x=c.execute("Select * from book_chapter where faculty_id='101'")
    for row in x.fetchall():
        count1=count1+1
    x=c.execute("Select * from case_study where faculty_id='101'")
    for row in x.fetchall():
        count2=count2+1
    x=c.execute("Select * from conference_international_attended where faculty_id='101'")
    for row in x.fetchall():
        count3=count3+1
    x=c.execute("Select * from conference_international_organised where faculty_id='101'")
    for row in x.fetchall():
        count3=count3+1
    x=c.execute("Select * from conference_national_attended where faculty_id='101'")
    for row in x.fetchall():
        count3=count3+1
    x=c.execute("Select * from paper_national where faculty_id='101'")
    for row in x.fetchall():
        count4=count4+1
    x=c.execute("Select * from patent where faculty_id='101'")
    for row in x.fetchall():
        count5=count5+1
    x=c.execute("Select * from events where faculty_id='101'")
    for row in x.fetchall():
        count6=count6+1
    slices=[count,count1,count2,count3,count4,count5,count6]
    labels=['Article','Book_Chapter','Case_Study','Conference','Paper','Patent','Events']
    colors=['#ffcc99','#ff9999','#663bff','#e062b2','#eeb725','#35a86b','#26f0ab']
    explode=[0,0,0,0,0,0,0]
    plt.pie(slices,labels=labels,colors=colors,explode=explode,shadow=True,startangle=90,autopct='%1.1f%%',wedgeprops={'edgecolor':'black'})
    
    plt.title('Prof. Nishee Shelat')
    plt.show()
def dhwani():
    plt.style.use('dark_background')
    count=0
    count1=0
    count2=0
    count3=0
    x=c.execute("Select * from case_study where faculty_id='102'")
    for row in x.fetchall():
        count=count+1
    x=c.execute("Select * from conference_national_attended where faculty_id='102'")
    for row in x.fetchall():
        count1=count1+1
    x=c.execute("Select * from conference_national_organised where faculty_id='102'")
    for row in x.fetchall():
        count1=count1+1
    x=c.execute("Select * from paper_international where faculty_id='102'")
    for row in x.fetchall():
        count2=count2+1
    x=c.execute("Select * from paper_national where faculty_id='102'")
    for row in x.fetchall():
        count2=count2+1
    x=c.execute("Select * from project_consult where faculty_id='102'")
    for row in x.fetchall():
        count3=count3+1
    slices=[count,count1,count2,count3]
    labels=['Case_Study','Conference','Paper','Project']
    colors=['#ffcc99','#ff9999','#663bff','#e062b2']
    explode=[0,0,0,0]
    plt.pie(slices,labels=labels,colors=colors,explode=explode,shadow=True,startangle=90,autopct='%1.1f%%',wedgeprops={'edgecolor':'black'})
    plt.title('Prof. Dhwani Shah')
    plt.show()
def yashesh():
    plt.style.use('dark_background')
    count=0
    count1=0
    count2=0
    count3=0
    x=c.execute("Select * from article_national where faculty_id='103'")
    for row in x.fetchall():
        count=count+1
    x=c.execute("Select * from conference_international_organised where faculty_id='103'")
    for row in x.fetchall():
        count1=count1+1
    x=c.execute("Select * from paper_international where faculty_id='103'")
    for row in x.fetchall():
        count2=count2+1
    x=c.execute("Select * from project_consult where faculty_id='103'")
    for row in x.fetchall():
        count3=count3+1
    x=c.execute("Select * from project_research where faculty_id='103'")
    for row in x.fetchall():
        count3=count3+1
    slices=[count,count1,count2,count3]
    labels=['Article','Conference','Paper','Project']
    colors=['#ffcc99','#ff9999','#663bff','#e062b2']
    explode=[0,0,0,0]
    plt.pie(slices,labels=labels,colors=colors,explode=explode,shadow=True,startangle=90,autopct='%1.1f%%',wedgeprops={'edgecolor':'black'})
    plt.title('Prof. Yashesh Sorathia')
    plt.show()
def kiara():
    plt.style.use('dark_background')
    count=0
    count1=0
    count2=0
    count3=0
    count4=0
    x=c.execute("Select * from Workshop where faculty_id='104'")
    for row in x.fetchall():
        count=count+1
    x=c.execute("Select * from article_national where faculty_id='104'")
    for row in x.fetchall():
        count1=count1+1
    x=c.execute("Select * from book_complete where faculty_id='104'")
    for row in x.fetchall():
        count2=count2+1
    x=c.execute("Select * from conference_international_attended where faculty_id='104'")
    for row in x.fetchall():
        count3=count3+1
    x=c.execute("Select * from project_research where faculty_id='104'")
    for row in x.fetchall():
        count4=count4+1
    slices=[count,count1,count2,count3,count4]
    labels=['Workshop','Article','Book','Conference','Project']
    explode=[0,0,0,0,0]
    colors=['#ffcc99','#ff9999','#663bff','#e062b2','#eeb725']
    plt.pie(slices,labels=labels,colors=colors,explode=explode,shadow=True,startangle=90,autopct='%1.1f%%',wedgeprops={'edgecolor':'black'})
    plt.title('Prof. Kiara Sharma')
    plt.show()
def kavya():
    plt.style.use('dark_background')
    count=0
    count1=0
    count2=0
    count3=0
    x=c.execute("Select * from article_international where faculty_id='105'")
    for row in x.fetchall():
        count=count+1
    x=c.execute("Select * from book_chapter where faculty_id='105'")
    for row in x.fetchall():
        count1=count1+1
    x=c.execute("Select * from events where faculty_id='105'")
    for row in x.fetchall():
        count2=count2+1
    x=c.execute("Select * from patent where faculty_id='105'")
    for row in x.fetchall():
        count3=count3+1
    slices=[count,count1,count2,count3]
    labels=['Article','Book','Event','Patent']
    explode=[0,0,0,0]
    colors=['#ffcc99','#ff9999','#663bff','#e062b2']
    plt.pie(slices,labels=labels,colors=colors,explode=explode,shadow=True,startangle=90,autopct='%1.1f%%',wedgeprops={'edgecolor':'black'})
    plt.title('Prof. Kavya Patel')
    plt.show()
def sakshi():
    plt.style.use('dark_background')
    count=0
    count1=0
    count2=0
    x=c.execute("Select * from article_international where faculty_id='106'")
    for row in x.fetchall():
        count=count+1
    x=c.execute("Select * from book_chapter where faculty_id='106'")
    for row in x.fetchall():
        count1=count1+1
    x=c.execute("Select * from project_consult where faculty_id='106'")
    for row in x.fetchall():
        count2=count2+1
    slices=[count,count1,count2]
    labels=['Article','Book','Project']
    colors=['#ffcc99','#ff9999','#663bff']
    explode=[0,0,0]
    plt.pie(slices,labels=labels,colors=colors,explode=explode,shadow=True,startangle=90,autopct='%1.1f%%',wedgeprops={'edgecolor':'black'})
    plt.title('Prof. Sakshi Singhvi')
    plt.show()
def ananya():
    plt.style.use('dark_background')
    count=0
    count1=0
    count2=0
    x=c.execute("Select * from events where faculty_id='107'")
    for row in x.fetchall():
        count=count+1
    x=c.execute("Select * from paper_national where faculty_id='107'")
    for row in x.fetchall():
        count1=count1+1
    x=c.execute("Select * from patent where faculty_id='107'")
    for row in x.fetchall():
        count2=count2+1
    slices=[count,count1,count2]
    labels=['Event','Paper','Patent']
    colors=['#ffcc99','#ff9999','#663bff']
    explode=[0,0,0]
    plt.pie(slices,labels=labels,colors=colors,explode=explode,shadow=True,startangle=90,autopct='%1.1f%%',wedgeprops={'edgecolor':'black'})
    plt.title('Prof. Ananya Singh')
    plt.show()
def prachi():
    plt.style.use('dark_background')
    count=0
    count1=0
    count2=0
    count3=0
    x=c.execute("Select * from Workshop where faculty_id='108'")
    for row in x.fetchall():
        count=count+1
    x=c.execute("Select * from book_complete where faculty_id='108'")
    for row in x.fetchall():
        count1=count1+1
    x=c.execute("Select * from conference_national_organised where faculty_id='108'")
    for row in x.fetchall():
        count2=count2+1
    x=c.execute("Select * from paper_international where faculty_id='108'")
    for row in x.fetchall():
        count3=count3+1
    slices=[count,count1,count2,count3]
    labels=['Workshop','Book','Conference','Paper']
    colors=['#ffcc99','#ff9999','#663bff','#e062b2']
    explode=[0,0,0,0]
    plt.pie(slices,labels=labels,colors=colors,explode=explode,shadow=True,startangle=90,autopct='%1.1f%%',wedgeprops={'edgecolor':'black'})
    plt.title('Prof. Prachi Shiveshwar')
    plt.show()

def open_gallery():
    t=Toplevel()
    t.title("Gallery")
    t.geometry("600x600")
    t.config(bg='black')
    Label(t,text='Conference conducted by Prof. Kavya Patel in Malaysia',bg='black',fg='white',font='30').grid()
    path="c_1.png"
    path1="c_2.png"
    path2="c_3.png"
    path3="p_2.png"
    path4="p_1.png"
    img=ImageTk.PhotoImage(Image.open(path))
    l=Label(t,image=img)
    l.grid(column=0)
    Label(t,text='Conference attended by Prof. Nishee Shelat in Italy',bg='black',fg='white',font='30').grid()
    img1=ImageTk.PhotoImage(Image.open(path1))
    l=Label(t,image=img1)
    l.grid(column=0)
    Label(t,text='Conference conducted by Prof. Yashesh Sorathia in America',bg='black',fg='white',font='30').grid()
    img2=ImageTk.PhotoImage(Image.open(path2))
    l=Label(t,image=img2)
    l.grid(column=0)
    Label(t,text='Paper presented by Prof. Yashesh Sorathia',bg='black',fg='white',font='30').grid(row=0,column=4)
    img3=ImageTk.PhotoImage(Image.open(path3))
    l=Label(t,image=img3)
    l.grid(row=1,column=4)
    Label(t,text='Paper presented by Prof. Prachi Shiveshwar',bg='black',fg='white',font='30').grid(row=2,column=4)
    img4=ImageTk.PhotoImage(Image.open(path4))
    l=Label(t,image=img4)
    l.grid(row=3,column=4)
    t.mainloop()
    

menubar=Menu(obj1)
file=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Personal Information",menu=file)
file.add_command(label="Prof. Nishee Shelat",command=lambda:n(101))
file.add_command(label="Prof. Yashesh Sorathia",command=ys)
file.add_command(label="Prof. Dhwani Shah",command=d)
file.add_command(label="Prof. Kiara Sharma",command=k)
file.add_command(label="Prof. Kavya Patel",command=kp)
file.add_command(label="Prof. Sakshi Singhvi",command=s)
file.add_command(label="Prof. Ananya Singh",command=a)
file.add_command(label="Prof. Prachi Shiveshwar",command=p)

file3=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Professional Information",menu=file3)
file3.add_command(label="Prof. Nishee Shelat",command=open_n)
file3.add_command(label="Prof. Yashesh Sorathia",command=open_ys)
file3.add_command(label="Prof. Dhwani Shah",command=open_d)
file3.add_command(label="Prof. Kiara Sharma",command=open_k)
file3.add_command(label="Prof. Kavya Patel",command=open_kp)
file3.add_command(label="Prof. Sakshi Singhvi",command=open_s)
file3.add_command(label="Prof. Ananya Singh",command=open_a)
file3.add_command(label="Prof. Prachi Shiveshwar",command=open_p)

file1=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Search",menu=file1)
file1.add_command(label="Search by year",command=y)
file1.add_command(label="Search by Professional parameter",command=prof_parameter)

file2=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Statistical Data",menu=file2)
file2.add_command(label="Prof. Nishee Shelat",command=nishee)
file2.add_command(label="Prof. Yashesh Sorathia",command=yashesh)
file2.add_command(label="Prof. Dhwani Shah",command=dhwani)
file2.add_command(label="Prof. Kiara Sharma",command=kiara)
file2.add_command(label="Prof. Kavya Patel",command=kavya)
file2.add_command(label="Prof. Sakshi Singhvi",command=sakshi)
file2.add_command(label="Prof. Ananya Singh",command=ananya)
file2.add_command(label="Prof. Prachi Shiveshwar",command=prachi)

menubar.add_cascade(label="Gallery",command=open_gallery)

obj1.config(menu=menubar)
obj1.mainloop()
    
    
