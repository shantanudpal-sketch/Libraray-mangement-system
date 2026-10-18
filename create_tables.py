
from database import engine, Base
from models import Book

Base.metadata.create_all(bind=engine)

print("Books table created successfully!")
