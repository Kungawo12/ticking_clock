from dotenv import load_dotenv
import os
import random
import smtplib
import ssl

load_dotenv()



def send_email(sender, receiver, recipient):
    password = os.environ['password']
    body_msg = f''' \
        From : {sender}
        Subject: Your Secret Santa Present 
        
        Hi! Your secret santa is: {recipient}! 🎅
        Remember to spent 10$- 20$ on your gift,but don't stress about it being the perfect gift.
        '''
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, body_msg)
        
    name_list =['Tenzin', 'Tsering', 'Rigzin', 'Norbu', 'Jugney', 'Kunga'] 
    names_and_emails = [
        ['Tenzin', 'tkunga662@gmail.com'],
        ['Tsering', 'tenzinkuga31@gmail.com'],
        ['Rigzin', 'tenzin.kunga082024@gmail.com'],
        ['Norbu', 'kungatenzin320@gmail.com'],
        ['Jugney', 'jampa@gmail.com'],
        ['Kunga', 'officialtenzin.kunga@gmail.com']
    ]
    
    if len(name_list ) <= 1:
        print('Not enough people to play Secret Santa')
        quit()
        
    first_name = name_list[0][0]
    
    while len(name_list) >= 2:
        send_email('<your email here>', names_and_emails[0][1], names_and_emails[1][0])
        names_and_emails.pop(0)
        random.shuffle(names_and_emails)
    
    send_email('<your email here>', names_and_emails[0][1], first_name)