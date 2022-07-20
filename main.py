import json

import ijson


data = {"Events":
            [{"FileQualifier": "-8245771827931738520", "LastEventFileName": "setup.exe", "Hash": "SHA1##9f67f6d894677a6160022ad9df749eebb3388188", "EventName": "LSASS Credentials Harvesting", "PolicyName": "LSASS Credentials Harvesting", "Publisher": "Microsoft Corporation", "EventType": "SuspiciousActivity", "LastEventDate": "2022-05-11T19:08:05.153", "LastEventUserName": "NT AUTHORITY\\SYSTEM", "LastEventComputer": "GUUP-71429-WL", "LastEventID": 6841297879508338237, "ExposedUsers": 63, "AffectedComputers": 99, "ThreatDetectionAction": "Detected", "TotalEvents": 99}, {"FileQualifier": "-7042691806256115329", "LastEventFileName": "splunkd.exe", "Hash": "SHA1##8b5399ce4b6a05d0b2bb58719d655aa7c4be8aae", "EventName": "LSASS Credentials Harvesting", "PolicyName": "LSASS Credentials Harvesting", "Publisher": "Splunk, Inc.", "EventType": "SuspiciousActivity", "LastEventDate": "2022-05-11T12:00:35.893", "LastEventUserName": "NT AUTHORITY\\SYSTEM", "LastEventComputer": "XOR-BSA-198", "LastEventID": -6040796867252783254, "ExposedUsers": 3, "AffectedComputers": 8, "ThreatDetectionAction": "Detected", "TotalEvents": 32023}, {"FileQualifier": "6838070108005085872", "LastEventFileName": "WRSA.exe", "Hash": "SHA1##1833fa9d05288d76111a828795b2cd5663c2af84", "EventName": "Chrome Credentials Theft", "PolicyName": "Chrome Credentials Theft", "Publisher": "Webroot", "EventType": "Attack", "LastEventDate": "2022-05-11T12:00:29.563", "LastEventUserName": "NT AUTHORITY\\SYSTEM", "LastEventComputer": "SACHIN-KR", "LastEventID": -6100890561586794373, "ExposedUsers": 54, "AffectedComputers": 6, "ThreatDetectionAction": "Detected"
, "TotalEvents": 25}, {"FileQualifier": "6105545530662713660", "LastEventFileName": "SensorLogonTask.exe", "Hash": "SHA1##e4b9435489eefe29bdcfc286d554d8ebfc5f72eb", "EventName": "LSASS Credentials Harvesting", "PolicyName": "LSASS Credentials Harvesting", "Publisher": "Microsoft Corporation", "EventType": "SuspiciousActivity", "LastEventDate": "2022-05-11T11:59:49.99", "LastEventUserName": "NT AUTHORITY\\SYSTEM", "LastEventComputer": "SACHIN-KR", "LastEventID": -3510536330941853756, "ExposedUsers": 175, "AffectedComputers": 310, "ThreatDetectionAction": "Detected", "TotalEvents": 564}, {"FileQualifier": "6838070108005085872", "LastEventFileName": "WRSA.exe", "Hash": "SHA11833fa9d05288d76111a828795b2cd5663c2af84", "EventName": "LSASS Credentials Harvesting", "PolicyName": "LSASS Credentials Harvesting",
"Publisher": "Webroot", "EventType": "SuspiciousActivity", "LastEventDate": "2022-05-11T11:58:35.113", "LastEventUserName": "NT AUTHORIY\\SYSTEM", "LastEventComputer": "SACHIN-KR", "LastEventID": 2258039075004769820, "ExposedUsers": 1, "AffectedComputers": 6, "ThreatDetectionAction": "Detected", "TotalEvents": 945}]}

import socket
import threading
import os

import buffer

import os
# path of the current script
path = 'D:\entryes'
HOST = '127.0.0.1'
PORT = 2345
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s = socket.socket()
s.connect(('localhost',8008))
# Before creating
dir_list = os.listdir(path)


# Creates a new file
# a to new file uncomment
    # this fp.write("New file created")
class Data:
    def send_string(sock, string):
        sock.sendall(string.encode() + b'\n')

    def send_int(sock, integer):
        sock.sendall(str(integer).encode() + b'\n')


    def DevideAndSendData(self):
        for ankur in data["Events"]:
            fileName = ankur['FileQualifier']
            if fileName.startswith("-"):
                fileName = fileName.lstrip("-")
            with open(os.path.join(path, fileName), 'w') as fp:
                print("dumped files",fp.write(json.dumps(ankur)))
        p=1
        return p

    def transmit(sock, folder):
        print(f'Sending folder: {folder}')
        D.send_string(sock, folder)
        global files
        files = os.listdir(folder)
        D.send_int(sock, len(files))
        for file in files:
            path = os.path.join(folder, file)
            filesize = os.path.getsize(path)
            print(f'Sending file: {file} ({filesize} bytes)')
            D.send_string(sock, file)
            D.send_int(sock, filesize)

    def deleteFiles(path):
        print(files)
        for file in files:
            print("Deleting File:-",file)
            os.remove(os.path.join(path, file))

D = Data
p=0
D.DevideAndSendData(self=p)
path = 'D:\entryes'
D.transmit(s,path)
D.deleteFiles(path)
