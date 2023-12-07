import smtplib

def main():
    fromaddr = "konrad@example.com"
    toaddrs = ["admin@example.com"]
    msg = "Hello World!"
    msg = "From: " + fromaddr + "\nTo: " + ", ".join(toaddrs) + "\n\n" + msg
    with smtplib.SMTP("warsztat.mywire.org", 5125) as server:
        server.sendmail(fromaddr, toaddrs, msg)

if __name__ == "__main__":
    main()
