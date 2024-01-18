import sqlite3
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Donnes Laics')
root.iconbitmap('c:/Users/admin/Documents/MOB/app/binary.ico')
root.geometry('260x150')

# define submit button
def submit():
    
    conn = sqlite3.connect('c:/Users/admin/Documents/MOB/app/laic.db')
    c = conn.cursor()

    c.execute(f"""
            INSERT INTO {classe} VALUES (
              :visites,
              :imprimes,
              :v_monetaire,
              :p_secourues,
              :h_medicales)""",

              {
                'visites': int(input_P_Secourues.get()),
                'imprimes': int(input_imprimes.get()),     
                'v_monetaire': float(input_V_Monetaire.get()),
                'p_secourues': int(input_P_Secourues.get()),
                'h_medicales': int(input_H_Medicales.get())
              }
              )
    conn.commit()
    conn.close()

    input_visite.delete(0, END)
    input_imprimes.delete(0, END)
    input_V_Monetaire.delete(0, END)
    input_H_Medicales.delete(0, END)
    input_P_Secourues.delete(0, END)


# Defining class_modif button
def class_modif():
    # setting up global variables
    global classe
    global input_visite
    global input_imprimes
    global input_H_Medicales
    global input_V_Monetaire
    global input_P_Secourues

        # Error handling
    if input_classe.get() not in ['1', '3', '2', '4', '5'] :
        label_error = Label(root, text="Il n'y a que 5 classes,\n veuillez entrer un numero \ncompris entre 1 et 5")
        label_error.grid(row=2, column=0, pady=10, columnspan=2)
    
    # setting class number
    if input_classe.get() == '1':
        classe = 'Classe_1'

    if input_classe.get() == '2':
        classe = 'Classe_2'

    if input_classe.get() == '3':
        classe = 'Classe_3'

    if input_classe.get() == '4':
        classe = 'Classe_4'

    if input_classe.get() == '5':
        classe = 'Classe_5'
        

    # creating new windows
    window_cls_1 = Tk()
    window_cls_1.title(f'Edit {classe}')
    window_cls_1.geometry('300x400')

    # creating text label
    label_presentation_1 = Label(window_cls_1, text='Ajouter les donnees')
    label_presentation_1.grid(row=0, column=0, columnspan=3, pady=15, ipadx=100)
    
    label_visite = Label(window_cls_1, text='Vsites')
    label_visite.grid(row=1, column=0)

    label_imprimes = Label(window_cls_1, text='Imprimes distribues')
    label_imprimes.grid(row=2, column=0)

    label_V_Monetaire = Label(window_cls_1, text='Valeur Monetaire')
    label_V_Monetaire.grid(row=3, column=0)

    label_P_Secourues = Label(window_cls_1, text='Personnes Secourues')
    label_P_Secourues.grid(row=4, column=0)

    label_H_Medicales = Label(window_cls_1, text='Heures Medicales')
    label_H_Medicales.grid(row=5, column=0)

    
    # creating text box input
    input_visite = Entry(window_cls_1, width=25)
    input_visite.grid(row=1, column=1, pady=10)

    input_imprimes = Entry(window_cls_1, width=25)
    input_imprimes.grid(row=2, column=1, pady=10)

    input_V_Monetaire = Entry(window_cls_1, width=25)
    input_V_Monetaire.grid(row=3, column=1, pady=10)

    input_P_Secourues = Entry(window_cls_1, width=25)
    input_P_Secourues.grid(row=4, column=1, pady=10)

    input_H_Medicales = Entry(window_cls_1, width=25)
    input_H_Medicales.grid(row=5, column=1, pady=10)


    # creating submit button
    button_submit = Button(window_cls_1, text='ENREGISTRER', command=submit)
    button_submit.grid(row=7, column=0, columnspan=2, ipadx=100, pady=15)


# setting up Label
label_classe = Label(root, text='Numero de classe')
label_classe.grid(row=0, column=0, pady=15)

# setting up entry
input_classe = Entry(root, width=25)
input_classe.grid(row=0, column=1, pady=15)

# setting up buttons
button_class_modif  = Button(root, text='Modifier', command=class_modif)
button_class_modif.grid(row=1, column=0, columnspan=2, ipadx=90)




root.mainloop()