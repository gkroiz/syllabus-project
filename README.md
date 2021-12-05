# UMBC Syllabus Synthsizer Project for CMSC 447 - Section 03

## For COEIT departments only:

    - Chemical, Biochemical, & Environmental Engineering (CBEE)
    - Computer Science and Electrical Engineering (CSEE)
    - Information Systems (IS)
    - Mechanical Engineering (ME)

## Authors:

    - Sam Bailor
    - Koby Samuel
    - Eddie Nieberding
    - Gerson Kroiz
    - Deep Mistry

## Technical information
The prerequisite software required to develop this program are Python 3, Django (pip module), textract (pip module), python-decouple (pip module), and optionally virtualenv (separate Python product) to make your life easier.

The software needs to be configured with the appropriate .env file (secret key and other related info) that can be collected from the project lead. From there, choose an IDE and make sure you have Git to push changes as needed.

To run the SynthesizePDF tests, at the moment, do nothing. The feature for synthesizing PDFs is not specifically tested without significantly redoing the codebase, so testing is done by ```runserver``` with ```manage.py``` instead of ```tests.py```.

To test with PDF, have available a PDF file that can be a syllabus where the appropriate fields can be extracted using pre-filled fields - running ```
python manage.py runserver``` and going to the server address/add - it will use your syllabus file as an example for ```extract_data.py```, the main component for the puzzle. 
