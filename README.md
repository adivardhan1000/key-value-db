# Implementing a basic database that operates on key value pair as queried

### For this implementation, we will be using redis cloud. This makes it usable across Linux and Windows. This can be implemented locally on a Linux system
Note: Redis is not supported by windows 10. To run on windows, you need to install Linux subsystem for windows and run it from there.

### Note: Not Production Ready:

    Logging will need to be removed from all try/catch blocks

Assumption:

    COMPACT works for only variables intialized in the session. Any already existing data/variables won't be used.
    Meaning, COMPACT lines generated will only consist of newly used variables in the current session.

Future:

    MULTI functionality will require a validate fucntion that will validate all the lines before it starts running them. In current setting it will stop the program where it breaks

Note:
* Story 5 doesn't seem to be applicable for on cloud database.

## Commands supported

| Command Name | Function                                                                          | Input             | Output                  |   |   |   |
|---------------|-----------------------------------------------------------------------------------|-------------------|-------------------------|---|---|---|
| SET           | sets/replaces/creates a key/value pair                                            | SET key value     | True(Success)           |   |   |   |
| GET           | gets value if exists                                                              | GET key           | Value                   |   |   |   |
| INCR          | increments the value by 1                                                         | INCR key          | Value (after increment) |   |   |   |
| INCRBY        | increments the value by amount specified                                          | INCRBY key amount | Value (after increment) |   |   |   |
| MULTI         | Starts storing the commands to be executed later                                  | MULTI             | None                    |   |   |   |
| EXEC          | Executes all commands since MULTI                                                 | EXEC              | None                    |   |   |   |
| DISCARD       | Deletes all stored commands                                                       | DISCARD           | None                    |   |   |   |
| DEL           | Deletes key and value                                                             | DEL key value     | True                    |   |   |   |
| COMPACT       | Converts all commands in session into set operation (limitations discussed above) | COMPACT           | List of commands        |   |   |   |


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
### Main file
    python .\key_value_db\main.py 
### Running tests
    coverage run -m pytest
    # To generate html report
    coverage html