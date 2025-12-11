import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit 
from login_ui import Ui_MainWindow as Ui_Login
from admin_dashboard_ui import Ui_MainWindow as Ui_Admin_Dashboard

ADMINUSERNAME = "Bob"
ADMINPASSWORD = "1234"

STUDENTUSERNAME = "Eric"
STUDENTPASSWORD = "4321"



class LoginPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.setWindowTitle("Login")

        self.ui.btnLoginstudent.clicked.connect(self.student_login)
        self.ui.btnClear.clicked.connect(self.clear_fields)
        self.ui.btnLoginadmin.clicked.connect(self.Admin_login)


    def Admin_login(self):
        
        
        username = self.ui.usernameInput.text()
        password = self.ui.passwordInput.text()

        if username == ADMINUSERNAME and password == ADMINPASSWORD:
            
            self.ui.lblStatus.setText("Login successful!")
            self.dashboard = AdminDashboard()
            self.dashboard.show()
            self.close()
        else:
            self.ui.lblStatus.setText("Invalid username or password.")
            

    def student_login(self):
        
        
        username = self.ui.usernameInput.text()
        password = self.ui.passwordInput.text()
        self.ui.lblStatus.setText("Invalid username or password.")

        if username == STUDENTUSERNAME and password == STUDENTPASSWORD:
            self.ui.lblStatus.setText("Login successful!")
            self.dashboard = DashboardWindow()
            self.dashboard.show()
            self.close()
        else:
            self.ui.lblStatus.setText("Invalid username or password.")

    def clear_fields(self):
        self.ui.usernameInput.clear()
        self.ui.passwordInput.clear()
        self.ui.lblStatus.setText("")



class AdminDashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Admin_Dashboard()
        self.ui.setupUi(self)
        self.setWindowTitle("Admin Dashboard")
        try:
            Bookdata = open("Booklist.txt")
        except:
            Bookdata = open("Booklist.txt", "xt")

        self.ui.Savebtn.clicked.connect(self.Save_list)
        self.ui.SearchBar.returnPressed.connect(self.Search)
        

    def Search(self):
        text = self.ui.SearchBar.text().lower()
        for row in range(self.ui.Booklist.rowCount()):
            item = self.ui.Booklist.item(row, 0)
                # add if statment to see if text exsist
            if(item is None):
                break
            print(text)
            print(item.text().lower())
            if text == item.text().lower():
                self.ui.Booklist.setRowHidden(row, False)

            else:
                self.ui.Booklist.setRowHidden(row, True)
                
  # text =           
    def Save_list(self):
        Booklist = ("Booklist.txt")
        with open(Booklist, 'w') as file:
            for row in range(self.ui.Booklist.rowCount()):
                for col in range(self.ui.Booklist.columnCount()):
                    print("test1")
                    
                    if self.ui.Booklist.item(row, col).text() is None:
                        print("test2")
                        text = " "
                    else:
                        text = self.ui.Booklist.item(row, col).text()
                        print(text)
                    file.write(text +", ")
                file.write("\n")
                
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginPage()
    window.show()
    sys.exit(app.exec_())

        
