from controller import *

def run():
    while True:
        show_menu()
        option = input("Silahkan pilih menu [1-6]: ")
        if option == "1":
            process_list()
        elif option == "2":
            process_operation("Tambah", process_create)
        elif option == "3":
            process_operation("Perbarui", process_update)
        elif option == "4":
            process_operation("Hapus", process_delete)
        elif option == "5":
            process_operation("Audit", process_audit)
        elif option == "6":
            print_notification("Sampai jumpa!", "success",  0.25)
            break
        else:
            print_notification("Menu tidak tersedia", "danger",  0.25)

run()
