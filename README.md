# Ice Cream Parlor Web Application

This is a simple Flask-based web application for managing ice cream flavors, customer carts, and allergens. The application uses SQLite as the database to store information about ice cream flavors, allergens, and the user's cart.

## Features

- **Add Flavors**: Admins can add new ice cream flavors with descriptions and allergens.
- **Browse Flavors**: Users can browse all available ice cream flavors.
- **Add to Cart**: Users can add flavors to their cart.
- **View Cart**: Users can view the items added to their cart.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/ice-cream-parlor.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd ice-cream-parlor
    ```

3. **Create and activate a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

4. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Run the application**:
    ```bash
    python app.py
    ```

    The application will be available at `http://127.0.0.1:5000/`.

## Usage

1. **Home Page**: Navigate to the home page to get an overview of the Ice Cream Parlor.
2. **Browse Flavors**: Go to the **Flavors** page to view and browse all available ice cream flavors.
3. **Add to Cart**: Add your favorite flavors to the cart by clicking the **Add to Cart** button next to each flavor.
4. **View Cart**: Visit
