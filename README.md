# Library Management System

A library management application built using Python, FastAPI, Streamlit, SQLAlchemy, and PostgreSQL.

## Overview

This project provides a web interface and backend APIs to manage library book records.

## Features

- Add book records
- View book records
- Update book records
- Delete book records
- PostgreSQL database integration

## Technologies Used

- Python
- FastAPI
- Streamlit
- SQLAlchemy
- PostgreSQL

## Project Files

- `main.py` - FastAPI backend
- `app.py` - Streamlit frontend
- `database.py` - Database connection
- `models.py` - Database models
- `create_tables.py` - Database table setup
- `Test_DB.py` - Database connection test

## Installation and Setup

1. Clone this repository.
2. Create and activate a Python virtual environment.
3. Install dependencies from `requirements.txt` (once added).
4. Configure your PostgreSQL connection in the expected environment configuration.

## Run the Backend

```bash
uvicorn main:app --reload
```

Open http://127.0.0.1:8000/docs to explore the API.

## Run the Frontend

Open a separate terminal and run:

```bash
streamlit run app.py
```

## Future Improvements

- Book issue and return tracking
- Due dates and overdue status
- Automated tests
- Online deployment
