nama = raw_input ("masukan nama : ")
password = raw_input  ("masukan password : ")
if nama == "deniganz" and password == "ganz":
  print "welcome Mr.Ds"
elif nama == "user1" and password == "user1":
  print "welcome Mr.Ds"
elif nama == "user2" and password == "user2":
  print "hay welcome Mr.Ds"
else:
  print "sapa lu woy"

import random
import os, sys
# Warna
G = "\033[32m";
O = "\033[33m";
B = "\033[36m";
R = "\033[31m";
W = "\033[0m";
P = "\033[35m";
print ""
print ""
 
print O+"create by : mrds"
print O+"contant me : 081274083829"
print R+"permainan batu gunting kertas"
print R+"bissmilah dulu cuy:v"
print O+"============================="
print O+"  ///////        ///////"
print B+"    //  //   // //   // ///////"
print B+"   //  //   // /////// //   //"
print R+"  //  /////// //   // //   //"
print R+"============================="
print R+"    ////,   /////"
print P+"   //  //  //"
print P+"  //  //  /////"
print G+" /// //     //"
print G+"/////`  /////"
print G+"============================="
print ""
print P+"pilihan :"
print ""
print G+"1, batu"
print B+"2, gunting"
print W+"3, kertas"

def restart():
        ngulang = sys.executable
        os.execl(ngulang, ngulang, *sys.argv) 
def permainan():
    kamu = int(input("masukan pilihanmu: "))
    kom = random.choice(["batu", "gunting", "kertas"])
    if kamu == 1:
        print G+"kamu    : batu"
        print("komputer :", kom)
        if kom == "batu":
           print G+"\tdraw"
        if kom == "gunting":
           print B+"\tlu menang"
        if kom == "kertas":
           print W+"\tlu kalah"
    if kamu == 2:
        print B+"kamu     : gunting"
        print("komputer :", kom)
        if kom == "batu":
           print G+"\tkamu kalah"
        if kom == "batu":
           print R+"\tkamu kalah"
        if kom == "guntimg":
           print W+"\tdraw"
        if kom == "kertas":
           print B+"\tlu menang"
    if kamu == 3:
        print B+"kamu     : kertas"
        print("komputer :", kom)
        if kom == "batu":
           print G+"\tlu menang"
        if kom == "gunting":
           print W+"\tlu kalah"
        if kom == "kertas":
           print B+"\tdraw"
    if kamu >=4:
      print R+"pilihanmu salah!!!"
      restart()
permainan()
restart()
try:
	permainan()
except keyboardinterrupt:
	os.system('clear')
	restart()
