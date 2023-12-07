import smtplib

def main():
    fromaddr = "konrad@example.com"
    toaddrs = ["admin@example.com"]
    msg = "Hello World!"
    # msg = "From: " + fromaddr + "\nTo: " + ", ".join(toaddrs) + "\n\n" + msg
    msg = f"From: {fromaddr}\nTo: {', '.join(toaddrs)}\n\n{msg}"
    with smtplib.SMTP("warsztat.mywire.org", 5125) as server:
        server.sendmail(fromaddr, toaddrs, msg)

if __name__ == "__main__":
    main()

# https://docs.python.org/3/library/email.examples.html#email-examples
# https://realpython.com/python-send-email/
# https://realpython.com/python-send-email/#yagmail
