#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import re

def send_email(SUBJECT='',TEXT=''):
            import smtplib

            gmail_user = "user.name@gmail.com"
            gmail_pwd = "password"
            FROM = 'user.name@gmail.com'
            TO = ['user.name@gmail.com'] #must be a list

            message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
            """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
            try:
                #server = smtplib.SMTP(SERVER)
                server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
                server.ehlo()
                server.starttls()
                server.login(gmail_user, gmail_pwd)
                server.sendmail(FROM, TO, message)
                #server.quit()
                server.close()
                # print 'successfully sent the mail'
            except:
                print "failed to send mail"

LIB_MESSAGE='הרשומה המבוקשת לא קיימת במאגר' # message given when item is not found

fp=open("/path/to/isbns.txt")
for isbn in fp:
    if len(isbn.rstrip('\n').split(' ',1))>1:
       message=isbn.rstrip('\n').split(' ',1)[1]
    else:
       message=''
    f = urllib2.urlopen('http://alephprd.tau.ac.il/F/?find_code=ISBN&func=find-b&local_base=U-TAU01&request='+isbn.rstrip('\n').split()[0])
    res=f.read()
    if re.search(LIB_MESSAGE,res)==None:
        send_email('ISBN '+isbn.rstrip('\n').split()[0]+' found at TAU!',message)
fp.close()
