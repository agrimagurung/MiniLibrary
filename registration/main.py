import sys, csv, os
import traceback
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from registration_ui import Ui_MainWindow as Ui_Registration

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'login'))
from Login_ui import Ui_MainWindow as Ui_Login

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'student'))
from studentDashboard2_ui import Ui_MainWindow as Ui_StudentDashboard

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'admin'))
from admin_dashboard_ui import Ui_MainWindow as Ui_AdminDashboard

def show_error_message(exc_type, exc_value, exc_traceback):
    print("\n--- PYQT ERROR ---")
    traceback.print_exception(exc_type, exc_value, exc_traceback)

sys.excepthook = show_error_message


ADMINUSERNAME = "ADMINUSERNAME" 
ADMINPASSWORD = "ADMINPASSWORD" 


class LoginPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.setWindowTitle("Login")

        self.ui.btnLoginstudent.clicked.connect(self.student_login)
        self.ui.btnClear.clicked.connect(self.clear_fields)
        self.ui.btnLoginadmin.clicked.connect(self.Admin_login)
        self.ui.btnRegister.clicked.connect(self.open_registration)


    # handle admin login:
    def Admin_login(self):
        username = self.ui.usernameInput.text()
        password = self.ui.passwordInput.text()

        if username == ADMINUSERNAME and password == ADMINPASSWORD:
            self.ui.lblStatus.setText("Login successful!")
            self.dashboard = QMainWindow()
            self.ui_dashboard = Ui_AdminDashboard()
            self.ui_dashboard.setupUi(self.dashboard)
            self.dashboard.showMaximized()
            self.close()
        else:
            self.ui.lblStatus.setText("Invalid username or password.")
            

    # handle student login:
    def student_login(self):
        username = self.ui.usernameInput.text()
        password = self.ui.passwordInput.text()

        # Check against CSV
        registration = RegistrationWindow()  # just to access the method
        result = registration.validateStudentLogin(username, password)

        if result:
            self.ui.lblStatus.setText("Login successful!")
            self.dashboard = DashboardWindow(result[0])  # pass first name
            self.dashboard.showMaximized()
            self.close()
        else:
            self.ui.lblStatus.setText("Invalid username or password.")

    # navigate new user to registration form:
    def open_registration(self):
            self.registration_window = RegistrationWindow()
            self.registration_window.showMaximized()
            self.close()

    # clear field after user logs in
    def clear_fields(self):
        self.ui.usernameInput.clear()
        self.ui.passwordInput.clear()
        self.ui.lblStatus.setText("")



class DashboardWindow(QMainWindow):
    def __init__(self, first_name):
        super().__init__()
        self.ui = Ui_StudentDashboard()
        self.ui.setupUi(self)
        self.first_name = first_name

        self.setWindowTitle(f"Student Dashboard - {first_name}")
        # update the header lbl with user's first name
        self.ui.dashboardLbl.setText(f"{first_name}'s Dashboard")

class RegistrationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Registration()
        self.ui.setupUi(self)
        # self.showMaximized()

        self.setWindowTitle("Registration")

        # connect submit button
        self.ui.btnSubmit.clicked.connect(self.register_user)
        # connect back to login page button
        self.ui.btnBack.clicked.connect(self.back_to_login)

    def back_to_login(self):
        self.login_window = LoginPage()
        self.login_window.showMaximized()
        self.close()

    def validateStudentLogin(self, username, password):
        csv_file = os.path.join(os.path.dirname(__file__), "users.csv")

        # read user csv file to check for username and password
        with open(csv_file, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) >= 4 and row[2] == username and row[3] == password:
                    return row  # return the entire row if found
        return None

    # check if username exists method:
    def username_exists(self, username):
        csv_file = os.path.join(os.path.dirname(__file__), "users.csv")
        if not os.path.exists(csv_file):
            return False
        with open(csv_file, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                # starting from row 2, and checking item in index 2 (username)
                if len(row) > 2 and row[2] == username:
                    self.ui.lblAlert.setText("Username already taken :( Please choose something else!")
                    return True
        return False  # username not found

#         username = self.ui.usernameInput.text()
# firstNameInput
    # register user method:       
    def register_user(self):
        first_name = self.ui.firstNameInput.text()
        last_name = self.ui.lastNameInput.text()
        username = self.ui.usernameInput.text()
        password = self.ui.passwordInput.text()
        question = self.ui.comboBoxSecurityQuestion.currentText()
        answer = self.ui.securityAnswerInput.text()

        # Check if a field is blank
        if not first_name or not last_name or not username or not password or not answer:
            self.ui.lblAlert.setText("Please fill in all fields!!")
            return
        
        # Check if username exists
        if self.username_exists(username):
            return
        
        # Save to CSV with absolute path
        csv_file = os.path.join(os.path.dirname(__file__), "users.csv")
        try:
            with open(csv_file, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([first_name, last_name, username, password, question, answer])
            self.ui.lblAlert.setText("Account created successfully!!")

            # Open Dashboard
            self.DashboardWindow = DashboardWindow(first_name)
            self.DashboardWindow.showMaximized()


            self.close()

            # Clear the fields
            self.ui.firstNameInput.clear()
            self.ui.lastNameInput.clear()
            self.ui.usernameInput.clear()
            self.ui.passwordInput.clear()
            self.ui.securityAnswerInput.clear()
        except Exception as e:
            self.ui.lblAlert.setText(f"Error saving account: {str(e)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginPage() # start off w login page
    window.showMaximized()

    sys.exit(app.exec_())
