import smtplib
import dns.resolver

def check_if_email_is_valid(email, providers):

    my_results = []

    for domain in providers:

        full_email = email + "@" + domain

        print("testing for", full_email)

        mx_record = dns.resolver.resolve(domain, 'MX')[0].exchange.to_text()

        server = smtplib.SMTP(mx_record)
        server.set_debuglevel(0)
        server.helo()
        server.mail('text@example.com')
        code, message = server.rcpt(full_email)
        server.quit()

        if code == 250:
            my_results.append({"domain": domain, "is_valid": True})

            print("Good")
        else:
            my_results.append({"domain": domain, "is_valid": False})

            print("Bad")

    return my_results
