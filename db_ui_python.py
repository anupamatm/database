import sys
import psycopg2
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton, QListWidget

# Database connection parameters
db_params = {
   "dbname": "thousand_records",
    "user": "postgres",
    "password": "root",
    "host": "localhost",
    "port": "5432"
}

# Initialize the database connection
try:
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()
except (Exception, psycopg2.Error) as error:
    print(f"Error: {error}")
    sys.exit(1)

# Create the products table if it doesn't exist
cursor.execute("CREATE TABLE IF NOT EXISTS products (id serial PRIMARY KEY, name VARCHAR(255), description TEXT)")
conn.commit()

class ItemApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Item Management")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.list_widget = QListWidget(self)
        self.layout.addWidget(self.list_widget)

        self.name_label = QLabel("Name:", self)
        self.name_input = QLineEdit(self)
        self.layout.addWidget(self.name_label)
        self.layout.addWidget(self.name_input)

        self.desc_label = QLabel("Description:", self)
        self.desc_input = QTextEdit(self)
        self.layout.addWidget(self.desc_label)
        self.layout.addWidget(self.desc_input)

        self.add_button = QPushButton("Add Item", self)
        self.add_button.clicked.connect(self.add_item)
        self.layout.addWidget(self.add_button)

        self.refresh_list()
    
    def refresh_list(self):
        self.list_widget.clear()
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()
        for item in products:
            self.list_widget.addItem(f"ID: {item[0]}, Name: {item[1]}, Description: {item[2]}")

    def add_item(self):
        name = self.name_input.text()
        description = self.desc_input.toPlainText()

        cursor.execute("INSERT INTO products (name, description) VALUES (%s, %s)", (name, description))
        conn.commit()

        self.name_input.clear()
        self.desc_input.clear()
        self.refresh_list()

def main():
    app = QApplication(sys.argv)
    window = ItemApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
