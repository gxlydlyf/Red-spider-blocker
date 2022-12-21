
@echo off
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"

if '%errorlevel%' NEQ '0' (

echo 请求管理员权限...

goto UACPrompt

) else ( goto gotAdmin )

:UACPrompt

echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"

echo UAC.ShellExecute "%~s0", "", "", "runas", 1 >> "%temp%\getadmin.vbs"

"%temp%\getadmin.vbs"

exit /B

:gotAdmin
echo C:\Program Files (x86)\3000soft\Red Spider
@echo on
:start


attrib -r "C:\Program Files (x86)\3000soft\Red Spider"

attrib -r "C:\Program Files\3000soft\Red Spider"
cd /d C:\Program Files\3000soft\Red Spider
taskkill /f /t /im "REDAgent.exe"
attrib -r "C:\Program Files (x86)\3000soft\Red Spider"
cd /d C:\Program Files (x86)\3000soft\Red Spider
taskkill /f /t /im "REDAgent.exe"
attrib -r "C:\Program Files(x86)\3000soft\Red Spider"
cd /d C:\Program Files(x86)\3000soft\Red Spider
taskkill /f /t /im "REDAgent.exe"
            
rmdir /s/q "C:\Program Files\3000soft\Red Spider"
rmdir /s/q "C:\Program Files (x86)\3000soft\Red Spider"
rmdir /s/q "C:\Program Files(x86)\3000soft\Red Spider"
taskkill /f /t /im "REDAgent.exe"

goto start
