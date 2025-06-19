from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Define the correct passwords
passwords = {
    "level1": "JIGGER",
    "level2": "3:33",
  #  "level3": "apple",
    "level4": "WTC",
    "level5": "Walter White",
    "level6": "I love Breaking Bad and I aspire to be like Walter White",
    "level9": "Grape"
}

@app.route("/")
def index():
    return redirect(url_for('level1'))

@app.route("/level1", methods=["GET", "POST"])
def level1():
    if request.method == "POST":
        entered = request.form.get("password")
        if entered == passwords["level1"]:
            return redirect(url_for('level2'))
        return render_template("level1.html", error=True)
    return render_template("level1.html", error=False)

@app.route("/level2", methods=["GET", "POST"])
def level2():
    if request.method == "POST":
        entered = request.form.get("password")
        if entered == passwords["level2"]:
            return redirect(url_for("level3"))
        return render_template("level2.html", error=True)
    return render_template("level2.html", error=False)

@app.route("/level3", methods=["GET", "POST"])
def level3():
    if request.method == "POST":
        return redirect(url_for("level4"))
    return render_template("level3.html")

@app.route("/level4", methods=["GET", "POST"])
def level4():
    if request.method == "POST":
        entered = request.form.get("password")
        if entered == passwords["level4"]:
            return render_template("level4.html", success=True, error=False)
        return render_template("level4.html", success=False, error=True)
    return render_template("level4.html", success=False, error=False)


@app.route("/level5", methods=["GET", "POST"])
def level5():
    if request.method == "POST":
        entered = request.form.get("password")
        if entered == passwords["level5"]:
            return render_template("level5.html", success=True, error=False)
        return render_template("level5.html", success=False, error=True)
    return render_template("level5.html", success=False, error=False)


@app.route("/level6", methods=["GET", "POST"])
def level6():
    if request.method == "POST":
        entered = request.form.get("phrase")
        if entered.strip() == "I love Breaking Bad and I aspire to be like Walter White":  # <- your phrase here
            return redirect(url_for('level7'))
        return render_template("level6.html", success=False, error=True)
    return render_template("level6.html", success=False, error=False)

@app.route("/level7", methods=["GET", "POST"])
def level7():
    if request.method == "POST":
        correct_answers = {
            "answer1": "Benito Mussolini",
            "answer2": "Osama Bin Laden",
            "answer3": "O.J. Simpson",
            "answer4": "Mao Zedong"
        }
        for key in correct_answers:
            if request.form.get(key, "").strip().lower() != correct_answers[key].lower():
                return render_template("level7.html", error=True)

        return redirect(url_for("level8"))

    return render_template("level7.html", error=False)



@app.route("/level8")
def level8():
    return render_template("level8.html")


@app.route("/level9", methods=["GET", "POST"])
def level9():
    if request.method == "POST":
        entered = request.form.get("password")
        if entered == passwords["level9"]:
            return redirect(url_for("level10"))
        return render_template("level9.html", error=True)
    return render_template("level9.html", error=False)



@app.route("/level10", methods=["GET", "POST"])
def level10():
    return "<h1>Congrats! <h1> <p> You Finished. Enjoy your prize.</p>"



if __name__ == "__main__":
    app.run(debug=True)
