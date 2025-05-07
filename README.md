# anaswer_analizer

Okay, here's a breakdown of the Django application, written to help someone set it up:

**What is this project?**

This Django application is an AI-powered grading system.  It uses the Google Gemini AI to automatically evaluate student answers to questions.  The application is designed to be integrated with an existing student management system or portal.  It assumes that student data (names, roll numbers, and answers) are already stored in a database.  This application will then:

1.  Retrieve those student answers from the database.
2.  Send the answers to the Gemini AI for evaluation.
3.  Receive grades and feedback from Gemini.
4.  Store those grades and feedback in the database, associated with the corresponding students.

**How to set up the project:**

1.  **Prerequisites:**
    * Python (3.8 or later)
    * Django (4.2 or later)
    * A Google Cloud Account with an API Key for the Gemini API.
    * A database (this application is designed to use the same database as your existing student management system).

2.  **Installation:**
    * Clone the repository containing this code.
    * Create a Python virtual environment (recommended):
        ```bash
        python -m venv env
        source env/bin/activate  # Linux/macOS
        env\Scripts\activate  # Windows
        ```
    * Install the necessary Python packages.  A `requirements.txt` file should be provided in the repository.  If not, you may need to install Django and the Google AI library:
        ```bash
        pip install -r requirements.txt  #If available
        pip install Django
        pip install google-generativeai
        ```

3.  **Database Configuration:**
    * This is a crucial step.  You **must** configure Django to use the same database as your existing student management system.
    * In the `settings.py` file, find the `DATABASES` setting.  Modify it to match your existing database configuration.  For example, if your student management system uses a MySQL database, the settings would look something like this:
        ```python
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'your_database_name',
                'USER': 'your_database_user',
                'PASSWORD': 'your_database_password',
                'HOST': 'your_database_host',
                'PORT': 'your_database_port',
            }
        }
        ```
        If your student management system uses SQLite, you'll need the correct path to the database file:
        ```python
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': '/path/to/your/student_management_system.sqlite3',
            }
        }
        ```
        **It is essential that the database settings here match exactly the settings of the other system (student portal).**

4.  **Set up Gemini API Key:**
    * In the `ai_evaluator/views.py` file, locate the following lines:
        ```python
        genai.configure(api_key="YOUR_API_KEY")  # Replace with your actual API key
        model = genai.GenerativeModel("gemini-pro")
        ```
    * Replace `"YOUR_API_KEY"` with your actual Gemini API key from Google Cloud.

5.  **Run Migrations (Potentially):**
        ```bash
        python manage.py migrate
        ```
        In most cases, you won't need to run migrations.  This application is designed to work with a database schema already created by your student management system.  However, if you encounter database-related errors, try running migrations.

6.  **Create a Superuser:**
        ```bash
        python manage.py createsuperuser
        ```
        This creates an administrator account for the Django admin interface.

**How to run the project:**

1.  Start the Django development server:
    ```bash
    python manage.py runserver
    ```

2.  The application will be accessible at `http://127.0.0.1:8000/`.
3.  You can view the evaluation data in the Django admin interface, usually at `http://127.0.0.1:8000/admin/`.  Log in with the superuser account you created.

**How to enter your own API key:**

* As mentioned in the setup, in the `ai_evaluator/views.py` file, replace `"YOUR_API_KEY"` with your actual Gemini API key.
