import smtplib


def sendEmail(to, msg):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('kartikeybihani05@gmail.com', 'KARTIKEYKOTA')
    server.sendmail('kartikeybihani05@gmail.com', to, msg)
    server.close()
