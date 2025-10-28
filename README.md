# Django CRUD Book Project

A simple Django project that allows users to Create, Read, Update, and Delete (CRUD) books using Django's models, forms, views, and templates.

## How to Run This Project

Follow these steps to run the project on any system.

### 1. Clone the Repository

git clone https://github.com/your-username/your-repo-name.git
cd crud_project

### 2. Create and Activate a Virtual Environment

Windows (PowerShell):

python -m venv venv
.\venv\Scripts\Activate.ps1

Windows (CMD):

python -m venv venv
venv\Scripts\activate.bat

macOS / Linux:

python3 -m venv venv
source venv/bin/activate

### 3. Install Dependencies

pip install django

Or use pip install -r requirements.txt if you add one later

### 4. Apply Migrations

python manage.py makemigrations
python manage.py migrate

### 5. (Optional) Add Sample Data

Run the Django shell:

python manage.py shell

Then add a book manually:

from books.models import Book
Book.objects.create(
    title="Django for Beginners",
    author="John Doe",
    published_date="2023-01-01",
    pages=300
)
exit()

### 6. Run the Development Server

python manage.py runserver

Visit http://127.0.0.1:8000/ in your browser.

## Features

- Full CRUD functionality for Book model
- User-friendly forms using ModelForm
- Basic HTML templates:
  - List view
  - Create / Update form
  - Delete confirmation

## Templates Overview

- book_list.html — shows all books
- book_form.html — used for both creating and editing
- book_confirm_delete.html — confirmation before deleting

## Requirements

- Python 3.8 or higher
- Django 5.x
- SQLite (included by default)

## Notes

- This setup is for development only. Do not use runserver in production.
- Do not commit your virtual environment or database to version control.

## .gitignore Example

venv/
__pycache__/
*.pyc
db.sqlite3
*.log
.env

## License

This project is open-source and free to use for learning and development purposes.

