
# Library Management System

## 📖 Project Description
The **Library Management System** is a Python-based application designed to efficiently manage a library's inventory, users, and loan operations. The system includes features such as adding books, user registration, lending and returning books, maintaining waiting lists, generating reports on popular books, and managing user notifications.

---

## 🚀 Instructions to Run the Project

### ✅ Prerequisites
**Python Installation**:
   - Ensure Python 3.6 or higher is installed on your system.


### ▶️ Steps to Run
1. Open a terminal and navigate to the project’s root directory.
2. Run the main script:
   ```bash
   python main.py
   ```

---

## ✨ Features

### 📚 Book Management
- Add new books to the library’s inventory.
- Update and remove books from the system.
- Search books by title, author, or genre.

### 👤 User Management
- Register new users and allow them to log in.
- Manage user notifications for events like book availability.

### 🔄 Lending System
- Lend books to registered users and track their status.
- Maintain a waiting list for books currently on loan.
- Notify users when books become available.

### 📥 Returning System
- Handle book returns and update inventory automatically.
- Notify users in the waiting list when a book becomes available.

### 📊 Reports and Analytics
- Display popular books based on loan and request counts.
- Generate insights into library usage and trends.

---

## 🛠️ Design Patterns Implemented

### 1️⃣ **Singleton Pattern**
- **Usage**: Implemented in the `NotificationSystem` class to ensure only one instance of the notification manager exists throughout the application.

### 2️⃣ **Factory Pattern**
- **Usage**: Used in the `BookFactory` class to create `Book` objects in a consistent and efficient way.

### 3️⃣ **Observer Pattern**
- **Usage**: Utilized in the `NotificationSystem` to allow users to subscribe to notifications and receive updates about book availability or other events.

---

## 📂 Project Structure

### Main Directories and Files:
- **`main.py`**: Entry point of the application.
- **`helpers/`**: Contains utility functions, file handling logic, and helpers like `FileHandler`, `Paths`, and `utils`.
- **`design/`**: Includes implementations of design patterns such as `Observer`, `Subject`, and `NotificationSystem`.
- **`buttons/`**: Contains logic for user actions, such as adding, searching, removing, lending, and returning books.
- **`files/`**: Directory for storing application data in CSV files:
  - `books.csv`: Main inventory of the library.
  - `available_books.csv`: Books currently available for lending.
  - `loaned_books.csv`: Books currently loaned out.
  - `popular_books.csv`: Most borrowed/requested books.
  - `users.csv`: User data, including login credentials and messages.
  - `logs.txt`: Application logs for debugging and tracking events.

---

## 🔮 Future Enhancements
- Add support for managing e-books.
- Develop a web-based interface for remote access to the library.
- Implement advanced analytics for user behavior and book trends.
- Enhance reporting with dynamic visualizations.

---

## 📝 Example Use Case
1. Register as a new user.
2. Add books to the library’s inventory.
3. Search for books by title, author, or genre.
4. Lend books to users and maintain a waiting list for unavailable books.
5. Return books and automatically notify waiting users.
6. View popular books and analytics on library usage.

---

## 📧 Contact
For any inquiries or support, feel free to reach out:
- **Author**: Ofek Bar Shalom
- **GitHub Repository**: [Library Management System](https://github.com/ofekbarshalom/Python/tree/main/Library/Library22)

---

Enjoy managing your library with ease! 📚✨
