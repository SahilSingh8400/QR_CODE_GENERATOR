from flask import Flask, render_template,request,send_file
import qrcode

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    if request.method=="POST":
        text=request.form["text"]
        qrcode.make(text).save("text_to_qr.png")
        return send_file("text_to_qr.png",mimetype="image/png")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)