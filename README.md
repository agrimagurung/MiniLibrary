# MiniLibrary – Library Management System 

A desktop Library Management System built with Python and PyQt5, featuring Student and Admin interfaces. Students can view borrowed books and due dates, while admins can manage the catalog through an intuitive GUI. This project demonstrates object-oriented programming, GUI development, file handling, and Python best practices! 

## Features
###  Login Page
- Separate login for Students and Admin
- Students can log in using their credentials saved in ````users.csv````
- Admin login is hardcoded for simplicity (logic can be extended easily!)
- Error messages display for invalid login attempts

### Student Dashboard
- View all books issued to the student
- See due dates for borrowed books
- Dashboard updates dynamically from ````books_data.csv````

###  Admin Dashboard
- Manage the full catalog of books
- Add, edit, or remove books
- Update book status and due dates

###  Registration Page
- Students can create accounts via registration form
- Validation for empty fields and unique usernames
- User data is saved in ````users.csv````
  
## How to Run
1. Install dependencies:
````pip install pyqt5````
2. Run the application in terminal: 
````python main.py````
3. Loads the login page where you can:
    1. Log in as a student or admin
    2. Register a new student account

## Dataset Source

The book dataset used in this project was obtained from Kaggle:

**Dataset:** Library books  
**Author:** Bimal Gajera  
**License:** CC0 (Public Domain)  
**Source:** https://www.kaggle.com/datasets/bimalgajera/library-books

---

## License

This project is licensed under the Apache 2.0 License.  
See the [LICENSE](LICENSE) file for full details.
