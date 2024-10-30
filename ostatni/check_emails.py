import socket
import smtplib
import dns.resolver

email_address = 'dominik.deminger@educanet.cz'

domain = email_address.split('@')[1]
mx_record = dns.resolver.resolve(domain, 'MX')[0].exchange.to_text()

server = smtplib.SMTP(mx_record)
server.set_debuglevel(0)
server.helo()
server.mail('text@example.com')
code, message = server.rcpt(email_address)
server.quit()

# Assume 250 as Success
if code == 250:
	print('Success')
else:
	print('Bad')
