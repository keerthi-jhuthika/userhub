# UserHub

## About

UserHub is a Django-based web application for account management and registration.  
## Tech Stack

- Language: Python 3.10+
- Backend: Django 6.1
- Frontend: HTML, Tailwind CSS
- Storage: Local Storage

---

## Project Structure

```text
nscc_project/
├── core/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── accounts/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## How to Run the Project

### 1. Create a virtual environment

```bash
python -m venv venv
```

### 2. Activate the virtual environment

On Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Start the Django development server

```bash
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

---

## Features Implemented

- User signup form with Username, Email, and Password fields
- Username validation (cannot be empty)
- Email validation using Regex
- Password validation (minimum 6 characters)
- Password hashing before storing
- User details stored in browser localStorage
- Dashboard displaying all registered users in a table
- Delete button to remove user entries from the dashboard
- Responsive and user-friendly interface

---

## Additional Features Added

- Added a user count display showing the total number of registered users.
- Added automatic redirection to the Dashboard after successful signup.
- Designed a responsive and visually appealing user interface.

---

## Concepts Learned While Completing the Task

- Form handling and user input validation
- Regular Expressions (Regex) for email validation
- Password hashing for secure data storage
- Using localStorage to store and retrieve user data
- DOM manipulation using JavaScript
- Creating and updating dynamic HTML tables
- Page navigation and redirection using JavaScript
- Handling button click events and user interactions

---

## Live Deployment Link

https://userhub-haz3.onrender.com/

---

## License

This project is distributed under the MIT License. See `LICENSE` for details.
