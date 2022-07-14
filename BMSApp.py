from customers import Customers
import PySimpleGUI as pg
# help(pg.DropDown)
# pg.theme_previewer()
pg.theme("DarkTeal11")

layout = [
    [pg.Button("View Customer Accounts")],
    [pg.Button("Add/Create Account")],
    [pg.Button("New Transaction")],
    [pg.Button("Latest Transactions")],
    [pg.Button("Update Customer Info")],
    [pg.Button("Exit Application")]
]
layout2 = [
    [pg.Text('NEW ACCOUNT CREATION',size=(5,1),key='_DISPLAY_')],
    [pg.Text('Enter your First name',size=(5,1)),pg.InputText(do_not_clear=False)],
    [pg.Text('Enter your Surname',size=(5,1)),pg.InputText(do_not_clear=False)],
    [pg.Text("Enter Deposit Amount",size=(5,1)),pg.InputText(do_not_clear=False)],
    [pg.Radio("Male",group_id="gender"),pg.Radio("Female",group_id="gender")],
    [pg.Text('Year'),pg.DropDown(values=['2022'],default_value='2022')],
    [pg.Text('Day in Month'),pg.InputText()],
    [pg.Text('Month',size=(8,1)),pg.InputText()],
    [pg.Text('Enter Phone Number',size=(10,1)),pg.InputText(do_not_clear=False)],
    [pg.Button("Create Now")],[pg.Button("Cancel")]
    ]
main_window = pg.Window("NEWGEN BANK BMS",layout,size=(1200,450))


while True:
    event,values = main_window.read()
    if event is None:
        break
    elif event == "Exit Application":
        break
    elif event == "View Customer Accounts":
        c = Customers()
        c.showCustomers()
    elif event == "Add/Create Account":
        main_window.minimize()
        add_window = pg.Window("CREATE ACCOUNT BANK BMS", layout2)

        while True:
            event, values = add_window.read()
            from random import randint
            def addZero(x):
                if int(x) < 10:
                    zerostr = '0'
                    zerostr = zerostr + x
                    return zerostr
                return x
            if event is None:
                break
            elif event == "Cancel":
                add_window.close()
            elif event == "Create Now":
                msgprocess = "Creating Account pls wait..."
                msgcomplete = "Account Created!"
                add_window['_DISPLAY_'].update(value=msgprocess)
                g = Customers()
                CustomerID = g.generateID()
                AccountNumber = '004' + str(randint(1000000,9999999))
                print(CustomerID)
                print(AccountNumber)
                input()
                DateCreated = values[5]+'-'+addZero(values[7])+'-'+addZero(values[6])
                print(DateCreated)
                gender = []
                if values[3]:
                    values[3] = 'Male'
                    gender.append(values[3])
                else:
                    values[4] = 'Female'
                    gender.append(values[4])
                print(values[3])
                print(values[4])
                print(gender)
                a = Customers()
                a.addCustomers(CustomerID,values[0],values[1],AccountNumber,values[2],DateCreated,values[8])
                print('New Customer Account Created!')
    elif event == "Update Customer Info":
        main_window.minimize()
        u = Customers()
        u.updateCustomer()










