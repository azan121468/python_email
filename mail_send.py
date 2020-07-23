import smtplib, webbrowser, getpass
def get_email():
    servicesAvaliable=['hotmail','outlook','yahoo','gmail',]
    while True:
        email_id=input("Emsil : ")
        #if '@' in mail_id and '.com' in mail_id:
        if '@' in email_id and email_id.endswith('.com'):
            symbol_pos=email_id.find("@")
            dotcom_pos=email_id.find(".com")
            sp=email_id[symbol_pos+1:dotcom_pos]
            if sp in servicesAvaliable:
                return email_id, sp
                break
            else:
                print("We don't provide service for"+sp)
                print("We provide service only for : ")
                for i in servicesAvaliable:
                    print(i)
        else:
            print("Invalid Email \n try again")
            continue

def set_smtp_domain(serviceProvider):
    if serviceProvider == 'gmail':
        return 'smtp.gmail.com'
    elif serviceProvider == 'hotmail' or serviceProvider == 'outlook':
        return 'smtp-mail.outlook.com'
    elif serviceProvider == 'yahoo':
        return 'smtp.mail.yahoo.com'

def main():
    print('Welcome to Email Sender')
    e_mail, serviceProvider=get_email()
    print("Your service provider is "+serviceProvider.capitalize())
    password=input("Password : ")

    while  True:
        try:
            smtpDomain=set_smtp_domain(serviceProvider)
            connection=smtplib.SMTP(smtpDomain)
            connection.ehlo()
            connection.starttls()
            connection.login(e_mail, password)
            print("Connection Sucessful.")
            break
        except:
            print("Connection failed")
            if serviceProvider == 'gmail':
                print("There are two possible reasons :-")
                print("1) You have typed wrong email or password")
                print("2) Your account has disable less secure apps")
                print("Do you want to enable less secue appsSS",end="")
                answer=input("yes or no : ")
                if answer=='y' or answer=='Y' or answer=="yes" \
                                       or answer=="Yes":
                    webbrowser.open("https://myaccount.google.com/lesssecureapps")
                else:
                     print("Do you want to retry [Y]es/[N]o : ",end=" ")
                     retry=input()
                     if retry=='y' or retry=='Y' or retry=="yes" \
                                       or retry=="Yes":
                         print("Please retype information")
                         e_mail, serviceProvider = get_mail()
                         continue
                     else:
                        print("Thanks for using service")
                        print("Better luck next time")
    print("Reciver's Email : ")
    recieverAddress, recieverSP = get_email()
    Subject = input("Subject : ")
    Message = input("Message : ")
    connection.sendmail(e_mail, recieverAddress, ("Subject: " + str(Subject) + "\n\n" + str(Message)))
    print("Email sent sucessfully")
    connection.quit()
main()
    
            
