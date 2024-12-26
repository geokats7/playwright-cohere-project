Installation of project. Create a new virtual environment using python 3.9+ and then run:  
`pip install -r requirements.txt`  
`playwright install`

Run the tests from project root:  
`pytest tests/tests_cohere_pom.py`


IMPOVEMENTS
- Refactor to use Page Object Model structure - The file `tests_cohere.py` contains the tests before applying POM
- Fix scenario 2 to work with upload file
- Replace hardcoded "wait" for file upload with actual waiting until the file is uploaded
- Get sensitive data (password) from .env file
