from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import secrets

db = SQLAlchemy()

class Tool(db.Model):
    """Model narzędzia w bazie danych"""
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50))
    description = db.Column(db.Text)
    status = db.Column(db.String(20), default='available')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Powiązanie z historią
    history = db.relationship('ToolHistory', backref='tool', lazy=True)
    
    def generate_code(self):
        """Generuje unikalny kod narzędzia"""
        prefix = self.category[:3].upper() if self.category else 'TOL'
        suffix = secrets.token_hex(3).upper()
        self.code = f"{prefix}-{suffix}"
        return self.code
    
    def to_dict(self):
        """Konwertuje obiekt na słownik (do JSON)"""
        return {
            'id': self.id,
            'code': self.code,
            'name': self.name,
            'category': self.category,
            'description': self.description,
            'status': self.status,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

class User(db.Model):
    """Model użytkownika"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200))
    role = db.Column(db.String(20), default='worker')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    history = db.relationship('ToolHistory', backref='user', lazy=True)

class Project(db.Model):
    """Model projektu"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    status = db.Column(db.String(20), default='active')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    history = db.relationship('ToolHistory', backref='project', lazy=True)

class ToolHistory(db.Model):
    """Historia wypożyczeń"""
    id = db.Column(db.Integer, primary_key=True)
    tool_id = db.Column(db.Integer, db.ForeignKey('tool.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    action = db.Column(db.String(20))
    borrowed_at = db.Column(db.DateTime, default=datetime.utcnow)
    returned_at = db.Column(db.DateTime)
    notes = db.Column(db.Text)
    
    def to_dict(self):
        return {
            'id': self.id,
            'tool': self.tool.name if self.tool else None,
            'tool_code': self.tool.code if self.tool else None,
            'user': self.user.username if self.user else None,
            'project': self.project.name if self.project else None,
            'action': self.action,
            'borrowed_at': self.borrowed_at.isoformat() if self.borrowed_at else None,
            'returned_at': self.returned_at.isoformat() if self.returned_at else None,
            'notes': self.notes
        }