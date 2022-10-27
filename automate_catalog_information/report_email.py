#!/usr/bin/env python3

import reports
import os 
import datetime
import emails

descriptions_path = 'supplier-data/descriptions/'

descriptions = os.listdir(descriptions_path)

data = []
report = []

def summary_pdf(data):
    for file in descriptions:
        with open(descriptions_path + file, 'r') as f:
            file_data = f.read()
            data.append(file_data.split('\n'))
            f.close()
    for i in data:
        report.append("name: {}<br/>weight: {}\n".format(i[0], i[1]))
    return (report)

if __name__ == "__main__":
    #Generate PDF Report
    summary = summary_pdf(data)
    paragraph = "<br/><br/>".join(summary)
    title = "Processed Update on {}\n".format(datetime.date.today().strftime("%B %d, %Y"))
    attachment = "/tmp/processed.pdf"
    reports.generate_report(attachment, title, paragraph)
    #Send email
    subject = "Upload Completed - Online Fruit Store"
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    message = emails.generate_email(sender, receiver, subject, body, attachment)
    emails.send_email(message)