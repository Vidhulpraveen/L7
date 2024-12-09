from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "supersecretkey"


def init_db():
    conn = sqlite3.connect("ice_cream_parlor.db")
    cursor = conn.cursor()

 
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS flavors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            allergens TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cart (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            flavor_id INTEGER,
            FOREIGN KEY(flavor_id) REFERENCES flavors(id)
        )
    """)
    conn.commit()
    conn.close()

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/flavors")
def flavors():
    conn = sqlite3.connect("ice_cream_parlor.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM flavors")
    flavors = cursor.fetchall()
    conn.close()
    return render_template("flavors.html", flavors=flavors)

@app.route("/add_flavor", methods=["GET", "POST"])
def add_flavor():
    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        allergens = request.form["allergens"]
        conn = sqlite3.connect("ice_cream_parlor.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO flavors (name, description, allergens) VALUES (?, ?, ?)", 
                       (name, description, allergens))
        conn.commit()
        conn.close()
        flash("Flavor added successfully!")
        return redirect(url_for("flavors"))
    return render_template("add_flavor.html")


@app.route("/add_to_cart/<int:flavor_id>")
def add_to_cart(flavor_id):
    conn = sqlite3.connect("ice_cream_parlor.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO cart (flavor_id) VALUES (?)", (flavor_id,))
    conn.commit()
    conn.close()
    flash("Flavor added to cart!")
    return redirect(url_for("flavors"))


@app.route("/cart")
def cart():
    conn = sqlite3.connect("ice_cream_parlor.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT flavors.name, flavors.description 
        FROM cart 
        JOIN flavors ON cart.flavor_id = flavors.id
    """)
    cart_items = cursor.fetchall()
    conn.close()
    return render_template("cart.html", cart_items=cart_items)

@app.route("/add_allergen/<int:flavor_id>", methods=["GET", "POST"])
def add_allergen(flavor_id):
    if request.method == "POST":
        allergen = request.form["allergen"]
        conn = sqlite3.connect("ice_cream_parlor.db")
        cursor = conn.cursor()

        # Fetch current allergens
        cursor.execute("SELECT allergens FROM flavors WHERE id = ?", (flavor_id,))
        current_allergens = cursor.fetchone()
        current_allergens = current_allergens[0] if current_allergens and current_allergens[0] else ""

        updated_allergens = ", ".join(set(current_allergens.split(", ") + [allergen]))

        cursor.execute("UPDATE flavors SET allergens = ? WHERE id = ?", (updated_allergens, flavor_id))
        conn.commit()
        conn.close()
        flash("Allergen added successfully!")
        return redirect(url_for("flavors"))

    return render_template("allergens.html", flavor_id=flavor_id)


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
