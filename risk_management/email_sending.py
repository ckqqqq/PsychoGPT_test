import smtplib
import email
# 负责构造文本
from email.mime.text import MIMEText
# 负责构造图片
from email.mime.image import MIMEImage
# 负责将多个对象集合起来
from email.mime.multipart import MIMEMultipart
from email.header import Header
import email_setting

def send_email(history_:str):
    mm = MIMEMultipart('related')
    subject_content="""PsychoGPT 心理危机预警"""
    ### 
    mm["From"]=f"keqi_c<{email_setting.mail_sender}>"
    target_list=[]
    for target in email_setting.mail_receivers:
        prefix=target.split("@")[0]
        if prefix:
            target_list.append(f"{prefix}<{target}>")
    mm["To"]=",".join(target_list)
    mm["Subject"]=Header(subject_content,'utf-8')
    # 邮件正文内容
    body_content = f"""你好，咨询者存在心理危机，需要人工干预介入，下面为咨询者对话历史:\n{history_}"""
    ### 构造文本
    message_text=MIMEText(body_content,"plain","utf-8")
    mm.attach(message_text)
    
    stp=smtplib.SMTP()
    # stp.connect("smtp.qq.com","465")# 端口和地址
    stp.connect("smtp.163.com","25")
    # stp.sendmail(mail_se)
    print(body_content)
    
    
    stp.set_debuglevel(1)
    stp.login(email_setting.mail_sender,email_setting.mail_license)
    stp.sendmail(email_setting.mail_sender,email_setting.mail_receivers,mm.as_string())
    stp.quit()
send_email("你好")
