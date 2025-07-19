from flask import Flask, render_template, request

app = Flask(__name__)

def categorize_postcode(postcode):
    cleaned = postcode.replace(" ", "").upper()
    if cleaned.startswith("SW147"):
        return "West"
    elif cleaned.startswith("SW148"):
        return "East"
    else:
        return "Out of Area"

@app.route("/", methods=["GET", "POST"])
def index():
    zone = None
    if request.method == "POST":
        name = request.form.get("name", "")
        phone = request.form.get("phone", "")
        postcode = request.form.get("postcode", "")
        service = request.form.get("service", "")
        zone = categorize_postcode(postcode)
        return render_template("index.html", zone=zone, name=name, phone=phone, postcode=postcode, service=service)
    return render_template("index.html", zone=zone)

if __name__ == "__main__":
    app.run(debug=True)
