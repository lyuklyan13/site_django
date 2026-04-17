# 📚 Site Django: Encyclopedia of Mathematicians

## ℹ️ Overview
Welcome to **Site Django** — a full-stack web application developed as an academic coursework  
project (2024). This project serves as a comprehensive digital encyclopedia dedicated to the   
biographies of world-renowned mathematicians.  

Beyond its educational purpose, this repository demonstrates a robust implementation of  
the **Django MVT (Model-View-Template)** architectural pattern, showcasing clean backend logic,   
efficient relational database interactions via Django ORM, and a structured, server-side  
rendered (SSR) frontend interface using HTML5 and CSS3.  


## ✨ Highlights & Key Features

* **Custom Content Management System (CMS):** A fully configured and localized Django   
  Admin interface (`MenAdmin`) that allows non-technical users to Create, Read, Update,  
  and Delete content effortlessly.  

* **Automated Slug Generation:** Client-side JavaScript auto-populates URL-safe slugs based  
  on article titles directly within the admin panel.  

* **Performance Optimized ORM:** Utilizes indexed database fields (`models.Index`)  
   and B-Tree optimization for sorting large datasets by creation time, reducing query latency.  

* **Resilient Frontend Architecture:** Built upon a modular template inheritance system (`base.html`),  
   embracing the DRY (Don't Repeat Yourself) principle. Features dynamic image rendering checks to  
   prevent broken UI states.  
* **Application Level Security:** Strict data validation algorithms (`MinLengthValidator`, `MaxLengthValidator`)   
 implemented directly within the models.

## 💻 Tech Stack & Architecture
* **Language:** Python  
* **Framework:** Django Web Framework  
* **Database:** SQLite (default configuration)  
* **Frontend:** HTML5, CSS3  
* **Architectural Pattern:** Model-View-Template (MVT) / Layered Architecture  


## 🚀 Getting Started (Local Development)
Follow these instructions to set up the project on your local machine for development, testing,   
or review purposes.

**Prerequisites**  
Make sure you have [Python 3.x](https://www.python.org/) installed. Familiarity with virtual environments is recommended.  


### **Installation Steps**

1. **Clone the repository:**
   ```bash
   git clone https://github.com/lyuklyan13/site_django.git
   cd site_django
   ```
2. **Create and activate a virtual environment:**  
   Isolating dependencies ensures the project does not conflict with global system packages.  
   Using modern Python package manager and project manager - [uv](https://docs.astral.sh/uv/)

   ```bash
   # On Windows
   uv venv
   .venv\Scripts\activate

   # On macOS/Linux
   uv venv
   source .venv/bin/activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations:**  
   This command compiles the Django models and generates the SQLite database schema.
   ``` bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. **Create an administrative user (Superuser):**  
   To access the Django Admin panel and populate the database:
   ``` bash
   python manage.py createsuperuser
   ```  
   *(Follow the interactive prompts to set your username and password).*

6. **Start the development server:**
   ``` bash
   python manage.py runserver
   ```  
7. **Access the application:**

   Main Application: `http://127.0.0.1:8000/`  

   Admin Dashboard: `http://127.0.0.1:8000/admin/`


## 📂 Project Structure Map

Understanding the repository structure:  
site_django/  
├── manage.py  &emsp;&emsp; # Django's command-line utility for administrative tasks  
├── requirements.txt  &emsp;&emsp; # Python dependency manifest  
├──.gitignore &emsp;&emsp; # Git ignore rules (excludes db, environments, secrets)  
├── site_django/ &emsp;&emsp; # Core project configuration package  
│   ├── settings.py &emsp;&emsp; # Global settings (Database, Apps, Middleware)  
│   ├── urls.py &emsp;&emsp; # Global URL dispatching rules  
│   └── wsgi.py  &emsp;&emsp; # WSGI entry-point for web servers  
├── men/       &emsp;&emsp; # Main business logic application  
│   ├── models.py &emsp;&emsp; # Database models and schemas (The 'M' in MVT)  
│   ├── views.py  &emsp;&emsp; # Request handlers and logic (The 'V' in MVT)  
│   ├── admin.py &emsp;&emsp; # CMS dashboard configuration   
│   ├── urls.py  &emsp;&emsp; # Application-specific routing  
│   └── templates/ &emsp;&emsp; # HTML Templates (The 'T' in MVT)  
└── media/  &emsp;&emsp; # Directory for user-uploaded files (excluded from repo)  





