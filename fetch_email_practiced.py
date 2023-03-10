import imaplib
import email


imap_server = "imap.gmail.com"
email_address = "vinz223665@gmail.com"
password = "ugyltbuxtnpmzijl"


imap = imaplib.IMAP4_SSL(imap_server)   #IMAP(Internet Message Access Protocol), SMTP (Simple Mail Transfer Protocol) cz encripted conn

imap.login(email_address, password)

imap.select("Inbox")
_, msgnums  = imap.search(None, "ALL") # to get all mails msg num is use to tterate through the emails

print(msgnums)
for msgnum in msgnums[0].split():
    _, data = imap.fetch(msgnum,("RFC822") ) # "RFC822" code to entire messege & result stored in data
    # print(data)
    meg = email.message_from_bytes(data[0],[1])
    print(f"Message Number: {msgnum}")
    print(f"From: {meg.get('From')}")
    print(f"To: {meg.get('To')}")
    print(f"BCC: {meg.get('BCC')}")
    print(f"Date: {meg.get('Date')}")
    print(f"From: {meg.get('From')}")
    print(f"Subject: {meg.get('Subject')}")

    print("Content: ")
    for part in meg.walk():   #walk is a genarator which reads all the part of msg
        if part.get_content_type() == "text/plain":
            print(part.as_string())
imap.close()