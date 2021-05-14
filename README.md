# SciHub

This project implements most of the knowned hrv (heart rate variability) analysis technics in django

## Running the Project Locally

First, clone the repository to your local machine

Install the requirements:

```bash
pip install -r requirements.txt
```

Create the database:

```bash
python manage.py makemigrations
python manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.
