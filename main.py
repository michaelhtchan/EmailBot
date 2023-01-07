import smtplib
import ssl
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import yfinance as yf
import pandas as pd

jpy=yf.Ticker('HKDJPY=X')
hist=pd.DataFrame(jpy.history(period='max'))
price_tdy=(1/hist.iat[-1,1])
day_before=(1/hist.iat[-2,1])

nowtime=str(pd.Timestamp.now())[0:10]
latest=str(hist.index[-1])[0:10]
day_before_time=str(hist.index[-2])[0:10]

if (nowtime==latest):

    space=str(" ")
    emaillist=['htmichaelchan1498@gmail.com', '1155157803@link.cuhk.edu.hk','micahpeter.12345@gmail.com','winkie426@gmail.com','1155159347@link.cuhk.edu.hk']
    emaillisttest=['htmichaelchan1498@gmail.com', 'micahpeter.12345@gmail.com','1155157803@link.cuhk.edu.hk']
    em = EmailMessage()
    sender='emmanuelgordon.2023@gmail.com';password = 'iaotaylrgvdqqcje'

    em['From'] = sender
    body = nowtime +': '+ str(price_tdy) + '\n'+str(day_before_time)+': '+ str(day_before)+'\n200 Day Average: ' + str(1/jpy.info['twoHundredDayAverage']) +'\n52 Week: '+str( 1/jpy.info['fiftyTwoWeekLow'])
    em.set_content(body)
    em['Subject'] = "JPY to HKD Exchange on " + space + nowtime+ space+ " is at "+str(price_tdy)[0:6]
    for i in emaillisttest:
        em['To'] = i
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(sender, password)
            smtp.sendmail(sender, i, em.as_string())
        del em['To']
        print("Email sent to " + i)
else:
    print('Not a market day!')