import time 
from datetime import datetime 
medicines ={}
logs=[]
def valid_time_formate(t):
    try: 
            datetime.strptime(t,"%H:%M")
            return True
    except:
        return False
def add_medicine():
    name = input("enter medicine name :")
    while True: 
         time_str = input("enter reminder time (HH:MM):")
         if valid_time_formate(time_str):
             break
         print("invalid time ! enter in HH:MM formate .")
         medicines[name] = time_str
         print(f"medicine'{name}'added successfully!\n")
def view_medicines():
    if not medicines :
        print (" no medicines scheduled.\n")
        return 
    print ("\n scheduled medicines:")
    for name , time_str in medicines.item ():
        print(f"-{name}:{time_str}")
        print ()
def delete_medicine():
    name = input("Enter medicine name to delete: ")

    if name in medicines:
        del medicines[name]
        print(f"'{name}' deleted successfully!\n")
    else:
        print("Medicine not found!\n")
def log_action(medicine, time_str, status):
    logs.append((medicine, time_str, status))        
def view_logs():
    if not logs:
        print("No logs available.\n")
        return

    print("\nMedicine Logs:")
    for med, t, status in logs:
        print(f"{med} at {t} → {status}")
    print()
def start_reminder():
    print("\nReminder Engine Started... (Press Ctrl+C to stop)\n")

    try:
        while True:
            now = datetime.now().strftime("%H:%M")

            for med, med_time in medicines.items():
                if now == med_time:
                    print(f"\n🔔 Reminder: Take your medicine → {med} ({med_time})")

                    taken = input("Did you take it? (yes/no): ").lower()

                    if taken == "yes":
                        log_action(med, med_time, "Taken")
                    else:
                        log_action(med, med_time, "Missed")

                    print()

            time.sleep(30)   # check every 30 seconds

    except KeyboardInterrupt:
        print("\nReminder engine stopped.\n")
def main_menu():
    while True:
        print("===== SMART MEDICINE REMINDER =====")
        print("1. Add Medicine")
        print("2. View Medicines")
        print("3. Delete Medicine")
        print("4. View Logs")
        print("5. Start Reminder Engine")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_medicine()
        elif choice == "2":
            view_medicines()
        elif choice == "3":
            delete_medicine()
        elif choice == "4":
            view_logs()
        elif choice == "5":
            start_reminder()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.\n")
main_menu()             