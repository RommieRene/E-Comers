# 🛒 Simple Shopping Site

A minimal yet functional e-commerce platform built with Django.  
This project allows users to buy and sell products, communicate directly, and manage items through an intuitive interface and admin dashboard.

---

## Features

###  User Functionality
- **User Registration & Login** – Secure authentication with session support.
- **List Items for Sale** – Users can upload products with a title, description, price, image, and category.
- **Buy Items** – Any registered user can browse products and initiate a purchase.
- **Item Detail View** – Displays product info, seller details, and related items.
- **Edit/Delete Items** – Sellers can manage their listings.
- **Chat with Sellers** – Buyers can message sellers directly and hold conversations.

### Messaging System
- **Inbox Section** – Simple threaded chat system.
- **Conversation History** – Buyers and sellers can view and continue previous discussions.

### Admin Control
- **Admin Panel** – Full Django admin support to manage:
  - Users
  - Items
  - Categories
  - Conversations
- **Category Management** – Admins can add, edit, or delete categories. Products can be grouped by category.

### Navigation
- **Dashboard** – Centralized panel for user’s items and interactions.
- **New Item Page** – Add a new product for sale.
- **Inbox** – Access all ongoing conversations.

---

## Project Structure (Main Sections)
- `Dashboard` – User-specific management page.
- `Inbox` – Messaging hub for buyer-seller interactions.
- `New Item` – Form for submitting a new listing.

---

## Categories
- Admin can create more categories anytime.
- Each item detail page displays **related items** based on category.

---

## Tech Stack
- **Backend**: Django (Python)
- **Database**: SQLite (default)
- **Frontend**: HTML5, CSS3 (with Django templating)
- **Auth**: Django's built-in auth system

---

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/RommieRene/E-Comers.git
   cd E-Comers
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   pip install -r requirements.txt
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
   http://127.0.0.1:8000/ – Main site
   http://127.0.0.1:8000/admin/ – Admin panel

## This project is for educational/demo purposes and can be extended with features like:

    Payment integration (Stripe, PayPal)

    Product images gallery

    Search & filtering

    Order tracking