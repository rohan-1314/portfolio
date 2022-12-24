import smtplib, ssl

password = 'tycioonycqrosntr'
username = 'rohan.vagadiya14@gmail.com'
host = 'smtp.gmail.com'
port = 465
reciever = 'adesarapriyal544@gmail.com'
context = ssl.create_default_context()
message = """\
subject:yooo!
I am sending this email from python.
So Rad!

"""
# we did context=context because the func has multiple args and context
# comes later and host, port are 1st,2nd, so they are in order
with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, reciever, message)
