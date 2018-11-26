#!/usr/bin/env python
# -*- coding: utf-8 -*-

# encoding=utf8 
import sys
from fluentmail.backends import SMTP, SSL
from fluentmail import Message

content =  sys.stdin.read()

if(len(sys.argv) < 2):
	print('warning: Email user and subject is madatory!')
	exit();

toUser = sys.argv[1]
subject = sys.argv[2]

message = Message(subject, html=content, from_address='name@domain.com', to=toUser)

# message.attach_file('/home/silas/Downloads/1245540689.jpg')

client = SMTP('smtp.domain.com', user='name@domain.com', password='xxxxxxxxx', security=SSL)

client.send(message)

# How to use? 
# $: cat file.html > python humansmtp.py 'name@domain.com' 'subject is here'