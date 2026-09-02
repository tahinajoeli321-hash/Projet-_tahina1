import tkinter as tk
from tkinter import messagebox

def inscrire():
    n = nom.get()
    c = classe.get()
    note = notes.get()

    if n and c and note:
        liste.insert(tk.END, f"{n} | {c} | {note}")
        nom.delete(0, tk.END)
        classe.delete(0, tk.END)
        notes.delete(0, tk.END)
    else:
        messagebox.showwarning("Erreur", "Remplir tous les champs")

f = tk.Tk()
f.title("Inscription scolaire")
f.geometry("400x400")

tk.Label(f, text="INSCRIPTION SCOLAIRE").pack(pady=15)

tk.Label(f, text="Nom").pack()
nom = tk.Entry(f)
nom.pack()

tk.Label(f, text="Classe").pack()
classe = tk.Entry(f)
classe.pack()

tk.Label(f, text="Note").pack()
notes = tk.Entry(f)
notes.pack()

tk.Button(f, text="Inscrire", command=inscrire).pack(pady=15)

liste = tk.Listbox(f, width=45)
liste.pack()

f.mainloop()