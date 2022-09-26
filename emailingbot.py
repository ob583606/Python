import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "anonstestingbot@gmail.com"  # Enter your address
receiver_email = "tfsmilepins@sobeys.com"  # Enter receiver address
scndrcvr = "katram144@gmail.com"
addresslst = [receiver_email, scndrcvr]
password = "583606banana"
message = """\
Subject: Smile Pin Nomination

Jacob smit really wowed me with his help and knowledge of fish. I felt warm and welcomed by his delightful charm. Thanks to Jacob Smit of Fairfield thrifty's!"""
for x in range (10000):
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)