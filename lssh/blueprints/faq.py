from flask import Blueprint, request
import json

from lssh.models import db, Categoryfaq, Question
faq = Blueprint('faq', __name__, url_prefix='/faq')


@faq.route("/question/", methods=["POST"])
def add_question():
    if(request.form.get("questionTitle") and
       request.form.get("categoryID") and
       request.form.get("questionAnswer")):
        category = Categoryfaq.query.get(request.form.get("categoryID"))
        if category:
            question = Question(questionTitle=request.form.get("questionTitle"),
                                questionAnswer=request.form.get(
                                    "questionAnswer"),
                                categoryfaq=category)
            db.session.add(question)
            db.session.commit()

            return question.serialize(), 200
        else:
            return {"msg": "missing category id"}, 400
    else:
        return {'msg': 'missing form components'}, 400


@faq.route("/question/<int:questionid>", methods=["PUT", "DELETE"])
def edit_question(questionid):
    q = Question.query.get_or_404(questionid)
    print(request.form)
    if request.method == "PUT":
        if request.form.get("questionTitle"):
            q.questionTitle = request.form.get("questionTitle")
        
        if request.form.get("questionAnswer"):
            q.questionAnswer = request.form.get("questionAnswer")
        
        if request.form.get("questionCategory"):
            category = Categoryfaq.query.get(request.form.get("questionCategory"))
            print(category)
            if category:
                q.categoryfaq = category
        
        db.session.commit()
        return q.serialize(), 200
    elif request.method == "DELETE":
        db.session.delete(q)
        db.session.commit()
        return q.serialize(), 200



@faq.route("/category/", methods=["POST"])
def add_category():
    if request.form.get("categoryName"):
        cat = Categoryfaq(name=request.form.get("categoryName"))
        db.session.add(cat)
        db.session.commit()
        return cat.serialize()
    else:
        return {"msg": "missing form components"}, 400

@faq.route("/category/<int:id>", methods=["PUT", "DELETE"])
def edit_category(id):
    c = Categoryfaq.query.get_or_404(id)

    if request.method == "PUT":
        print(request.form)
        if request.form.get("categoryName"):
            print("JA")
            c.name = request.form.get("categoryName")
        
        db.session.commit()
        return c.serialize(), 200
    elif request.method == "DELETE":
        db.session.delete(c)
        db.session.commit()
        return c.serialize(), 200