import argparse         # Use to processing command line
import email            # it is a A package for parsing, handling, and generating email messages
import imaplib          # it will provides an IMAP client API for accessing email messages from an IMAP server.
import sqlite3          # its a relational DBMS for python

def fetch_emails(name_or_duration):                # Connect to email account and fetch relevant emails
    
    conn = imaplib.IMAP4_SSL('imap.gmail.com')
    conn.login('vinz223665@gmail.com', 'ugyltbuxtnpmzijl')
    conn.select('Inbox')
    result, data = conn.search(None, f'(SUBJECT "{name_or_duration}" BODY "{name_or_duration}")')
    emails = []
    for num in data[0].split():
        _, data = conn.fetch(num, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_bytes(raw_email)
        emails.append(email_message)
    conn.close()
    print(email_message)


    # Extract relevant details from emails and store in database

    conn = sqlite3.connect('emails.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS emails (subject TEXT, body TEXT)')
    for email_message in emails:
        subject = email_message['Subject']
        body = email_message.get_payload()
        c.execute('INSERT INTO emails (subject, body) VALUES (?, ?)', (subject, body))
    conn.commit()
    conn.close()

    return emails