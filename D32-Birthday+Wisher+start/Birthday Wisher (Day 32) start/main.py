import smtplib

my_email = "to.chenxiaoyan@gmail.com"
password = "111"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(
    from_addr=my_email,
    to_addrs="",
    msg="Subject:Hello\n\nThis is the body of email")
connection.close()