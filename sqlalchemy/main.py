from sqlalchemy import Column, Integer, String, ForeignKey, Sequence, create_engine
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

engine = create_engine('sqlite:///orm.db', echo =True)

Session = sessionmaker(bind = engine)
session = Session()

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    email = Column(String(50))

    posts = relationship('Post', back_populates="user") 

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    content = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', back_populates="posts") 

Base.metadata.create_all(engine)

user1 = User(name = "Sarthak", email= "sarthakvyas@gmail.com")
user2 = User(name = "Vansh", email= "vanshvora@gmail.com")

post1 = Post(title= 'sarthak first post', content= "this sarthak's first post", user= user1)
post2 = Post(title= 'sarthak seconf post', content= "this sarthak's second post", user= user1)
post3 = Post(title= 'vansh first post', content= "this vansh's first post", user= user2)

session.add_all([user1, user2, post1, post2, post3])
session.commit()

post_with_users = session.query(Post, User).join(User).all()

for post, user in post_with_users:
    print(f"{post.title} {user.name}")

Sarthak = session.query(User).filter_by(name = 'Sarthak').first()
for post in Sarthak.posts:
    print(f"{post.title}")