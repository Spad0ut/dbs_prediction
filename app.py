from flask import Flask
app = Flask(__name__)
from flask import request, render_template
@app.route("/", methods = ["GET", "POST"])
def i():
    if request.method == "POST":
        num = float(request.form.get("rates"))
        return(render_template("index.html", result = 23.5+(26.3*num)))
    else:
        return render_template("index.html", result ="Waiting……….")
if __name__=="__main__":
    app.run()
