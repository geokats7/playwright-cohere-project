Installation of project. Create a new virtual environment using python 3.9+ and then run:  
`pip install -r requirements.txt`  
`playwright install`

**NOTE**  
Make sure to add a `.env` file with the appropriate values at the project root

Run the tests from project root:  
`pytest tests/tests_cohere_pom.py`


IMPOVEMENTS
- Refactor to use Page Object Model structure - The file `tests_cohere.py` contains the tests before applying POM
- Fix scenario 2 to work with upload file
- Replace hardcoded "wait" for file upload with actual waiting until the file is uploaded
- Get sensitive data (password) from .env file
- Add XML report under `tests/reports` folder for further automation (integration with test management tools, etc)
