from input_validator import *
            
def process_list():
    while True:
        show_list_menu()
        option = input("Silahkan pilih menu [1-5]: ")
        if option == "1":
            print_all_patients(patient_list)
            print_continue_prompt()
        elif option == "2":
            id = input("Masukkan ID Pasien: ")
            patient = find_patient("id", id)
            print_patient(patient)
            print_continue_prompt()
        elif option == "3":
            room_number = input("Masukkan Nomor Kamar: ")
            if room_number in room_list:
                patient = find_patient("nomor_kamar", room_number)
                print_patient(patient)
                print_continue_prompt()
            else:
                print_notification("Nomor kamar tidak valid", "danger", 0.25)
        elif option == "4":
            process_filter()
        elif option == "5":
            break
        else:
            print_notification("Menu tidak tersedia", "danger", 0.25)

def process_filter():
    print_notification("Filter Data Pasien")
    print("Masukkan parameter pencarian atau kosongkan untuk melewati")
    name = input_validate_name("Nama: ", True)
    age_min = input_validate_number("Usia Min: ", True)
    age_max = input_validate_number("Usia Max: ", True)
    gender = input_validate_gender("Jenis Kelamin: ", True)
    bpjs = input_validate_boolean("Terdaftar BPJS? [Y/N]:", "BPJS", True)
    filtered_patient_list = filter_patient(name, age_min, age_max, gender, bpjs)
    print_all_patients(filtered_patient_list)
    print_continue_prompt()

def process_operation(operation, callback):
    while True:
        show_operation_menu(operation)
        option = input("Silahkan pilih menu [1-2]: ")
        if option == "1":
            callback()
        elif option == "2":
            break
        else:
            print_notification("Menu tidak tersedia", "danger", 0.25)

def process_create():
    print_notification("Tambah Data Pasien")
    print("Masukkan data pasien")
    id = input_validate_id("ID: ")
    nama = input_validate_name("Nama: ")
    usia = input_validate_number("Usia: ")
    jenis_kelamin = input_validate_gender("Jenis Kelamin [L/P]: ")
    nomor_kamar = input_validate_room_number("Nomor Kamar: ")
    bpjs = input_validate_boolean("Apakah Pasien BPJS? [Y/N]: ", "BPJS")
    patient = { "id": id, "nama": nama, "usia": usia, "jenis_kelamin": jenis_kelamin, "nomor_kamar": nomor_kamar, "bpjs": bpjs }
    print_notification("Konfirmasi Penambahan Data Pasien", "warning",  0.25)
    print_patient(patient)
    confirm = input_validate_boolean("Tambah Data Pasien? [Y/N]: ", "Konfirmasi")
    if confirm:
        add_patient(patient)
        add_patient_history("Tambah", patient)
        print_notification("Berhasil menambah pasien", "success",  0.25)
    else:
        print_notification("Batal menambah pasien", "info",  0.25)

def process_update():
    print_notification("Perbarui Data Pasien")
    patient = input_validate_id("Masukkan ID: ", True)
    print_patient(patient)
    print("Masukkan data terbaru atau kosongkan untuk jika tidak berubah")
    nama = input_validate_name(f"Nama Terbaru: ", True)
    usia = input_validate_number("Usia Terbaru: ", True)
    jenis_kelamin = input_validate_gender("Jenis Kelamin Terbaru [L/P]: ", True)
    nomor_kamar = input_validate_room_number("Nomor Kamar: ", True, patient["id"], True)
    bpjs = input_validate_boolean("Apakah Pasien BPJS? [Y/N]: ", "BPJS", True)

    updated_patient = { 
        "id": patient["id"], 
        "nama": patient["nama"] if nama == None else nama, 
        "usia":  patient["usia"] if usia == None else usia, 
        "jenis_kelamin": patient["jenis_kelamin"] if jenis_kelamin == None else jenis_kelamin, 
        "nomor_kamar": patient["nomor_kamar"] if nomor_kamar == None else nomor_kamar, 
        "bpjs": patient["bpjs"] if bpjs == None else bpjs
    }
    if (updated_patient == patient):
        print_notification("Tidak ada perubahan data pasien", "info",  0.25)
        return
    
    print_notification("Konfirmasi Pembaruan Data Pasien", "warning",  0.25)
    print_patient(updated_patient)
    confirm = input_validate_boolean("Perbarui Data Pasien? [Y/N]: ", "Konfirmasi")
    if confirm:
        add_patient_history("Perbarui", patient, updated_patient)
        update_patient(patient, updated_patient)
        print_notification("Berhasil perbarui pasien", "success",  0.25)
    else:
        print_notification("Batal perbarui pasien", "info",  0.25)

def process_delete():
    print_notification("Hapus Data Pasien")
    patient = input_validate_id("Masukkan ID: ", True)
    print_notification("Konfirmasi Hapus Data Pasien", "warning",  0.25)
    print_patient(patient)
    confirm = input_validate_boolean("Hapus Data Pasien? [Y/N]: ", "Konfirmasi")
    if confirm:
        delete_patient(patient)
        add_patient_history("Hapus", patient)
        print_notification("Berhasil hapus pasien", "success",  0.25)
    else:
        print_notification("Batal hapus pasien", "info",  0.25)

def process_audit():
    print_notification("Audit Data Pasien")
    print_all_patient_histories(patient_history_list)
    print_continue_prompt()
