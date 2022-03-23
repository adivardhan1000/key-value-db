Implementing a basic database that operates on key value pair as queried

For this implementation, we will creating our own Database instead of using a NoSQL in backend.

Assumption:
    COMPACT works for only variables intialized in the session
    Any variables alredy existing won't be accounted for
    


## Managing Environment 
### Create a env:
    python -m venv myenv

### Activate env:
     .\myenv\Scripts\activate

### Install all required packages from requirements.txt
    pip install -r requirements.txt

#### Note: Always update requirements.txt if new packages are installed
    pip freeze > requirements.txt

## Running Code
### Running tests
    coverage run -m pytest
    # To generate html report
    coverage html