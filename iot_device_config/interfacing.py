from firebase import firebase
import RPi.GPIO as GPIO
import time
import subprocess

n = 3 # number of students in the class
device_id = "TP000"
time_window = 10


def update_fire():
    firebase = firebase.FirebaseApplication('https://iot-studentreg.firebaseio.com/', None)
    ref_faculty = firebase.get('Faculty/All_ID', None)
    ref_faculty_val = ref_faculty.value()
    ref_stud = firebase.get('Student/Attendance/All_ID', None)
    ref_stud_val = ref_stud.value()
    if get_nfc_id() in ref_faculty_val:
        start_time = time.time()
        present_id = get_nfc_id()
        for i in range(n):
            if time.time() - start_time <= time_window and present_id in ref_stud_val:
                str_id_p = str(present_id)
                data_ifPresent = {"ID": str_id_p, "PRESENT": 'true', "TIME STAMP": time.time()}
                firebase.post('Student/Attendance/s' + str(i), data_ifPresent)
                print(data_ifPresent)
                print('Above data entered')
            elif time.time() - start_time > time_window:
                for ids in ref_stud_val:
                    data_notPresent = {"ID": ids, "PRESENT": 'false', "TIME STAMP": time.time()}
                    firebase.post('Student/Attendance/s' + str(i), data_notPresent)
                    print(data_notPresent)
                    print('Above data is submitted')
            elif present_id not in ref_stud_val or present_id not in ref_faculty_val:
                print('Unidentified ID, no data is submitted')


def get_nfc_id():
    while 1:  # later this will contain the class (distinguished by DEVICE ID) information
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
