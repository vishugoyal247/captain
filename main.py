from file import File
from random import choice


class Main:

    def __init__(self):

        # The file_handler object will be used to read and write to files.
        self.file_handler = File()

        login_menu_is_running = True

        while login_menu_is_running:

            print('1 - Sign up')
            print('2 - Login')

            menu_choice = input('\nEnter menu option: ')

            login_menu_is_running = False

            if menu_choice == '1':
                self.signup()
            elif menu_choice == '2':
                self.login()
            else:
                print('Please choose a number from the menu.')
                login_menu_is_running = True

        menu_is_running = True

        while menu_is_running:

            print('\n1 - Add a new student to the system.')
            print('2 - Display a student\'s details.')
            print('3 - Edit a students details.')
            print('4 - Log out.')

            menu_choice = input('\nEnter menu option: ')

            if menu_choice == '1':
                self.add_student()

            elif menu_choice == '2':
                self.print_student_details()

            elif menu_choice == '3':
                self.edit_student_details()

            elif menu_choice == '4':
                menu_is_running = False

            else:
                print('Please choose a number from the menu.')

    def signup(self):

        username = input('Enter username: ')
        password = input('Enter password: ')

        if len(password) < 8:
            print('Password should contain at lease 8 characters.')
            self.signup()
        else:
            self.file_handler.add_account(username, password)

    def login(self):

        accounts = self.file_handler.get_accounts()

        input_loop = True

        while input_loop:

            username_attempt = input('Enter username: ')

            for account in accounts:

                account = account.split(', ')

                if username_attempt == account[0]:

                    password_attempt = input('Enter password: ')

                    if password_attempt == account[1]:
                        print('\nLogin successful.')
                        return

            print('Incorrect username or password.')

    def add_student(self):

        print('Please enter the student\'s details:\n')

        surname = input('Surname: ')
        forename = input('Forename: ')
        date_of_birth = input('Date of birth: ')
        home_address = input('Home address: ')
        home_phone_number = input('Home phone number: ')
        gender = input('Gender: ')

        student_id = self.get_new_id()
        tutor_group = self.get_tutor_group()
        school_email_address = student_id + '@student.treehouseschool.co.uk'

        details = [
            student_id, surname, forename, date_of_birth,
            home_address, home_phone_number, gender,
            tutor_group, school_email_address
        ]

        details = ', '.join(details)

        self.file_handler.add_student(details)

        print('\nThe new student has been added.')
        print(('His' if gender.lower() == 'male' else 'Her'), 'student ID is', student_id)

    def get_new_id(self):

        lines = self.file_handler.get_students()

        if len(lines) <= 1:
            return '0000'

        last_line = lines[-2].split(', ')

        new_id = str(int(last_line[0]) + 1)
        zeros = '0' * (4 - len(new_id))

        new_id = zeros + new_id
        return new_id

    @staticmethod
    def get_tutor_group():
        return choice(['Amphtill Leaves', 'London Flowers', 'Kempston Stones', 'Cardington Grass'])

    def edit_student_details(self):
        print('Sorry, this feature has not been added yet.')

    def print_student_details(self):

        student_id = input('Enter student ID: ')

        lines = self.file_handler.get_students()
        details_found = False

        for line in lines:
            details = line.split(', ')
            if details[0] == student_id:
                details_found = True
                break

        if details_found:

            print('ID: ', details[0])
            print('Surname: ', details[1])
            print('Forename: ', details[2])
            print('Date of birth: ', details[3])
            print('Home address: ', details[4])
            print('Home phone number: ', details[5])
            print('Gender: ', details[6])
            print('Tutor group: ', details[7])
            print('School email address: ', details[8])

        else:
            print('Student ', student_id, ' could not be found.')


if __name__ == '__main__':
    Main()
