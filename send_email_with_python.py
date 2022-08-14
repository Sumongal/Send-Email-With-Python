import pywhatkit.mail
your_email="enter your gmail id here"
password="app password" # enter the password . To get it go to gmail then go to account then security and then on two step verification after that go to app password and sign in after that will get a password. Then copy that password and paste it in Password variable with double or single quote
reciever_email="enter the reciever email id"
pywhatkit.mail.send_mail(your_email,password,"enter the subject of your","type the message",reciever_email)

# after that if you get on screen email sent successfully then understand that your message delivered to the reciever if not you put wrong email or wrong password