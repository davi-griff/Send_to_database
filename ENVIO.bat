@echo off

set HOME_SCRIPT=%~dp0
set HOME_VIRTUAL_ENV=%HOME_SCRIPT%\env

call "%HOME_VIRTUAL_ENV%\Scripts\activate.bat"

py "%HOME_SCRIPT%\main.py" 
