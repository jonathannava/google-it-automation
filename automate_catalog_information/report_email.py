import reports
import os 
import datetime

descriptions_path = 'descriptions/'

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

    summary = summary_pdf(data)
    paragraph = "<br/><br/>".join(summary)
    title = "Processed Update on {}\n".format(datetime.date.today().strftime("%B %d, %Y"))
    attachment = "reports/processed.pdf"
    reports.generate_report(attachment, title, paragraph)