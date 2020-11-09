import os

def generatersa():
    name = input("Enter the applicant's name: ")
    id = input("Enter the unique ID: ")
    name = name + id
    if os.path.isdir(name):
        print("Sorry,",name,"cannot generate new Keypairs. It already has been assigned one.")
    else:
        os.system('mkdir ' + name)
        os.system('mkdir ' + name + '/sent')
        os.system('mkdir ' + name + '/received')
        priv = 'openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:2048 -pkeyopt rsa_keygen_pubexp:3 -out ' + name + '/' + name + 'priv.pem'
        os.system(priv)
        pub = 'openssl pkey -in ' + name + '/' + name + 'priv.pem' + ' -out ' + name + '/' + name + 'pub.pem -pubout'
        os.system(pub)
        print("User added to the system and keys generated.")

def sendmessages():
    sender = input("Enter your username: ")
    if os.path.isdir(sender):
        receiver = input("Enter the receiver's username: ")
        if os.path.isdir(receiver):
            message = input("Enter your secret message: ")
            filename = input("What do you name the message file: ")

            path = sender + '/sent/' + filename + ".txt"
            f = open(path,"w")
            f.write(message)
            f.close()

            operatin = 'openssl pkeyutl -encrypt -in ' + path + ' -pubin -inkey ' + receiver + '/' + receiver + 'pub.pem ' + '-out server/' + filename + '.bin'
            os.system(operatin)
            print("\nYour message is sent to the server.")
        else:
            print("No such username exists. Try again!")
    else:
        print("No such username exists. Try again!")

def receivemessages():
    receiver = input("Enter your username: ")
    if os.path.isdir(receiver):
        os.system('ls server/')
        print()
        filename = input("Which file do you want to access: ")
        newpath = 'server/' + filename
        if os.path.isfile(newpath):
            operation = 'openssl pkeyutl -decrypt -in ' + newpath + ' -inkey ' + receiver + '/' + receiver + 'priv.pem' + ' -out ' + receiver + '/received/' + filename[:-4] + '.txt'
            #print(operation)
            os.system(operation)
            newpath = receiver + '/received/' + filename[:-4] + '.txt'
            operation = 'cat ' + newpath
            print("The Message is: ")
            os.system(operation)
            print()
        else:
            print("No such file exists. Try again!")
    else:
        print("No such username exists. Try again!")

while (True):
    print("\nWhat do you want to do?")
    print("1: Generate RSA Keypair.")
    print("2: Send Messages.")
    print("3: Receive Messages.")
    print("4: Exit.")
    choice = int(input("Enter the choice: "))

    if choice == 1:
        generatersa()
    elif choice == 2:
        sendmessages()
    elif choice == 3:
        receivemessages()
    elif choice == 4:
        print("Exiting the System. Thank You!")
        break
    else:
        print("You entered a wrong choice. Please re-enter!")
