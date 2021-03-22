# Python code to illustrate Sending mail from
# your Gmail account
import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("mrudulapolavarapu@gmail.com", "ibzlhpxnniybwtyu")

# message to be sent
message = "Hello"

# sending the mail
s.sendmail("mrudulapolavarapu@gmail.com", "mrudulapolavarapu@gmail.com", message)

# terminating the session
s.quit()
