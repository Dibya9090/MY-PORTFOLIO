from flask import Flask ,render_template

app=Flask("__name__")

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",title="Dibyajyoti Kamila")

@app.route("/about")
def about():
    return render_template("about.html",title="about")

@app.route("/projects")
def projects():
    return render_template("projects.html",title="projects")

@app.route("/skills")
def skills():
    return render_template("skills.html",title="skills")


@app.route("/contact")
def contact():
    return render_template("contact.html",title="contact")

if __name__ == "__main__":
    app.run(debug=True)