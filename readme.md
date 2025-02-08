# Django & Aiogram template

- `Django`
- `Aiogram 3`
- `i18n`
- ORM: `DjangoORM`
- Database: `PostgreSQL \ Sqlite, Redis`

## 📥 How to Install?

### 1. Clone the Repository
First, clone the repository and navigate to its directory:

```bash
git clone https://github.com/devvsima/aiogram-django-template.git
cd django_and_aiogram
```

### 2. Setting up a virtual environment ".venv"


#### Linux
Install dependencies and activate the virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

#### Windows
Similar steps for Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

> 💡 Note: The name `.venv` can be changed to anything else you wish.

### 3. Setting environment variable

First, copy the `.env.dist` file and rename it to `.env`:

```bash
cp .env.dist .env
```

Then edit the environment variables file:

```bash
vim .env
# or
nano .env
```

### 4. Django commands


#### ~Migrations
```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

#### ~Create admin
```bash
$ python manage.py createsuperuser
```

#### ~Launch 🚀
```bash
$ python manage.py runserver
# or
$ python manage.py runserver 0.0.0.0:8000
```
