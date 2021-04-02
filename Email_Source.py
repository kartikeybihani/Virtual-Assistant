import smtplib


def Email(to, msg):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('YOUR EMAIL ADDRESS HERE', 'YOUR EMAIL PASSWORD HERE')
    server.sendmail('YOUR EMAIL ADDRESS HERE', to, msg)
    server.close()
