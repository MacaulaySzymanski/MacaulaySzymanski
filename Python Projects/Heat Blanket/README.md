heatblanket.py

Purpose: Created to help wife make a heat blanket with submission of accurate 
average temparatures via scripted automation

Method: Gets historical data from api.worldweatheronline.com and extracts
average temperatures twice per week on Monday and Thursday. Afterwards, it
adds the information to a google sheet. Example photo included in Git repository.

Usage:

1. Set up a worldweatheronline.com account
	1b. file for an API Key
	1c. input key into script under Parameters.apikey
2. Set up a Google Developer account
	2b. File for a Google Sheets access + refresh token
	2c. Authorize/Authenticate gsheets relating a key file to SERVICE_ACCOUNT_FILE
	2d. Replace SAMPLE_SPREADSHEET_ID with the google sheet ID where you are going
	to write the info
3. Convert location to latitude & longitudinal Geographic coordinate system via converter
systems such as latlong.net
	3b. Input info to variables 'lat' & 'lon' in the class 'Parameters'
4. Determine how frequently an average should be taken and modify the following
	- '_resolveDate' with as many dates as needed per week related as an integer
	example: Mondays are considered day 0, and Thursdays are day 3
	- in addition to '_resolveDate', under each time averaged, the time delta should
	be changed in order to reflect the amount of days being averaged represented as
	the var startDay with a time delta subtracting the amount of days queried/averaged
5. Input which colors and temperature ranges will be assigned to each color