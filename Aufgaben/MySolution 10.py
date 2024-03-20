import tkinter as tk
import mysql.connector

from res.classes.bankaccount import BankAccount

class component_creator:

    def getButton(dependency, button_text):
        button = tk.Button(dependency, text=button_text)
        button.config(bg="white",fg="blue")
        button.place(width = 250, height = 50, anchor = "w", relx = 0.1)
        return button
    
    def getSubWindow(dependency):
        window = tk.Toplevel(dependency)
        window.config(bg="gray")
        return window
    
    def getLabel(dependency, label_text):
        label = tk.Label(dependency, text=label_text, width=15, height=1)
        label.config(bg="orange")
        return label
    
    def getTextbox(dependency ):
        text = tk.Text(dependency, width=15, height=1)
        return text
    
    def getEntry(dependency):
        entry = tk.Entry(dependency, width=15)
        return entry

root = tk.Tk()
root.geometry("250x150")
root.title("Bank-Account")
root.config(bg="gray")
root.resizable(0,0)
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)


def create_new_account_window():
    new_account_window = component_creator.getSubWindow(root)
    new_account_window.title("New account")
    new_account_window.geometry("300x200")
    new_account_window.resizable(0,0)
    new_account_window.columnconfigure(0,weight=3)
    new_account_window.columnconfigure(1,weight=3)
    return new_account_window

def on_button_new_account_click():
    window = create_new_account_window()
    
    first_name_label = component_creator.getLabel(window, "First Name:")
    first_name_label.grid(column=0, row=0, padx=5, pady=5)
    first_name_text = component_creator.getEntry(window)
    first_name_text.grid(column=1, row=0, padx=5, pady=5)

    last_name_label = component_creator.getLabel(window, "Last Name:")
    last_name_label.grid(column=0, row=1, padx=5, pady=5)
    last_name_text = component_creator.getEntry(window)
    last_name_text.grid(column=1, row=1, padx=5, pady=5)

    initial_deposit_label = component_creator.getLabel(window, "Initial Deposit:")
    initial_deposit_label.grid(column=0, row=2, padx=5, pady=5)
    initial_deposit_text = component_creator.getEntry(window)
    initial_deposit_text.grid(column=1,row=2,padx=5,pady=5)

    status_label = component_creator.getLabel(window, " ")
    status_label.grid(column=0, row=5, padx=5, pady=5)

    submit_button = component_creator.getButton(window,"Confirm")
    submit_button.grid(column=1,row=5)
    submit_button.config(command=on_submit_button_click)

    global run_create
    def run_create():
        firstName = first_name_text.get()
        lastName = last_name_text.get()
        initialDeposit = initial_deposit_text.get()
        new_bank_account = BankAccount(firstName, lastName, initialDeposit)


def on_submit_button_click():
    run_create()



def create_deposit_window():
    window = component_creator.getSubWindow(root)
    window.title("Deposit")
    window.geometry("300x200")
    window.resizable(0,0)
    window.columnconfigure(0,weight=3)
    window.columnconfigure(1,weight=3)
    return window

def on_button_deposit_click():
    window = create_deposit_window()

    id_label = component_creator.getLabel(window, "Please enter your id:")
    id_label.grid(column=0, row=0)
    id_entry = component_creator.getEntry(window)
    id_entry.grid(column=1, row=0)

    value_label = component_creator.getLabel(window, "Your deposit:")
    value_label.grid(column=0, row=1)
    value_entry = component_creator.getEntry(window)
    value_entry.grid(column=1, row=1)

    output_text = component_creator.getLabel(window,"")
    output_text.grid(column=0,row=2)

    submit_deposit_button = component_creator.getButton(window, "Confirm")
    submit_deposit_button.config(command=on_deposit_submit_click)
    submit_deposit_button.grid(column=1, row=2)

    global deposit
    def deposit():
        id = id_entry.get()
        bankaccount = BankAccount.getAccountByID(id)
        if (bankaccount == None):
            output_text.config(text="ID not found")
        else:
            output_text.config(text="ID found")
            try:
                amount = float(value_entry.get())
            except:
                amount = 0
                
            message = bankaccount.deposit(amount)
            output_text.config(text=message)

def on_deposit_submit_click():
    deposit()


def on_button_withdraw_click():
    pass

def on_button_show_account_details_click():
    pass

button_new_account = component_creator.getButton(root,"New Account")
button_new_account.config(command=on_button_new_account_click)
button_new_account.grid(column=0,row=0,sticky="ew",padx=2,pady=5)

button_deposit = component_creator.getButton(root,"Deposit")
button_deposit.config(command=on_button_deposit_click)
button_deposit.grid(column=1,row=0,sticky="ew",padx=2,pady=5)

button_withdraw = component_creator.getButton(root,"Withdraw")
button_withdraw.config(command=on_button_withdraw_click)
button_withdraw.grid(column=1,row=1,sticky="ew",padx=2,pady=5)

button_show_account_details = component_creator.getButton(root,"Show Details")
button_show_account_details.config(command=on_button_show_account_details_click)
button_show_account_details.grid(column=0,row=1,sticky="ew",padx=2,pady=5)


root.mainloop()

# second_window = tk.Toplevel(root) #Erzeugen eines zweiten Fensters mit abhängigkeit zu root
# second_window.title("Mein zweites Sub-Fenster") 
# second_window.geometry("600x600")
