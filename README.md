# 📝 BlogShare — Django Blog & Image Sharing Platform

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Django](https://img.shields.io/badge/Django-4.x-green?logo=django)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple?logo=bootstrap)
![License](https://img.shields.io/badge/License-MIT-yellow)

A full-featured blog and image sharing web application built with **Django**, featuring user authentication, rich post management, comments, search, pagination, and a responsive Bootstrap 5 UI.

---

## ✨ Features

- 🔐 **User Authentication** — Register, Login, Logout with CSRF protection
- 👤 **Profile Management** — Update name, email, contact, profile picture
- 🔑 **Password Reset** — Email-based password reset flow
- 📝 **Blog Posts** — Full CRUD (Create, Read, Update, Delete) — owner only
- 🖼️ **Image Uploads** — Attach images to posts and profile pictures
- 💬 **Comments** — Add, edit, delete comments on posts — owner only
- 🔍 **Search & Pagination** — Search posts by title/content with paginated results
- 🛡️ **Admin Panel** — Block users, moderate posts and comments
- ✅ **Live Form Validation** — Real-time username/email availability check via JavaScript
- 📱 **Responsive UI** — Bootstrap 5 with clean card-based layout

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Anandhu-0p/blog-project.git
cd blog-project

# 2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py makemigrations users blog
python manage.py migrate

# 5. Create a superuser (admin)
python manage.py createsuperuser

# 6. Start the development server
python manage.py runserver
```

### Access the App
| URL | Description |
|---|---|
| `http://127.0.0.1:8000/` | Login page |
| `http://127.0.0.1:8000/register/` | Register new account |
| `http://127.0.0.1:8000/blog/` | Blog posts home |
| `http://127.0.0.1:8000/admin/` | Admin panel |

---

## 🗂️ Project Structure

```
blog_project/
├── blog/               # Blog app (posts, comments)
├── users/              # Users app (auth, profile)
├── templates/          # HTML templates
│   ├── base.html
│   ├── blog/
│   └── users/
├── static/             # CSS, JS, images
├── media/              # User-uploaded files (gitignored)
├── blog_project/       # Django project settings & URLs
├── manage.py
└── requirements.txt
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django (Python) |
| Frontend | Bootstrap 5, Bootstrap Icons, Vanilla JS |
| Database | SQLite (dev) |
| Auth | Django custom user model |
| File Storage | Django FileField / ImageField |

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

> Built by [Anandhu-0p](https://github.com/Anandhu-0p)
