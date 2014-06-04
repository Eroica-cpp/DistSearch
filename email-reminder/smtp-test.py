"""
Reference: http://blog.sina.com.cn/s/blog_68b1a51b0100upx1.html
"""

import smtplib, mimetypes  
from email.mime.text import MIMEText  
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import sys

password = sys.argv[1]
from_add = "szucse@163.com"
to_add = "china.litao@163.com"

msg = MIMEMultipart()
msg["From"] = from_add
msg["To"] = to_add
msg["Subject"] = "Test SMTP by Python"

text = MIMEText("This is text content.")
msg.attach(text)

# filename=r'F:\Novel\peach.zip'
# ctype,encoding = mimetypes.guess_type(filename)
# if ctype is None or encoding is not None:
#     ctype='application/octet-stream'
# maintype,subtype = ctype.split('/',1)

# #att=MIMEImage(open(filename,'r').read(),subtype)
# att=MIMEImage(open(filename, 'rb').read(),subtype)
# print ctype,encoding
# att["Content-Disposition"] = 'attachmemt;filename="peach.zip"'
# msg.attach(att)

smtp = smtplib.SMTP()
smtp.connect("smtp.163.com")
smtp.login(from_add, password)
smtp.sendmail(msg["From"], msg["To"], msg.as_string())

smtp.quit()
print 'send mail successfully'