1. 
## Your index.html file must be inside the templates folder for Flask to find it. 
The render_template() function specifically looks for HTML files within a directory named templates by default.

2. 
## Activate Your Environment
Open a terminal in your project folder and run the activation script if you haven't already.

PowerShell

.\venv\Scripts\activate


3. 
## List the Packages

pip list


4.
## To generate a requirements file:

pip freeze > requirements.txt


5. 
## Deactivate the Current Environment

deactivate


6. 
## Whenever stuck in environment 
Copy the path of your python.exe file inside the Scripts folder inside venv file, You will get the interpreter path and paste it in interpreter path option in vs code.