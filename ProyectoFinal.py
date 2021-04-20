import platform
import random
import hashlib
import os

user = None
balance = None

def clearConsole():
    if platform.system() == 'Windows':
        os.system('cls');
    else:
        os.system('clear');

def userExists(user):
    with open('registeredUsers.txt') as users:
        for line in users:
            if user in line:
                return True;
        else:
            return False;

def userRecarga(user):
    print("""
        \t\t\t\t\t-------------------\n
        \t\t\t\t\tRECARGAS\n
        \t\t\t\t\t-------------------\n
        \t\t\t\t\tESCOJA LA COMPAÑÍA:
        \t\t\t\t\t-------------------\n
        \t\t\t\t\t1) ALTICE
        \t\t\t\t\t-------------------\n
        \t\t\t\t\t2) CLARO
        \t\t\t\t\t-------------------\n
        \t\t\t\t\t3) VIVA
        \t\t\t\t\t-------------------\n
        """);
    option = int(input('\t\t\t\t\tOPCION: '))
    if option == 1 or option == 2 or option == 3:
        clearConsole();
        amount = int(input('\t\t\t\t\t\t\tMONTO DE LA RECARGA: '));
        userFactura = open(f'factura-{user}.txt', 'a');
        userBalanceFile = open(f'userBalance-{user}.txt', 'r');
        balanceQuantity = int(userBalanceFile.read());
        if amount > balanceQuantity:
            print("""
            \t\t\t\t\t-------------------------------------------------------------\n
            \t\t\t\t\tLA CANTIDAD QUE DESEA RETIRAR EXCEDE DEL BALANCE DE SU CUENTA\n
            \t\t\t\t\t-------------------------------------------------------------\n
            """);
            os.system("pause");
            mainMenu();
        else: 
            balanceQuantity-=amount;
            userBalanceFileFinal = open(f'userBalance-{user}.txt', 'w');
            userBalanceFileFinal.write(str(balanceQuantity));
            codigo = random.randint(10000,99999);
            information = '\n\n' + 'FACTURA:' + '\n' + 'Cliente:' + str(user) + '\n' + 'Codigo:' + str(codigo) + '\n' +'Monto:' + str(amount) + '\n'
            userFactura.write(information);
            userFactura.close();
            userBalanceFileFinal.close();
            clearConsole();
            print(f"""
            \t\t\t\t\t------------------\n
            \t\t\t\t\tLA RECARGA EXITOSA\n
            \t\t\t\t\tCODIGO: {str(codigo)}\n
            \t\t\t\t\t------------------\n
            """);
            os.system("pause");
            mainMenu();

def userBalance(user):
    balance = open(f'userBalance-{user}.txt', 'r');
    print(f"""
        \t\t\t\t\t-------------------------------------\n
        \t\t\t\t\tSU BALANCE ACTUAL ES DE RD$ {balance.read()}\n
        \t\t\t\t\t-------------------------------------\n
        """);
    os.system("pause");
    mainMenu();

def userRemoveCash(user):
    userBalanceFile = open(f'userBalance-{user}.txt', 'r');
    balanceQuantity = int(userBalanceFile.read());
    quantity = int(input('\t\t\t\t\t\t\tCANTIDAD A RETIRAR: '));
    if quantity > balanceQuantity:
        print("""
        \t\t\t\t\t-------------------------------------------------------------\n
        \t\t\t\t\tLA CANTIDAD QUE DESEA RETIRAR EXCEDE DEL BALANCE DE SU CUENTA\n
        \t\t\t\t\t-------------------------------------------------------------\n
        """);
        os.system("pause");
        mainMenu();
    else:
        balanceQuantity-=quantity;
        userBalanceFileFinal = open(f'userBalance-{user}.txt', 'w');
        userBalanceFileFinal.write(str(balanceQuantity));
        print(f"""
        \t\t\t\t\t---------------------------------------\n
        \t\t\t\t\tHA RETIRADO RD$ {quantity} DE SU CUENTA\n
        \t\t\t\t\t---------------------------------------\n
        """);
        userBalanceFile.close();
        userBalanceFileFinal.close();
        os.system("pause");
        mainMenu();

def userDeposit(user):
    userBalanceFile = open(f'userBalance-{user}.txt', 'r');
    balanceQuantity = int(userBalanceFile.read());
    if balanceQuantity == '':
        balanceQuantity = 0;
    quantity = int(input('\t\t\t\t\t\t\tCANTIDAD A DEPOSITAR: '));
    balanceQuantity+=quantity;
    userBalanceFileFinal = open(f'userBalance-{user}.txt', 'w');
    userBalanceFileFinal.write(str(balanceQuantity));
    print(f"""
        \t\t\t\t\t----------------------------------------\n
        \t\t\t\t\tHA DEPOSITADO RD$ {quantity} A SU CUENTA\n
        \t\t\t\t\t----------------------------------------\n
        """);
    userBalanceFile.close();
    userBalanceFileFinal.close();
    os.system("pause");
    mainMenu();

def userRegister():
    print("""
        \t\t\t\t\t-------------------\n
        \t\t\t\t\tREGISTRO DE USUARIO\n
        \t\t\t\t\t-------------------\n
        """);
    print('\t\t\t\t\t\t-------------------\n');
    user = input('\t\t\t\t\t\tUSER:');
    print('\t\t\t\t\t\t-------------------\n');
    password = input('\t\t\t\t\t\tPASSWORD:');
    print('\t\t\t\t\t\t-------------------\n');
    hashPassword = hashlib.sha256(password.encode("UTF-8"));
    hexPassword = hashPassword.hexdigest();
    encryptedPassword = hexPassword[::5];
    if userExists(user) == True:
        print("""
            \t\t\t\t\t----------------\n
            \t\t\t\t\tESTE USER EXISTE\n
            \t\t\t\t\t----------------\n
        """);
        os.system('pause');
        clearConsole();
        menu();
    else:
        global balance
        print("""
            \t\t\t\t\t------------------\n
            \t\t\t\t\tUSUARIO REGISTRADO\n
            \t\t\t\t\t------------------\n
        """);
        os.system('pause');
        registeredUser = open('registeredUsers.txt', 'a');
        userData = user + ' ' + password + '\n';
        registeredUser.write(userData);
        registeredUser.close();
        userBalance = open(f'userBalance-{user}.txt', 'a');
        balance = '0';
        userBalance.write(balance);
        userBalance.close();
        clearConsole();
        userLogin();

def userLogin():
    global user
    print("""
        \t\t\t\t\t-------------------\n
        \t\t\t\t\t\tLOGIN\n
        \t\t\t\t\t-------------------\n    
        """);
    print('\t\t\t\t\t\t-------------------\n');
    user = input('\t\t\t\t\t\tUSER:');
    print('\t\t\t\t\t\t-------------------\n');
    password = input('\t\t\t\t\t\tPASSWORD:');
    hashPassword = hashlib.sha256(password.encode("UTF-8"));
    hexPassword = hashPassword.hexdigest();
    encryptedPassword = hexPassword[::5];
    print('\t\t\t\t\t\t-------------------\n');
    for line in open('registeredUsers.txt', 'r').readlines():
        userCredentials = line.split();
        if user == userCredentials[0] and password == userCredentials[1]:
            clearConsole();
            mainMenu();
            return True
    else:
        clearConsole();
        print("""
    \t\t\t\t\t----------------------------\n
    \t\t\t\t\t CREDENCIALES INCORRECTAS
    \t\t\t\t\t----------------------------\n
    """);
        os.system("pause");
        clearConsole();
        menu();
        return False          

def mainMenu():
     print("""
        \t\t\t\t\t----------------------------\n
        \t\t\t\t\tBIENVENIDO AL CAJERO VIRTUAL\n
        \t\t\t\t\t----------------------------\n
        \t\t\t\t\tQUE ACCION DESEA REALIZAR:
        \t\t\t\t\t----------------------------\n
        \t\t\t\t\t1) RETIRO
        \t\t\t\t\t----------------------------\n
        \t\t\t\t\t2) CONSULTA
        \t\t\t\t\t----------------------------\n
        \t\t\t\t\t3) DEPOSITO
        \t\t\t\t\t----------------------------\n
        \t\t\t\t\t4) RECARGA
        \t\t\t\t\t----------------------------\n
        \t\t\t\t\t5) SALIR
        \t\t\t\t\t----------------------------\n
        """);
     action = int(input('\t\t\t\t\tACCION: '));
     if action == 1:
         clearConsole();
         userRemoveCash(user)
     elif action == 2:
         clearConsole();
         userBalance(user);
     elif action == 3:
         clearConsole();
         userDeposit(user);
     elif action == 4:
         clearConsole();
         userRecarga(user);
     elif action == 5:
         print("""
         \t\t\t\t\t-----------------------------
         \t\t\t\t\tPASE BUEN RESTO DEL DIA/NOCHE
         \t\t\t\t\t-----------------------------
         """);
        
def menu():
        print("""
        \t\t\t\t\t----------------------------\n
        \t\t\t\t\tBIENVENIDO AL CAJERO VIRTUAL\n
        \t\t\t\t\t----------------------------\n
        \t\t\t\t\tQUE ACCION DESEA REALIZAR:
        \t\t\t\t\t----------------------------\n
        \t\t\t\t\t1) REGISTRARSE
        \t\t\t\t\t----------------------------\n
        \t\t\t\t\t2) INICIAR SESION
        \t\t\t\t\t----------------------------\n
        """);
        action = int(input('\t\t\t\t\tACCION: '));
        clearConsole();
        if action == 1:
            userRegister();
        elif action == 2:
            userLogin();
        else:
            print("""
            \t\t\t\t\t-----------------\n
            \t\t\t\t\tACCION INCORRECTA\n
            \t\t\t\t\t-----------------\n
            """);
            os.system("pause");
            clearConsole();
            menu();
    
menu();















