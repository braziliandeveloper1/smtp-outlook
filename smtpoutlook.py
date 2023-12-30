

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_mail(remetente, senha, destinatario, subject, mensagem):
    # MENSAGEM DE TEXTO
    msg = MIMEMultipart('alternativo')
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = subject


    html = 'Lembre-se sua fatura vence hoje!'
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

        #
        server.login(remetente, senha)

        #
        server.sendmail(remetente, destinatario, msg.as_string())

        print(f'EMAIL ENVIADO COM SUCESSO!')
    
    except smtplib.SMTPException as e:
        print(f'EMAIL NÃO ENVIADO!', str(e))

    finally:
        server.quit()


remetente = 'braziliandeveloper1@outlook.com' 
senha = 'PASSWWORD-KEY-PASSWWORD-KEY'  
destinatario = '50cent@gmail.com'
subject = 'COMUNICADO IMPORTANTE'
mensagem = 'Lembre-se sua fatura vence hoje!'
send_mail(remetente, senha, destinatario, subject, mensagem)
