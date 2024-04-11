
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model): 
    
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    
    username = db.Column(db.String(80), unique=True, nullable=False)
    
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        
        return self.username
    
    def get_id(self) -> int:
        
        return self.id
    
    def get_username(self) -> str: 
        
        return self.username
    
    def set_username(self,username) -> None:
        
        self.username = username
        
    def get_email(self) -> str: 
        
        return self.email
        
    def set_email(self,email) -> None:
        
        self.email = email
        
    
        
        
