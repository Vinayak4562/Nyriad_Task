import argparse          # Use to processing command line
import sqlite3           # To create DB
import email             # it is a A package for parsing, handling, and generating email messages
import imaplib


parser = argparse.ArgumentParser()
parser.add_argument('--name', type=str, help='Name of the user')
parser.add_argument('--time', type=int, help='Duration of time in seconds')
args = parser.parse_args()
print(f"Hello {args.name}, you entered a duration of {args.time} seconds")

def fetch_emails(name):

    imap_server = "imap.gmail.com"
    email_address = "vinz223665@gmail.com"
    password = "ugyltbuxtnpmzijl"

    imap = imaplib.IMAP4_SSL(imap_server,993)   #IMAP(Internet Message Access Protocol), SMTP (Simple Mail Transfer Protocol) cz encripted conn

    imap.login(email_address, password)
   
    imap.select("Inbox")
    _, msgnums  = imap.search(None, "ALL") # to get all mails msg num is use to tterate through the emails


    for msgnum in msgnums[0].split():
        _, data = imap.fetch(msgnum,("RFC822") ) # "RFC822" code to entire messege & result stored in data
      
        message = email.message_from_bytes(data[0],[1])
        print(f"From: {message.get('From')}")
        print(f"To: {message.get('To')}")
        print(f"Date: {message.get('Date')}")
        print(f"Subject: {message.get('Subject')}")

        print("Content: ")
        for part in message.walk():   #walk is a genarator which reads all the part of msg
            if part.get_content_type() == "text/plain":
                print(part.as_string())

    imap.close()



    # Extract relevant details from emails and store in database
    connect = sqlite3.connect('emails.db')
    cursor = connect.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS emails (subject TEXT, body TEXT)')
    for email_message in email:
        subject = email_message['Subject']
        body = email_message.get_payload()
        cursor.execute('INSERT INTO emails (subject, body) VALUES (?, ?)', (subject, body))
    connect.commit()
    connect.close()

    return email