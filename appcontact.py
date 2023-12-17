from tkinter import *
from tkinter import messagebox, ttk
import tkinter as tk
from tkcalendar import DateEntry
import pymysql
class Contact:
        def __init__(self, root, parent= None):
            self.root = root
            self.root.title("AppContact")
            self.root.geometry('1920x1080+0+0')
            
            self.compteur1 = 0
            self.compteur =0
            frame1 = Frame(self.root, bg="grey")
            frame1.place(x=5, y=10, width=630, height=800)
                      
            title= Label(frame1, text="Contact", font=("time new roman", 20, "bold"), bg="grey", fg= "green").place(x=50, y= 30) 
            
            labelnom= Label(frame1, text="NOM", font=("time new roman", 15, "bold"),bg="grey" ,fg='black').place(x=50, y=100)
            
            self.entryNom_enr= Entry(frame1, text='NOM',font=("time new roman", 15, "bold"), bg='lightgrey')
            self.entryNom_enr.place(x=50, y= 130, width=250)
            
            
            labelprenom= Label(frame1, text="PRENOM", font=("time new roman", 15, "bold"),bg="grey" ,fg='black').place(x=370, y=100)
            self.entryPrenom_enr= Entry(frame1, text='PRENOM',font=("time new roman", 15, "bold"), bg='lightgrey')
            self.entryPrenom_enr.place(x=370, y= 130, width=250)
            
            labelprenom= Label(frame1, text="EMAIL", font=("time new roman", 15, "bold"),bg="grey" ,fg='black').place(x=50, y=200)
            self.entryEmail_enr= Entry(frame1, text='EMAIL',font=("time new roman", 15, "bold"), bg='lightgrey')
            self.entryEmail_enr.place(x=50, y= 230, width=250)
            
            labedate= Label(frame1, text="DATE", font=("time new roman", 15, "bold"),bg="grey" ,fg='black').place(x=370, y=200)
            
            self.entryDate_enr= DateEntry(frame1, text='DATE',font=("time new roman", 15, "bold"), bg='lightgrey', date_pattern="yyyy-mm-dd")
            self.entryDate_enr.delete(0, 'end')
            self.entryDate_enr.place(x=370, y= 230, width=250)
            
            
            labelcontact= Label(frame1, text="CONTACT", font=("time new roman", 15, "bold"),bg="grey" ,fg='black').place(x=50, y=300)
            self.entryContact_enr= Entry(frame1, text='CONTACT',font=("time new roman", 15, "bold"), bg='lightgrey' )
            self.entryContact_enr.place(x=50, y= 330, width=250)  
        

            self.btn_enr = Button(frame1, text="ENREGISTRER", font=("time new roman", 15, "bold"), command=self.validation)
            self.btn_enr.place(x=250, y=400)
            
            
            
            self.supp = Button(text="SUPPRIMER", font=("time new roman", 15, "bold"), border=0.0, command= self.supprimer)
            self.supp.place(x=640, y=50)
            
            
            self.modifier = Button(text="MODIFIER", font=("time new roman", 15, "bold"), bg="red4", activebackground='red4', border=0.0, command= self.modifier)
          
            self.modifier.place(x=800, y=50)
            
            self.rechercher= Button(text="RECHERCHER", font=("time new roman", 15, "bold"), border=0.0, command= self.Rechercher)
            self.rechercher.place(x=1430, y=50)
            
            self.rec= Entry(text='RECHERCHE',font=("time new roman", 15, "bold") )
            self.rec.place(x=1200, y=55, height=35)
            self.rec.delete(0, END)
            nom= self.entryNom_enr.get()
            prenom=self.entryPrenom_enr.get()
            email= self.entryEmail_enr.get()
            date=self.entryDate_enr.get_date()
            cont=self.entryContact_enr.get()
           



            self.treeview= ttk.Treeview(self.root)
            self.treeview.place(x= 640, y=100, width=950, height=710)
            
            self.treeview["columns"]=("NOM","PRENOM", "EMAIL", "DATE", "CONTACT") 
      
            self.treeview= ttk.Treeview(self.root)
            self.treeview.place(x= 640, y=100, width=950, height=710)
        
            self.treeview["columns"]=("NOM","PRENOM", "EMAIL", "DATE", "CONTACT")
            self.treeview.column("#0", width= 0 , stretch=NO)
            self.treeview.column("NOM", width= 125 , minwidth= 25)
            self.treeview.column("PRENOM", anchor=W, width= 100)
            self.treeview.column("EMAIL", anchor= W ,width= 120)
            self.treeview.column("DATE", anchor=W ,width= 90)
            self.treeview.column("CONTACT", anchor=W ,width= 100)
            
            
            self.treeview.heading("#0", text="", anchor= CENTER)
            self.treeview.heading("NOM", text="NOM", anchor= W)
            self.treeview.heading("PRENOM", text="PRENOM", anchor= W)
            self.treeview.heading("EMAIL", text="EMAIL", anchor= W)
            self.treeview.heading("DATE", text="DATE", anchor= W)
            self.treeview.heading("CONTACT", text="CONTACT", anchor= W)



            self.display_data()
        def display_data(self):
            conn = pymysql.connect(host="localhost",user="root",  password="root", database="appcontact")
            cur= conn.cursor()
            cur.execute("SELECT * FROM contacts")  # Remplacez ma_table par le nom de votre table
            rows = cur.fetchall()
            for row in rows:
               self.treeview.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4]))   
            conn.close()
            
#------------------------------------------------------------------------PERMET D'AFFICHER TOUT LES CONTACTS DE LA BD A CHAQUE LANCEMENT DE L4
        def verification(self):
        
            # Vérifie si tous les champs obligatoires sont remplis
       

            # Vérifie si les champs contiennent des valeurs valides
            if not isinstance(self.entryContact_enr.get(), int):
                messagebox.showerror("ERREUR", "Vous avez entrer un contact invalide")
                return
            if not isinstance(self.entryPrenom_enr.get(), str):
                messagebox.showerror("ERREUR", "Vous avez entrer des caracteres incorrects dans le champ PRENOM")
                return
            if not isinstance(self.entryNom_enr.get(), str):
                messagebox.showerror("ERREUR", "Vous avez entrer des caracteres incorrects dans le champ NOM")
                return
            if not isinstance(self.entryEmail_enr.get(), str):
                messagebox.showerror("ERREUR", "Vous avez entrer des caracteres incorrects dans le champ EMAIL")
                return
            
        def renitialisation(self):
                self.entryNom_enr.delete(0, END)
                self.entryPrenom_enr.delete(0, END)
                self.entryEmail_enr.delete(0, END)
                self.entryDate_enr.delete(0, END)
                self.entryContact_enr.delete(0, END) 
            
        def validate(self):
            # Vérifie que tous les champs requis sont remplis
            if (not self.entryNom_enr.get() or
                not self.entryPrenom_enr.get() or
                not self.entryEmail_enr.get() or
                not self.entryDate_enr.get_date() or
                not self.entryContact_enr.get()):
                messagebox.showerror("ERREUR", "Tous les champs doivent être remplis", parent=self.root)
                self.verification()
                return False
            return True
  
        def validation(self):
           if not self.validate():  
                return  
                 # Vérifie si les champs contiennent des valeurs valides
                if not isinstance(self.entryContact_enr.get(), int):
                    messagebox.showerror("ERREUR", "Vous avez entrer un contact invalide")
                    return
                if not isinstance(self.entryPrenom_enr.get(), str):
                    messagebox.showerror("ERREUR", "Vous avez entrer des caracteres incorrects dans le champ PRENOM")
                    return
                if not isinstance(self.entryNom_enr.get(), str):
                    messagebox.showerror("ERREUR", "Vous avez entrer des caracteres incorrects dans le champ NOM")
                    return
                if not isinstance(self.entryEmail_enr.get(), str):
                    messagebox.showerror("ERREUR", "Vous avez entrer des caracteres incorrects dans le champ EMAIL")
                    return

           try:
                conn = pymysql.connect(
                host="localhost",
                user="root",
                password="root",)
               # Fixed typo in the database name )
                cur = conn.cursor()
                cur.execute("CREATE DATABASE IF NOT EXISTS APPCONTACT")
                cur.execute("USE APPCONTACT")
                cur.execute("CREATE TABLE IF NOT EXISTS CONTACTS (Nom VARCHAR(50) NOT NULL, Prenom VARCHAR(50) NOT NULL, Adresse_email VARCHAR(50) NOT NULL, date_enr DATE NOT NULL, Contact VARCHAR(50) )")  # Added missing parenthesis and fixed case for table name
               # cur.execute("CREATE TABLE IF NOT EXISTS CONTACTS ( id INT AUTO_INCREMENT PRIMARY KEY ,Nom VARCHAR(50) NOT NULL, Prenom VARCHAR(50) NOT NULL, Adresse_email VARCHAR(50) NOT NULL, date_enr DATE NOT NULL, Contact VARCHAR(50) )")  # Added missing parenthesis and fixed case for table name
                cur.execute("SELECT * FROM CONTACTS WHERE  Adresse_email= %s", self.entryEmail_enr.get())  # Fixed table name case
                verification = cur.fetchone()
                
                if verification is not None:  # Changed comparison operator to 'is not'
                    messagebox.showerror("ERREUR", "Cet email existe déjà", parent=self.root)  # Fixed typo and translated the message
                else:
                    cur.execute("INSERT INTO CONTACTS (Nom, Prenom, Adresse_email, date_enr, Contact) VALUES (%s, %s, %s, %s, %s)",
                            (self.entryNom_enr.get(),
                             self.entryPrenom_enr.get(),
                             self.entryEmail_enr.get(),  # Fixed typo in the method name
                             self.entryDate_enr.get_date(),
                             self.entryContact_enr.get()  
                            ))
                
                self.compteur +=1
                #self.treeview.insert(parent='', index='end', iid=self.compteur, text="", values=(self.entryNom_enr.get(), self.entryPrenom_enr.get(), self.entryEmail_enr.get(), self.entryDate_enr.get_date(), self.entryContact_enr.get()))
                self.treeview.insert(parent="", index='end', iid=self.compteur, text="", values=(self.entryNom_enr.get(), self.entryPrenom_enr.get(), self.entryEmail_enr.get(), self.entryDate_enr.get_date(), self.entryContact_enr.get()))
                self.renitialisation()  

               

                conn.commit()
                conn.close()
               
            #---------------------------------------------------------------inserer dans la treeview---
          
           except pymysql.Error as es:  # Specified the exception type
                messagebox.showerror('ERREUR', f"Erreur de connexion: {str(es)}", parent=self.root)
                
   
                
        def supprimer(self):
            ids_delete = []
            x = self.treeview.selection()
    
            if not x:
                messagebox.showinfo("INFO", "Veuillez sélectionner un élément à supprimer")
                return

            for record in x:
                values = self.treeview.item(record, 'values')
                ids_delete.append(values)
                print(ids_delete)
                self.treeview.delete(record)

            # Use the IN operator to delete all the records in a single query
            placeholders = ','.join(['%s'] * len(ids_delete))
            query = f"DELETE FROM contacts WHERE (Nom, Prenom, Adresse_email, date_enr, Contact) IN ({placeholders})"

            conn = pymysql.connect(
            host="localhost",
            user="root",
            password="root",
            database="appcontact")
       

            cur = conn.cursor()
            cur.execute(query, tuple(ids_delete))

            messagebox.showinfo("SUCCES", "L'objet a été supprimer avec succes")
            conn.commit()
            conn.close()
        

        
        def Rechercher(self):

            
             search= Toplevel(self.root)
             search.title("Resultat de la recherche")
             search.minsize(1080,1080)
             self.treeview= ttk.Treeview(search)

             self.treeview.place(x= 60, y=60, width=950, height=710)
                 # for recod in self.treeview.get_children():
                #     self.treeview.delete(recod)
             self.treeview["columns"]=("NOM","PRENOM", "EMAIL", "DATE", "CONTACT")
                
             self.treeview["columns"]=("NOM","PRENOM", "EMAIL", "DATE", "CONTACT")
             self.treeview.column("#0", width= 0 , stretch=NO)
             self.treeview.column("NOM", width= 125 , minwidth= 25)
             self.treeview.column("PRENOM", anchor=W, width= 100)
             self.treeview.column("EMAIL", anchor= W ,width= 120)
             self.treeview.column("DATE", anchor=W ,width= 90)
             self.treeview.column("CONTACT", anchor=W ,width= 100)
                
                
             self.treeview.heading("#0", text="", anchor= CENTER)
             self.treeview.heading("NOM", text="NOM", anchor= W)
             self.treeview.heading("PRENOM", text="PRENOM", anchor= W)
             self.treeview.heading("EMAIL", text="EMAIL", anchor= W)
             self.treeview.heading("DATE", text="DATE", anchor= W)
             self.treeview.heading("CONTACT", text="CONTACT", anchor= W)
            
    
                
         
            
             try:
                conn = pymysql.connect(host="localhost",user="root",  password="root", database="appcontact")
                cur= conn.cursor()
                
                query= "SELECT * FROM contacts WHERE Nom= %s"
                nom =self.rec.get()
                val= ( nom,)
                print(nom)
                cur.execute(query, val)
                result= cur.fetchall()
                self.treeview.delete(*self.treeview.get_children())
                print(result) 
                for row in result:
                    print(row)
                    self.treeview.insert("", index="end", values=row)
              #  self.renitialisation()

             except Exception as e:
               messagebox.showinfo("no found", f"AUCUN RESULTAT TROUVER, {str(e)}")
       
#-------------------------------------------------------------------------FONCTION DE MODIFICATION D'UN CONTACT---------------------------------------------------------------------------------------------------------                      
        def modifier(self):
           # self.treeview= ttk.Treeview(self.root)
            
            self.modifier_window = Toplevel(self.root)
            self.modifier_window.title("Modifier")
            
            self.modifier_window.minsize(720, 1080)
        
            item = self.treeview.selection()[0]
            nom_initial = self.treeview.item(item, "values")[0]
            prenom_initial = self.treeview.item(item, "values")[1]
            email_initial = self.treeview.item(item, "values")[2]
            date_initial = self.treeview.item(item, "values")[3]
            cont_initial = self.treeview.item(item, "values")[4]
                    
            

            
            
            title1= Label( self.modifier_window, text="MODIFICATION", font=("time new roman", 20, "bold"), bg="grey", fg= "green").place(x=50, y= 30) 
            
            labelnom1= Label(self.modifier_window, text="NOM", font=("time new roman", 15, "bold"),bg="grey" ,fg='black').place(x=50, y=100)
            
            self.entryNomModification= Entry(self.modifier_window, text='NOMS',font=("time new roman", 15, "bold"), bg='lightgrey')
            self.entryNomModification.place(x=50, y= 130, width=250)
            
            
            labelprenom1= Label(self.modifier_window, text="PRENOM", font=("time new roman", 15, "bold"),bg="grey" ,fg='black').place(x=370, y=100)
            self.entryPrenomModification= Entry(self.modifier_window, text='PRENOMS',font=("time new roman", 15, "bold"), bg='lightgrey')
            self.entryPrenomModification.place(x=370, y= 130, width=250)
            
            labelprenom1= Label(self.modifier_window, text="EMAIL", font=("time new roman", 15, "bold"),bg="grey" ,fg='black').place(x=50, y=200)
            self.entryEmailModification= Entry( self.modifier_window, text='EMAILS',font=("time new roman", 15, "bold"), bg='lightgrey')
            self.entryEmailModification.place(x=50, y= 230, width=250)
            
            labedate1= Label( self.modifier_window, text="DATE", font=("time new roman", 15, "bold"),bg="grey" ,fg='black').place(x=370, y=200)
            
            self.entryDateModification= DateEntry(self.modifier_window,text="DATES",font=("time new roman", 15, "bold"), bg='lightgrey', date_pattern="yyyy-mm-dd")
            
            self.entryDateModification.place(x=370, y= 230, width=250)
            
            
            labelcontact1= Label( self.modifier_window, text="CONTACTS", font=("time new roman", 15, "bold"),bg="grey" ,fg='black').place(x=50, y=300)
            self.entryContactModification= Entry( self.modifier_window, text='CONTACTS',font=("time new roman", 15, "bold"), bg='lightgrey' )
            self.entryContactModification.place(x=50, y= 330, width=250)  
        

            self.btn = Button(self.modifier_window, text="FACTORISER", font=("time new roman", 15, "bold"), command=lambda: self.enregistrer_modification(item, self.modifier_window))
            self.btn.place(x=250, y=400)
            
            
            
            self.entryNomModification.insert(0, nom_initial)
            self.entryPrenomModification.insert(0, prenom_initial)
            self.entryEmailModification.insert(0, email_initial)
            self.entryDateModification.set_date(date_initial)
            self.entryContactModification.insert(0, cont_initial)
            
            self.modifier_window.resizable(False, False)
       
            
        def enregistrer_modification(self, item, window):
            nom1 = self.entryNomModification.get()
            prenom1 = self.entryPrenomModification.get()
            email1 = self.entryEmailModification.get()
            date1 = self.entryDateModification.get_date()
            cont1 = self.entryContactModification.get()

            conn = None  # Initialisation de la connexion pour être sûr de la fermer dans le bloc finally

            try:
                conn = pymysql.connect(
                    host="localhost",
                    user="root",
                    password="root",
                    database="appcontact")
                cur = conn.cursor()

                cur.execute("UPDATE Contacts SET Nom = %s, Prenom = %s, Adresse_email = %s, date_enr = %s WHERE Contact = %s", (nom1, prenom1, email1, date1, cont1))

                conn.commit()
                self.treeview.item(item, values=(nom1, prenom1, email1, date1, cont1))
                window.destroy()
            except pymysql.Error as e:
              messagebox.showerror("Erreur", f"Erreur lors de l'enregistrement de la modification : {str(e)}")
            finally:
                if conn:
                    conn.close()

#----------------------------------------------------------------------------------
# --FIN DE LA FONCTION DE MODIFICATION D'UN CONTACT----------------------------------------------------------------------------------------------------------------
root = Tk()
contact = Contact(root)
root.mainloop()