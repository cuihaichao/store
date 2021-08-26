import smtplib
from email.header import Header  # header()定义邮件标题
from email.mime.text import MIMEText # MIMEText()定义邮件正文
from email.mime.multipart import MIMEMultipart   # 附件

mail_host = "smtp.qq.com"    # 邮箱服务器
user = "207988470@qq.com"
password = "usaaltuqxvcdcabe"   # 邮箱授权码
sender = "207988470@qq.com"   # 发送邮箱
receiver = "207988470@qq.com"    # 接受邮箱
subject = "计算器测试报告"

message = MIMEMultipart()  # 附件管理器
message["from"] = Header("崔海朝","utf-8")
message["TO"] = Header("测试", "utf-8")
message["Subject"] = Header(subject, "utf-8")

message.attach(MIMEText("这是附件", "plain", "utf-8"))
# 构造附件1，传送当前目录下的 test.txt 文件
att1 = MIMEText(open('计算器测试报告.html').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment;filename="computer.html"'
message.attach(att1)
try:
    smtp = smtplib.SMTP()  # smtp()发送器
    smtp.connect(mail_host)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, att1.as_string())
    smtp.quit()
    print("发送成功")
except Exception as error:
    print("发送失败")
