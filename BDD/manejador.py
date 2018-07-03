import os

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

# enlace a base de datos vía sqlalchemy
from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "bookdatabase.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)

# modelado
class Student(db.Model):
    """
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    lastName = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return "<Name: {}>".format(self.name)

# vistas
# @app.route("/")
@app.route("/", methods=["GET", "POST"])
def index():
    # return "My flask app"
    if request.form:
        print(request.form)
        est = Student(name=request.form.get("newName"), lastName=request.form.get("newLastName"))
        db.session.add(est)
        db.session.commit()
        return redirect("/index.html")

    students = Student.query.all()
    return render_template("/index.html", students=students)


    

    


if __name__ == "__main__":
    app.run(debug=True)



