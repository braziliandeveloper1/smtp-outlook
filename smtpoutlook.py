

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_mail(remetente, senha, destinatario, subject, mensagem):
    # MENSAGEM DE TEXTO
    msg = MIMEMultipart('alternativo')
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = subject


    html = 'get rich or die trying'
    #pt1 = MIMEText(text, 'text')
    pt2 = MIMEText(html, 'html')
    #msg.attach(pt1)
    msg.attach(pt2)

    # CONFIGURACOES SERVER SMTP
    smtp_server = 'smtp-mail.outlook.com'
    smtp_port = 587

    try:
        # CONEXAO SEGURA SSL/TLS
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()

        # L OUTLOOK
        server.login(remetente, senha)

        # SEND EMAIL
        server.sendmail(remetente, destinatario, msg.as_string())

        print(f'EMAIL ENVIADO COM SUCESSO!')
    
    except smtplib.SMTPException as e:
        print(f'EMAIL NÃO ENVIADO!', str(e))

    finally:
        server.quit()


remetente = 'braziliandeveloper1@outlook.com' # YOUR OUTLOOK
senha = 'PASSWWORD-KEY-PASSWWORD-KEY'   # YOUR PASSWORD
destinatario = '50cent@gmail.com'
subject = 'brazilian phishing'
mensagem = 'get rich or die trying'
send_mail(remetente, senha, destinatario, subject, mensagem)