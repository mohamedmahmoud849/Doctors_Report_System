def send_email(report_id, patient_email):
    from email.mime.application import MIMEApplication
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    import smtplib
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    server.login('hospitalsystemfcai@gmail.com', "hospitalsystem21")
    # Craft message (obj)
    msg = MIMEMultipart()
    subject = "Medical Report"
    message = "your medical report is here."
    msg['Subject'] = subject
    msg['From'] = 'hospitalsystemfcai@gmail.com'
    msg['To'] = patient_email
    # Insert the text to the msg going by e-mail
    msg.attach(MIMEText(message, "plain"))
    # Attach the pdf to the msg going by e-mail
    path_to_pdf= ""+report_id+".docx"
    with open(path_to_pdf, "rb") as f:
        attach = MIMEApplication(f.read(), _subtype="docx")
    attach.add_header('Content-Disposition', 'attachment', filename=str(path_to_pdf))
    msg.attach(attach)
    # send msg
    server.send_message(msg)
   

