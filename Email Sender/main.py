import smtplib as sl

ob = sl.SMTP("smtp.gmail.com",587)
ob.ehlo()
ob.starttls()

try:
  ob.login('abc@gmail.com', '1234567890')
except Exception as e:
  print("Login Failed!!",e)
else:
  print("Successful login")

subject = "Learning SMTP in python"
body = "Hi, Learning Python is Fun"

mssg = "subject:{}\n\n{}".format(subject,body)
listadd = ["abc@gmail.com","xyz@gmail.com"]

try:
  ob.sendmail("abc@gmail.com",listadd,mssg)
except Exception as e:
  print("Failed to send the mails",e)
else:
  print("Sent the email to the destination addresses")

ob.quit()
