from SendingEmail import sendEmail
from datetime import datetime


def update_line_by_name(name_to_find, new_data):
    with open('userData.txt', 'r') as file:
        lines = file.readlines()
        print(lines)
        file.close()

    with open('userData.txt', 'w') as file:
        i=0
        for line in lines:
            if i<Users.userNumber:
                if line.startswith(name_to_find):
                    line = line.strip() + ' ' + new_data + '\n'
                file.write(line)
                i+=1

            
def update_balance(name, new_balance):
    with open('userData.txt', 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if line.startswith(name):
            parts = line.split()
            if len(parts) >= 4:
                parts[3] = str(new_balance)
                lines[i] = ' '.join(parts) + '\n'
            break

    with open('userData.txt', 'w') as file:
        file.writelines(lines)



email_sender = 'mustaphaossama2000@gmail.com'

class Users:
    userNumber=0
    users= list()
    def __init__(self, name, email, password, balance):
        self.name = name
        self.password = password
        self.email = email
        self.balance = balance
        self.transaction_history = list()
        Users.users.append([self.name, self.password, self.email, str(self.balance)])
        Users.userNumber += 1
                
    def withdraw(self, money):
        self.balance -= money
        tran_time_formated  = datetime.now().strftime('%H:%M %d %m %Y' )
        tran_time= datetime.now().strftime('%M%H%d%m%Y')
        sendEmail(email_sender, self.email, "Mu bank: Transaction", f'you have withdrawn {money} LE at {tran_time_formated}')
        update_line_by_name(self.name, f"{money}withdrawn{tran_time}")
        update_balance(self.name,self.balance)
        
    def deposit(self, money):
        self.balance += money
        tran_time_formated  = datetime.now().strftime('%H:%M %d %m %Y' )
        tran_time= datetime.now().strftime('%M%H%d%m%Y')
        sendEmail(email_sender, self.email, "Mu bank: Transaction", f'you have deposited {money} LE at {tran_time_formated}')
        update_line_by_name(self.name, f"{money}deposited{tran_time}")
        update_balance(self.name,self.balance)
        
        

