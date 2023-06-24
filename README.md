# Simple Flask Database Website
The purpose of this project was to demo a simple proof of concept that implemented flask, waitress, sqlite, regex on cloud computing platform such as AWS and Azure.
This project assumes you have your own webserver or you are running this on your own machine.

The inital goal are as follow:
1. Setup virtual enviroment to containize project
2. Process any type of mass input such as chat or and api call for line bye line data
3. Store processed data in a SQL or CSV format
4. Display and sort data in a easy to read format
5. Deploy project to production server

## Setup Virtual Environemnt
In console or terminal, type `python -m venv venv` to initalize the python virtual environment. In linux, you might have to run `sudo apt upgrate && apt update -y` to install pip for later uses.
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