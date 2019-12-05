import email
import imaplib

def checkemail():
	try:

		email = imaplib.IMAP4_SSL("imap.gmail.com")

		email.login("your-id", "your-password")
		email.select("INBOX", readonly=True)
		
		response, myid = email.search(None, 'ALL')

		idlist	=	myid[0].split()
		first	=	int(idlist[0])
		last	=	int(idlist[-1])

		for z in range(first, last, -1):
			typ, data = email.fetch(str(z), '(RFC822)')

			for d in data:

				if isinstance(d, tuple):
					
					msg = email.message_from_string(d[1])

					Subject = msg['Subject']
					From 	= msg['From']
					Date	= msg['Date']
					print("Subject : "+Subject+ "From : "+From+" Date : "+Date)
	
	except imaplib.IMAP4.error:
		print("error - invalid username or password");

if __name__ == '__main__':
	checkemail()