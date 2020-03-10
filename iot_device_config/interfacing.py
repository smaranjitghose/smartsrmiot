from typing import List
from firebase import firebase
import RPi.GPIO as GPIO
import time
import subprocess
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


def main():
    # initializing firebase cred
    cred = credentials.Certificate("path/to/serviceAccountKey.json")
    firebase_admin.initialize_app(cred)
    # database init
    ref_stud = db.collection('STUDENT')
    ref_faculty = db.collection('FACULTY')
    # code for attendance grant
    device_id = "TP000"
    time_window = 10
    while 1:
        doc_faculty = ref_faculty.document('FACULTY')
        doc_stud = ref_stud.document('STUDENT')
        if get_nfc_id() in doc_faculty.values():
            start_time = time.time()
            present_id = get_nfc_id()
            if time.time() - start_time <= time_window and present_id in doc_stud.value():
                str_id_p = str(present_id)
                time_now = time.time()
                data_ifPresent = {"DEVICE ID": device_id, "ID": str_id_p, "BOOLEAN VALUE": 'true', "TIME STAMP": time_now}
                ref_stud.reset(data_ifPresent)
                print(data_ifPresent)


def get_nfc_id():
    while 1:  # later this will contain the class( distinguished by DEVICE ID) information
        myLines = get_nfc_out()
        buffer = []
        for line in myLines.splitlines():
            line_content = line.split()
            if not line_content[0] == 'UID':
                pass
            else:
                buffer.append(line_content)
        str = buffer[0]
        id_str = str[2] + str[3] + str[4] + str[5]
        return id_str


def get_nfc_out():
    lines = raw_nfc()
    return lines


def raw_nfc():
    lines = subprocess.check_output("usr/bin/nfc-poll", stderr=open('/dev/null', 'w'))
    return lines
