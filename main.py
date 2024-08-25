import getpass
import time
import os
def search_word_in_logs(file_path, search_word):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        found = False
        for line_number, line in enumerate(lines, start=1):
            if search_word in line:
                print(f'Results: {line.strip()}')
                found = True

        if not found:
            print(f'Word "{search_word}" not found in the file.')

    except FileNotFoundError:
        print(f'The file "{file_path}" does not exist.')
    except Exception as e:
        print(f'An error occurred: {e}')
def add_name_to_logs(file_path, name):
    try:
        with open(file_path, 'a') as file:
            file.write(f'{name}\n')
        print(f'Name "{name}" has been added to the file.')
    except Exception as e:
        print(f'An error occurred: {e}')

def main():
    while True:
        print("\nMenu:")
        print("1. Add a name")
        print("2. Search for a name")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            password = input("Enter the password to add a name: ")
            if password == 'ADMIN':
                os.system('clear')
                info = input("Enter the citizen to add: [First and Last Roleplay Name, Discord ID, Roleplay Age, Roleplay Gender]: ")
                os.system('clear')
                add_name_to_logs('logs.txt', "--------------------")
                add_name_to_logs('logs.txt', info)
                add_name_to_logs('logs.txt', "--------------------")
                os.system('clear')
                print("Authenticating...")
                time.sleep(2)
                os.system('clear')
                print("Uploading 1%")
                time.sleep(0.25)
                os.system('clear')
                print("Uploading 5%")
                time.sleep(0.4)
                os.system('clear')
                print("Uploading 48%")
                time.sleep(1)
                os.system('clear')
                print("Uploading 87%")
                time.sleep(2)
                os.system('clear')
                print("Uploading 99%")
                time.sleep(2)
                os.system('clear')
                print("Uploading Completed, the name has been added to the database.")
                time.sleep(5)
                os.system('clear')
            else:
                print("Invalid password. Access denied.")

        elif choice == '2':
            search_word = input("Enter the word to search for: ")
            os.system('clear')
            results = search_word_in_logs('logs.txt', search_word)
            
            print(results)
            skip = input("Press enter to continue...")

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == '__main__':
    main()
