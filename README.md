# sonicwall_export
Script for extracting certain information from a Sonicwall firewall API using Python and extracting them into a CSV.

# Info
I made this script in a pinch to export my Sonicwall's info for migration to Palo Alto. It was used against SonicOS 6.5. Some items may not fit your firewalls. As such, security wasn't a priority. For connecting to the SW, you just need a username and password.

# Files
`sonicos.py` - The main script. You will need to edit the connection information on line 8.
`SonicOS/SonicAPI` - Contains a class for the API object. Nothing should be edited here unless you want to add more endpoints for extrations. The existing endpoints are all I needed.

# Requirements
- Tested against python 3.9
- `requests` - module for making http calls.

Be sure to run `pip install -r requirements.txt` to install from the requirements file.
