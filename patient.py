import datetime

room_list = [
    "101", "102", "103", "104", "105",
    "201", "202", "203", "204", "205",
    "301", "302", "303", "304", "305"
]
patient_list = [
    {"id": "001", "nama": "Andi", "usia": 30, "jenis_kelamin": "Laki-laki", "nomor_kamar": "101", "bpjs": True},
    {"id": "002", "nama": "Budi", "usia": 58, "jenis_kelamin": "Laki-laki", "nomor_kamar": "102", "bpjs": False},
    {"id": "003", "nama": "Chika", "usia": 18, "jenis_kelamin": "Perempuan", "nomor_kamar": "103", "bpjs": True},
    {"id": "012", "nama": "Donny", "usia": 21, "jenis_kelamin": "Laki-laki", "nomor_kamar": "202", "bpjs": True},
    {"id": "022", "nama": "Emma", "usia": 7, "jenis_kelamin": "Perempuan", "nomor_kamar": "302", "bpjs": False},
]

patient_history_list = []

def add_patient(patient):
    patient_list.append(patient)

def update_patient(patient, updated_patient):
    patient.update(updated_patient)

def delete_patient(patient):
    patient_list.remove(patient)

def find_patient(key, value):
    for patient in patient_list:
        if patient[key] == value:
            return patient
    return None

def filter_patient(name, age_min, age_max, gender, bpjs):
    result = []
    for patient in patient_list:
        if (name == None or name.lower() in patient["nama"].lower()) and \
           (age_min == None or age_min <= patient["usia"]) and \
           (age_max == None or age_max >= patient["usia"]) and \
           (gender == None or gender == patient["jenis_kelamin"]) and \
           (bpjs == None or bpjs == patient["bpjs"]):
            result.append(patient)
    return result

def add_patient_history(action, patient, updated_patient = None):
    patient_history = {
        "id": patient["id"], 
        "nama": patient["nama"], 
        "usia": str(patient["usia"]),
        "jenis_kelamin": patient["jenis_kelamin"],
        "nomor_kamar": patient["nomor_kamar"],
        "bpjs": str(patient["bpjs"]),
        "action": action,
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    if action == "Perbarui":
        for key in patient.keys():
            if patient[key] != updated_patient[key]:
                patient_history[key] = patient_history[key] + " -> " + str(updated_patient[key])

    patient_history_list.append(patient_history)
