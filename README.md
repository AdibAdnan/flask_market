# Flask Market

A simple Flask web application for a virtual marketplace where users can register, log in, and buy/sell items.

## Features

*   **User Authentication:** Users can register for a new account and log in with their credentials.
*   **Marketplace:** A central marketplace where users can view items available for purchase.
*   **Purchase Items:** Users can purchase items from the market, which deducts the item's price from their points.
*   **Sell Items:** Users can sell items they own back to the market, which adds the item's price back to their points.
*   **Purchase Confirmation:** A modal dialog prompts users to confirm their purchase before the transaction is finalized.
*   **User-Specific Views:** The market page dynamically displays available items and items owned by the logged-in user.

## Project Structure

```
.
├── App
│   ├── __init__.py
│   ├── forms.py
│   ├── model.py
│   ├── routes.py
│   └── templates
│       ├── base.html
│       ├── index.html
│       ├── login.html
│       ├── market.html
│       ├── modal.html
│       └── register.html
├── instance
│   └── market.db
├── venv
├── create_db.py
├── requirements.txt
└── run.py
```

## Setup and Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Create the database:**

    ```bash
    python create_db.py
    ```

5.  **Run the application:**

    ```bash
    python run.py
    ```

The application will be running at `http://127.0.0.1:5000/`.

## Usage

*   Navigate to `http://127.0.0.1:5000/` in your web browser.
*   Register for a new account or log in with an existing one.
*   Browse the market, purchase items, or sell your own.

## Technologies Used

*   **Flask:** A micro web framework for Python.
*   **Flask-SQLAlchemy:** A Flask extension for SQLAlchemy.
*   **Flask-WTF:** A Flask extension for working with WTForms.
*   **Flask-Login:** A Flask extension for handling user sessions.
*   **SQLite:** A C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine.