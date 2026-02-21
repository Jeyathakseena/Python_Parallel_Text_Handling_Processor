Python Parallel Text Handling Processor 

This project focuses on making a text handling processor that 
works at the same time, using Python's multi-tasking for breaking up text, a module 
for simple pattern finding, and a simple database for text storage. It has csv files for 
batch checks and email service for summaries. The system handles big text sets, 
runs tasks at the same time like scoring feelings with rule-based rules, and makes 
searchable lists. It helps language experts and data workers mine text well without 
special text tools. 

Outcomes: 

● Easy to grow handling of text for quick checks. 

● Rule-based scoring of feelings and patterns that works right. 

● Stored text that's easy to search for info. 

● Better text work with auto alerts and group reports. 


🔹 Task 1 – Multithreaded Text Processing

● Processes multiple text files in parallel using Python threading.

● Converts text to lowercase.

● Applies rule-based sentiment scoring.

● Calculates execution time for multitasking.

Technologies used:

● Python threading module


🔹 Task 2 – SQLite Database Integration

● Creates a local SQLite database.

● Stores filename and sentiment score.

● Retrieves and displays stored records.

Technologies used:

● sqlite3 module


🔹 Task 3 – Hotel Review Sentiment Analysis

● Uses TripAdvisor hotel review dataset (CSV).

● Implements domain-specific rule-based scoring system.

Classifies reviews as:
        ● Satisfied
        ● Dissatisfied
        ● Neutral

● Stores text, score, sentiment, and timestamp in SQLite database.

● Includes proper file and database exception handling.

Technologies used:

● csv module

● sqlite3

● datetime
