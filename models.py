from sqlalchemy import Table, Column, Integer, String, ForeignKey, Text, DateTime, Boolean
from sqlalchemy.orm import validates
from database import Base
from validators import ValidateHelper

class User(Base):
    __tablename__ = 'user'
    id            = Column(Integer, primary_key=True)
    name          = Column(String(255))
    email         = Column(String(255))
    user_agent    = Column(Text)
    insert_date   = Column(DateTime)

    @validates('name')
    def validate_name(self, key, field):
        return ValidateHelper.validate_string(field)
#        return str(type(field))
#        return field

    @validates('email')
    def validate_email(self, key, field):
# key= 'email', field=email value 
        return ValidateHelper.validate_email(field)
#        return field

    def __init__(self, name=None, email=None, user_agent=None, insert_date=None):
        self.name        = name
        self.email       = email
        self.user_agent  = user_agent
        self.insert_date = insert_date

    def __repr__(self):
        return '<User %r>' % (self.name)

class Quiz(Base):
    __tablename__ = 'quiz'
    id            = Column(Integer, primary_key=True)
    title         = Column(String(255))
    insert_date   = Column(DateTime)
    publish_date  = Column(DateTime)
    category_id   = Column(Integer, ForeignKey("category.id"))

    def __init__(self, title=None, insert_date=None, publish_date=None, category_id=None):
        self.title        = title
        self.insert_date  = insert_date
        self.publish_date = publish_date
        self.category_id  = category_id

    def __repr__(self):
        return '<Quiz %r>' % (self.title)


class UserQuiz(Base):
    __tablename__     = 'user_quiz'
    id                = Column(Integer, primary_key=True)
    user_id           = Column(Integer, ForeignKey("user.id"))
    quiz_id           = Column(Integer, ForeignKey("quiz.id"))
    score             = Column(Integer)
    selected_answers  = Column(Text)
    completed_date    = Column(DateTime)

    def __init__(self, user_id=None, quiz_id=None, score=None, selected_answers=None, completed_date=None):
        self.user_id          = user_id
        self.quiz_id          = quiz_id
        self.score            = score
        self.selected_answers = selected_answers
        self.completed_date   = completed_date

    def __repr__(self):
        return '<UserQuiz %r>' % (self.id)


class Question(Base):
    __tablename__     = 'question'
    id                = Column(Integer, primary_key=True)
    question          = Column(Text)
    hint              = Column(Text)

    def __init__(self, question=None, hint=None):
        self.question         = question
        self.hint             = hint

    def __repr__(self):
        return '<Question %r>' % (self.id)


class QuizQuestion(Base):
    __tablename__     = 'quiz_question'
    id                = Column(Integer, primary_key=True)
    quiz_id           = Column(Integer, ForeignKey("quiz.id"))
    question_id       = Column(Integer, ForeignKey("question.id"))

    def __init__(self, quiz_id=None, question_id=None):
        self.quiz_id      = quiz_id
        self.question_id  = question_id

    def __repr__(self):
        return '<QuizQuestion %r>' % (self.id)


class Answer(Base):
    __tablename__    = 'answer'
    id               = Column(Integer, primary_key=True)
    question_id      = Column(Integer, ForeignKey("question.id"))
    answer           = Column(Text)
    correct          = Column(Boolean)

    def __init__(self, question_id=None, answer=None, correct=None):
        self.question_id  = question_id
        self.answer       = answer
        self.correct      = correct

    def __repr__(self):
        return '<Answer %r>' % (self.id)

class Category(Base):
    __tablename__    = 'category'
    id               = Column(Integer, primary_key=True)
    category         = Column(String(255))
    description      = Column(Text)

    def __init__(self, category=None, description=None):
        self.category      = category
        self.description   = description

    def __repr__(self):
        return '<Category %r>' % (self.id)


