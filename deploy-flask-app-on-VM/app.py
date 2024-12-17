from flask import Flask, request, render_template

# Initialize the Flask app
app = Flask(__name__)

# Define route for both GET and POST
@app.route("/", methods=["GET", "POST"])
def home():
    name = None
    if request.method == "POST":
        # Get name from the form
        name = request.form.get("name")
    # Render the HTML page and pass the name (if any)
    return render_template("index.html", name=name)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)


