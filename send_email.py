import smtplib
# type in the senders email
senders_email = 'nitinprakash48@gmail.com'
# type in the recievers email
reciever_email = 'sachinkrishna8@gmail.com'
# make the password input from the user
password = input(str('please type your gmail password'))
# type the message that u want to send
message = 'hey this mail was send by usig pyhton'
# establish the server(and on which u want to connect to like google)
server = smtplib.SMTP('smtp.gmail.com', 587)
# for server
server.starttls()
# establish login into the server
server.login(senders_email, password)
print('sent succesfully')
server.sendmail(senders_email, reciever_email, password)
print("email is sent to ", reciever_email)
