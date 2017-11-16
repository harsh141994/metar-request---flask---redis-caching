This is a flask application.
I have used the python-metar module to help me with the parsing of the data that I am getting after making the request

How to use:

the url is of the form :

http://localhost:8080/metar/info/<code>/<int:nocache>

for eg,:

http://localhost:8080/metar/info/KSGS/1

where code is the station code and for nocache=1, I make a new request call.

