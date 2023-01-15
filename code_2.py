import tkinter as tk
from tkinter import ttk,messagebox
import mysql.connector
from tkinter import *


root = tk.Tk()
root.geometry("300x200+500+200")
root.title("who are you?")




def add_project(uname):

	add_pro_win=Toplevel()
	add_pro_win.geometry("500x500+500+200")
	add_pro_win.title("ADD NEW PROJECT")



	def add_pro_btn():
		try:

			if p_id == "": 
				messagebox.showinfo('Information', "Please Enter ProjectID")  
				p_id.focus_set()  
				return
			elif p_name=="":
				messagebox.showinfo('Information', "Please Enter ProjectName")  
				p_name.focus_set()  
				return
			elif p_back=="":
				messagebox.showinfo('Information', "Please Enter BackendDetails")  
				p_back.focus_set()  
				return
			elif p_front=="":
				messagebox.showinfo('Information', "Please Enter FrontEndDetails")  
				p_front.focus_set()  
				return
			elif p_desc=="":
				messagebox.showinfo('Information', "Please Enter ProjectDescription")  
				p_desc.focus_set()  
				return
			elif p_link=="":
				messagebox.showinfo('Information', "Please Enter ProjectLink")  
				p_link.focus_set()  
				return
			
			

			else :
				db = mysql.connector.connect(host ="localhost",user = "root",password = "papai@356910",db ="project_management_system_2")
				cursor = db.cursor()
				savequery = "insert into project(p_id,p_name,p_front,p_back,p_link,p_desc,s_id) values(%s,%s,%s,%s,%s,%s,%s)"
				try:
					cursor.execute(savequery,(p_id.get(),p_name.get(),p_front.get(),p_back.get(),p_link.get(),p_desc.get(),uname))
					db.commit()
					
					messagebox.showinfo("success","project added")
				except Exception as e:
					db.rollback()
					messagebox.showerror("error",e)
		except:
			db.rollback()

	lb_p_id = Label(add_pro_win, text ="PROJECT ID -",padx=20,pady=10)
	lb_p_id.grid(row=0,column=0)
	p_id = Entry(add_pro_win, width = 35)
	p_id.grid(row=0,column=1)

	lb_p_name = tk.Label(add_pro_win, text ="PROJECT NAME -",padx=20,pady=10 )
	lb_p_name.grid(row = 1, column= 0)
	p_name = Entry(add_pro_win, width = 35)
	p_name.grid(row=1,column=1)

	lb_p_front = tk.Label(add_pro_win, text ="FRONTEND DETAILS-",padx=20,pady=10 )
	lb_p_front.grid(row=2,column=0)
	p_front = tk.Entry(add_pro_win, width = 35)
	p_front.grid(row=2,column=1)

	lb_p_back = tk.Label(add_pro_win, text ="BACKEND DETAILS-",padx=20,pady=10 )
	lb_p_back.grid(row=3,column=0)
	p_back= tk.Entry(add_pro_win, width = 35)
	p_back.grid(row=3,column=1)


	lb_p_link = tk.Label(add_pro_win, text ="PROJECT LINK -",padx=20,pady=10 )
	lb_p_link.grid(row=4,column=0)
	p_link = tk.Entry(add_pro_win, width = 35)
	p_link.grid(row=4,column=1)

	lb_p_desc= tk.Label(add_pro_win, text ="PROJECT DESCRIPTION",padx=20,pady=10 )
	lb_p_desc.grid(row=5,column=0)
	p_desc = Entry(add_pro_win, width= 35)
	p_desc.grid(row=5,column=1)



	submitbtn = tk.Button(add_pro_win, text ="SAVE",bg ='green', command = add_pro_btn,width=15)
	submitbtn.grid(row=7,column=0)

def view_projects(uname):
	tvp_win=Toplevel()
	tvp_win.geometry("950x500+200+200")
	tvp_win.title("My Projects")

	global p
	my_connect = mysql.connector.connect(host ="localhost",user = "root",password = "papai@356910",db ="project_management_system_2")
	my_conn = my_connect.cursor()	

	def display():
		my_conn.execute("select project.*,mark.marks from project join mark on project.p_id=mark.p_id where project.s_id=%s",(uname,))
		print(uname)
		global pi
		pi=0 

		for count in my_conn: 
			print(count)
			for j in range(len(count)):
				e = Label(tvp_win,width=10, text=count[j],
				relief='ridge', anchor="w")  
				e.grid(row=pi, column=j) 
				print("outside")
			pi=pi+1
		print("done")
			
		
	display()
	


def s_profile(uname):
	messagebox.showinfo("login succesful","welcome "+uname)
	prof_win=Toplevel()
	prof_win.geometry("300x200+500+200")
	prof_win.title("Welcome "+uname)


	view_project_btn = tk.Button(prof_win, text ="ADD NEW PROJECT",
					bg ='green', command =lambda:add_project(uname))
	view_project_btn.place(x = 50, y = 50, width = 200,height=50)

	add_project_btn = tk.Button(prof_win, text ="VIEW PROJECTS",
					bg ='green', command =lambda:view_projects(uname))
	add_project_btn.place(x = 50, y = 100, width = 200,height=50)



def sign_up():

	create_window=Toplevel()
	create_window.geometry("700x700+300+50")
	create_window.title("enter details")

	DataFrame = Frame(create_window,bd=20,padx=20,relief=RIDGE)
	DataFrame.place(x=20,y=30,width=650,height=550)

	buttondataframe=Frame(create_window,bd=20,relief=RIDGE)
	buttondataframe.place(x=170,y=600,width=160,height=70)

	

		

	def save():
		try:

			if s_usn == "": 
				messagebox.showinfo('Information', "Please Enter Username")  
				s_usn.focus_set()  
				return
			elif s_fname=="":
				messagebox.showinfo('Information', "Please Enter Username")  
				s_fname.focus_set()  
				return
			elif s_lname=="":
				messagebox.showinfo('Information', "Please Enter Username")  
				s_fname.focus_set()  
				return
			elif s_dob=="":
				messagebox.showinfo('Information', "Please Enter Username")  
				s_fname.focus_set()  
				return
			elif s_address=="":
				messagebox.showinfo('Information', "Please Enter Username")  
				s_fname.focus_set()  
				return
			elif s_sem=="":
				messagebox.showinfo('Information', "Please Enter Username")  
				s_fname.focus_set()  
				return
			elif s_sec=="":
				messagebox.showinfo('Information', "Please Enter Username")  
				s_fname.focus_set()  
				return
			elif s_gender=="":
				messagebox.showinfo('Information', "Please Enter Username")  
				s_fname.focus_set()  
				return
			elif s_pass=="":
				messagebox.showinfo('Information', "Please Enter Username")  
				s_fname.focus_set()  
				return
			elif s_phno=="":
				messagebox.showerror('Information',"please Enter phone number")
				s_phno.focus_set()
			

			else :
				db = mysql.connector.connect(host ="localhost",user = "root",password = "papai@356910",db ="project_management_system_2")
				cursor = db.cursor()
				savequery = "insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
				try:
					cursor.execute(savequery,(s_usn.get(),s_fname.get(),s_lname.get(),s_phno.get(),s_address.get(),s_sem.get(),s_dob.get(),s_sec.get(),s_gender.get(),s_pass.get()))
					db.commit()
					messagebox.showinfo("success","student added")

				except Exception as e:
					db.rollback()
					messagebox.showerror("error",e)
		except:
			db.rollback()

	lb_s_fname = Label(DataFrame, text ="First Name -",padx=20,pady=10)
	lb_s_fname.grid(row=0,column=0)
	s_fname = Entry(DataFrame, width = 35)
	s_fname.grid(row=0,column=1)

	lb_s_lname = tk.Label(DataFrame, text ="Last Name -",padx=20,pady=10 )
	lb_s_lname.grid(row = 1, column= 0)
	s_lname = Entry(DataFrame, width = 35)
	s_lname.grid(row=1,column=1)

	lb_s_usn = tk.Label(DataFrame, text ="USN -",padx=20,pady=10 )
	lb_s_usn.grid(row=2,column=0)
	s_usn = tk.Entry(DataFrame, width = 35)
	s_usn.grid(row=2,column=1)

	lb_s_address = tk.Label(DataFrame, text ="Address -",padx=20,pady=10 )
	lb_s_address.grid(row=3,column=0)
	s_address= tk.Entry(DataFrame, width = 35)
	s_address.grid(row=3,column=1)

	lb_s_gender = tk.Label(DataFrame, text ="Gender -",pady=10 )
	lb_s_gender.grid(row=4,column=0)
	s_gender = StringVar()
	RBttn = Radiobutton(DataFrame, text = "M", variable = s_gender,value = "M")
	RBttn.grid(row=4,column=1)
	RBttn2 = Radiobutton(DataFrame, text = "F", variable = s_gender,value = "F")
	RBttn2.grid(row=4,column=2)

	lb_s_phno = tk.Label(DataFrame, text ="Phone Number -",padx=20,pady=10 )
	lb_s_phno.grid(row=5,column=0)
	s_phno = tk.Entry(DataFrame, width = 35)
	s_phno.grid(row=5,column=1)

	lb_s_dob = tk.Label(DataFrame, text ="Dob (dd-mm-yy)-",padx=20,pady=10 )
	lb_s_dob.grid(row=6,column=0)
	s_dob = Entry(DataFrame, width= 16)
	s_dob.grid(row=6,column=1)

	lb_s_sec = tk.Label(DataFrame, text ="Section-",padx=20,pady=10)
	lb_s_sec.grid(row=7,column=0)
	s_sec = StringVar()
	RBttn = Radiobutton(DataFrame, text = "A", variable = s_sec,value = "A")
	RBttn.grid(row=8,column=0)
	RBttn2 = Radiobutton(DataFrame, text = "B", variable = s_sec,value = "B")
	RBttn2.grid(row=8,column=1)
	RBttn2 = Radiobutton(DataFrame, text = "C", variable = s_sec,value = "C")
	RBttn2.grid(row=8,column=2)

	lb_s_sem = tk.Label(DataFrame, text ="Semester-",padx=20,pady=10)
	lb_s_sem.grid(row=9,column=0)
	s_sem = StringVar()
	RBttn = Radiobutton(DataFrame, text = "3rd", variable = s_sem,value = 3)
	RBttn.grid(row=10,column=0)
	RBttn2 = Radiobutton(DataFrame, text = "5th", variable = s_sem,value = 5)
	RBttn2.grid(row=10,column=1)
	RBttn2 = Radiobutton(DataFrame, text = "7th", variable = s_sem,value = 7)
	RBttn2.grid(row=10,column=2)

	lb_s_pass = tk.Label(DataFrame, text ="password-",padx=20,pady=10 )
	lb_s_pass.grid(row=11,column=0)
	s_pass = tk.Entry(DataFrame, width = 35,show='*')
	s_pass.grid(row=11,column=1)

	

	submitbtn = tk.Button(buttondataframe, text ="SAVE",bg ='green', command = save,width=15)
	submitbtn.grid(row=0,column=0)





def logintodb(Username,password):
	db = mysql.connector.connect(host ="localhost",user = "root",password = "papai@356910",db ="project_management_system_2")
	cursor = db.cursor()
	try: 
			uname=Username.get()
			pas=password.get()
			if uname == "": 
				messagebox.showinfo('Information', "Please Enter Username")  
				Username.focus_set()  
				return
			if pas == "": 
				messagebox.showinfo('Information', "Please Enter Password")  
				password.focus_set()  
				return
	
			print(uname)  
			print(pas)  
			query = "SELECT * FROM student WHERE s_id = '"+uname+"' and s_pas= '"+pas+"';"  
			print(query) 
			cursor.execute(query) 
			print(cursor.fetchall()) 
			rowcount = cursor.rowcount  
			print(rowcount)


			if rowcount == 1:  
				s_profile(uname)  

			else :
				messagebox.showinfo('Information', "Login failed,Invalid Username or Password.Try again!!!")  
	except:  
		db.disconnect()

def t_view_stu():
	tvs_win=Toplevel()
	tvs_win.geometry("950x500+200+200")
	tvs_win.title("Student list")

	global i
	my_connect = mysql.connector.connect(host ="localhost",user = "root",password = "papai@356910",db ="project_management_system_2")
	my_conn = my_connect.cursor()	

	def display():
		my_conn.execute("SELECT * FROM student order by s_id limit 0,10 ")
		global i
		i=0 
		for student in my_conn: 
			for j in range(len(student)):
				e = Label(tvs_win,width=10, text=student[j],
				relief='ridge', anchor="w")  
				e.grid(row=i, column=j) 
			e = tk.Button(tvs_win,width=5, text='Edit',relief='ridge',
				 anchor="w",command=lambda k=student[0]:edit_data(k))  
			e.grid(row=i, column=11)     
			i=i+1
	display()
	def edit_data(id):
		global i 
		my_conn.execute("SELECT * FROM student WHERE s_id=%s",(id,))
		s = my_conn.fetchone()
		print(s)

		e1_str_s_usn=tk.StringVar(tvs_win) 
		e2_str_fname=tk.StringVar(tvs_win)
		e3_str_lname=tk.StringVar(tvs_win)
		e4_str_phno=tk.StringVar(tvs_win)
		e5_str_city=tk.StringVar(tvs_win)
		e6_str_sem=tk.StringVar(tvs_win)
		e7_str_dob=tk.StringVar(tvs_win)
		e8_str_sec=tk.StringVar(tvs_win)
		e9_str_gender=tk.StringVar(tvs_win)
		e10_str_pas=tk.StringVar(tvs_win)
		
		e1_str_s_usn.set(s[0]) 
		e2_str_fname.set(s[1])
		e3_str_lname.set(s[2]) 
		e4_str_phno.set(s[3])
		e9_str_gender.set(s[8]) 
		e6_str_sem.set(s[5])
		e7_str_dob.set(s[6])
		e5_str_city.set(s[4])
		e8_str_sec.set(s[7])
		e10_str_pas.set(s[9])

		e1=tk.Entry(tvs_win,textvariable=e1_str_s_usn,width=10,state='disabled')
		e1.grid(row=i,column=0)

		e2=tk.Entry(tvs_win,textvariable=e2_str_fname,width=10)
		e2.grid(row=i,column=1)

		e3=tk.Entry(tvs_win,textvariable=e3_str_lname,width=10)
		e3.grid(row=i,column=2)

		e4=tk.Entry(tvs_win,textvariable=e4_str_phno,width=10)
		e4.grid(row=i,column=3)

		e5=tk.Entry(tvs_win,textvariable=e5_str_city,width=10)
		e5.grid(row=i,column=4)

		e6=tk.Entry(tvs_win,textvariable=e6_str_sem,width=10)
		e6.grid(row=i,column=5)

		e7=tk.Entry(tvs_win,textvariable=e7_str_dob,width=10)
		e7.grid(row=i,column=6)

		e8=tk.Entry(tvs_win,textvariable=e9_str_gender,width=10)
		e8.grid(row=i,column=8)

		e9=tk.Entry(tvs_win,textvariable=e8_str_sec,width=10)
		e9.grid(row=i,column=7)

		e10=tk.Entry(tvs_win,textvariable=e10_str_pas,width=10)
		e10.grid(row=i,column=9)

		b1 = tk.Button(tvs_win,text='Delete',command=lambda: my_delete(id),
				relief='ridge', anchor="w",width=5)  
		b1.grid(row=i, column=11)

		b2 = tk.Button(tvs_win,text='Update',command=lambda: my_update(),
				relief='ridge', anchor="w",width=5)  
		b2.grid(row=i, column=10) 
		def my_delete(id):
			my_conn.execute("DELETE FROM student WHERE s_id=%s",(id,))
			my_connect.commit()
			print("succesfully deleted")
			for w in tvs_win.grid_slaves(i):
				w.grid_forget()
			display()

		def my_update(): 
			data=(e2_str_fname.get(),e3_str_lname.get(),e4_str_phno.get(),e5_str_city.get(),e6_str_sem.get(),e7_str_dob.get(),e8_str_sec.get(),e9_str_gender.get(),e10_str_pas.get(),e1_str_s_usn.get())
			my_conn.execute("UPDATE student SET fname=%s,lname=%s,\
				phone=%s,city=%s,sem=%s,dob=%s,sec=%s,gender=%s,s_pas=%s WHERE s_id=%s",data)
			my_connect.commit()
			print("succesfully updated")
			for w in tvs_win.grid_slaves(i):
				w.grid_forget()
			display()   


def t_view_pro(t_id):
	tvp_win=Toplevel()
	tvp_win.geometry("950x500+200+200")
	tvp_win.title("Project list")

	global p
	my_connect = mysql.connector.connect(host ="localhost",user = "root",password = "papai@356910",db ="project_management_system_2")
	my_conn = my_connect.cursor()	

	def display():
		query=("select * from project order by p_id limit 0,10")
		my_conn.execute(query)
		global p
		p=0 
		for project in my_conn: 
			for j in range(len(project)):
				e = Label(tvp_win,width=10, text=project[j],
				relief='ridge', anchor="w")  
				e.grid(row=p, column=j) 
			e = tk.Button(tvp_win,width=15, text='Edit',relief='ridge',
				 anchor="w",command=lambda k=project[0]:edit_data(k))  
			e.grid(row=p, column=11)  
			eval=tk.Button(tvp_win,width=8,text="Evaluate",relief='ridge',anchor="w",command=lambda k=project[0]:evaluate(k))
			eval.grid(row=p,column=12)
			p=p+1
			print(project[6])
	display()

	def evaluate(id):
		global p
		print(id)

		
		
		#declaring vars
		e1_str_p_id=tk.StringVar(tvp_win)
		e2_str_t_id=tk.StringVar(tvp_win)
		e3_str_marks=tk.StringVar(tvp_win)

		
		#initializing vars
		e1_str_p_id.set(id) 
		e2_str_t_id.set(t_id)
		e3_str_marks.set("")
		
		#taking values
		e1=tk.Entry(tvp_win,textvariable=e1_str_p_id,width=10,state='disabled')
		e1.grid(row=p,column=2)

		e2=tk.Entry(tvp_win,textvariable=e2_str_t_id,width=10,state='disabled')
		e2.grid(row=p,column=3)

		e3=tk.Entry(tvp_win,textvariable=e3_str_marks,width=10)
		e3.grid(row=p,column=4)

		
		b0 = tk.Button(tvp_win,text='Update',command=lambda: update(),
				relief='ridge', anchor="w",width=5)  
		b0.grid(row=p, column=6) 
		
		def update(): 
			data=(id,t_id,e3_str_marks.get())

			try:
				my_conn.execute("insert into mark(p_id,t_id,marks) values(%s,%s,%s)",(data))
				my_connect.commit()
				print("succesfully updated")
				print(data)
			except :
				messagebox.showerror("Invalid Request","Already Evaluated")

			for w in tvp_win.grid_slaves(p):
				w.grid_forget()
			display()  

	
	def edit_data(id):
		global p
		my_conn.execute("SELECT * FROM project WHERE p_id=%s",(id,))
		s = my_conn.fetchone()
		print(s)

		e1_str_p_id=tk.StringVar(tvp_win) 
		e2_str_p_name=tk.StringVar(tvp_win)
		e3_str_p_front=tk.StringVar(tvp_win)
		e4_str_p_back=tk.StringVar(tvp_win)
		e5_str_p_link=tk.StringVar(tvp_win)
		e6_str_desc=tk.StringVar(tvp_win)
		
		e1_str_p_id.set(s[0]) 
		e2_str_p_name.set(s[1])
		e3_str_p_front.set(s[2]) 
		e4_str_p_back.set(s[3])
		e5_str_p_link.set(s[4]) 
		e6_str_desc.set(s[5])
		

		e1=tk.Entry(tvp_win,textvariable=e1_str_p_id,width=10,state='disabled')
		e1.grid(row=p,column=0)

		e2=tk.Entry(tvp_win,textvariable=e2_str_p_name,width=10)
		e2.grid(row=p,column=1)

		e3=tk.Entry(tvp_win,textvariable=e3_str_p_front,width=10)
		e3.grid(row=p,column=2)

		e4=tk.Entry(tvp_win,textvariable=e4_str_p_back,width=10)
		e4.grid(row=p,column=3)

		e5=tk.Entry(tvp_win,textvariable=e5_str_p_link,width=10)
		e5.grid(row=p,column=4)

		e6=tk.Entry(tvp_win,textvariable=e6_str_desc,width=10)
		e6.grid(row=p,column=5)



		b1 = tk.Button(tvp_win,text='Update',command=lambda: my_update(),
				relief='ridge', anchor="w",width=5)  
		b1.grid(row=p, column=6) 

		b2 = tk.Button(tvp_win,text='Delete',command=lambda: my_delete(id),
				relief='ridge', anchor="w",width=5)  
		b2.grid(row=p, column=7)

		def my_delete(id):
			my_conn.execute("DELETE FROM PROJECT WHERE p_id=%s",(id,))
			my_connect.commit()
			print("succesfully deleted")
			for w in tvp_win.grid_slaves(p):
				w.grid_forget()
			display()


		def my_update(): 
			data=(e2_str_p_name.get(),e3_str_p_front.get(),e4_str_p_back.get(),e5_str_p_link.get(),e6_str_desc.get())
			my_conn.execute("UPDATE project SET p_name=%s,p_front=%s,\
				p_back=%s,p_link=%s,p_desc=%s",data)
			my_connect.commit()
			print("succesfully updated")
			for w in tvp_win.grid_slaves(p):
				w.grid_forget()
			display()   

def create_teacher():
	def t_save():
		try:

			if t_id == "": 
				messagebox.showinfo('Information', "Please Enter ID")  
				t_id.focus_set()  
				return
			elif t_name=="":
				messagebox.showinfo('Information', "Please Enter Username")  
				t_name.focus_set()  
				return
			elif t_sub=="":
				messagebox.showinfo('Information', "Please Enter Subject")  
				t_sub.focus_set()  
				return
			elif t_pass=="":
				messagebox.showinfo('Information', "Please Enter Password")  
				t_pass.focus_set()  
				return
			else :
				db = mysql.connector.connect(host ="localhost",user = "root",password = "papai@356910",db ="project_management_system_2")
				cursor = db.cursor()
				savequery = "insert into teacher values(%s,%s,%s,%s)"
				try:
					cursor.execute(savequery,(t_id.get(),t_name.get(),t_sub.get(),t_pass.get()))
					db.commit()
					messagebox.showinfo("success","teacher added")

				except Exception as e:
					db.rollback()
					messagebox.showerror("error",e)
		except:
			db.rollback()



	c_t_win=Toplevel()
	c_t_win.geometry("300x200+500+200")
	c_t_win.title("Enter Teacher Details")

	lb_t_id=Label(c_t_win,text="enter ID")
	lb_t_id.grid(row=0,column=0)
	t_id=Entry(c_t_win,width=35)
	t_id.grid(row=0,column=1)

	lb_t_name=Label(c_t_win,text="enter name")
	lb_t_name.grid(row=1,column=0)
	t_name=Entry(c_t_win,width=35)
	t_name.grid(row=1,column=1)

	lb_t_sub=Label(c_t_win,text="enter subject")
	lb_t_sub.grid(row=2,column=0)
	t_sub=Entry(c_t_win,width=35)
	t_sub.grid(row=2,column=1)

	lb_t_pass=Label(c_t_win,text="enter password")
	lb_t_pass.grid(row=3,column=0)
	t_pass=Entry(c_t_win,width=35,show='*')
	t_pass.grid(row=3,column=1)

	t_sub_btn = tk.Button(c_t_win, text ="create profile",
					bg ='green', command =t_save)
	t_sub_btn.grid(row=4,column=0)


	
def t_profile(uname):
	t_prof_win=Toplevel()
	t_prof_win.geometry("300x200+500+200")
	t_prof_win.title("wecome "+uname)

	view_students_btn = tk.Button(t_prof_win, text ="VIEW STUDENTS",
					bg ='green', command =t_view_stu)
	view_students_btn.place(x = 50, y = 50, width = 200,height=50)

	view_projects_btn = tk.Button(t_prof_win, text ="VIEW PROJECTS",
					bg ='green', command =lambda:t_view_pro(uname))
	view_projects_btn.place(x = 50, y = 100, width = 200,height=50)



def tlogintodb(Username,password):
	db = mysql.connector.connect(host ="localhost",user = "root",password = "papai@356910",db ="project_management_system_2")
	cursor = db.cursor()
	try: 
			uname=Username.get()
			pas=password.get()
			if uname == "": 
				messagebox.showinfo('Information', "Please Enter Username")  
				Username.focus_set()  
				return
			if pas == "": 
				messagebox.showinfo('Information', "Please Enter Password")  
				password.focus_set()  
				return
	
			print(uname)  
			print(pas)  
			query = "SELECT * FROM teacher WHERE t_id = '"+uname+"' and t_pass= '"+pas+"';"  
			print(query) 
			cursor.execute(query) 
			print(cursor.fetchall()) 
			rowcount = cursor.rowcount  
			print(rowcount)


			if rowcount == 1:  
				t_profile(uname)  

			else :
				messagebox.showinfo('Information', "Login failed,Invalid Username or Password.Try again!!!")  
	except:  
		db.disconnect()


		
			

def t_login():
	t_window=Toplevel()
	t_window.geometry("300x200+500+200")
	t_window.title("Teacher Login Page")
	

	lblfrstrow = tk.Label(t_window, text ="Username ", )
	lblfrstrow.grid(row=0,column=0,pady=5,padx=25)

	Username = tk.Entry(t_window, width = 35)
	Username.grid(row=1,column=0,pady=5,padx=25)
	Username.focus_set()

	lblsecrow = tk.Label(t_window, text ="Password ")
	lblsecrow.grid(row=2,column=0,pady=5,padx=25)

	password = tk.Entry(t_window, width = 35,show='*')
	password.grid(row=3,column=0,pady=5,padx=25)

	submitbtn = tk.Button(t_window, text ="Login",
					bg ='blue', command = lambda:tlogintodb(Username,password))
	submitbtn.grid(row=4,column=0,pady=5,padx=25)

	createbtn = tk.Button(t_window, text ="Create",
					bg ='blue', command = create_teacher)
	createbtn.grid(row=5,column=0,pady=5,padx=25)

	t_window.mainloop()
def s_login():


	s_window=Toplevel()
	s_window.geometry("300x200+500+200")
	s_window.title("Student Login Page")
	

	lblfrstrow = tk.Label(s_window, text ="Username -", )
	lblfrstrow.place(x = 50, y = 20)

	Username = tk.Entry(s_window, width = 35)
	Username.place(x = 150, y = 20, width = 100)
	Username.focus_set()

	lblsecrow = tk.Label(s_window, text ="Password -")
	lblsecrow.place(x = 50, y = 50)

	password = tk.Entry(s_window, width = 35,show='*')
	password.place(x = 150, y = 50, width = 100)

	submitbtn = tk.Button(s_window, text ="Login",
					bg ='blue', command = lambda:logintodb(Username,password))
	submitbtn.place(x = 150, y = 135, width = 55)

	createbtn = tk.Button(s_window, text ="Create",
					bg ='blue', command = sign_up)
	createbtn.place(x = 50, y = 135, width = 55)

	s_window.mainloop()



def check():
	def check_fn():
		if check_entry.get() == "password":
			messagebox.showinfo("welcome","permission granted")
			t_login()
		else:
			messagebox.showerror("error","invalid access")
	check_win=Toplevel()
	check_win.geometry("300x200+500+200")
	check_win.title("Admin Permission")

	check_lb=Label(check_win,text="ENTER ADMIN PASSWORD",width=20,height=5)
	check_lb.grid(row=0,column=0,padx=25,pady=10)

	check_entry=Entry(check_win,width=35,show='*')
	check_entry.grid(row=1,column=0,padx=25,pady=10)
	check_entry.focus_set()

	check_btn=tk.Button(check_win,text="check",bg='blue',command=check_fn)
	check_btn.grid(row=2,column=0,padx=55,pady=10)
	

studentbtn = tk.Button(root, text ="STUDENT",
					bg ='green', command =s_login)
studentbtn.place(x = 50, y = 50, width = 200,height=50)

teacherbtn = tk.Button(root, text ="TEACHER",
					bg ='green', command =check)
teacherbtn.place(x = 50, y = 100, width = 200,height=50)

root.mainloop()
