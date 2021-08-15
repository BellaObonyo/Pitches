from app.models import Comment, User
from app import db

def setUp(self):
  self.user_Bella= User(username = 'Cynthia',password = '123456', email = 'obonyocy@ueab.ac.ke')
  self.new_comment = Comment(id=1,user_id=10,comment='This Pitch is nice', pitch_id = 12)

