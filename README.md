# Library Management System
The createTable_sqlfile contains all the sql codes for creatig the table and queries used in this project.
## Project Overview
This Library Management System (LMS) enhances library operations by providing insights into borrowing patterns, managing late book returns, and generating personalized book recommendations. By transitioning from spreadsheet-based systems to a robust SQL database, this system optimizes the storage, retrieval, and management of library data. It includes a web interface for easy interaction with the database, enabling users to perform essential operations like adding new records, viewing borrowing history, and analyzing library trends.

### Features:
- **Backend Database**: A PostgreSQL database hosted on Render for online accessibility.
- **Web Interface**: User-friendly interface developed in Python to interact with library data.
- **Data Insights**: Analyzes user behavior, identifies popular book genres, and explores late return patterns.

---

## Project Files and Structure

### 1. **Database Setup & Deployment**:
- **Render**: Deployed PostgreSQL database on Render for remote access.
- **Data Import**: Fake-generated CSV files populated the database with data on books, authors, users, transactions, and subscriptions.
- **SQL Scripts**: SQL queries created tables and inserted data while ensuring referential integrity with foreign key constraints.

### 2. **Web Interface**: ( can be accesed using this link https://library-management-h292.onrender.com/)
- **Python Files**: (Go to this link to get access to all these files https://drive.google.com/drive/folders/1B2IeCn5gIvYco9ofMnCTDBHkZqmYqVW0?usp=drive_link)
  - `urls.py`: Defines URLs for accessing different views in the system.
  - `views.py`: Contains core functions to handle website features, such as adding, updating, and retrieving records.
  - `settings.py`: Configures the database connection to the cloud-hosted PostgreSQL instance.

### 3. **Key Database Tables**:
- **Books**: Information about books, such as title, genre, and publisher.
- **Authors**: Details of authors, including name and country.
- **Users**: User details such as name, occupation, and subscription type.
- **Transactions**: Tracks the borrowing and returning of books.
- **Publishers**: Contains publisher details.
- **Subscriptions**: Information on subscription types, return policies, and costs.

### 4. **Database Schema**:
An **Entity-Relationship (ER) Diagram** was created to visualize the relationships between tables such as books, authors, transactions, and users. The system ensures data integrity and supports complex queries.

### 5. **Queries and Insights**:
- **Most Borrowed Genres**: Identifies the most frequently borrowed book genres.
- **Popular Author’s Books**: Finds the most borrowed books by authors.
- **Late Returns**: Analyzes reasons for late returns based on user demographics and subscription types.

---

## Setup and Execution

### Prerequisites:
- Python 3.4 or higher
- PostgreSQL database and **pgAdmin** for managing the database
- **Render** account for hosting the PostgreSQL database
- Python libraries: `Django`, `psycopg2`, `sqlalchemy` for database interaction

### Installation Steps:
1. **Clone the Repository**:
   ```bash
   git clone <repo-url>
