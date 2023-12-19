from tkinter import *
import tkinter as tk
import customtkinter
from PIL import Image
import database_module
import sort_module

#self.destroy_pag_2(btn_3, button_img_back_button, label_login, label_img_user, user_entry_username, user_entry_password, writen_username, is_prof)

#using color:
#bg          = 39a1aa
#top default = 2C2D38
#top text    = 488AC1
#intro text  = D4C6C0
#butoane     = 488AC1

customtkinter.set_appearance_mode("dark")
root = customtkinter.CTk()
root.title("Online exam system")
root.geometry("1100x700+250+50")

font1 = ("Arial", 15)
font2 = ("Arial", 40)
font3 = ("Arial", 20)

str_label_introductive_text = "Our platform will help you save time and manage tests more efficiently, streamlining the examination process."

img_book = customtkinter.CTkImage(Image.open(r"C:\Users\Cristian\Desktop\Proiect de an\Proiect photoes\book_image.jpg"), size =(90, 70))
img_student = customtkinter.CTkImage(Image.open(r"C:\Users\Cristian\Desktop\Proiect de an\Proiect photoes\1566798061-exam-online.jpg"), size = (450, 360))
img_user = customtkinter.CTkImage(Image.open(r"C:\Users\Cristian\Desktop\Proiect de an\Proiect photoes\photo.png"), size = (200, 200))
img_user_second = customtkinter.CTkImage(Image.open(r"C:\Users\Cristian\Desktop\Proiect de an\Proiect photoes\photo_second2.png"), size = (70, 70))
img_back_button = customtkinter.CTkImage(Image.open(r"C:\Users\Cristian\Desktop\Proiect de an\Proiect photoes\back_button.png"), size = (60, 60))
img_forward_button = customtkinter.CTkImage(Image.open(r"C:\Users\Cristian\Desktop\Proiect de an\Proiect photoes\forward_button.png"), size = (60, 60))
img_search = customtkinter.CTkImage(Image.open(r"C:\Users\Cristian\Desktop\Proiect de an\Proiect photoes\search_image.png"), size = (650, 500))

username_prof = ("Cristian Gheorghe", "Dibrian Victor", "Afanasiev Ruslan", "Lisnic Inga")
password_prof = ("1111", "2222", "3333", "4444")
username_student = ("Andrei Popescu", "Elena Ionescu", "Mihai Radu", "Maria Georgescu", "Ion Dumitrescu", "Ana Gheorghe", "Vlad Stan", "Mihaela Vasile", "Alexandru Munteanu", "Laura Cojocaru")
password_student = ("ParolaAndrei123", "P@rolaElena456", "MihaiParola789", "ParolaMaria!2022", "IonDumitrescuParola", "Ana123Parola", "ParolaStanVlad@22", "ParolaMihaela456", "ParolaAlex2023", "P@rolaLaura!")

#Andrei Popescu - ParolaAndrei123
#Elena Ionescu - P@rolaElena456
#Mihai Radu - MihaiParola789
#Maria Georgescu - ParolaMaria!2022
#Ion Dumitrescu - IonDumitrescuParola
#Ana Gheorghe - Ana123Parola
#Vlad Stan - ParolaStanVlad@22
#Mihaela Vasile - ParolaMihaela456
#Alexandru Munteanu - ParolaAlex2023
#Laura Cojocaru - P@rolaLaura!

label_eror_username = None
label_eror_password = None

is_prof_global = None
written_username = None



# CLASS
class Aplicatie:        
    def __init__(self):
        self.sort = sort_module.Sortare()
        self.db = database_module.DataBase()
    # Pag 1:
    def create_pag_1(self, root):
        root.config(bg="#39a1aa")
        is_prof = 1
        is_elev = 0
        #label:
        label_top_default = customtkinter.CTkLabel(root, text="", bg_color="#2C2D38", fg_color = "#2C2D38", height=100, width=1100)
        label_top_default.place(x=0, y=0)
    
        label_introductive_text = customtkinter.CTkLabel(root, text = str_label_introductive_text, font = font1, text_color = "#2C2D38", fg_color = "#D4C6C0", bg_color = "#39a1aa", height = 71, width = 900, corner_radius = 10)
        label_introductive_text.place(x = 130, y = 140)
    
        label_top_text = customtkinter.CTkLabel(root, text="Knowledge review platform",text_color = "#2C2D38", font=font1, bg_color="#2C2D38", fg_color="#39a1aa", height=50, width=300, corner_radius=15)
        label_top_text.place(x=400, y=20)
    
        label_login = customtkinter.CTkLabel(root, text = "", bg_color = "#39a1aa",fg_color ="#2C2D38",  height = 360, width = 450, corner_radius = 20)
        label_login.place(x = 550, y = 250)
    
        label_login_text = customtkinter.CTkLabel(root, text="Login", font=font2, bg_color="#2C2D38", fg_color="#488AC1", text_color = "#2C2D38", height=75, width=300, corner_radius=20)
        label_login_text.place(x=625, y=300)
    
        #buttons:
        btn_1 = customtkinter.CTkButton(root,command = lambda: self.destroy_pag_1(btn_1, btn_2, label_introductive_text, label_login, label_login_text, label_img_book, label_img_student, is_prof),
                                                                                  text="Profesor",text_color ="#2C2D38", font=font1, bg_color="#2C2D38", fg_color = "#488AC1", width=200, height=60)
        btn_1.place(x=675, y=400)
        btn_2 = customtkinter.CTkButton(root,command = lambda: self.destroy_pag_1(btn_1, btn_2, label_introductive_text, label_login, label_login_text, label_img_book, label_img_student, is_elev),
                                                                                  text="Student", font=font1, bg_color="#2C2D38", text_color ="#2C2D38", fg_color = "#488AC1", width=200, height=60)
        btn_2.place(x=675, y=500)
    
        #images:
        label_img_book = customtkinter.CTkLabel(root, text = "",image = img_book)
        label_img_book.place(x = 50, y = 140)
        label_img_student = customtkinter.CTkLabel(root,text = "", image = img_student)
        label_img_student.place(x = 100, y = 250)
    def destroy_pag_1(self, btn_1, btn_2,label_introductive_text, label_login, label_login_text, label_img_book, label_img_student, is_profesor):
        btn_1.destroy()
        btn_2.destroy()
        label_login.destroy()
        label_login_text.destroy()
        label_introductive_text.destroy()
        label_img_book.destroy()
        label_img_student.destroy()
        if(is_profesor == 1):
            self.create_pag_2_profesor(root)
        elif(is_profesor == 0):
            self.create_pag_2_student(root)    
    # Pag 2:
    def create_pag_2_profesor(self, root):
        #label:
        label_login = customtkinter.CTkLabel(root, text = "", bg_color = "#39a1aa",fg_color ="#2C2D38",  height = 300, width = 480, corner_radius = 20)
        label_login.place(x = 300, y = 350)
    
        #images:
        label_img_user = customtkinter.CTkLabel(root, text = "", image = img_user)
        label_img_user.place(x = 450, y = 150)
    
        #entry:
        user_entry_username= customtkinter.CTkEntry(master=root, placeholder_text="Username", font = font3, text_color = "#2C2D38", placeholder_text_color = "#2C2D38", width = 350, height = 50, fg_color = "#488AC1")
        user_entry_username.place(x = 365, y = 400)
        user_entry_password= customtkinter.CTkEntry(master=root, placeholder_text="Password", font = font3, text_color = "#2C2D38", placeholder_text_color = "#2C2D38", width = 350, height = 50, fg_color = "#488AC1", show = "*")
        user_entry_password.place(x = 365, y = 500)
        #buttons:
        btn_3 = customtkinter.CTkButton(root, command = lambda: self.login_as_prof(btn_4, user_entry_username, user_entry_password, btn_3, label_login, label_img_user), text ="Submit", text_color = "#2C2D38", font = font3, fg_color = "#488AC1", width = 200, height = 45, bg_color = "#2C2D38")
        btn_3.place(x = 450, y = 580)
        btn_4 = customtkinter.CTkButton(root, image = img_back_button, text = "", fg_color = "#2C2D38", bg_color = "#2C2D38", command = lambda:  self.destroy_pag_2_and_create_pag_1(btn_3, btn_4, label_login, label_img_user, user_entry_username, user_entry_password), height = 60, width = 60)
        btn_4.place(x = 50, y = 20)
    def create_pag_2_student(self, root):
        #label:
        label_login = customtkinter.CTkLabel(root, text = "", bg_color = "#39a1aa",fg_color ="#2C2D38",  height = 300, width = 480, corner_radius = 20)
        label_login.place(x = 300, y = 350)
    
        #images:
        label_img_user = customtkinter.CTkLabel(root, text = "", image = img_user)
        label_img_user.place(x = 450, y = 150)
    
        #entry:
        user_entry_username= customtkinter.CTkEntry(master=root, placeholder_text="Username", font = font3, text_color = "#2C2D38", placeholder_text_color = "#2C2D38", width = 350, height = 50, fg_color = "#488AC1")
        user_entry_username.place(x = 365, y = 400)
        user_entry_password= customtkinter.CTkEntry(master=root, placeholder_text="Password", font = font3, text_color = "#2C2D38", placeholder_text_color = "#2C2D38", width = 350, height = 50, fg_color = "#488AC1", show = "*")
        user_entry_password.place(x = 365, y = 500)
        #buttons:
        btn_3 = customtkinter.CTkButton(root, command = lambda: self.login_as_student(btn_4, user_entry_username, user_entry_password, btn_3, label_login, label_img_user), text ="Submit", text_color = "#2C2D38", font = font3, fg_color = "#488AC1", width = 200, height = 45, bg_color = "#2C2D38")
        btn_3.place(x = 450, y = 580)
        btn_4 = customtkinter.CTkButton(root, image = img_back_button, text = "", fg_color = "#2C2D38", bg_color = "#2C2D38", command = lambda:  self.destroy_pag_2_and_create_pag_1(btn_3, btn_4, label_login, label_img_user, user_entry_username, user_entry_password), height = 60, width = 60)
        btn_4.place(x = 50, y = 20)
    def login_as_prof(self, button_img_back_button, user_entry_username, user_entry_password, btn_3, label_login, label_img_user):
        global label_eror_username, label_eror_password
        indicator1 = False
        indicator2 = False
        is_prof = 1
        if label_eror_username:
            label_eror_username.destroy()
        if label_eror_password:
            label_eror_password.destroy()
    
        writen_username = user_entry_username.get()
        writen_password = user_entry_password.get()
        if writen_username == "":
            label_eror_username = customtkinter.CTkLabel(root, text="Input username", font=font1, text_color="#488AC1", fg_color="#2C2D38", bg_color="#2C2D38", height = 20, width = 100)
            label_eror_username.place(x=380, y=450)
        else:
            for index, row in enumerate(username_prof):
                if writen_username != row:
                   label_eror_username = customtkinter.CTkLabel(root, text="Incorrect username", font=font1, text_color="#488AC1", fg_color="#2C2D38", bg_color="#2C2D38", height = 20, width = 100)
                   label_eror_username.place(x=380, y=450)
                else:
                   indicator1 = True
                   username_index = index

                
        if writen_password == "":
            label_eror_password = customtkinter.CTkLabel(root, text="Input password", font=font1, text_color="#488AC1", fg_color="#2C2D38", bg_color="#2C2D38", height = 20, width = 100)
            label_eror_password.place(x=380, y=550)
        else:
            for index, row in enumerate(password_prof):
                if writen_password != row:
                   label_eror_password = customtkinter.CTkLabel(root, text="Incorrect password", font=font1, text_color="#488AC1", fg_color="#2C2D38", bg_color="#2C2D38", height = 20, width = 100)
                   label_eror_password.place(x=380, y=550)
                else:
                    indicator2 = True
                    password_index = index
        if(indicator1 == True and indicator2 == True and username_index == password_index):
            self.destroy_pag_2(btn_3, button_img_back_button, label_login, label_img_user, user_entry_username, user_entry_password, writen_username, is_prof)
    def login_as_student(self, button_img_back_button, user_entry_username, user_entry_password, btn_3, label_login, label_img_user):
         global label_eror_username, label_eror_password
    
         indicator1 = False 
         indicator2 = False    
         is_prof = 0

         if label_eror_username:
             label_eror_username.destroy()
         if label_eror_password:
             label_eror_password.destroy()
        
         writen_username = user_entry_username.get()
         writen_password = user_entry_password.get()
    
         if writen_username == "":
             label_eror_username = customtkinter.CTkLabel(root, text="Input username", font=font1, text_color="#488AC1", fg_color="#2C2D38", bg_color="#2C2D38")
             label_eror_username.place(x=380, y=450)
         else:
            for index, row in enumerate(username_student):
                if writen_username != row:
                    label_eror_username = customtkinter.CTkLabel(root, text="Incorrect username", font=font1, text_color="#488AC1", fg_color="#2C2D38", bg_color="#2C2D38")
                    label_eror_username.place(x=380, y=450)
                else:
                    indicator1 = True
                    username_index = index
                
         if writen_password == "":
             label_eror_password = customtkinter.CTkLabel(root, text="Input password", font=font1, text_color="#488AC1", fg_color="#2C2D38", bg_color="#2C2D38")
             label_eror_password.place(x=380, y=550)
         else:
            for index, row in enumerate(password_student):
                if writen_password != row:
                    label_eror_password = customtkinter.CTkLabel(root, text="Incorrect password", font=font1, text_color="#488AC1", fg_color="#2C2D38", bg_color="#2C2D38")
                    label_eror_password.place(x=380, y=550)
                else:
                    indicator2 = True
                    password_index = index
         if(indicator1 == True and indicator2 == True and username_index == password_index):
             self.destroy_pag_2(btn_3, button_img_back_button, label_login, label_img_user, user_entry_username, user_entry_password, writen_username, is_prof)
    def destroy_pag_2(self, btn_3, button_img_back_button, label_login, label_img_user, user_entry_username, user_entry_password, writen_username, is_prof):
        btn_3.destroy()
        label_login.destroy()
        label_img_user.destroy()
        user_entry_username.destroy() 
        user_entry_password.destroy()
        button_img_back_button.destroy()
        if(is_prof == 1):
           self.create_pag_3_prof(root, writen_username)
        elif(is_prof == 0):
           self.create_pag_3_student(root, writen_username)
    def destroy_pag_2_and_create_pag_1(self, btn_3, btn_4, label_login, label_img_user, user_entry_username, user_entry_password):
        btn_3.destroy()
        label_login.destroy()
        label_img_user.destroy()
        user_entry_username.destroy() 
        user_entry_password.destroy()
        self.create_pag_1(root)
    # Pag 3:
    def create_pag_3_prof(self, root, writen_username):
        global is_prof_global
        is_prof_global = 1
        is_button_1 = 1
        is_button_2 = 2
        is_button_3 = 3
    
        label_img_user_second = customtkinter.CTkLabel(root, text = "", image = img_user_second)
        label_img_user_second.place(x = 1000, y = 10)
    
        label_prof_name = customtkinter.CTkLabel(root, text = writen_username, font = font3, bg_color = "#2C2D38", fg_color = "#2C2D38", text_color = "#39a1aa", width = 200, height = 40)
        label_prof_name.place(x = 780, y = 25)
    
        label_menu = customtkinter.CTkLabel(root, text = "", fg_color ="#2C2D38", bg_color = "#39a1aa", height = 500, width = 400, corner_radius = 20)
        label_menu.place(x = 675, y = 180)
    
        label_menu_text = customtkinter.CTkLabel(root, text = "Menu", font = font2, text_color = "#2C2D38", fg_color ="#488AC1", bg_color = "#2C2D38", height = 75, width = 300, corner_radius=15)
        label_menu_text.place(x = 725, y = 210)
    
        label_img_search = customtkinter.CTkLabel(root, text ="", image = img_search)
        label_img_search.place(x = 20, y = 180)
        all_abjects_to_destroy = []
        all_to_destroy_and_create_2 = []
    
        btn_5 = customtkinter.CTkButton(root, text = "Tests", command = lambda: self.destoy_pag_3(all_abjects_to_destroy, writen_username, is_button_1), text_color ="#2C2D38", font = font1, bg_color = "#2C2D38", fg_color = "#488AC1", height = 60, width = 200)
        btn_5.place(x = 775, y = 320)
        btn_6 = customtkinter.CTkButton(root, text = "Results", command = lambda: self.destoy_pag_3(all_abjects_to_destroy, writen_username, is_button_2), text_color ="#2C2D38", font = font1, bg_color = "#2C2D38", fg_color = "#488AC1", height = 60, width = 200)
        btn_6.place(x = 775, y = 415)    
        btn_7 = customtkinter.CTkButton(root, text = "Add Test", command = lambda: self.destoy_pag_3(all_abjects_to_destroy, writen_username, is_button_3), text_color ="#2C2D38", font = font1, bg_color = "#2C2D38", fg_color = "#488AC1", height = 60, width = 200)
        btn_7.place(x = 775, y = 510)
        btn_8 = customtkinter.CTkButton(root, image = img_back_button, text = "", fg_color = "#2C2D38", bg_color = "#2C2D38", command = lambda:  self.destroy_pag_3_and_create_pag_2(all_to_destroy_and_create_2), height = 60, width = 60)
        btn_8.place(x = 50, y = 20)       
        all_abjects_to_destroy.append(label_img_user_second)
        all_abjects_to_destroy.append(label_menu)
        all_abjects_to_destroy.append(label_menu_text)
        all_abjects_to_destroy.append(label_img_search)
        all_abjects_to_destroy.append(btn_5)
        all_abjects_to_destroy.append(btn_6)
        all_abjects_to_destroy.append(btn_7)
        all_abjects_to_destroy.append(btn_8)
        
        all_to_destroy_and_create_2.append(label_img_user_second)
        all_to_destroy_and_create_2.append(label_prof_name)
        all_to_destroy_and_create_2.append(label_menu)
        all_to_destroy_and_create_2.append(label_menu_text)
        all_to_destroy_and_create_2.append(label_img_search)
        all_to_destroy_and_create_2.append(btn_5)
        all_to_destroy_and_create_2.append(btn_6)
        all_to_destroy_and_create_2.append(btn_7)
        all_to_destroy_and_create_2.append(btn_8)        
    def create_pag_3_student(self, root, writen_username):
        global is_prof_global
        is_prof_global = 0
        is_button_1 = 1
        is_button_2 = 2
        global global_writen_username_student
        global_writen_username_student = writen_username
        customtkinter.CTkLabel(root, text = "", image = img_user_second)
        label_img_user_second = customtkinter.CTkLabel(root, text = "", image = img_user_second)
        label_img_user_second.place(x = 1000, y = 10)
    
        label_prof_name = customtkinter.CTkLabel(root, text = writen_username, font = font3, bg_color = "#2C2D38", fg_color = "#2C2D38", text_color = "#39a1aa", width = 200, height = 40)
        label_prof_name.place(x = 780, y = 25)
    
        label_menu = customtkinter.CTkLabel(root, text = "", fg_color ="#2C2D38", bg_color = "#39a1aa", height = 500, width = 400, corner_radius = 20)
        label_menu.place(x = 675, y = 180)
        
        label_menu_text = customtkinter.CTkLabel(root, text = "Menu", font = font2, text_color = "#2C2D38", fg_color ="#488AC1", bg_color = "#2C2D38", height = 75, width = 300, corner_radius=15)
        label_menu_text.place(x = 725, y = 210)
    
        label_img_search = customtkinter.CTkLabel(root, text ="", image = img_search)
        label_img_search.place(x = 20, y = 180)
        all_abjects_to_destroy = []
        all_to_destroy_and_create_2 = []

        btn_5 = customtkinter.CTkButton(root, text = "Solve", command = lambda: self.destoy_pag_3(all_abjects_to_destroy, writen_username, is_button_1), text_color ="#2C2D38", font = font1, bg_color = "#2C2D38", fg_color = "#488AC1", height = 60, width = 200)
        btn_5.place(x = 775, y = 360)
        btn_6 = customtkinter.CTkButton(root, text = "Results", command = lambda: self.destoy_pag_3(all_abjects_to_destroy, writen_username, is_button_2), text_color ="#2C2D38", font = font1, bg_color = "#2C2D38", fg_color = "#488AC1", height = 60, width = 200)
        btn_6.place(x = 775, y = 500)    
        btn_8 = customtkinter.CTkButton(root, image = img_back_button, text = "", fg_color = "#2C2D38", bg_color = "#2C2D38", command = lambda:  self.destroy_pag_3_and_create_pag_2(all_to_destroy_and_create_2), height = 60, width = 60)
        btn_8.place(x = 50, y = 20)
        all_abjects_to_destroy.append(label_img_user_second)
        all_abjects_to_destroy.append(label_menu)
        all_abjects_to_destroy.append(label_menu_text)
        all_abjects_to_destroy.append(label_img_search)
        all_abjects_to_destroy.append(btn_5)
        all_abjects_to_destroy.append(btn_6)
        all_abjects_to_destroy.append(btn_8)
        
        all_to_destroy_and_create_2.append(label_img_user_second)
        all_to_destroy_and_create_2.append(label_prof_name)
        all_to_destroy_and_create_2.append(label_menu)
        all_to_destroy_and_create_2.append(label_menu_text)
        all_to_destroy_and_create_2.append(label_img_search)
        all_to_destroy_and_create_2.append(btn_5)
        all_to_destroy_and_create_2.append(btn_6)
        all_to_destroy_and_create_2.append(btn_8)    
    def destroy_pag_3_and_create_pag_2(self, all_to_destroy_and_create_2):
        for object in all_to_destroy_and_create_2:
            if object:
                object.destroy()
        if is_prof_global == 1:
            self.create_pag_2_profesor(root)
        elif is_prof_global == 0:
            self.create_pag_2_student(root) 
    def destoy_pag_3(self, all_abjects_to_destroy, writen_username, is_button):
        for object in all_abjects_to_destroy:
            if object:
                object.destroy()
        if is_prof_global == 1:
           if(is_button == 1):
                self.create_pag_4_prof_tests(root, writen_username)
           elif(is_button == 2):
               self.create_pag_4_resultate(root, writen_username)
           elif(is_button == 3):
               self.create_pag_4_prof_add_test(root, writen_username)
        elif is_prof_global == 0:
            if is_button == 1:
                self.create_pag_4_student_solve(root, writen_username)
            elif is_button == 2:
                self.create_pag_4_resultate(root, writen_username)
    # Pag 4:
    def create_pag_4_prof_tests(self, root, writen_username):
        tests = self.db.afiseaza_test()
        global is_prof_global
        is_prof_global = 1
        global global_writen_username_prof
        global_writen_username_prof = writen_username
        global written_username
        written_username = writen_username
        all_buttons_test = []

        btns_to_destroy_back = []

     
        label_tests_view = customtkinter.CTkLabel(root, text = "", height = 500, width = 700, fg_color = "#2C2D38", bg_color ="#39a1aa", corner_radius = 15)
        label_tests_view.place(x = 50, y = 150)
        label_tests_sort = customtkinter.CTkLabel(root, text = "", height = 500, width = 275, fg_color = "#2C2D38", bg_color ="#39a1aa", corner_radius =15)
        label_tests_sort.place(x = 775, y = 150)
 
        
        label_sort_by = customtkinter.CTkLabel(root, text = "Sort by",  text_color = "#2C2D38",  height = 75, width = 255, fg_color = "#488AC1", bg_color ="#2C2D38", corner_radius =15)
        label_sort_by.place(x = 785, y = 160)
        
        btn_sort_name = customtkinter.CTkButton(root, text="Name",  text_color = "#2C2D38",command=lambda: self.sort_by_name(btns_to_destroy_back, tests, all_buttons_test, btn_test_1, btn_test_2, btn_test_3, btn_test_4, btn_test_5, btn_next_text_page, label_tests_view, label_tests_sort), fg_color="#488AC1", bg_color="#2C2D38", height=50, width=225)
        btn_sort_name.place(x=800, y=250)

        btn_sort_by_questions = customtkinter.CTkButton(root, text="Num of questions", text_color = "#2C2D38", command=lambda: self.sort_by_questions(btns_to_destroy_back, tests, all_buttons_test, btn_test_1, btn_test_2, btn_test_3, btn_test_4, btn_test_5, btn_next_text_page, label_tests_view, label_tests_sort), fg_color="#488AC1", bg_color="#2C2D38", height=50, width=225)
        btn_sort_by_questions.place(x=800, y=315)
        
        label_search_by = customtkinter.CTkLabel(root, text = "Filter by",  text_color = "#2C2D38",  height = 75, width = 255, fg_color = "#488AC1", bg_color ="#2C2D38", corner_radius =15)
        label_search_by.place(x = 785, y = 420)
        
        entry_test_name= customtkinter.CTkEntry(master=root, placeholder_text="Name", font = font3, text_color = "#2C2D38", placeholder_text_color = "#2C2D38", width = 165, height = 50, fg_color = "#488AC1")
        entry_test_name.place(x = 800, y = 510)
        entry_nr_questions = customtkinter.CTkEntry(master=root, placeholder_text="Nr of questions", font = font3, text_color = "#2C2D38", placeholder_text_color = "#2C2D38", width = 165, height = 50, fg_color = "#488AC1")
        entry_nr_questions.place(x = 800, y = 575)

        
        btn_search_name = customtkinter.CTkButton(root, text="Name", command = lambda: self.search_name(entry_test_name, btns_to_destroy_back, all_buttons_test, btn_test_1, btn_test_2, btn_test_3, btn_test_4, btn_test_5, btn_next_text_page, label_tests_view, label_tests_sort), text_color = "#2C2D38", fg_color="#488AC1", bg_color="#2C2D38", height=50, width=50)
        btn_search_name.place(x=975, y=510)

        btn_search_questions = customtkinter.CTkButton(root, text="Num", command = lambda: self.search_questions(entry_nr_questions, btns_to_destroy_back, all_buttons_test,btn_test_1, btn_test_2, btn_test_3, btn_test_4, btn_test_5, btn_next_text_page, label_tests_view, label_tests_sort), text_color = "#2C2D38", fg_color="#488AC1", bg_color="#2C2D38", height=50, width=50)
        btn_search_questions.place(x=975, y=575)
        




        btns_to_destroy_back.append(btn_sort_name)
        btns_to_destroy_back.append(btn_sort_by_questions)
        btns_to_destroy_back.append(label_sort_by)
        btns_to_destroy_back.append(label_search_by)
        btns_to_destroy_back.append(btn_search_name)
        btns_to_destroy_back.append(btn_search_questions)
        btns_to_destroy_back.append(label_tests_sort)
        btns_to_destroy_back.append(entry_test_name)
        btns_to_destroy_back.append(entry_nr_questions)
        

        
        
        
        
        btn_test_1 = None
        btn_test_2 = None
        btn_test_3 = None
        btn_test_4 = None
        btn_test_5 = None
        btn_next_text_page = None
        
        all_buttons_test.append(btn_test_1)
        all_buttons_test.append(btn_test_2)
        all_buttons_test.append(btn_test_3)
        all_buttons_test.append(btn_test_4)
        all_buttons_test.append(btn_test_5)
        all_buttons_test.append(btn_next_text_page)
                
        
        self.print_all_tests(btns_to_destroy_back, tests, all_buttons_test, 0, 1, btn_test_1, btn_test_2, btn_test_3, btn_test_4, btn_test_5, btn_next_text_page, label_tests_view, label_tests_sort)
        

            
        btn_9 = customtkinter.CTkButton(root, image = img_back_button, text = "", fg_color = "#2C2D38", bg_color = "#2C2D38", command = lambda:  self.destroy_pag_4_prof_tests_and_create_pag_3(btns_to_destroy_back, btn_9, all_buttons_test, label_tests_view, label_tests_sort, writen_username), height = 60, width = 60)
        btn_9.place(x = 50, y = 20)
    def sort_by_name(self, btns_to_destroy_back, tests, all_buttons_test, btn_test_1, btn_test_2, btn_test_3, btn_test_4, btn_test_5, btn_next_text_page, label_tests_view, label_tests_sort):
        tests = self.sort.quick_sort_cresc(tests)
        for button in all_buttons_test:
            if button:
                button.destroy()
        self.print_all_tests(btns_to_destroy_back, tests,  all_buttons_test, 0, 1, btn_test_1, btn_test_2, btn_test_3, btn_test_4, btn_test_5, btn_next_text_page, label_tests_view, label_tests_sort)
    def sort_by_questions(self, btns_to_destroy_back, tests, all_buttons_test, btn_test_1, btn_test_2, btn_test_3, btn_test_4, btn_test_5, btn_next_text_page, label_tests_view, label_tests_sort):
        tests = tuple((t[1], t[0]) for t in tests)
        tests = self.sort.quick_sort_cresc(tests)
        tests = tuple((t[1], t[0]) for t in tests)
        for button in all_buttons_test:
            if button:
                button.destroy()
        self.print_all_tests(btns_to_destroy_back, tests, all_buttons_test, 0, 1, btn_test_1, btn_test_2, btn_test_3, btn_test_4, btn_test_5, btn_next_text_page, label_tests_view, label_tests_sort)
    def search_name(self, user_entry_username, btns_to_destroy_back, all_buttons_test, btn_test_1, btn_test_2, btn_test_3, btn_test_4, btn_test_5, btn_next_text_page, label_tests_view, label_tests_sort):
        written_name = user_entry_username.get()
        filtred_tests = self.db.find_by_name(str(written_name))
        for button in all_buttons_test:
            if button:
                button.destroy()

        self.print_all_tests(btns_to_destroy_back, filtred_tests, all_buttons_test, 0, 1, btn_test_1, btn_test_2, btn_test_3, btn_test_4, btn_test_5, btn_next_text_page, label_tests_view, label_tests_sort)
    def search_questions(self, user_entry_username, btns_to_destroy_back, all_buttons_test, btn_test_1, btn_test_2, btn_test_3, btn_test_4, btn_test_5, btn_next_text_page, label_tests_view, label_tests_sort):
        written_nr_questions = user_entry_username.get()
        filtred_tests = self.db.filter_by_questions(int(written_nr_questions))
        for button in all_buttons_test:
            if button:
                button.destroy()

        self.print_all_tests(btns_to_destroy_back, filtred_tests, all_buttons_test, 0, 1, btn_test_1, btn_test_2, btn_test_3, btn_test_4, btn_test_5, btn_next_text_page, label_tests_view, label_tests_sort)
    def print_all_tests(self, btns_to_destroy_back, tests, all_buttons_test, count, i, old_button_1, old_button_2, old_button_3, old_button_4, old_button_5, btn_next_text_page, label_tests_view, label_tests_filter):
        if old_button_1:
            old_button_1.destroy()
        if old_button_2:
            old_button_2.destroy()
        if old_button_3:
            old_button_3.destroy()
        if old_button_4:
            old_button_4.destroy()
        if old_button_5:
            old_button_5.destroy()
        if btn_next_text_page:
            btn_next_text_page.destroy()
        btn_test_1 = None
        btn_test_2 = None
        btn_test_3 = None
        btn_test_4 = None
        btn_test_5 = None
        len_matrice = len(tests)

        len_pagini = int(len_matrice / 5)
        len_rest = len_matrice % 5
        
        if len_pagini >= 1:
             btn_test_1 = customtkinter.CTkButton(root, text = tests[count][0] + "  Nr  intrebari: " + str(tests[count][1]),  text_color = "#2C2D38", command = lambda: self.print_a_test(btns_to_destroy_back, 1, count+1, tests[count][0],int(tests[count][1]), all_buttons_test, label_tests_view, label_tests_filter), fg_color = "#488AC1", bg_color = "#2C2D38", height = 50, width = 500)
             btn_test_1.place(x = 150, y = 200)       
             btn_test_2 = customtkinter.CTkButton(root, text = tests[count+1][0] + "  Nr  intrebari: " + str(tests[count+1][1]), text_color = "#2C2D38", command = lambda: self.print_a_test(btns_to_destroy_back, 1, count+2,  tests[count+1][0],int(tests[count+1][1]), all_buttons_test, label_tests_view, label_tests_filter), fg_color = "#488AC1", bg_color = "#2C2D38", height = 50, width = 500)
             btn_test_2.place(x = 150, y = 280)       
             btn_test_3 = customtkinter.CTkButton(root, text = tests[count+2][0] + "  Nr  intrebari: " + str(tests[count+2][1]), text_color = "#2C2D38", command = lambda: self.print_a_test(btns_to_destroy_back, 1, count+3, tests[count+2][0],int(tests[count+2][1]), all_buttons_test, label_tests_view, label_tests_filter), fg_color = "#488AC1", bg_color = "#2C2D38", height = 50,  width = 500)
             btn_test_3.place(x = 150, y = 360)      
             btn_test_4 = customtkinter.CTkButton(root, text = tests[count+3][0] + "  Nr  intrebari: " + str(tests[count+3][1]), text_color = "#2C2D38", command = lambda: self.print_a_test(btns_to_destroy_back, 1, count+4,  tests[count+3][0],int(tests[count+3][1]), all_buttons_test, label_tests_view, label_tests_filter), fg_color = "#488AC1", bg_color = "#2C2D38", height = 50, width = 500)
             btn_test_4.place(x = 150, y = 440)
             btn_test_5 = customtkinter.CTkButton(root, text = tests[count+4][0] + "  Nr  intrebari: " + str(tests[count+4][1]),  text_color = "#2C2D38", command = lambda: self.print_a_test(btns_to_destroy_back, 1, count+5, tests[count+4][0],int(tests[count+4][1]), all_buttons_test, label_tests_view, label_tests_filter), fg_color = "#488AC1", bg_color = "#2C2D38", height = 50, width = 500)
             btn_test_5.place(x = 150, y = 520)
             all_buttons_test.append(btn_test_1)
             all_buttons_test.append(btn_test_2)
             all_buttons_test.append(btn_test_3)
             all_buttons_test.append(btn_test_4)
             all_buttons_test.append(btn_test_5)
        else:
            if len_rest == 0:
                pass
            elif len_rest == 1:
                btn = customtkinter.CTkButton(root, text = tests[0][0] + "  Nr  intrebari: " + str(tests[0][1]),  text_color = "#2C2D38", command = lambda: self.print_a_test(btns_to_destroy_back, 1, 1, tests[0][0],int(tests[0][1]), all_buttons_test, label_tests_view, label_tests_filter), fg_color = "#488AC1", bg_color = "#2C2D38", height = 50, width = 500)
                btn.place(x = 150, y = 200) 
                all_buttons_test.append(btn)
            elif len_rest == 2:
                btn1 = customtkinter.CTkButton(root, text = tests[0][0] + "  Nr  intrebari: " + str(tests[0][1]), text_color = "#2C2D38", command = lambda: self.print_a_test(btns_to_destroy_back, 1, 1, tests[0][0],int(tests[0][1]), all_buttons_test, label_tests_view, label_tests_filter), fg_color = "#488AC1", bg_color = "#2C2D38", height = 50, width = 500)
                btn1.place(x = 150, y = 200) 
                btn2 = customtkinter.CTkButton(root, text = tests[1][0] + "  Nr  intrebari: " + str(tests[1][1]), text_color = "#2C2D38", command = lambda: self.print_a_test(btns_to_destroy_back, 1, 2, tests[1][0],int(tests[1][1]), all_buttons_test, label_tests_view, label_tests_filter), fg_color = "#488AC1", bg_color = "#2C2D38", height = 50, width = 500)
                btn2.place(x = 150, y = 280) 
                all_buttons_test.append(btn1)
                all_buttons_test.append(btn2)
            elif len_rest == 3:
                btn1 = customtkinter.CTkButton(root, text = tests[0][0] + "  Nr  intrebari: " + str(tests[0][1]), text_color = "#2C2D38", command = lambda: self.print_a_test(btns_to_destroy_back, 1, 1, tests[0][0],int(tests[0][1]), all_buttons_test, label_tests_view, label_tests_filter), fg_color = "#488AC1", bg_color = "#2C2D38", height = 50, width = 500)
                btn1.place(x = 150, y = 200) 
                btn2 = customtkinter.CTkButton(root, text = tests[1][0] + "  Nr  intrebari: " + str(tests[1][1]), text_color = "#2C2D38", command = lambda: self.print_a_test(btns_to_destroy_back, 1, 2, tests[1][0],int(tests[1][1]), all_buttons_test, label_tests_view, label_tests_filter), fg_color = "#488AC1", bg_color = "#2C2D38", height = 50, width = 500)
                btn2.place(x = 150, y = 280) 
                btn3 = customtkinter.CTkButton(root, text = tests[2][0] + "  Nr  intrebari: " + str(tests[2][1]), text_color = "#2C2D38", command = lambda: self.print_a_test(btns_to_destroy_back, 1, 3, tests[2][0],int(tests[2][1]), all_buttons_test, label_tests_view, label_tests_filter), fg_color = "#488AC1", bg_color = "#2C2D38", height = 50, width = 500)
                btn3.place(x = 150, y = 360) 
                all_buttons_test.append(btn1)
                all_buttons_test.append(btn2)
                all_buttons_test.append(btn3)
            elif len_rest == 4:
                btn1 = customtkinter.CTkButton(root, text = tests[0][0] + "  Nr  intrebari: " + str(tests[0][1]), text_color = "#2C2D38", command = lambda: self.print_a_test(btns_to_destroy_back, 1, 1, tests[0][0],int(tests[0][1]), all_buttons_test, label_tests_view, label_tests_filter), fg_color = "#488AC1", bg_color = "#2C2D38", height = 50, width = 500)
                btn1.place(x = 150, y = 200) 
                btn2 = customtkinter.CTkButton(root, text = tests[1][0] + "  Nr  intrebari: " + str(tests[1][1]), text_color = "#2C2D38", command = lambda: self.print_a_test(btns_to_destroy_back, 1, 2, tests[1][0],int(tests[1][1]), all_buttons_test, label_tests_view, label_tests_filter), fg_color = "#488AC1", bg_color = "#2C2D38", height = 50, width = 500)
                btn2.place(x = 150, y = 200) 
                btn3 = customtkinter.CTkButton(root, text = tests[2][0] + "  Nr  intrebari: " + str(tests[2][1]), text_color = "#2C2D38", command = lambda: self.print_a_test(btns_to_destroy_back, 1, 3, tests[2][0],int(tests[2][1]), all_buttons_test, label_tests_view, label_tests_filter), fg_color = "#488AC1", bg_color = "#2C2D38", height = 50, width = 500)
                btn3.place(x = 150, y = 200) 
                btn4 = customtkinter.CTkButton(root, text = tests[3][0] + "  Nr  intrebari: " + str(tests[3][1]) , text_color = "#2C2D38", command = lambda: self.print_a_test(btns_to_destroy_back, 1, 4, tests[3][0],int(tests[3][1]), all_buttons_test, label_tests_view, label_tests_filter), fg_color = "#488AC1", bg_color = "#2C2D38", height = 50, width = 500)
                btn4.place(x = 150, y = 200) 
                all_buttons_test.append(btn1)
                all_buttons_test.append(btn2)
                all_buttons_test.append(btn3)
                all_buttons_test.append(btn4)
                
                




        if i < len_pagini:
             btn_next_text_page = customtkinter.CTkButton(root, text = "Next",  text_color = "#2C2D38",fg_color = "#488AC1", bg_color = "#2C2D38", command = lambda:  self.print_all_tests(btns_to_destroy_back, tests, all_buttons_test, count+5, i+1, btn_test_1, btn_test_2, btn_test_3, btn_test_4, btn_test_5, btn_next_text_page,  label_tests_view, label_tests_filter), height = 60, width = 60)
             btn_next_text_page.place(x = 670, y = 570)
             all_buttons_test.append(btn_next_text_page)
        elif len_pagini != 0 and len_rest != 0:
             btn_page_rest_tests = customtkinter.CTkButton(root, text = "Next",  text_color = "#2C2D38", fg_color = "#488AC1", bg_color = "#2C2D38", command = lambda:  self.print_rest_tests(btns_to_destroy_back, tests, btn_page_rest_tests, all_buttons_test, len_rest, btn_test_1, btn_test_2, btn_test_3, btn_test_4, btn_test_5, label_tests_view, label_tests_filter), height = 60, width = 60)
             btn_page_rest_tests.place(x = 670, y = 570)
             all_buttons_test.append(btn_page_rest_tests)
    def print_rest_tests(self, btns_to_destroy_back, tests, btn_page_rest_tests, all_buttons_test, len_rest, btn_test_1, btn_test_2, btn_test_3, btn_test_4, btn_test_5, label_tests_view, label_tests_filter):
        if btn_test_1:
            btn_test_1.destroy()        
        if btn_test_2:
            btn_test_2.destroy()       
        if btn_test_3:
            btn_test_3.destroy()      
        if btn_test_4:
            btn_test_4.destroy()        
        if btn_test_5:
            btn_test_5.destroy()   
        if btn_page_rest_tests:
            btn_page_rest_tests.destroy()
            if len_rest == 0:
                pass
            elif len_rest == 1:
                btn = customtkinter.CTkButton(root, text = tests[len(tests) - len_rest][0] + "  Nr  intrebari: " + str(tests[len(tests) - len_rest][1]),  text_color = "#2C2D38",command = lambda: self.print_a_test(btns_to_destroy_back, 1, len(tests) - len_rest + 1, tests[len(tests) - len_rest][0],int(tests[len(tests) - len_rest][1]), all_buttons_test, label_tests_view, label_tests_filter), fg_color = "#488AC1", bg_color = "#2C2D38", height = 50, width = 500)
                btn.place(x = 150, y = 200) 
                all_buttons_test.append(btn)
            elif len_rest == 2:
                btn1 = customtkinter.CTkButton(root, text = tests[len(tests) - len_rest][0] + "  Nr  intrebari: " + str(tests[len(tests) - len_rest][1]), text_color = "#2C2D38", command = lambda: self.print_a_test(btns_to_destroy_back, 1, len(tests) - len_rest + 1, tests[len(tests) - len_rest][0],int(tests[len(tests) - len_rest][1]), all_buttons_test, label_tests_view, label_tests_filter), fg_color = "#488AC1", bg_color = "#2C2D38", height = 50, width = 500)
                btn1.place(x = 150, y = 200) 
                btn2 = customtkinter.CTkButton(root, text = tests[len(tests) - len_rest + 1][0] + "  Nr  intrebari: " + str(tests[len(tests) - len_rest + 1][1]), text_color = "#2C2D38", command = lambda: self.print_a_test(btns_to_destroy_back, 1, len(tests) - len_rest + 2, tests[len(tests) - len_rest + 1][0],int(tests[len(tests) - len_rest + 1][1]), all_buttons_test, label_tests_view, label_tests_filter), fg_color = "#488AC1", bg_color = "#2C2D38", height = 50, width = 500)
                btn2.place(x = 150, y = 280) 
                all_buttons_test.append(btn1)
                all_buttons_test.append(btn2)
            elif len_rest == 3:
                btn1 = customtkinter.CTkButton(root, text = tests[len(tests) - len_rest][0] + "  Nr  intrebari: " + str(tests[len(tests) - len_rest][1]), text_color = "#2C2D38", command = lambda: self.print_a_test(btns_to_destroy_back, 1, len(tests) - len_rest + 1, tests[len(tests) - len_rest][0],int(tests[len(tests) - len_rest][1]), all_buttons_test, label_tests_view, label_tests_filter), fg_color = "#488AC1", bg_color = "#2C2D38", height = 50, width = 500)
                btn1.place(x = 150, y = 200) 
                btn2 = customtkinter.CTkButton(root, text = tests[len(tests) - len_rest + 1][0] + "  Nr  intrebari: " + str(tests[len(tests) - len_rest + 1][1]), text_color = "#2C2D38", command = lambda: self.print_a_test(btns_to_destroy_back, 1, len(tests) - len_rest + 2, tests[len(tests) - len_rest + 1][0],int(tests[len(tests) - len_rest + 1][1]), all_buttons_test, label_tests_view, label_tests_filter), fg_color = "#488AC1", bg_color = "#2C2D38", height = 50, width = 500)
                btn2.place(x = 150, y = 280) 
                btn3 = customtkinter.CTkButton(root, text = tests[len(tests) - len_rest + 2][0] + "  Nr  intrebari: " + str(tests[len(tests) - len_rest + 2][1]), text_color = "#2C2D38", command = lambda: self.print_a_test(btns_to_destroy_back, 1, len(tests) - len_rest + 3, tests[len(tests) - len_rest + 2][0],int(tests[len(tests) - len_rest + 2][1]), all_buttons_test, label_tests_view, label_tests_filter), fg_color = "#488AC1", bg_color = "#2C2D38", height = 50, width = 500)
                btn3.place(x = 150, y = 360) 
                all_buttons_test.append(btn1)
                all_buttons_test.append(btn2)
                all_buttons_test.append(btn3)
            elif len_rest == 4:
                btn1 = customtkinter.CTkButton(root, text = tests[len(tests) - len_rest][0] + "  Nr  intrebari: " + str(tests[len(tests) - len_rest][1]), text_color = "#2C2D38", command = lambda: self.print_a_test(btns_to_destroy_back, 1, len(tests) - len_rest + 1, tests[len(tests) - len_rest][0],int(tests[len(tests) - len_rest][1]), all_buttons_test, label_tests_view, label_tests_filter), fg_color = "#488AC1", bg_color = "#2C2D38", height = 50, width = 500)
                btn1.place(x = 150, y = 200) 
                btn2 = customtkinter.CTkButton(root, text = tests[len(tests) - len_rest + 1][0] + "  Nr  intrebari: " + str(tests[len(tests) - len_rest + 1][1]), text_color = "#2C2D38", command = lambda: self.print_a_test(btns_to_destroy_back, 1, len(tests) - len_rest + 2, tests[len(tests) - len_rest + 1][0],int(tests[len(tests) - len_rest + 1][1]), all_buttons_test, label_tests_view, label_tests_filter), fg_color = "#488AC1", bg_color = "#2C2D38", height = 50, width = 500)
                btn2.place(x = 150, y = 280) 
                btn3 = customtkinter.CTkButton(root, text = tests[len(tests) - len_rest + 2][0] + "  Nr  intrebari: " + str(tests[len(tests) - len_rest + 2][1]), text_color = "#2C2D38", command = lambda: self.print_a_test(btns_to_destroy_back, 1, len(tests) - len_rest + 3, tests[len(tests) - len_rest + 2][0],int(tests[len(tests) - len_rest + 2][1]), all_buttons_test, label_tests_view, label_tests_filter), fg_color = "#488AC1", bg_color = "#2C2D38", height = 50, width = 500)
                btn3.place(x = 150, y = 360) 
                btn4 = customtkinter.CTkButton(root, text = tests[len(tests) - len_rest + 3][0] + "  Nr  intrebari: " + str(tests[len(tests) - len_rest + 3][1]), text_color = "#2C2D38", command = lambda: self.print_a_test(btns_to_destroy_back, 1, len(tests) - len_rest + 4, tests[len(tests) - len_rest + 3][0],int(tests[len(tests) - len_rest + 3][1]), all_buttons_test, label_tests_view, label_tests_filter), fg_color = "#488AC1", bg_color = "#2C2D38", height = 50, width = 500)
                btn4.place(x = 150, y = 440) 
                all_buttons_test.append(btn1)
                all_buttons_test.append(btn2)
                all_buttons_test.append(btn3)
                all_buttons_test.append(btn4)
    def print_a_test(self,btns_to_destroy_back, count, test_id, test_name, nr_questions, all_buttons_test, label_tests_view, label_tests_filter):
        all_labels_to_destroy = []
        two_labels_to_destroy = []

        if is_prof_global == 1:
        
            if label_tests_view:
                label_tests_view.destroy()
            if label_tests_filter:
                label_tests_filter.destroy()
            for button in all_buttons_test:
                if button:
                    button.destroy()
            for btn in btns_to_destroy_back:
                if btn: 
                    btn.destroy()
                
            test_id = self.db.returneaza_rowid(test_name, nr_questions)
            print(test_name,nr_questions)
            print(test_id)
            questions = self.db.afiseaza_intrebari(test_id)
        
            label_for_all = customtkinter.CTkLabel(root, text = "", height = 510, width = 1000, fg_color = "#2C2D38", bg_color ="#39a1aa", corner_radius = 15)
            label_for_all.place(x = 50, y = 150) 
            label_denumire = customtkinter.CTkLabel(root, text = "Denumire Test: " + str(test_name), text_color = "#2C2D38", height = 50, width = 300, fg_color = "#488AC1", bg_color ="#2C2D38", corner_radius = 15)
            label_denumire.place(x = 350, y = 180)  
            two_labels_to_destroy = []
            two_labels_to_destroy.append(label_for_all)
            two_labels_to_destroy.append(label_denumire)
        
            label_ques = customtkinter.CTkLabel(root, text = questions[0][1], text_color = "#2C2D38", height = 50, width = 700, fg_color = "#488AC1", bg_color ="#2C2D38", corner_radius = 15)
            label_ques.place(x = 200, y = 260)       
            label_answer_1 = customtkinter.CTkLabel(root, text = questions[0][2], text_color = "#2C2D38", height = 50, width = 500, fg_color = "#488AC1", bg_color ="#2C2D38", corner_radius = 15)
            label_answer_1.place(x = 200, y = 340)        
            label_answer_2 = customtkinter.CTkLabel(root, text = questions[0][3], text_color = "#2C2D38", height = 50, width = 500, fg_color = "#488AC1", bg_color ="#2C2D38", corner_radius = 15)
            label_answer_2.place(x = 200, y = 420)       
            label_answer_3 = customtkinter.CTkLabel(root, text = questions[0][4], text_color = "#2C2D38", height = 50, width = 500, fg_color = "#488AC1", bg_color ="#2C2D38", corner_radius = 15)
            label_answer_3.place(x = 200, y = 490)
            label_answer_4 = customtkinter.CTkLabel(root, text = questions[0][5], text_color = "#2C2D38", height = 50, width = 500, fg_color = "#488AC1", bg_color ="#2C2D38", corner_radius = 15)
            label_answer_4.place(x = 200, y = 570)
        
            all_labels_to_destroy.append(label_ques)
            all_labels_to_destroy.append(label_answer_1)
            all_labels_to_destroy.append(label_answer_2)
            all_labels_to_destroy.append(label_answer_3)
            all_labels_to_destroy.append(label_answer_4)
        
            if nr_questions > 1 and count < nr_questions:
                 btn_next = customtkinter.CTkButton(root, text = "Next", command = lambda: self.next_page_test_view(btn_next, all_labels_to_destroy, 2, questions, nr_questions), fg_color = "#488AC1", bg_color = "#2C2D38", height = 60, width = 60)
                 btn_next.place(x = 970, y = 570)     
                 all_labels_to_destroy.append(btn_next)
            btn_10 = customtkinter.CTkButton(root, image = img_back_button, text = "", fg_color = "#2C2D38", bg_color = "#2C2D38", command = lambda:  self.destroy_tests_view_and_create_initial_pag(btns_to_destroy_back, btn_10, all_labels_to_destroy, two_labels_to_destroy), height = 60, width = 60)
            btn_10.place(x = 50, y = 20)
            

        elif is_prof_global == 0:
            written_answers = []
            if label_tests_view:
                label_tests_view.destroy()
            if label_tests_filter:
                label_tests_filter.destroy()
            for button in all_buttons_test:
                if button:
                    button.destroy()
            for btn in btns_to_destroy_back:
                if btn: 
                    btn.destroy()
            test_id = self.db.returneaza_rowid(test_name, nr_questions)
            print(test_name,nr_questions)
            print(test_id)
            questions = self.db.afiseaza_intrebari(test_id)
            
            label_for_all = customtkinter.CTkLabel(root, text = "", height = 510, width = 1000, fg_color = "#2C2D38", bg_color ="#39a1aa", corner_radius = 15)
            label_for_all.place(x = 50, y = 150) 
            label_denumire = customtkinter.CTkLabel(root, text = "Test name: " + str(test_name), text_color = "#2C2D38", height = 50, width = 300, fg_color = "#488AC1", bg_color ="#2C2D38", corner_radius = 15)
            label_denumire.place(x = 350, y = 180)  
            two_labels_to_destroy.append(label_for_all)
            two_labels_to_destroy.append(label_denumire)
        
            label_ques = customtkinter.CTkLabel(root, text = questions[0][1], text_color = "#2C2D38", height = 50, width = 700, fg_color = "#488AC1", bg_color ="#2C2D38", corner_radius = 15)
            label_ques.place(x = 200, y = 260)       
            label_answer_1 = customtkinter.CTkLabel(root, text = questions[0][2], text_color = "#2C2D38", height = 50, width = 500, fg_color = "#488AC1", bg_color ="#2C2D38", corner_radius = 15)
            label_answer_1.place(x = 200, y = 340) 
            
            label_answer_2 = customtkinter.CTkLabel(root, text = questions[0][3], text_color = "#2C2D38", height = 50, width = 500, fg_color = "#488AC1", bg_color ="#2C2D38", corner_radius = 15)
            label_answer_2.place(x = 200, y = 420)       
            label_answer_3 = customtkinter.CTkLabel(root, text = questions[0][4], text_color = "#2C2D38", height = 50, width = 500, fg_color = "#488AC1", bg_color ="#2C2D38", corner_radius = 15)
            label_answer_3.place(x = 200, y = 490)
            label_answer_4 = customtkinter.CTkLabel(root, text = questions[0][5], text_color = "#2C2D38", height = 50, width = 500, fg_color = "#488AC1", bg_color ="#2C2D38", corner_radius = 15)
            label_answer_4.place(x = 200, y = 570)
            
            check_var_1 = tk.StringVar(value = "off")
            check_var_2 = tk.StringVar(value = "off")
            check_var_3 = tk.StringVar(value = "off")
            check_var_4 = tk.StringVar(value = "off")

            check_box_1 = customtkinter.CTkCheckBox(root, text ="", variable = check_var_1, onvalue = "on", offvalue = " off", fg_color = "#2C2D38", bg_color= "#2C2D38", height = 10, width = 10)
            check_box_1.place(x = 750, y = 355)        
            check_box_2 = customtkinter.CTkCheckBox(root, text ="", variable = check_var_2, onvalue = "on", offvalue = " off", fg_color = "#2C2D38", bg_color= "#2C2D38", height = 10, width = 10)
            check_box_2.place(x = 750, y = 425)        
            check_box_3 = customtkinter.CTkCheckBox(root, text ="", variable = check_var_3, onvalue = "on", offvalue = " off", fg_color = "#2C2D38", bg_color= "#2C2D38", height = 10, width = 10)
            check_box_3.place(x = 750, y = 495)       
            check_box_4 = customtkinter.CTkCheckBox(root, text ="", variable = check_var_4, onvalue = "on", offvalue = " off", fg_color = "#2C2D38", bg_color= "#2C2D38", height = 10, width = 10)
            check_box_4.place(x = 750, y = 565)
            all_labels_to_destroy.append(check_box_1)
            all_labels_to_destroy.append(check_box_2)
            all_labels_to_destroy.append(check_box_3)
            all_labels_to_destroy.append(check_box_4)
        
            all_labels_to_destroy.append(label_ques)
            all_labels_to_destroy.append(label_answer_1)
            all_labels_to_destroy.append(label_answer_2)
            all_labels_to_destroy.append(label_answer_3)
            all_labels_to_destroy.append(label_answer_4)
            
            if nr_questions > 1 and count < nr_questions:
                 btn_next = customtkinter.CTkButton(root, text = "Next", command = lambda: self.nex_text_solve(two_labels_to_destroy, test_id, written_answers, btn_next, all_labels_to_destroy, 2, questions, nr_questions, check_var_1, check_var_2, check_var_3, check_var_4), fg_color = "#488AC1", bg_color = "#2C2D38", height = 60, width = 60)
                 btn_next.place(x = 970, y = 570)     
                 all_labels_to_destroy.append(btn_next)
            btn_10 = customtkinter.CTkButton(root, image = img_back_button, text = "", fg_color = "#2C2D38", bg_color = "#2C2D38", command = lambda:  self.destroy_tests_view_and_create_initial_pag(btns_to_destroy_back, btn_10, all_labels_to_destroy, two_labels_to_destroy), height = 60, width = 60)
            btn_10.place(x = 50, y = 20)
    def nex_text_solve(self, two_labels_to_destroy, test_id, written_answers, btn_next, all_labels_to_destroy, i, questions, nr_questions, check_var_1, check_var_2, check_var_3, check_var_4):
        if check_var_1.get() == "on":
            written_answers.append(1)
        elif check_var_2.get() == "on":
            written_answers.append(2)
        elif check_var_3.get() == "on":
            written_answers.append(3)
        elif check_var_4.get() == "on":
            written_answers.append(4)
        for widget in all_labels_to_destroy:
            if widget.winfo_exists():
                widget.destroy()
        if btn_next:
            btn_next.destroy()

 


        label_ques = customtkinter.CTkLabel(root, text = questions[i-1][1], text_color = "#2C2D38", height = 50, width = 700, fg_color = "#488AC1", bg_color ="#2C2D38", corner_radius = 15)
        label_ques.place(x = 200, y = 260)       
        label_answer_1 = customtkinter.CTkLabel(root, text = questions[i-1][2], text_color = "#2C2D38", height = 50, width = 500, fg_color = "#488AC1", bg_color ="#2C2D38", corner_radius = 15)
        label_answer_1.place(x = 200, y = 340)        
        label_answer_2 = customtkinter.CTkLabel(root, text = questions[i-1][3], text_color = "#2C2D38", height = 50, width = 500, fg_color = "#488AC1", bg_color ="#2C2D38", corner_radius = 15)
        label_answer_2.place(x = 200, y = 420)       
        label_answer_3 = customtkinter.CTkLabel(root, text = questions[i-1][4], text_color = "#2C2D38", height = 50, width = 500, fg_color = "#488AC1", bg_color ="#2C2D38", corner_radius = 15)
        label_answer_3.place(x = 200, y = 490)
        label_answer_4 = customtkinter.CTkLabel(root, text = questions[i-1][5], text_color = "#2C2D38", height = 50, width = 500, fg_color = "#488AC1", bg_color ="#2C2D38", corner_radius = 15)
        label_answer_4.place(x = 200, y = 570)
        
        check_box_var_1 = tk.StringVar(value = "off")
        check_box_var_2 = tk.StringVar(value = "off")
        check_box_var_3 = tk.StringVar(value = "off")
        check_box_var_4 = tk.StringVar(value = "off")

        check_box_1 = customtkinter.CTkCheckBox(root, text ="", variable = check_box_var_1, onvalue = "on", offvalue = " off", fg_color = "#2C2D38", bg_color= "#2C2D38", height = 10, width = 10)
        check_box_1.place(x = 750, y = 355)        
        check_box_2 = customtkinter.CTkCheckBox(root, text ="", variable = check_box_var_2, onvalue = "on", offvalue = " off", fg_color = "#2C2D38", bg_color= "#2C2D38", height = 10, width = 10)
        check_box_2.place(x = 750, y = 425)        
        check_box_3 = customtkinter.CTkCheckBox(root, text ="", variable = check_box_var_3, onvalue = "on", offvalue = " off", fg_color = "#2C2D38", bg_color= "#2C2D38", height = 10, width = 10)
        check_box_3.place(x = 750, y = 495)       
        check_box_4 = customtkinter.CTkCheckBox(root, text ="", variable = check_box_var_4, onvalue = "on", offvalue = " off", fg_color = "#2C2D38", bg_color= "#2C2D38", height = 10, width = 10)
        check_box_4.place(x = 750, y = 565)
        all_labels_to_destroy.append(check_box_1)
        all_labels_to_destroy.append(check_box_2)
        all_labels_to_destroy.append(check_box_3)
        all_labels_to_destroy.append(check_box_4)

        all_labels_to_destroy.append(label_ques)
        all_labels_to_destroy.append(label_answer_1)
        all_labels_to_destroy.append(label_answer_2)
        all_labels_to_destroy.append(label_answer_3)
        all_labels_to_destroy.append(label_answer_4)
        if i < len(questions):
            btn_recursiv = customtkinter.CTkButton(root, text = "Next", command = lambda: self.nex_text_solve(two_labels_to_destroy, test_id, written_answers, btn_recursiv, all_labels_to_destroy, i+1, questions, nr_questions, check_box_var_1, check_box_var_2, check_box_var_3, check_box_var_4), fg_color = "#488AC1", bg_color = "#2C2D38", height = 60, width = 60)
            btn_recursiv.place(x = 970, y = 570)
            all_labels_to_destroy.append(btn_recursiv)
        else:
            submit_button = customtkinter.CTkButton(root, text="Submit",command=lambda: self.save_solve_data_and_go_to_pag_4_student(two_labels_to_destroy, test_id, written_answers, submit_button, all_labels_to_destroy,check_box_var_1, check_box_var_2, check_box_var_3, check_box_var_4),fg_color="#488AC1", bg_color="#2C2D38", height = 60, width = 60)
            submit_button.place(x=970, y=570) 
    def save_solve_data_and_go_to_pag_4_student(self, two_labels_to_destroy, test_id, written_answers, submit_button, all_labels_to_destroy,check_box_var_1, check_box_var_2, check_box_var_3, check_box_var_4):
        if check_box_var_1.get() == "on":
            written_answers.append(1)
        elif check_box_var_2.get() == "on":
            written_answers.append(2)
        elif check_box_var_3.get() == "on":
            written_answers.append(3)
        elif check_box_var_4.get() == "on":
            written_answers.append(4)        
        global written_username
        correct_answers = self.db.intrebari_corecte_a_unui_test(test_id)
        nr_intrebari = len(written_answers)
        intrebari_corecte_introduse = 0
        print(correct_answers)
        print(written_answers)
        for i in range(nr_intrebari):
            if int(written_answers[i]) == correct_answers[i][0]:
                intrebari_corecte_introduse += 1
        if intrebari_corecte_introduse != 0:
            nota = 10/len(written_answers)*intrebari_corecte_introduse
        else:
            nota = 0
        nota = round(nota, 2)
        nume_test = self.db.afiseaza_nume_test(test_id)
        self.db.adauga_rezultat(test_id, nume_test[0][0], written_username, nota)
        for label in all_labels_to_destroy:
            if label.winfo_exists():
                label.destroy()
        if submit_button:
            submit_button.destroy()
        for label in two_labels_to_destroy:
            if label:
                label.destroy()

        labels_to_go_home = []
        label_back = customtkinter.CTkLabel(root, text = "", text_color = "#2C2D38", height = 300, width = 400, fg_color = "#2C2D38", bg_color ="#39a1aa", corner_radius = 15)
        label_back.place(x = 350, y = 280)
        label_text = customtkinter.CTkLabel(root, text = "Congratulations!! The obtained grade is:" + str(nota),  text_color = "#2C2D38", height = 100, width = 200, fg_color = "#488AC1", bg_color ="#2C2D38", corner_radius = 15)
        label_text.place(x = 450, y = 380)
        button_go_home = customtkinter.CTkButton(root, text="Home",command=lambda: self.go_home(labels_to_go_home),fg_color="#488AC1", bg_color="#2C2D38", height=50, width=50)
        button_go_home.place(x=690, y=520)
        label_above_back_button = customtkinter.CTkLabel(root,text = "", height = 70, width = 80, fg_color = "#2C2D38", bg_color ="#2C2D38", corner_radius = 15)
        label_above_back_button.place(x = 50, y = 20)
        labels_to_go_home.append(label_back)
        labels_to_go_home.append(label_text)
        labels_to_go_home.append(button_go_home)
        labels_to_go_home.append(label_above_back_button)
    def go_home(self, labels_to_go_home):
        for label in labels_to_go_home:
            if label:
                label.destroy()
        global written_username
        self.create_pag_4_student_solve(root, written_username)
    def next_page_test_view(self, btn_next, all_labels_to_destroy,  i, questions, nr_questions):
        
        for label in all_labels_to_destroy:
            if label:
                label.destroy()
        if btn_next:
            btn_next.destroy()
        label_ques = customtkinter.CTkLabel(root, text = questions[i-1][1], text_color = "#2C2D38", height = 50, width = 700, fg_color = "#488AC1", bg_color ="#2C2D38", corner_radius = 15)
        label_ques.place(x = 200, y = 260)       
        label_answer_1 = customtkinter.CTkLabel(root, text = questions[i-1][2], text_color = "#2C2D38", height = 50, width = 500, fg_color = "#488AC1", bg_color ="#2C2D38", corner_radius = 15)
        label_answer_1.place(x = 200, y = 340)        
        label_answer_2 = customtkinter.CTkLabel(root, text = questions[i-1][3], text_color = "#2C2D38", height = 50, width = 500, fg_color = "#488AC1", bg_color ="#2C2D38", corner_radius = 15)
        label_answer_2.place(x = 200, y = 420)       
        label_answer_3 = customtkinter.CTkLabel(root, text = questions[i-1][4], text_color = "#2C2D38", height = 50, width = 500, fg_color = "#488AC1", bg_color ="#2C2D38", corner_radius = 15)
        label_answer_3.place(x = 200, y = 490)
        label_answer_4 = customtkinter.CTkLabel(root, text = questions[i-1][5], text_color = "#2C2D38", height = 50, width = 500, fg_color = "#488AC1", bg_color ="#2C2D38", corner_radius = 15)
        label_answer_4.place(x = 200, y = 570)
        all_labels_to_destroy.append(label_ques)
        all_labels_to_destroy.append(label_answer_1)
        all_labels_to_destroy.append(label_answer_2)
        all_labels_to_destroy.append(label_answer_3)
        all_labels_to_destroy.append(label_answer_4)
        
        if i < len(questions):
            btn_recursiv = customtkinter.CTkButton(root, text = "Next", command = lambda: self.next_page_test_view(btn_recursiv, all_labels_to_destroy, i+1, questions, nr_questions), fg_color = "#488AC1", bg_color = "#2C2D38", height = 60, width = 60)
            btn_recursiv.place(x = 970, y = 570)
            all_labels_to_destroy.append(btn_recursiv)
    def destroy_tests_view_and_create_initial_pag(self,btns_to_destroy_back, btn_10, all_labels_to_destroy, two_labels_to_destroy):
        btn_10.destroy()
        for btn in btns_to_destroy_back:
            btn.destroy()
        for label in two_labels_to_destroy:
            if label:
                label.destroy()
        for label in all_labels_to_destroy:
            label.destroy()
        if is_prof_global == 1:
            self.create_pag_4_prof_tests(root, global_writen_username_prof)
        elif is_prof_global == 0:
            self.create_pag_4_student_solve(root, global_writen_username_student)
    def create_pag_4_prof_add_test(self, root, writen_username):
        is_prof = 1
        questions = []
        answers = []
        correct_answers = []
        check_boxes_to_destroy = []
        label_create_test = customtkinter.CTkLabel(root, text = "", height = 500, width = 1000, fg_color = "#2C2D38", bg_color ="#39a1aa", corner_radius = 15)
        label_create_test.place(x = 50, y = 150)
        
        test_name_entry = customtkinter.CTkEntry(root, placeholder_text = "Test name", height = 50, width = 200)
        test_name_entry.place(x = 200, y = 200)
        nr_ques_entry = customtkinter.CTkEntry(root, placeholder_text = "Num of questions", height = 50, width = 200)
        nr_ques_entry.place(x = 400, y = 200)
        submit_button = customtkinter.CTkButton(root, text = "Create",command = lambda: self.create_test_questions(check_boxes_to_destroy, correct_answers, label_create_test, submit_button, writen_username, questions, answers, 1,test_name_entry, nr_ques_entry) ,fg_color = "#488AC1", bg_color = "#2C2D38", height = 50, width = 100)
        submit_button.place(x = 650, y = 200)

        btn_10 = customtkinter.CTkButton(root, image = img_back_button, text = "", fg_color = "#2C2D38", bg_color = "#2C2D38", command = lambda:  self.destroy_pag_4_prof_add_test_and_create_pag_3(submit_button, nr_ques_entry, label_create_test, test_name_entry, writen_username, is_prof), height = 60, width = 60)
        btn_10.place(x = 50, y = 20)
    def checkbox_event(self):
        pass
    def create_test_questions(self, check_boxes_to_destroy,  correct_answers, label_create_test, to_delete_button, writen_username, questions, answers, count, test_name_entry, nr_ques_entry):
        nr_ques_text = nr_ques_entry.get()
        if nr_ques_text:
            try:
                written_nr_ques = int(nr_ques_text)
            except ValueError:
                return  # Exit the function if the value is not valid

            # Create lists to store questions and answers
        question_entry = customtkinter.CTkEntry(root, placeholder_text="Question", height=50, width=500)
        question_entry.place(x=200, y=280)
        var_1_entry = customtkinter.CTkEntry(root, placeholder_text=f"Answer 1", height=50, width=300)
        var_1_entry.place(x=200, y=355)
        var_2_entry = customtkinter.CTkEntry(root, placeholder_text=f"Answer 2", height=50, width=300)
        var_2_entry.place(x=200, y=425)
        var_3_entry = customtkinter.CTkEntry(root, placeholder_text=f"Answer 3", height=50, width=300)
        var_3_entry.place(x=200, y=495)
        var_4_entry = customtkinter.CTkEntry(root, placeholder_text=f"Answer 4", height=50, width=300)
        var_4_entry.place(x=200, y=565)
        
        check_var_1 = tk.StringVar(value = "off")
        check_var_2 = tk.StringVar(value = "off")
        check_var_3 = tk.StringVar(value = "off")
        check_var_4 = tk.StringVar(value = "off")

        check_box_1 = customtkinter.CTkCheckBox(root, text ="", variable = check_var_1, onvalue = "on", offvalue = " off", fg_color = "#2C2D38", bg_color= "#2C2D38", height = 10, width = 10)
        check_box_1.place(x = 550, y = 355)        
        check_box_2 = customtkinter.CTkCheckBox(root, text ="", variable = check_var_2, onvalue = "on", offvalue = " off", fg_color = "#2C2D38", bg_color= "#2C2D38", height = 10, width = 10)
        check_box_2.place(x = 550, y = 425)        
        check_box_3 = customtkinter.CTkCheckBox(root, text ="", variable = check_var_3, onvalue = "on", offvalue = " off", fg_color = "#2C2D38", bg_color= "#2C2D38", height = 10, width = 10)
        check_box_3.place(x = 550, y = 495)       
        check_box_4 = customtkinter.CTkCheckBox(root, text ="", variable = check_var_4, onvalue = "on", offvalue = " off", fg_color = "#2C2D38", bg_color= "#2C2D38", height = 10, width = 10)
        check_box_4.place(x = 550, y = 565)
        check_boxes_to_destroy.append(check_box_1)
        check_boxes_to_destroy.append(check_box_2)
        check_boxes_to_destroy.append(check_box_3)
        check_boxes_to_destroy.append(check_box_4)
        if question_entry and var_1_entry and var_2_entry and var_3_entry and var_4_entry and count != written_nr_ques:
            next_button = customtkinter.CTkButton(root, text="Next",command=lambda: self.save_data(check_boxes_to_destroy, correct_answers, next_button, label_create_test, to_delete_button, writen_username, questions, answers, count, question_entry, var_1_entry, var_2_entry, var_3_entry, var_4_entry, test_name_entry, nr_ques_entry, check_box_1, check_box_2, check_box_3, check_box_4, check_var_1, check_var_2, check_var_3, check_var_4) ,fg_color="#488AC1", bg_color="#2C2D38", height=50, width=100)
            next_button.place(x=650, y=580)

            

             
        if count == written_nr_ques:
            submit_button = customtkinter.CTkButton(root, text="Submit",command=lambda: self.save_data_and_go_to_create_pag_4_prof_add_test(check_boxes_to_destroy, correct_answers, submit_button, label_create_test, to_delete_button, written_nr_ques, writen_username, questions, answers, question_entry, var_1_entry, var_2_entry, var_3_entry, var_4_entry, test_name_entry, nr_ques_entry, check_box_1, check_box_2, check_box_3, check_box_4, check_var_1, check_var_2, check_var_3, check_var_4),fg_color="#488AC1", bg_color="#2C2D38", height=50, width=100)
            submit_button.place(x=650, y=580)
    def save_data(self, check_boxes_to_destroy, correct_answers, next_button, label_create_test, to_delete_button, writen_username, questions, answers,count, question_entry, var_1_entry, var_2_entry, var_3_entry, var_4_entry, test_name_entry, nr_ques_entry, check_box_1, check_box_2, check_box_3, check_box_4, check_var_1, check_var_2, check_var_3, check_var_4):
        count += 1
        written_1_var = var_1_entry.get()
        written_2_var = var_2_entry.get()
        written_3_var = var_3_entry.get()
        written_4_var = var_4_entry.get()
        written_question = question_entry.get()
        _4_variants = []
        _4_variants.append(written_1_var)
        _4_variants.append(written_2_var)
        _4_variants.append(written_3_var)
        _4_variants.append(written_4_var)
        
        if check_var_1.get() == "on":
            correct_answers.append(1)
        if check_var_2.get() == "on":
           correct_answers.append(2)
        if check_var_3.get() == "on":
           correct_answers.append(3)
        if check_var_4.get() == "on":
           correct_answers.append(4)
        

        questions.append(written_question)
        answers.append(_4_variants)
        question_entry.destroy()  
        var_1_entry.destroy()
        var_2_entry.destroy()
        var_3_entry.destroy()
        var_4_entry.destroy()
        next_button.destroy()
        self.create_test_questions( check_boxes_to_destroy, correct_answers, label_create_test, to_delete_button, writen_username, questions, answers, count, test_name_entry, nr_ques_entry)
    def save_data_and_go_to_create_pag_4_prof_add_test(self,check_boxes_to_destroy,  correct_answers, submit_button, label_create_test, to_delete_button, written_nr_ques, writen_username, questions, answers, question_entry, var_1_entry, var_2_entry, var_3_entry, var_4_entry, test_name_entry, nr_ques_entry, check_box_1, check_box_2, check_box_3, check_box_4, check_var_1, check_var_2, check_var_3, check_var_4):
        written_1_var = var_1_entry.get()
        written_2_var = var_2_entry.get()
        written_3_var = var_3_entry.get()
        written_4_var = var_4_entry.get()
        written_question = question_entry.get()
        test_name = test_name_entry.get()
        _4_variants = []
        _4_variants.append(written_1_var)
        _4_variants.append(written_2_var)
        _4_variants.append(written_3_var)
        _4_variants.append(written_4_var)
        questions.append(written_question)
        answers.append(_4_variants)
        
        if check_var_1.get() == "on":
            correct_answers.append(1)
        if check_var_2.get() == "on":
            correct_answers.append(2)
        if check_var_3.get() == "on":
            correct_answers.append(3)
        if check_var_4.get() == "on":
            correct_answers.append(4)
        
        self.db.adauga_test(test_name, written_nr_ques)
        last_row_id = self.db.cursor.lastrowid
        for i in range(written_nr_ques):
            self.db.adauga_intrebare(last_row_id, questions[i], answers[i][0], answers[i][1], answers[i][2], answers[i][3], correct_answers[i])
            
        question_entry.destroy()  
        var_1_entry.destroy()
        var_2_entry.destroy()
        var_3_entry.destroy()
        var_4_entry.destroy()
        label_create_test.destroy()
        to_delete_button.destroy()
        test_name_entry.destroy()
        submit_button.destroy()
        nr_ques_entry.destroy()
        for box in check_boxes_to_destroy:
            if box:
                box.destroy()
        self.create_pag_4_prof_add_test(root, writen_username)
    def destroy_pag_4_prof_add_test_and_create_pag_3(self, submit_button, nr_ques_entry, label_create_test, test_name_entry, writen_username, is_prof):
        label_create_test.destroy()
        test_name_entry.destroy()
        submit_button.destroy()
        nr_ques_entry.destroy()
        if(is_prof == 1):
            self.create_pag_3_prof(root, writen_username)
        elif(is_prof == 0):
            self.create_pag_3_student(root, writen_username)
    def destroy_pag_4_prof_tests_and_create_pag_3(self, btns_to_destroy_back, btn_9, all_buttons_test, label_tests_view, label_tests_sort, writen_username):
        label_tests_view.destroy()
        label_tests_sort.destroy()
        btn_9.destroy()
        global is_prof_global
        for button in btns_to_destroy_back:
            if button:
                button.destroy()
        for button in all_buttons_test:
            if button:
                button.destroy()
        if(is_prof_global == 1):
            self.create_pag_3_prof(root, writen_username)
        elif(is_prof_global == 0):
            self.create_pag_3_student(root, writen_username)
    def destroy_pag_4_prof_results_and_create_pag_3(self, btn_back, all_obiects_to_destroy, writen_username, is_prof):
        btn_back.destroy()
        for obiect in all_obiects_to_destroy:
            obiect.destroy()
        if(is_prof == 1):
            self.create_pag_3_prof(root, writen_username)
        elif(is_prof == 0):
            self.create_pag_3_student(root, writen_username)
    def create_test(self, test_name_entry, nr_intrebari_entry):
        test_name = test_name_entry.get()
        self.db_test.adauga_test(test_name)
        nr_intrebari = nr_intrebari_entry.get()
        test_id = self.db_test.adauga_test(test_name)
        
        for i in range(nr_intrebari):
            intrebare_entry = customtkinter.CTkEntry(root, placeholder_text = "Question", height = 100, width = 400)
            intrebare_entry.place(x = 300, y = 300)
            nr_intrebari_entry = customtkinter.CTkEntry(root, placeholder_text = "Num of Questions", height = 100, width = 400)
            nr_intrebari_entry.place(x = 800, y = 300)
            intrebare = intrebare_entry.get()
            self.db_test.adauga_intrebare(test_id, intrebare)
            self.seve_data_and_destroy(intrebare_entry, nr_intrebari_entry)

    #pag 4 student
    def create_pag_4_student_solve(self, root, _written_username):
        tests = self.db.afiseaza_test()
        global is_prof_global
        is_prof_global = 0
        global written_username
        written_username = _written_username
        
        all_buttons_test = []

        btns_to_destroy_back = []
        
        btn_test_1 = None
        btn_test_2 = None
        btn_test_3 = None
        btn_test_4 = None
        btn_test_5 = None
        btn_next_text_page = None
     
        label_tests_view = customtkinter.CTkLabel(root, text = "", height = 500, width = 700, fg_color = "#2C2D38", bg_color ="#39a1aa", corner_radius = 15)
        label_tests_view.place(x = 50, y = 150)
        label_tests_sort = customtkinter.CTkLabel(root, text = "", height = 500, width = 275, fg_color = "#2C2D38", bg_color ="#39a1aa", corner_radius =15)
        label_tests_sort.place(x = 775, y = 150)
 
        
        label_sort_by = customtkinter.CTkLabel(root, text = "Sort by",  text_color = "#2C2D38",  height = 75, width = 255, fg_color = "#488AC1", bg_color ="#2C2D38", corner_radius =15)
        label_sort_by.place(x = 785, y = 160)
        
        btn_sort_name = customtkinter.CTkButton(root, text="Test Name",  text_color = "#2C2D38",command=lambda: self.sort_by_name(btns_to_destroy_back, tests, all_buttons_test, btn_test_1, btn_test_2, btn_test_3, btn_test_4, btn_test_5, btn_next_text_page, label_tests_view, label_tests_sort), fg_color="#488AC1", bg_color="#2C2D38", height=50, width=225)
        btn_sort_name.place(x=800, y=250)

        btn_sort_by_questions = customtkinter.CTkButton(root, text="Num of questions", text_color = "#2C2D38", command=lambda: self.sort_by_questions(btns_to_destroy_back, tests, all_buttons_test, btn_test_1, btn_test_2, btn_test_3, btn_test_4, btn_test_5, btn_next_text_page, label_tests_view, label_tests_sort), fg_color="#488AC1", bg_color="#2C2D38", height=50, width=225)
        btn_sort_by_questions.place(x=800, y=315)
        
        label_search_by = customtkinter.CTkLabel(root, text = "Filter by",  text_color = "#2C2D38",  height = 75, width = 255, fg_color = "#488AC1", bg_color ="#2C2D38", corner_radius =15)
        label_search_by.place(x = 785, y = 420)
        
        entry_test_name= customtkinter.CTkEntry(master=root, placeholder_text="Name", font = font3, text_color = "#2C2D38", placeholder_text_color = "#2C2D38", width = 165, height = 50, fg_color = "#488AC1")
        entry_test_name.place(x = 800, y = 510)
        entry_nr_questions = customtkinter.CTkEntry(master=root, placeholder_text="Nr of questions", font = font3, text_color = "#2C2D38", placeholder_text_color = "#2C2D38", width = 165, height = 50, fg_color = "#488AC1")
        entry_nr_questions.place(x = 800, y = 575)

        
        btn_search_name = customtkinter.CTkButton(root, text="Name", command = lambda: self.search_name(entry_test_name, btns_to_destroy_back, all_buttons_test, btn_test_1, btn_test_2, btn_test_3, btn_test_4, btn_test_5, btn_next_text_page, label_tests_view, label_tests_sort), text_color = "#2C2D38", fg_color="#488AC1", bg_color="#2C2D38", height=50, width=50)
        btn_search_name.place(x=975, y=510)

        btn_search_questions = customtkinter.CTkButton(root, text="Num", command = lambda: self.search_questions(entry_nr_questions, btns_to_destroy_back, all_buttons_test,btn_test_1, btn_test_2, btn_test_3, btn_test_4, btn_test_5, btn_next_text_page, label_tests_view, label_tests_sort), text_color = "#2C2D38", fg_color="#488AC1", bg_color="#2C2D38", height=50, width=50)
        btn_search_questions.place(x=975, y=575)

        btns_to_destroy_back.append(btn_sort_name)
        btns_to_destroy_back.append(btn_sort_by_questions)
        btns_to_destroy_back.append(label_sort_by)
        btns_to_destroy_back.append(label_search_by)
        btns_to_destroy_back.append(btn_search_name)
        btns_to_destroy_back.append(btn_search_questions)
        btns_to_destroy_back.append(label_tests_sort)
        btns_to_destroy_back.append(entry_test_name)
        btns_to_destroy_back.append(entry_nr_questions)

        
        all_buttons_test.append(btn_test_1)
        all_buttons_test.append(btn_test_2)
        all_buttons_test.append(btn_test_3)
        all_buttons_test.append(btn_test_4)
        all_buttons_test.append(btn_test_5)
        all_buttons_test.append(btn_next_text_page)
                
        
        self.print_all_tests(btns_to_destroy_back, tests, all_buttons_test, 0, 1, btn_test_1, btn_test_2, btn_test_3, btn_test_4, btn_test_5, btn_next_text_page, label_tests_view, label_tests_sort)
        

            
        btn_9 = customtkinter.CTkButton(root, image = img_back_button, text = "", fg_color = "#2C2D38", bg_color = "#2C2D38", command = lambda:  self.destroy_pag_4_prof_tests_and_create_pag_3(btns_to_destroy_back, btn_9, all_buttons_test, label_tests_view, label_tests_sort, written_username), height = 60, width = 60)
        btn_9.place(x = 50, y = 20)
        
    def create_pag_4_resultate(self, root, written_username):
        global is_prof_global 
        if is_prof_global == 0:
            results = self.db.afiseaza_rezultate_student(written_username)
        elif is_prof_global == 1:
            results = self.db.afiseaza_rezultate_prof()
        all_buttons_test = []

        btns_to_destroy_back = []
        label_tests_view = customtkinter.CTkLabel(root, text = "", height = 500, width = 700, fg_color = "#2C2D38", bg_color ="#39a1aa", corner_radius = 15)
        label_tests_view.place(x = 50, y = 150)
        label_tests_sort = customtkinter.CTkLabel(root, text = "", height = 500, width = 275, fg_color = "#2C2D38", bg_color ="#39a1aa", corner_radius =15)
        label_tests_sort.place(x = 775, y = 150)
 
        
        label_sort_by = customtkinter.CTkLabel(root, text = "Sort by",  text_color = "#2C2D38",  height = 75, width = 255, fg_color = "#488AC1", bg_color ="#2C2D38", corner_radius =15)
        label_sort_by.place(x = 785, y = 160)
        btn_sort_results_nota_cresc = customtkinter.CTkButton(root, text="Grade ascending",  text_color = "#2C2D38",command=lambda: self.sort_student_by_mark(1, written_username, btns_to_destroy_back, all_buttons_test, btn_test_1, btn_test_2, btn_test_3, btn_test_4, btn_test_5, btn_next_text_page, label_tests_view, label_tests_sort), fg_color="#488AC1", bg_color="#2C2D38", height=50, width=225)
        btn_sort_results_nota_cresc.place(x=800, y=250)

        btn_sort_results_nota_desc = customtkinter.CTkButton(root, text="Grade descending", text_color = "#2C2D38", command=lambda: self.sort_student_by_mark(0, written_username, btns_to_destroy_back, all_buttons_test, btn_test_1, btn_test_2, btn_test_3, btn_test_4, btn_test_5, btn_next_text_page, label_tests_view, label_tests_sort), fg_color="#488AC1", bg_color="#2C2D38", height=50, width=225)
        btn_sort_results_nota_desc.place(x=800, y=315)
       
        btn_sort_results_nume_test_cresc = customtkinter.CTkButton(root, text="Test name ascending",  text_color = "#2C2D38",command=lambda: self.sort_student_by_test_name(1, written_username, btns_to_destroy_back, all_buttons_test, btn_test_1, btn_test_2, btn_test_3, btn_test_4, btn_test_5, btn_next_text_page, label_tests_view, label_tests_sort), fg_color="#488AC1", bg_color="#2C2D38", height=50, width=225)
        btn_sort_results_nume_test_cresc.place(x=800, y=380)

        btn_sort_results_nume_test_desc = customtkinter.CTkButton(root, text="Test name descending",  text_color = "#2C2D38",command=lambda: self.sort_student_by_test_name(0, written_username, btns_to_destroy_back, all_buttons_test, btn_test_1, btn_test_2, btn_test_3, btn_test_4, btn_test_5, btn_next_text_page, label_tests_view, label_tests_sort), fg_color="#488AC1", bg_color="#2C2D38", height=50, width=225)
        btn_sort_results_nume_test_desc.place(x=800, y=445)
        
        btn_sort_results_nume_student_cresc = customtkinter.CTkButton(root, text="Student name descending", text_color = "#2C2D38", command=lambda: self.sort_student_by_student_name(1, written_username, btns_to_destroy_back, all_buttons_test, btn_test_1, btn_test_2, btn_test_3, btn_test_4, btn_test_5, btn_next_text_page, label_tests_view, label_tests_sort), fg_color="#488AC1", bg_color="#2C2D38", height=50, width=225)
        btn_sort_results_nume_student_cresc.place(x=800, y=512)
        
        btn_sort_results_nume_student_desc = customtkinter.CTkButton(root, text="Student name descending", text_color = "#2C2D38", command=lambda: self.sort_student_by_student_name(0, written_username, btns_to_destroy_back, all_buttons_test, btn_test_1, btn_test_2, btn_test_3, btn_test_4, btn_test_5, btn_next_text_page, label_tests_view, label_tests_sort), fg_color="#488AC1", bg_color="#2C2D38", height=50, width=225)
        btn_sort_results_nume_student_desc.place(x=800, y=580)

        btns_to_destroy_back.append(label_tests_view)
        btns_to_destroy_back.append(label_tests_sort)
        btns_to_destroy_back.append(label_sort_by)
        btns_to_destroy_back.append(btn_sort_results_nota_cresc)
        btns_to_destroy_back.append(btn_sort_results_nota_desc)
        btns_to_destroy_back.append(btn_sort_results_nume_test_cresc)
        btns_to_destroy_back.append(btn_sort_results_nume_test_desc)
        btns_to_destroy_back.append(btn_sort_results_nume_student_cresc)
        btns_to_destroy_back.append(btn_sort_results_nume_student_desc)
        
        btn_test_1 = None
        btn_test_2 = None
        btn_test_3 = None
        btn_test_4 = None
        btn_test_5 = None
        btn_next_text_page = None
        
        all_buttons_test.append(btn_test_1)
        all_buttons_test.append(btn_test_2)
        all_buttons_test.append(btn_test_3)
        all_buttons_test.append(btn_test_4)
        all_buttons_test.append(btn_test_5)
        all_buttons_test.append(btn_next_text_page)

        self.print_all_results(btns_to_destroy_back, results, all_buttons_test, 0, 1, btn_test_1, btn_test_2, btn_test_3, btn_test_4, btn_test_5, btn_next_text_page, label_tests_view, label_tests_sort)

        if is_prof_global == 0: 
            btn_9 = customtkinter.CTkButton(root, image = img_back_button, text = "", fg_color = "#2C2D38", bg_color = "#2C2D38", command = lambda:  self.destroy_pag_4_prof_tests_and_create_pag_3(btns_to_destroy_back, btn_9, all_buttons_test, label_tests_view, label_tests_sort, written_username), height = 60, width = 60)
            btn_9.place(x = 50, y = 20)
        elif is_prof_global == 1:
            btn_9 = customtkinter.CTkButton(root, image = img_back_button, text = "", fg_color = "#2C2D38", bg_color = "#2C2D38", command = lambda:  self.destroy_pag_4_prof_tests_and_create_pag_3(btns_to_destroy_back, btn_9, all_buttons_test, label_tests_view, label_tests_sort, written_username), height = 60, width = 60)
            btn_9.place(x = 50, y = 20)
        
    def print_all_results(self, btns_to_destroy_back, results, all_buttons_test, count, i, old_button_1, old_button_2, old_button_3, old_button_4, old_button_5, btn_next_text_page, label_tests_view, label_tests_filter):
        if old_button_1:
            old_button_1.destroy()
        if old_button_2:
            old_button_2.destroy()
        if old_button_3:
            old_button_3.destroy()
        if old_button_4:
            old_button_4.destroy()
        if old_button_5:
            old_button_5.destroy()
        if btn_next_text_page:
            btn_next_text_page.destroy()
        btn_test_1 = None
        btn_test_2 = None
        btn_test_3 = None
        btn_test_4 = None
        btn_test_5 = None
        len_matrice = len(results)

        len_pagini = int(len_matrice / 5)
        len_rest = len_matrice % 5
        
        if len_pagini >= 1:
             btn_test_1 = customtkinter.CTkButton(root, text = "Student:     " + str(results[count][1]) + "   Test:   " + str(results[count][3]) + "   Grade:   " + str(results[count][2]), text_color = "#2C2D38", fg_color = "#488AC1", bg_color = "#2C2D38", height = 50, width = 500)
             btn_test_1.place(x = 150, y = 200)       
             btn_test_2 = customtkinter.CTkButton(root, text = "Student:     " + str(results[count+1][1]) + "   Test:   " + str(results[count+1][3]) + "   Grade:   " + str(results[count+1][2]), text_color = "#2C2D38", fg_color = "#488AC1", bg_color = "#2C2D38", height = 50, width = 500)
             btn_test_2.place(x = 150, y = 280)       
             btn_test_3 = customtkinter.CTkButton(root, text = "Student:     " + str(results[count+2][1]) + "   Test:   " + str(results[count+2][3]) + "   Grade:   " + str(results[count+2][2]), text_color = "#2C2D38", fg_color = "#488AC1", bg_color = "#2C2D38", height = 50,  width = 500)
             btn_test_3.place(x = 150, y = 360)      
             btn_test_4 = customtkinter.CTkButton(root, text = "Student:     " + str(results[count+3][1]) + "   Test:   " + str(results[count+3][3]) + "   Grade:   " + str(results[count+3][2]), text_color = "#2C2D38", fg_color = "#488AC1", bg_color = "#2C2D38", height = 50, width = 500)
             btn_test_4.place(x = 150, y = 440)
             btn_test_5 = customtkinter.CTkButton(root, text = "Student:     " + str(results[count+4][1]) + "   Test:   " + str(results[count+4][3]) + "   Grade:   " + str(results[count+4][2]),  text_color = "#2C2D38", fg_color = "#488AC1", bg_color = "#2C2D38", height = 50, width = 500)
             btn_test_5.place(x = 150, y = 520)
             all_buttons_test.append(btn_test_1)
             all_buttons_test.append(btn_test_2)
             all_buttons_test.append(btn_test_3)
             all_buttons_test.append(btn_test_4)
             all_buttons_test.append(btn_test_5)
        else:
            if len_rest == 0:
                pass
            elif len_rest == 1:
                btn = customtkinter.CTkButton(root, text = "Student:   " + str(results[0][1]) + "   Test:   " + str(results[0][3]) + "   Grade:   " + str(results[0][2]),  text_color = "#2C2D38", fg_color = "#488AC1", bg_color = "#2C2D38", height = 50, width = 500)
                btn.place(x = 150, y = 200) 
                all_buttons_test.append(btn)
            elif len_rest == 2:
                btn1 = customtkinter.CTkButton(root, text = "Student:   " + str(results[0][1]) + "   Test:   " + str(results[0][3]) + "   Grade:   " + str(results[0][2]), text_color = "#2C2D38", fg_color = "#488AC1", bg_color = "#2C2D38", height = 50, width = 500)
                btn1.place(x = 150, y = 200) 
                btn2 = customtkinter.CTkButton(root, text = "Student:   " + str(results[1][1]) + "   Test:   " + str(results[1][3]) + "   Grade:   " + str(results[1][2]), text_color = "#2C2D38", fg_color = "#488AC1", bg_color = "#2C2D38", height = 50, width = 500)
                btn2.place(x = 150, y = 280) 
                all_buttons_test.append(btn1)
                all_buttons_test.append(btn2)
            elif len_rest == 3:
                btn1 = customtkinter.CTkButton(root, text = "Student:   " + str(results[0][1]) + "   Test:   " + str(results[0][3]) + "   Grade:   " + str(results[0][2]), text_color = "#2C2D38", fg_color = "#488AC1", bg_color = "#2C2D38", height = 50, width = 500)
                btn1.place(x = 150, y = 200) 
                btn2 = customtkinter.CTkButton(root, text = "Student:   " + str(results[1][1]) + "   Test:   " + str(results[1][3]) + "   Grade:   " + str(results[1][2]), text_color = "#2C2D38", fg_color = "#488AC1", bg_color = "#2C2D38", height = 50, width = 500)
                btn2.place(x = 150, y = 280) 
                btn3 = customtkinter.CTkButton(root, text = "Student:   " + str(results[2][1]) + "   Test:   " + str(results[2][3]) + "   Grade:   " + str(results[2][2]), text_color = "#2C2D38", fg_color = "#488AC1", bg_color = "#2C2D38", height = 50, width = 500)
                btn3.place(x = 150, y = 360) 
                all_buttons_test.append(btn1)
                all_buttons_test.append(btn2)
                all_buttons_test.append(btn3)
            elif len_rest == 4:
                btn1 = customtkinter.CTkButton(root, text = "Student:   " + str(results[0][1]) + "   Test:   " + str(results[0][3]) + "   Grade:   " + str(results[0][2]), text_color = "#2C2D38", fg_color = "#488AC1", bg_color = "#2C2D38", height = 50, width = 500)
                btn1.place(x = 150, y = 200) 
                btn2 = customtkinter.CTkButton(root, text = "Student:   " + str(results[1][1]) + "   Test:   " + str(results[1][3]) + "   Grade:   " + str(results[1][2]), text_color = "#2C2D38", fg_color = "#488AC1", bg_color = "#2C2D38", height = 50, width = 500)
                btn2.place(x = 150, y = 280) 
                btn3 = customtkinter.CTkButton(root, text = "Student:   " + str(results[2][1]) + "   Test:   " + str(results[2][3]) + "   Grade:   " + str(results[2][2]), text_color = "#2C2D38", fg_color = "#488AC1", bg_color = "#2C2D38", height = 50, width = 500)
                btn3.place(x = 150, y = 360) 
                btn4 = customtkinter.CTkButton(root, text = "Student:   " + str(results[3][1]) + "   Test:   " + str(results[3][3]) + "   Grade:   " + str(results[3][2]), text_color = "#2C2D38", fg_color = "#488AC1", bg_color = "#2C2D38", height = 50, width = 500)
                btn4.place(x = 150, y = 200) 
                all_buttons_test.append(btn1)
                all_buttons_test.append(btn2)
                all_buttons_test.append(btn3)
                all_buttons_test.append(btn4)
                
                




        if i < len_pagini:
             btn_next_text_page = customtkinter.CTkButton(root, text = "Next",  text_color = "#2C2D38",fg_color = "#488AC1", bg_color = "#2C2D38", command = lambda:  self.print_all_results(btns_to_destroy_back, results, all_buttons_test, count+5, i+1, btn_test_1, btn_test_2, btn_test_3, btn_test_4, btn_test_5, btn_next_text_page,  label_tests_view, label_tests_filter), height = 60, width = 60)
             btn_next_text_page.place(x = 670, y = 570)
             all_buttons_test.append(btn_next_text_page)
        elif len_pagini != 0 and len_rest != 0:
             btn_page_rest_tests = customtkinter.CTkButton(root, text = "Next",  text_color = "#2C2D38", fg_color = "#488AC1", bg_color = "#2C2D38", command = lambda:  self.print_rest_results(btns_to_destroy_back, results, btn_page_rest_tests, all_buttons_test, len_rest, btn_test_1, btn_test_2, btn_test_3, btn_test_4, btn_test_5, label_tests_view, label_tests_filter), height = 60, width = 60)
             btn_page_rest_tests.place(x = 670, y = 570)
             all_buttons_test.append(btn_page_rest_tests)
    def print_rest_results(self, btns_to_destroy_back, results, btn_page_rest_tests, all_buttons_test, len_rest, btn_test_1, btn_test_2, btn_test_3, btn_test_4, btn_test_5, label_tests_view, label_tests_filter):
        if btn_test_1:
            btn_test_1.destroy()        
        if btn_test_2:
            btn_test_2.destroy()       
        if btn_test_3:
            btn_test_3.destroy()      
        if btn_test_4:
            btn_test_4.destroy()        
        if btn_test_5:
            btn_test_5.destroy()   
        if btn_page_rest_tests:
            btn_page_rest_tests.destroy()
            if len_rest == 0:
                pass
            elif len_rest == 1:
                btn = customtkinter.CTkButton(root, text = "Student:   " + str(results[len(results) - len_rest][1]) + "   Test:   " + str(results[len(results) - len_rest][3]) + "   Grade:   " +  str(results[len(results) - len_rest][2]),  text_color = "#2C2D38", fg_color = "#488AC1", bg_color = "#2C2D38", height = 50, width = 500)
                btn.place(x = 150, y = 200) 
                all_buttons_test.append(btn)
            elif len_rest == 2:
                btn1 = customtkinter.CTkButton(root, text = "Student:   " + str(results[len(results) - len_rest][1]) + "   Test:   " + str(results[len(results) - len_rest][3]) + "   Grade:   " +  str(results[len(results) - len_rest][2]), text_color = "#2C2D38", fg_color = "#488AC1", bg_color = "#2C2D38", height = 50, width = 500)
                btn1.place(x = 150, y = 200) 
                btn2 = customtkinter.CTkButton(root, text = "Student:   " + str(results[len(results) - len_rest+1][1]) + "   Test:   " + str(results[len(results) - len_rest+1][3]) + "   Grade:   " +  str(results[len(results) - len_rest+1][2]), text_color = "#2C2D38", fg_color = "#488AC1", bg_color = "#2C2D38", height = 50, width = 500)
                btn2.place(x = 150, y = 280) 
                all_buttons_test.append(btn1)
                all_buttons_test.append(btn2)
            elif len_rest == 3:
                btn1 = customtkinter.CTkButton(root, text = "Student:   " + str(results[len(results) - len_rest][1]) + "   Test:   " + str(results[len(results) - len_rest][3]) + "   Grade:   " +  str(results[len(results) - len_rest][2]), text_color = "#2C2D38", fg_color = "#488AC1", bg_color = "#2C2D38", height = 50, width = 500)
                btn1.place(x = 150, y = 200) 
                btn2 = customtkinter.CTkButton(root, text = "Student:   " + str(results[len(results) - len_rest+1][1]) + "   Test:   " + str(results[len(results) - len_rest+1][3]) + "   Grade:   " +  str(results[len(results) - len_rest+1][2]), text_color = "#2C2D38", fg_color = "#488AC1", bg_color = "#2C2D38", height = 50, width = 500)
                btn2.place(x = 150, y = 280)  
                btn3 = customtkinter.CTkButton(root, text = "Student:   " + str(results[len(results) - len_rest+2][1]) + "   Test:   " + str(results[len(results) - len_rest+2][3]) + "   Grade:   " +  str(results[len(results) - len_rest+2][2]), text_color = "#2C2D38", fg_color = "#488AC1", bg_color = "#2C2D38", height = 50, width = 500)
                btn3.place(x = 150, y = 360) 
                all_buttons_test.append(btn1)
                all_buttons_test.append(btn2)
                all_buttons_test.append(btn3)
            elif len_rest == 4:
                btn1 = customtkinter.CTkButton(root, text = "Student:   " + str(results[len(results) - len_rest][1]) + "   Test:   " + str(results[len(results) - len_rest][3]) + "   Grade:   " +  str(results[len(results) - len_rest][2]), text_color = "#2C2D38", fg_color = "#488AC1", bg_color = "#2C2D38", height = 50, width = 500)
                btn1.place(x = 150, y = 200) 
                btn2 = customtkinter.CTkButton(root, text = "Student:   " + str(results[len(results) - len_rest+1][1]) + "   Test:   " + str(results[len(results) - len_rest+1][3]) + "   Grade:   " +  str(results[len(results) - len_rest+1][2]), text_color = "#2C2D38", fg_color = "#488AC1", bg_color = "#2C2D38", height = 50, width = 500)
                btn2.place(x = 150, y = 280)  
                btn3 = customtkinter.CTkButton(root, text = "Student:   " + str(results[len(results) - len_rest+2][1]) + "   Test:   " + str(results[len(results) - len_rest+2][3]) + "   Grade:   " +  str(results[len(results) - len_rest+2][2]), text_color = "#2C2D38", fg_color = "#488AC1", bg_color = "#2C2D38", height = 50, width = 500)
                btn3.place(x = 150, y = 360)  
                btn4 = customtkinter.CTkButton(root, text = "Student:   " + str(results[len(results) - len_rest+3][1]) + "   Test:   " + str(results[len(results) - len_rest+3][3]) + "   Grade:   " +  str(results[len(results) - len_rest+3][2]), text_color = "#2C2D38", fg_color = "#488AC1", bg_color = "#2C2D38", height = 50, width = 500)
                btn4.place(x = 150, y = 440) 
                all_buttons_test.append(btn1)
                all_buttons_test.append(btn2)
                all_buttons_test.append(btn3)
                all_buttons_test.append(btn4)
                
    def sort_student_by_mark(self, crescator, written_username, btns_to_destroy_back, all_buttons_test, btn_test_1, btn_test_2, btn_test_3, btn_test_4, btn_test_5, btn_next_text_page, label_tests_view, label_tests_sort):
        global is_prof_global
        if is_prof_global == 1:
            results = self.db.afiseaza_rezultate_prof()
        elif is_prof_global == 0:
            results = self.db.afiseaza_rezultate_student(written_username)
        for button in all_buttons_test:
            if button:
                button.destroy()
                
        print(results)
        new_results = []
        for row in results:
            element_0 = row[0]
            element_1 = row[1]
            element_2 = row[2]
            element_3 = row[3]

            tuplu_modificat = (element_2, element_1, element_0, element_3)
            
            new_results.append(tuplu_modificat)
        print(new_results)

        if crescator == 1:
           results = self.sort.quick_sort_cresc(new_results)
        elif crescator == 0:
           results = self.sort.quick_sort_descresc(new_results)
        print(results)

        sorted_tuple = []
        for row in results:
            element_0 = row[0]
            element_1 = row[1]
            element_2 = row[2]
            element_3 = row[3] 
            tuplu_modificat = (element_2, element_1, element_0, element_3)
            sorted_tuple.append(tuplu_modificat)
        results = sorted_tuple
        
        print(results)
        self.print_all_results(btns_to_destroy_back, results,  all_buttons_test, 0, 1, btn_test_1, btn_test_2, btn_test_3, btn_test_4, btn_test_5, btn_next_text_page, label_tests_view, label_tests_sort)
    def sort_student_by_test_name(self, crescator, written_username, btns_to_destroy_back, all_buttons_test, btn_test_1, btn_test_2, btn_test_3, btn_test_4, btn_test_5, btn_next_text_page, label_tests_view, label_tests_sort):
        global is_prof_global
        if is_prof_global == 1:
            results = self.db.afiseaza_rezultate_prof()
        elif is_prof_global == 0:
            results = self.db.afiseaza_rezultate_student(written_username)
        for button in all_buttons_test:
            if button:
                button.destroy()
        print(results)
        new_results = []
        for row in results:
            element_0 = row[0]
            element_1 = row[1]
            element_2 = row[2]
            element_3 = row[3]

            tuplu_modificat = (element_3, element_1, element_2, element_0)
            
            new_results.append(tuplu_modificat)
        print(new_results)

        if crescator == 1:
           results = self.sort.quick_sort_cresc(new_results)
        elif crescator == 0:
           results = self.sort.quick_sort_descresc(new_results)
        print(results)

        sorted_tuple = []
        for row in results:
            element_0 = row[0]
            element_1 = row[1]
            element_2 = row[2]
            element_3 = row[3] 
            tuplu_modificat = (element_3, element_1, element_2, element_0)
            sorted_tuple.append(tuplu_modificat)
        results = sorted_tuple
        
        print(results)
        self.print_all_results(btns_to_destroy_back, results,  all_buttons_test, 0, 1, btn_test_1, btn_test_2, btn_test_3, btn_test_4, btn_test_5, btn_next_text_page, label_tests_view, label_tests_sort)   
    def sort_student_by_student_name(self, crescator, written_username, btns_to_destroy_back, all_buttons_test, btn_test_1, btn_test_2, btn_test_3, btn_test_4, btn_test_5, btn_next_text_page, label_tests_view, label_tests_sort):
        global is_prof_global
        if is_prof_global == 1:
            results = self.db.afiseaza_rezultate_prof()
        elif is_prof_global == 0:
            results = self.db.afiseaza_rezultate_student(written_username)
        for button in all_buttons_test:
            if button:
                button.destroy()
        print(results)
        new_results = []
        for row in results:
            element_0 = row[0]
            element_1 = row[1]
            element_2 = row[2]
            element_3 = row[3]

            tuplu_modificat = (element_1, element_0, element_2, element_3)
            
            new_results.append(tuplu_modificat)
        print(new_results)

        if crescator == 1:
           results = self.sort.quick_sort_cresc(new_results)
        elif crescator == 0:
           results = self.sort.quick_sort_descresc(new_results)
        print(results)

        sorted_tuple = []
        for row in results:
            element_0 = row[0]
            element_1 = row[1]
            element_2 = row[2]
            element_3 = row[3] 
            tuplu_modificat = (element_1, element_0, element_2, element_3)
            sorted_tuple.append(tuplu_modificat)
        results = sorted_tuple
        
        print(results)
        self.print_all_results(btns_to_destroy_back, results,  all_buttons_test, 0, 1, btn_test_1, btn_test_2, btn_test_3, btn_test_4, btn_test_5, btn_next_text_page, label_tests_view, label_tests_sort)   
        


app = Aplicatie()
    
app.create_pag_1(root)

root.mainloop()
