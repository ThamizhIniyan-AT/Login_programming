import re


def checkemail():
    regexp = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if not re.findall(regexp, email):
        print("Email DOSE NOT satisfies the condition")
        register()


def checkpassword():
    regex_pass = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{5,16}$'
    if not re.findall(regex_pass, password):
        print("""PASSWORD DOES NOT MATCH CONDITION!!
                           1.Must have minimum one special character,
                           2.onedigit,
                           3.oneuppercase,
                           4.onelowercasecharacter""")
        register()


def forgetpassword():
    pass
def register():
    global email
    global password
    db = open("LoginDatabase.txt", "r")
    email = input("Enter User EmailAddress: ")
    password = input("Enter User Password: ")
    confrim_password = input("Enter Password Again: ")
    e = []
    p = []
    for i in db:
        a, b = i.split(",")
        b = b.strip()
        e.append(a)
        p.append(b)
    data = dict(zip(e, p))
    if password != confrim_password:
        print("PASSWORD DOESN'T EXISTS")
        register()

    else:
        checkemail()
        checkpassword()
        if email in e:
            print("username exists already")
            register()

        else:
            db = open("LoginDatabase.txt", "a")
            db.write(email + "," + password + "\n")
            print("Registered is Successful")


def access():
    email_ = input("Enter your Email ID :")
    password_ = input("Enter your Passsword :")

    if not len(email_ or password_) < 1:
        db = open("LoginDatabase.txt", "r")
        e = []
        p = []
        for i in db:
            a, b = i.split(",")
            b = b.strip()
            e.append(a)
            p.append(b)
        data = dict(zip(e, p))
        try:
            if data[email_]:
                try:
                    if password_ == data[email_]:
                        print("Login Success!!!")
                        print("Hi..User,welcome..!!")
                    else:
                        print("Password is INCORRECT!")
                except:
                    print("Email or password not match")
            else:
                print(" User Doesn't Exists ")
        except:
            print("emailid is incorrect")
    else:
        print("Please!, Register")
        register()


def start():
    option = input(" Login | SignUp | ForgetPassword : ")
    if option == "Login":
        access()
    elif option == "SignUp":
        register()
    elif option == "ForgetPassword":
        forgetpassword()
    else:
        print("Enter your Option")


start()
