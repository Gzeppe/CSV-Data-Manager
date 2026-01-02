# 📊 CSV Data Manager — Python CLI Tool

A command-line tool for loading, filtering, and exporting CSV data. This project focuses on data manipulation, user input validation, and practical workflows commonly found in configuration and data-processing tasks.

## Why This Project
I built this tool to practice working with structured data files, handling user-driven filtering logic, and designing CLI workflows that are resilient to invalid input — similar to internal tools used for data cleanup, configuration management, and reporting.

## Features
- Load CSV files into memory
- Filter rows by column and value
- Sort and refine datasets
- Save filtered results to a new CSV file
- Input validation and user-friendly error handling

## Backend / Data Concepts Demonstrated
- File I/O and structured data processing
- User input validation and error handling
- Conditional filtering logic
- Separation of concerns between data handling and CLI flow
- Reusable functions for data operations

## Tech Stack
- Python 3.10+
- pandas (for data manipulation and filtering)
- Standard library modules (`csv`, `os`) where applicable

## Project Structure
```text
CSV-Data-Manager/
├── data.csv             # Sample dataset
├── filtered_data.csv    # Output after filtering
├── main.py              # Application entry point
├── README.md            # Project documentation
└── .gitignore
