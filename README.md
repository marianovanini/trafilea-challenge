# Trafilea-API-python-flask

This is a Flask project that contains a basic web application.

## Requirements

- Python 3.8 or higher
- Flask 1.1.2 or higher
- flask-swagger-ui 0.0.3 or higher


## Project structure

```
I use python in this case with Flask as a framework, I made an small API to do the following challenge. I just considered to use memory to save the numbers, so if you decide to reload the script, all changes will be lost. I added an small swagger documentation

```

## The challenge

This exercise challenges you to develop a RESTful API with functionalities similar to a
specific logic while adhering to certain constraints.

Objective
Implement an API that categorizes and stores numbers based on their divisibility by
3 and 5, mimicking the logic described below:
● Numbers divisible by 3: Categorized as "Type 1"
● Numbers divisible by 5: Categorized as "Type 2"
● Numbers divisible by both 3 and 5: Categorized as "Type 3"
● Other numbers: Stored as their original value

Constraints

● Utilize only one if statement within the core logic. Avoid else, else if, ternary
operators, or switch statements.

Functional Requirements
● Data Storage:

○ The API shall store numbers and their classifications in memory or any other support you consider appropriate.

○ Classifications include:
    ■ Numbers divisible by 3: Categorized as "Type 1"
    ■ Numbers divisible by 5: Categorized as "Type 2"
    ■ Numbers divisible by both 3 and 5: Categorized as "Type 3"
    ■ Other numbers: Stored as their original value

● Number Addition:
    ○ The API shall provide a mechanism to save a number into its collection.
● Number Retrieval:
    ○ The API shall allow the retrieval of a specific number's classification. If the number is not found, the API should indicate this.

● Collection Retrieval:
    ○ The API shall enable the retrieval of all stored numbers and their classifications.

## Execution
To run the application, use the following command in your terminal:

python app.py

This will start the application at localhost:5000.

## API Documentation
The API documentation is available at localhost:5000/api/docs after starting the application.

