from app import db, User

# Create a new user
new_user = User(username='john_doe', email='john@example.com', password='password123')
db.session.add(new_user)
db.session.commit()
