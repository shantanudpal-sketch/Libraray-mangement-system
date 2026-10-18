
# Import FastAPI tools
from fastapi import FastAPI, Depends, HTTPException, status

# Import SQLAlchemy session
from sqlalchemy.orm import Session

# Import database session
from database import SessionLocal

# Import database model
from models import Book

# Import Pydantic schemas
from schemas import BookCreate, BookUpdate, BookResponse


# Create FastAPI application
app = FastAPI(title="Library Management System API")


# Provide database session to each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# HOME: Check whether API is running
@app.get("/")
def home():
    return {"message": "Library Management System is running"}


# CREATE: Add a new book
@app.post(
    "/books",
    response_model=BookResponse,
    status_code=status.HTTP_201_CREATED
)
def add_book(book: BookCreate, db: Session = Depends(get_db)):

    # Create database object
    new_book = Book(
        title=book.title,
        author=book.author
    )

    # Save book to PostgreSQL
    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return new_book


# READ: Get all books
@app.get("/books", response_model=list[BookResponse])
def get_books(db: Session = Depends(get_db)):

    # Fetch all books from database
    return db.query(Book).all()


# READ: Get one book by ID
@app.get("/books/{book_id}", response_model=BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):

    # Find book by ID
    book = db.query(Book).filter(Book.id == book_id).first()

    # Return 404 if book does not exist
    if book is None:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return book


# UPDATE: Update an existing book
@app.put("/books/{book_id}", response_model=BookResponse)
def update_book(
    book_id: int,
    updated_book: BookUpdate,
    db: Session = Depends(get_db)
):

    # Find book by ID
    book = db.query(Book).filter(Book.id == book_id).first()

    # Check whether book exists
    if book is None:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    # Get only the fields provided by the user
    update_data = updated_book.model_dump(exclude_unset=True)

    # Reject an empty update request
    if not update_data:
        raise HTTPException(
            status_code=400,
            detail="Provide title or author to update"
        )

    # Apply changes
    for field, value in update_data.items():
        setattr(book, field, value)

    # Save changes
    db.commit()
    db.refresh(book)

    return book


# DELETE: Remove a book
@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):

    # Find book by ID
    book = db.query(Book).filter(Book.id == book_id).first()

    # Check whether book exists
    if book is None:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    # Delete book from PostgreSQL
    db.delete(book)
    db.commit()

    return {"message": "Book deleted successfully"}
