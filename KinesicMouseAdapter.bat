echo off
set facialAction=%1
set upOrDown=%2
shift
shift
echo actions.user.genericFacialAction("%facialAction%", "%upOrDown%") | "%ProgramFiles%/Talon/python.exe" "%ProgramFiles%/Talon/repl.py"