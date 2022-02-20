from flask import Flask, redirect, render_template, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask("__name__")

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False # to remove the warning after creating the 
                                                   # database model
db=SQLAlchemy(app)


Bootstrap(app) 

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_Text = db.Column(db.String(100), nullable=False)
    complete_Status = db.Column(db.Integer, default=0)
    date_Created=db.Column(db.DateTime)
    

    def __repr__(self):
        return "<Task > %r" % self.id


@app.route("/", methods=["POST","GET"])
def index():
    if request.method=="POST":
        listname = request.form["addInput"]
        todoItem= Todo(item_Text=listname)

        try:
            db.session.add(todoItem)
            db.session.commit()
            return redirect("/")
        
        except:
            return "Oops! Looks like there was error submitting your task"

    else:
        items = Todo.query.order_by(Todo.date_Created).all()
        return render_template("index.html",items=items)