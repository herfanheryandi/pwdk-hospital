import re
from printer import *

def input_validate_number(message, allow_blank = False):
    while True:
        try:
            number = input(message)
            if not number and allow_blank == True:
                return None
            elif int(number) >= 0 and int(number) <= 100:
                return int(number)
            else:
                print_notification("Input harus berada di antara 0 dan 100", "danger", 0.5)
        except:
            print_notification("Input harus berupa angka", "danger", 0.5)

def input_validate_id(message, is_update = False):
    while True:
        id = input(message)
        if not id:
            print_notification("ID tidak valid", "danger", 0.5)
            continue

        patient = find_patient("id", id)
        if is_update == False and patient == None:
            return id
        elif is_update == True and patient != None:
            return patient
        elif is_update == True and patient == None:
            print_notification("ID tidak ditemukan", "danger", 0.5)
        else:
            print_notification("ID sudah terdaftar", "danger", 0.5)

def input_validate_name(message, allow_blank = False):
    while True:
        name = input(message)
        name_regex = r"^[A-Za-z\s]+$"
        if not name and allow_blank == True:
            return None
        elif re.match(name_regex, name):
            return name
        else:
            print_notification("Nama tidak valid", "danger", 0.5)

def input_validate_gender(message, allow_blank = False):
    while True:
        gender = input(message).upper()
        if gender == 'L':
            return "Laki-laki"
        elif gender == 'P':
            return "Perempuan"
        elif not gender and allow_blank == True:
            return None
        else:
            print_notification("Jenis kelamin tidak valid", "danger", 0.5)

def input_validate_room_number(message, is_update = False, id = None, allow_blank = False):
    while True:
        room_number = input(message)
        if not room_number and allow_blank == True:
            return None
        
        if room_number in room_list:
            patient = find_patient("nomor_kamar", room_number)
            if patient == None or (is_update == True and patient["id"] == id):
                return room_number
            else:
                print_notification("Nomor kamar sudah terisi", "danger", 0.5)
        else:
            print_notification("Nomor kamar tidak valid", "danger", 0.5)

def input_validate_boolean(message, field, allow_blank = False):
    while True:
        bool = input(message).upper()
        if bool == 'Y':
            return True
        elif bool == 'N':
            return False
        elif not bool and allow_blank == True:
            return None
        else:
            print_notification(f"{field} tidak valid", "danger", 0.5)