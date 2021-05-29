class File:

    @staticmethod
    def get_accounts():
        with open('accounts.txt', 'r') as file:
            return file.read().split('\n')

    @staticmethod
    def add_account(username, password):
        with open('accounts.txt', 'a') as file:
            file.write(username)
            file.write(', ')
            file.write(password)
            file.write('\n')

    @staticmethod
    def get_students():
        with open('student_details.txt', 'r') as file:
            return file.read().split('\n')

    @staticmethod
    def add_student(student_details):
        with open('student_details.txt', 'a') as file:
            file.write(student_details)
            file.write('\n')

    @staticmethod
    def remove_student(student_id):
        pass
