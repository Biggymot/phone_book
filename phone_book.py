import pickle

phone_book = [{"surname": "Bogach", "name": "Dmytro", "age": 36}]

def print_entry(number, entry):
    print "[ " + str(number) + " ]" + "-----------------"
    print "Surname:    " + entry["surname"]
    print "Name:    " + entry["name"]
    print "Age:     " + str(entry["age"])


def print_phonebook():
    print ""
    print "###### Phone book #######"
    print ""

    number = 1
    for entry in phone_book:
        print_entry(number, entry)
        number += 1


def add_entry_phonebook(surname, name, age):
    entry = {}
    entry["surname"] = surname
    entry["name"] = name
    entry["age"] = age
    phone_book.append(entry)


def printMessage(message):
    print "MESSAGE: %s" % message


def find_entry_name_phonebook(name):
    for entry in phone_book:
        if entry["name"] == name:
            print_entry(1, entry)
            return
    printMessage("Not found!!")


def find_entry_age_phonebook(age):
    for entry in phone_book:
        if entry["age"] == age:
            print_entry(1, entry)
            return
    printMessage("Not found!!")


def delete_entry_name_phonebook(name):
    for entry in phone_book:
        if entry["name"] == name:
            phone_book.remove(entry)
            return
    printMessage("Not found!!")


def count_all_entries_in_phonebook():
    print len(phone_book)


def print_all_pensioners():
    number = 1
    for entry in phone_book:
        if isPensioner(entry):
            print_entry(number, entry)
            number += 1

def count_all_pensioners():
    pensioners = 0
    for entry in phone_book:
        if isPensioner(entry):
            pensioners += 1
    print pensioners


def avr_age_of_all_pensioners():
    pensioners = []
    for entry in phone_book:
        if isPensioner(entry):
            pensioners.append(entry)
    total_age = 0
    for entry in pensioners:
        total_age += entry.get("age")
    print total_age / len(pensioners)


def print_all_students():
    number = 1
    for entry in phone_book:
        if isStudent(entry):
            print_entry(number, entry)
            number += 1


def increase_age(nmbr_of_years):
    for entry in phone_book:
        entry["age"] = entry.get("age") + nmbr_of_years


def update_name():
    for entry in phone_book:
        if isStudent(entry):
            entry["name"] = entry["name"] + ' - student'

    for entry in phone_book:
        if isPensioner(entry):
            entry["name"] = entry["name"] + ' - pensioner'


def func(item):
    return item["age"]

def sorted_by_age():
    phone_book = sorted(phone_book, key=func)
    print phone_book


def isStudent(entry):
    return entry["age"] in range(17, 26)


def isPensioner(entry):
    return entry["age"] >= 65


def save_to_file():
    pickle.dump(phone_book, open("phone_book.save", "wb"))
    printMessage("Phonebook is saved into 'phone_book.save'")


def load_from_file():
    global phone_book
    phone_book = pickle.load(open("phone_book.save", "rb"))
    printMessage("Phonebook is loaded from 'phone_book.save'")


def main():
    while True:
        user_input = ""
        try:
            print ""
            print ""
            print ""
            print "~ Welcome to Dmitry Bogach phonebook ~"
            print "Select one of actions below:"
            print "     1 - Print phonebook entries"
            print "     2 - Add new entry"
            print "     3 - Find entry by name"
            print "     4 - Find entry by age"
            print "     5 - Delete entry by name"
            print "     6 - The number of entries in the phonebook"
            print "     7 - Print all pensioners"
            print "     8 - The number of all pensioners"
            print "     9 - Avr. age of all pensioners"
            print "     10 - Print all students"
            print "     11 - Increase age"
            print "     12 - Update name"
            print "     13 - Sorted by age"
            print "-----------------------------"
            print "     s - Save to file"
            print "     l - Load from file"
            print "     0 - Exit"

            user_input = raw_input("Enter you choice: ")
            choice = int(user_input)

            if choice == 1:
                print_phonebook()
            elif choice == 2:
                surname = str(raw_input("    Enter surname: "))
                name = str(raw_input("    Enter name: "))
                age = int(raw_input("    Enter age: "))
                add_entry_phonebook(surname, name, age)
            elif choice == 3:
                name = str(raw_input("    Enter name: "))
                find_entry_name_phonebook(name)
            elif choice == 4:
                age = int(raw_input("    Enter age: "))
                find_entry_age_phonebook(age)
            elif choice == 5:
                name = str(raw_input("    Enter name: "))
                delete_entry_name_phonebook(name)
            elif choice == 6:
                count_all_entries_in_phonebook()
            elif choice == 7:
                print_all_pensioners()
            elif choice == 8:
                count_all_pensioners()
            elif choice == 9:
                avr_age_of_all_pensioners()
            elif choice == 10:
                print_all_students()
            elif choice == 11:
                nmbrs_of_years = int(raw_input("    Enter number of years: "))
                increase_age(nmbrs_of_years)
            elif choice == 12:
                update_name()
            elif choice == 13:
                sorted_by_age()
            elif choice == 0:
                print "Bye!"
                break
            else:
                print "Enter action within range [0..8]"

        except ValueError:
            if str(user_input) == 's':
                save_to_file()
            elif str(user_input) == 'l':
                load_from_file()
            else:
                print "Oops!  Something went wrong.  Try again..."


if __name__ == '__main__':
    main()