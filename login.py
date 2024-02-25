import tkinter as tk
from tkinter import messagebox

class LoginPage:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        self.master.attributes("-fullscreen", True)  # Imposta la finestra a tutto schermo

        # Etichetta per visualizzare il numero inserito
        self.entry_var = tk.StringVar()
        self.entry_label = tk.Label(master, textvariable=self.entry_var, font=("Arial", 24))
        self.entry_label.pack()

        # Tastierino numerico
        self.keypad_frame = tk.Frame(master)
        self.keypad_frame.pack()

        # Crea i pulsanti numerici
        for i in range(1, 10):
            button = tk.Button(self.keypad_frame, text=str(i), font=("Arial", 20),
                               command=lambda num=i: self.add_digit(num))
            button.grid(row=(i-1)//3, column=(i-1)%3, padx=10, pady=10)

        # Pulsante "<" per cancellare l'ultimo carattere
        button_backspace = tk.Button(self.keypad_frame, text="<", font=("Arial", 20),
                                     command=self.backspace)
        button_backspace.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Pulsante per effettuare il login
        button_login = tk.Button(self.keypad_frame, text="Login", font=("Arial", 20),
                                 command=self.login)
        button_login.grid(row=3, column=2, padx=10, pady=10)

        # Password di accesso
        self.password = "1234"  # Modifica la password secondo necessità
        self.input_string = ""

    def add_digit(self, digit):
        self.input_string += str(digit)
        self.update_entry()

    def backspace(self):
        self.input_string = self.input_string[:-1]
        self.update_entry()

    def update_entry(self):
        self.entry_var.set(self.input_string)

    def login(self):
        if self.input_string == self.password:
            messagebox.showinfo("Success", "Login successful!")
            self.master.destroy()  # Chiude la finestra di login se il login è riuscito
        else:
            messagebox.showerror("Error", "Incorrect password")
            self.input_string = ""  # Resetta l'input
            self.update_entry()

def main():
    root = tk.Tk()
    login_page = LoginPage(root)
    root.mainloop()

if __name__ == "__main__":
    main()
