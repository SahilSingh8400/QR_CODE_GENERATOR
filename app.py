from flask import Flask, render_template, request
import qrcode

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    qr_code = None

    if request.method == "POST":
        text = request.form["text"]

        qr_code = "qr.png"
        qrcode.make(text).save(f"static/{qr_code}")

    return render_template("index.html", qr_code=qr_code)

if __name__ == "__main__":
    app.run(debug=True)