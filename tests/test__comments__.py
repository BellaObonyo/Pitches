from app.models import Comment, User
from app import db

def setUp(self):
  self.user_Bella= User(username = 'Cynthia',password = '123456', email = 'obonyocy@ueab.ac.ke')
  self.new_comment = Comment(id=1,user_id=10,comment='This Pitch is nice', pitch_id = 9)

def tearDown(self):
  Comment.query.delete()
  User.query.delete()
  def test_check_instance_variables(self):
    self.assertEquals(self.new_comment.id,1)
    self.assertEquals(self.new_comment.user_id,10)
    self.assertEquals(self.new_comment.comment,'This Pitch is nice')
    self.assertEquals(self.new_comment.pitch_id,9)
        
def test_save_comment(self):
  self.new_comment.save_comment()
  self.assertTrue(len(Comment.query.all())>0)
        
def test_get_comment_by_id(self):
  self.new_comment.save_comment()
  got_comments = Comment.get_comments(12345)
  self.assertTrue(len(got_comments) == 1)