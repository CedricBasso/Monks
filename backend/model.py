from database import db
from datetime import datetime

class Workflow(db.Model):
   __tablename__ = 'workflow'
   id   = db.Column('workflow_id', db.Integer, primary_key = True)
   name = db.Column('workflow_name',db.String(100),nullable=False)
   creattion_date = db.Column('workflow_creation_date',db.DateTime,nullable=False,default=datetime.utcnow)
   status = db.relationship("Status")


class Status(db.Model):
   __tablename__ = 'status'
   id   = db.Column('status_id', db.Integer, primary_key = True)
   name = db.Column('status_name',db.String(100),nullable=False)
   creattion_date = db.Column('workflow_creation_date',db.DateTime,nullable=False,default=datetime.utcnow)
   workflow_id = db.Column(db.Integer, db.ForeignKey('workflow.workflow_id'))
   image = db.relationship("Image")

class Image(db.Model):
   __tablename__ = 'image'
   id  = db.Column('image_id', db.Integer, primary_key = True)
   url = db.Column('image_url',db.String(100))
   creattion_date = db.Column('workflow_creation_date',db.DateTime,nullable=False,default=datetime.utcnow)
   status_id = db.Column(db.Integer, db.ForeignKey('status.status_id'))


