
from flask import Flask, render_template, request

app = Flask(__name__)

def categorize_postcode(postcode):
    cleaned = postcode.replace(" ", "").upper()
    if cleaned.startswith("SW147"):
        return "East"
    elif cleaned.startswith("SW148"):
        return "West"
    else:
        return "Out of Area"

@app.route("/", methods=["GET", "POST"])
def index():
    zone = None
    if request.method == "POST":
        postcode = request.form.get("postcode", "")
        zone = categorize_postcode(postcode)
    return f"<h1>Postcode Zone: {zone}</h1>" if zone else '''
        <form method='post'>
            <label>Enter Postcode:</label>
            <input type='text' name='postcode'>
            <button type='submit'>Check</button>
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
