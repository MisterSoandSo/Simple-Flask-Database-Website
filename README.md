# Simple Flask Database Website
The purpose of this project was to demo a simple proof of concept that implemented flask, waitress, sqlite, regex on cloud computing platforms such as AWS and Azure.
This project assumes you have your own web server or you are running this on your own machine.

The initial goal are as follow:
1. Setup virtual environment to containerize project
2. Process any type of mass input such as chat or and api call for line by line data
3. Store processed data in a SQL or CSV format
4. Display and sort data in a easy to read format
5. Deploy project to production server

## Setup Virtual Environment
In the console or terminal, type `python -m venv venv` to initialize the python virtual environment. In linux, you might have to run `sudo apt update && apt update -y` to install pip for later uses.
```
# Windows Users
.\venv\Scripts\activate

# Unix/ Mac Users
source venv/bin/activate

# Exit venv Command
deactivate

```

## Requirements
- `flask <https://pypi.org/project/Flask/>`_
- `waitress <https://pypi.org/project/waitress/>`_


Using ``pip install -r requirements.txt`` should cover everything.

## License
This project is licensed under the GNU v3 License.

