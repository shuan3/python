import smtplib

smtp_object = smtplib.SMTP("smtp.gmail.com", 587)
smtp_object.ehlo()
smtp_object.starttls()
password = input("what is your password")
import getpass

password = getpass.getpass("pass word")


email = getpass.getpass("email")
email = getpass.getpass("pass word")

smtp_object.login(email, password)


from_address = email
to_address = email
subject = input("ss")
message = input("ss")
msg = f"Subject: " + subject + "\n" + message
smtp_object.sendmail(from_address, to_address, msg)
smtp_object.quit()
