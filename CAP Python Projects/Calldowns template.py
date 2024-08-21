import sqlite3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def get_cadets():
    conn = sqlite3.connect('cadets.db')
    c = conn.cursor()
    c.execute('SELECT name, test_required FROM cadets')
    cadets = c.fetchall()  
    conn.close()
    return cadets


def clear_cadets():
    conn = sqlite3.connect('cadets.db')
    c = conn.cursor()
    c.execute('DELETE FROM cadets')  
    conn.commit()
    conn.close()


def send_email(subject, body, to_email):
    from_email = "YOUR CAP EMAIL" #MAKE SURE TO PUT YOUR EMAIL AND PASSWORD IN EXACTLY RIGHT SO THE PROGRAM CAN SEND THE EMAIL
    from_password = "YOUR CAP EMAIL PASSWORD"

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))  

    try:
        server = smtplib.SMTP('smtp-mail.outlook.com', 587)
        server.starttls()
        server.login(from_email, from_password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        print("Email successfully sent!")  
    except Exception as e:
        print(f"Failed to send email: {e}")


def generate_email_content():
    cadets = get_cadets()
    if not cadets:
        return "Good Evening Sir,\n\nHere are the calldown results from Charlie Flight.\n\nNo cadets for this week's meeting.\n\nV/R,"

    body = "Good Evening Sir,\n\nHere are the calldown results from Charlie Flight:\n\n"
    for cadet in cadets:
        body += f"Name: {cadet[0]}, Test Required: {cadet[1]}\n"
    body += ("\nV/R,\n\n"
             "YOUR NAME AND RANK\n" #THIS IS WHERE YOU PUT YOUR NAME AND RANK FOR YOUR SIGNATURE - DON'T TOUCH ANY OF The OTheR CODE
             "Bethesda Chevy Chase Composite Squadron, Charlie Flight Commander\n"
             "Civil Air Patrol, U.S. Air Force Auxiliary\n"
             "(M) 240-921-6079\n\n"
             "GoCivilAirPatrol.com\n\n"
             "Volunteers serving America's communities, saving lives, and shaping futures.")
    return body


def weekly_email():
    subject = "Charlie Flight Calldowns"
    body = generate_email_content()
    to_email = ["example@md.cap.gov"]

    send_email(subject, body, to_email)
    clear_cadets()

if __name__ == "__main__":
    weekly_email()
