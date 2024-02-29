from SendingEmail import sendEmail
from UsersData import *
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import RPi.GPIO as gpio
import time

usersList = list()
Getinfo_led_pin = 20
deposit_led_pin = 21
withdraw_led_pin = 26
login_led_pin = 16
Buzzer_pin = 19

gpio.setwarnings(False)
#set BCM convention
gpio.setmode(gpio.BCM)
#set pins as output
gpio.setup(Getinfo_led_pin, gpio.OUT)
gpio.setup(deposit_led_pin, gpio.OUT)
gpio.setup(withdraw_led_pin, gpio.OUT)
gpio.setup(login_led_pin, gpio.OUT)
gpio.setup(Buzzer_pin, gpio.OUT)
#turn off the system
gpio.output(Getinfo_led_pin, gpio.LOW)
gpio.output(deposit_led_pin, gpio.LOW)
gpio.output(withdraw_led_pin, gpio.LOW)
gpio.output(login_led_pin, gpio.LOW)
gpio.output(Buzzer_pin, gpio.LOW)


def initialize_users_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    for line in lines:
        parts = line.strip().split()
        if len(parts) >= 4:
            name = parts[0]
            email = parts[1]
            password = parts[2]
            balance = parts[3]
            user = Users(name, email, password, int(balance))
            usersList.append(user)

initialize_users_from_file('userData.txt')

root = Tk()
root.config(bg='white')
root.title("Mu Bank")
# Set the size of the window to 800x600 pixels
root.geometry("800x600")
# Change the icon of the window
im = Image.open('icon.ico')
photo = ImageTk.PhotoImage(im)
root.wm_iconphoto(True, photo)

background = ImageTk.PhotoImage(Image.open("Bank.png"))
bgLabel = Label(root, image=background)

bgLabel.place(x=0, y=60)

usernameLabel = Label(root, text="username",height=1,width=20, bg='gray')
passLabel = Label(root, text="password",height=1,width=20, bg="gray")
usernameLabel.place(x=0,y=0)
passLabel.place(x=0,y=35)

usernameEntry = Entry(root,width=20,highlightthickness=2)
passEntry = Entry(root,width=20,highlightthickness=2)
usernameEntry.place(x=130,y=0)
passEntry.place(x=130,y=35)

def search_in_file(filename, name_to_find, pass_to_find):
    with open(filename, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) >= 3 and parts[0] == name_to_find and parts[2] == pass_to_find:
                return parts[0], parts[2]
    return None, None

def authpassed():
    b,t = parseInfo('userData.txt', usernameEntry.get())
    print(b)
    print(t)
    balanceLabel = Label(root, text=b,height=2,width=23, bg='orange')
    balanceLabel.place(x=590,y=35)
    balanceLabelTxt = Label(root, text="Balance",height=2,width=23, bg='orange')
    balanceLabelTxt.place(x=590,y=0)
    transectionsLabelTxt = Label(root, text="Transactions",height=2,width=23, bg='yellow')
    transectionsLabelTxt.place(x=590,y=70)
    i=0
    gpio.output(Getinfo_led_pin, gpio.HIGH)
    gpio.output(Buzzer_pin, gpio.HIGH)
    time.sleep(1)
    gpio.output(Buzzer_pin, gpio.LOW)
    gpio.output(Getinfo_led_pin, gpio.LOW)



    for transcetion in t:
        transectionsLabel = Label(root, text=transcetion,height=2,width=23, bg="yellow")
        transectionsLabel.place(x=590,y=105+i)
        i+=35
    
    
    
def parseInfo(filename, search_term):
    transcetions = list()
    with open(filename, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) >= 3 and parts[0] == search_term:
                for i in range(0,len(parts)):
                    if i > 3:
                        transcetions.append(parts[i])
                return parts[3], transcetions
    return None, None
    
withdrawEntry = Entry(root,width=10,highlightthickness=2)
withdrawEntry.place(x=400,y=35)
depositeEntry = Entry(root,width=10,highlightthickness=2)
depositeEntry.place(x=400,y=0)
def withdraw():    
    money = int(withdrawEntry.get())
    for user in usersList:
        if user.name == usernameEntry.get():
            user.withdraw(money)
            print(user.balance)
            gpio.output(withdraw_led_pin, gpio.HIGH)
            gpio.output(Buzzer_pin, gpio.HIGH)
            time.sleep(1)
            gpio.output(Buzzer_pin, gpio.LOW)
            gpio.output(withdraw_led_pin, gpio.LOW)


def deposite():    
    money = int(depositeEntry.get())
    for user in usersList:
        if user.name == usernameEntry.get():
            user.deposit(money)
            gpio.output(deposit_led_pin, gpio.HIGH)
            gpio.output(Buzzer_pin, gpio.HIGH)
            time.sleep(1)
            gpio.output(Buzzer_pin, gpio.LOW)
            gpio.output(deposit_led_pin, gpio.LOW)


def auth():
    global authflag
    passinput = passEntry.get()
    usernameinput = usernameEntry.get()
    u,p = search_in_file('userData.txt',usernameinput, passinput)
    if u == None or p == None:
        # Show a message dialog
        messagebox.showinfo("Login failed", "please enter valid username and password.")
    else:
        authButton.config(authButton,bg='green')
        messagebox.showinfo("Login Sucessflly ", "you can know get into your data.")
        getInfoLabel = Button(root, text="My Info",command =authpassed, height=1,width=7, bg='cyan')
        getInfoLabel.place(x=500,y=0)
        WithdrawLabel = Button(root, text="Withdraw",command =withdraw, height=1,width=7, bg='blue')
        WithdrawLabel.place(x=310,y=35)
        depositedrawLabel = Button(root, text="Deposite",command =deposite, height=1,width=7, bg='blue')
        depositedrawLabel.place(x=310,y=0)
        b,t = parseInfo('userData.txt', usernameinput)
        gpio.output(login_led_pin, gpio.HIGH)
        gpio.output(Buzzer_pin, gpio.HIGH)
        time.sleep(0.5)
        gpio.output(Buzzer_pin, gpio.LOW)



    
authButton = Button(root, command=auth, text="Login", width=17)
authButton.place(x=0,y=60)


root.mainloop()
    
            
