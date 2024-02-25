import tkinter as tk
from tkinter import messagebox

class POSApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Point of Sale")
        self.master.attributes("-fullscreen", True)  # Imposta la finestra a tutto schermo
        
        self.total_price = 0
        self.items = []

        # Creazione dei widget
        self.label_total = tk.Label(master, text="Total: $0.00", font=("Arial", 20))
        self.label_total.pack()

        self.entry_item = tk.Entry(master, font=("Arial", 16))
        self.entry_item.pack()

        self.entry_price = tk.Entry(master, font=("Arial", 16))
        self.entry_price.pack()

        self.button_add_item = tk.Button(master, text="Add Item", command=self.add_item, font=("Arial", 16))
        self.button_add_item.pack()

        # Pulsanti sulla destra
        self.button_actions = tk.Button(master, text="Azioni", command=self.open_actions_window, font=("Arial", 16))
        self.button_actions.pack(side=tk.RIGHT, padx=10, pady=10)

        self.button_orders = tk.Button(master, text="Ordini", command=self.open_orders_window, font=("Arial", 16))
        self.button_orders.pack(side=tk.RIGHT, padx=10, pady=10)

        self.button_discounts = tk.Button(master, text="Sconti", command=self.open_discounts_window, font=("Arial", 16))
        self.button_discounts.pack(side=tk.RIGHT, padx=10, pady=10)

        self.button_products = tk.Button(master, text="Prodotti", command=self.open_products_window, font=("Arial", 16))
        self.button_products.pack(side=tk.RIGHT, padx=10, pady=10)

    def add_item(self):
        item_name = self.entry_item.get()
        try:
            item_price = float(self.entry_price.get())
        except ValueError:
            messagebox.showerror("Error", "Price must be a number")
            return

        self.items.append((item_name, item_price))
        self.total_price += item_price

        self.label_total.config(text="Total: ${:.2f}".format(self.total_price))

        self.entry_item.delete(0, tk.END)
        self.entry_price.delete(0, tk.END)

    def open_actions_window(self):
        actions_window = tk.Toplevel(self.master)
        actions_window.title("Azioni")
        # Aggiungi contenuto alla finestra delle azioni qui...

    def open_orders_window(self):
        orders_window = tk.Toplevel(self.master)
        orders_window.title("Ordini")
        # Aggiungi contenuto alla finestra degli ordini qui...

    def open_discounts_window(self):
        discounts_window = tk.Toplevel(self.master)
        discounts_window.title("Sconti")
        # Aggiungi contenuto alla finestra degli sconti qui...

    def open_products_window(self):
        products_window = tk.Toplevel(self.master)
        products_window.title("Prodotti")
        # Aggiungi contenuto alla finestra dei prodotti qui...

def main():
    root = tk.Tk()
    app = POSApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
