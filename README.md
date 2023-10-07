

# Django Celery Mail Queue

Django Celery Mail Queue is a project that allows you to efficiently send emails to multiple recipients with optional attachments . It provides a queuing mechanism to ensure that emails are sent .

## Features

- Send emails to multiple recipients with customizable content.
- Attach multiple files to your emails with a single click.
- Uses Celery to handle email sending asynchronously
- Utilizes a Postgres database to store email tasks and their status.
- Easy setup and configuration.

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/niluws/mail-queue.git
   ```

2. Create a virtual environment and install the required dependencies:

   ```bash
   cd mail-queue
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. Configure your Django settings, including your database and email settings, in the `settings.py` file.

4. Migrate the database:

   ```bash
   python manage.py migrate
   ```

5. Start the Celery worker:

   ```bash
   celery -A core worker --loglevel=info
   ```

6. Run the Django development server:

   ```bash
   python manage.py runserver
   ```

7. Access the application in your web browser at [http://localhost:8000/](http://localhost:8000/).

## Usage

1. Create a new task by specifying the email subject, content, recipients, and attachments.

2. Submit the task, and it will be added to the email queue for asynchronous processing.

3. Monitor the status of email tasks in the admin panel.

## Technologies Used

- [Django](https://www.djangoproject.com/)
- [Celery](https://docs.celeryproject.org/en/stable/index.html)
- [PostgreSQL](https://www.postgresql.org/)
- [Redis](https://redis.io/)

