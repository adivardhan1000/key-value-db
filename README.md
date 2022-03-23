Implementing a basic database that operates on key value pair as queried

For this implementation, we will be using redis cloud.

Assumption:
    COMPACT works for only variables intialized in the session. Any already existing data/variables won't be used.
    Meaning, COMPACT lines generated will only consist of newly used variables in the current session.



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