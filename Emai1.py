# coding:utf-8
# 参考   https://www.cnblogs.com/sundawei7/p/11948961.html
import smtplib
from email.mime.text import MIMEText


print("START")



smtp_host = 'smtp.qq.com'  # 设置发件服务器地址
smtp_port = 465  # 设置发件服务器端口号。注意，这里有SSL和非SSL两种形式
smtp_sender = 'whale_hunter@qq.com'  # 设置发件邮箱,用户名
smtp_pwd = 'qhbrpezdaothgiig'  # 设置发件邮箱的密码  qhbrpezdaothgiig


mime_body = '这是邮件正文' # 设置邮件正文，这里是支持HTML的
mime_subject="这是邮件标题"
mime_from=smtp_sender
mime_to = ['lindadarling@yeah.net', 'liangyipei@cmbc.com.cn'] # 设置邮件接收人

msg = MIMEText(mime_body, 'html','utf-8') # 设置正文为符合邮件格式的HTML内容，还可以选择纯文本plain
msg['subject'] = mime_subject # 设置邮件标题
msg['from'] = smtp_sender  # 设置发送人
msg['to'] = ';'.join(mime_to)  # 设置接收人
#msg['date']="2029-12-31" #若无时间，就默认一般为当前时间，该值一般不设置

s = smtplib.SMTP_SSL(smtp_host, smtp_port)  # 注意！如果是使用SSL端口，这里就要改为SMTP_SSL，否则用SMTP
s.login(smtp_sender, smtp_pwd)  # 登陆邮箱
s.sendmail(smtp_sender, mime_to, msg.as_string())  # 发送邮件！
s.close()

print("FINISH")