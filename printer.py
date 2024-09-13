from patient import *
from tabulate import tabulate
import time

def print_notification(message, alert = "default", timeout = 0):
    if alert == "danger":
        color_code = "\033[31m"
    elif alert == "success":
        color_code = "\033[32m"
    elif alert == "warning":
        color_code = "\033[33m"
    elif alert == "info":
        color_code = "\033[34m"
    else:
        color_code = "\033[0m"

    padding = (50 - len(message) - 2) // 2
    offset = 0;
    if len(message) % 2 == 1:
        offset = 1
    separator = "-" * (50 - 2)
    print(f"{color_code}+{separator}+")
    print(f"|{' ' * padding}{message}{' ' * padding}{' ' * offset}|")
    print(f"+{separator}+\033[0m")
    time.sleep(timeout)

def print_separator():
    print("=" * 50)

def print_option(order, message):
    padding = (50 - len(message) - 10)
    print(f"|  {order}.    {message}{' ' * padding}|")

def print_patient(patient):
    if patient == None:
        print_notification("Pasien tidak ditemukan", "info", 0.5)
    else:
        table_data = [
            ["ID", patient["id"]],
            ["Nama", patient["nama"]],
            ["Usia", patient["usia"]],
            ["Jenis Kelamin", patient["jenis_kelamin"]],
            ["Nomor Kamar", patient["nomor_kamar"]],
            ["BPJS", patient["bpjs"]]
        ]
        print(tabulate(table_data, tablefmt="fancy_grid"))


def print_all_patients(patient_list):
    if len(patient_list) == 0:
        print_notification("Tidak ada data pasien", "info")
    else:
        table_data = []
        table_headers = ["ID", "Nama", "Usia", "Jenis Kelamin", "Nomor Kamar", "BPJS"]
        for patient in patient_list:
            table_data.append([
                patient["id"], 
                patient["nama"], 
                patient["usia"], 
                patient["jenis_kelamin"], 
                patient["nomor_kamar"], 
                patient["bpjs"]
            ])
        print(tabulate(table_data, headers = table_headers, tablefmt = "fancy_grid"))

def print_all_patient_histories(patient_history_list):
    if len(patient_history_list) == 0:
        print_notification("Tidak ada history data pasien", "info")
    else:
        table_data = []
        table_headers = ["ID", "Nama", "Usia", "Jenis Kelamin", "Nomor Kamar", "BPJS", "Action", "Timestamp"]
        for patient_history in patient_history_list:
            table_data.append([
                patient_history["id"], 
                patient_history["nama"], 
                patient_history["usia"], 
                patient_history["jenis_kelamin"], 
                patient_history["nomor_kamar"], 
                patient_history["bpjs"],
                patient_history["action"],
                patient_history["timestamp"]
            ])
        print(tabulate(table_data, headers = table_headers, tablefmt = "fancy_grid"))

def print_continue_prompt():
    print("Tekan <Enter> untuk melanjutkan...")
    input()

def show_menu():
    print_notification("Rumah Sakit PWDK")
    print_option(1, "Daftar Semua Pasien")
    print_option(2, "Tambah Data Pasien Baru")
    print_option(3, "Perbarui Data Pasien")
    print_option(4, "Hapus Data Pasien")
    print_option(5, "Audit Data Pasien")
    print_option(6, "Keluar")
    print_separator()

def show_list_menu():
    print_notification("Daftar Pasien")
    print_option(1, "Seluruh Daftar Pasien")
    print_option(2, "Cari Pasien Berdasarkan ID")
    print_option(3, "Cari Pasien Berdasarkan Kamar")
    print_option(4, "Filter Data Pasien")
    print_option(5, "Kembali")
    print_separator()

def show_operation_menu(operation):
    print_notification(f"{operation} Data Pasien")
    print_option(1, f"{operation} Pasien")
    print_option(2, "Kembali")
    print_separator()
