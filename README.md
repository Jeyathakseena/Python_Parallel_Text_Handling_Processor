
#  Python Parallel Text Handling Processor

##  Project Overview

This project focuses on building a text handling processor that works at the same time using Python's multi-tasking. It breaks up text, applies simple pattern finding, and stores results in a database for easy access.

The system uses CSV files for batch processing and provides summaries for analysis. It is designed to handle large text datasets efficiently, run tasks simultaneously such as rule-based sentiment scoring, and generate searchable records.

This project helps language experts and data workers analyze text efficiently without requiring advanced text processing tools.

---

##  Outcomes

* Scalable handling of text for quick processing.
* Accurate rule-based scoring of feelings and pattern detection.
* Structured and searchable text storage using a database.
* Improved text processing workflow with automated handling and reporting.

---

# 🔹 Task 1 – Multithreaded Text Processing

###  Features

* Processes multiple text files in parallel using Python threading.
* Converts text content to lowercase for uniform processing.
* Applies rule-based sentiment scoring.
* Calculates total execution time for multitasking.

###  Technologies Used

* Python `threading` module

---

# 🔹 Task 2 – SQLite Database Integration

###  Features

* Creates and manages a local SQLite database.
* Stores filename and sentiment score.
* Retrieves and displays stored records.
* Ensures proper database connection handling.

###  Technologies Used

* `sqlite3` module

---

# 🔹 Task 3 – Hotel Review Sentiment Analysis

###  Features

* Uses TripAdvisor hotel review dataset (CSV format).
* Implements domain-specific rule-based scoring system.
* Performs aspect-based sentiment classification.
* Stores review text, score, sentiment, and timestamp in SQLite database.
* Includes proper exception handling for file and database operations.

###  Reviews Classification

Reviews are classified as:

* **Satisfied**
* **Dissatisfied**
* **Neutral**




###  Technologies Used

* `csv` module
* `sqlite3`
* `datetime`

---

## 🔹 Task 4 – Performance & Optimization Test

● Processed a large dataset (~1 million records simulated using repeated CSV data).

● Inserted scored records into SQLite database.

● Measured:

* Insert execution time
* Query execution time

● Applied table optimization using indexing on `overall_sentiment` column.

● Re-ran the same query and recorded new execution time.

● Compared performance before and after optimization.



### Technologies Used:

● sqlite3

● time module (execution time measurement)

● CSV dataset processing

● SQL indexing

---

