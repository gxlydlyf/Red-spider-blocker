
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

:start

@echo on
C:\Windows\System32\attrib -r "C:\Program Files (x86)\3000soft\Red Spider"

C:\Windows\System32\attrib -r "C:\Program Files\3000soft\Red Spider"
cd /d C:\Program Files\3000soft\Red Spider
C:\Windows\System32\taskkill /f /t /im "RSpider.exe"
C:\Windows\System32\taskkill /f /t /im "REDAgent.exe"
del /f /s /q REDAgent.exe
C:\Windows\System32\attrib -r "C:\Program Files (x86)\3000soft\Red Spider"
cd /d C:\Program Files (x86)\3000soft\Red Spider
C:\Windows\System32\taskkill /f /t /im "RSpider.exe"
C:\Windows\System32\taskkill /f /t /im "REDAgent.exe"
del /f /s /q REDAgent.exe
C:\Windows\System32\attrib -r "C:\Program Files(x86)\3000soft\Red Spider"
cd /d C:\Program Files(x86)\3000soft\Red Spider
C:\Windows\System32\taskkill /f /t /im "RSpider.exe"
C:\Windows\System32\taskkill /f /t /im "REDAgent.exe"
del /f /s /q REDAgent.exe
            
C:\Windows\System32\taskkill /f /t /im "RSpider.exe"
C:\Windows\System32\taskkill /f /t /im "REDAgent.exe"
del /f /s /q REDAgent.exe
cd /d C:\Program Files\3000soft\Red Spider
rmdir /s/q "C:\Program Files\3000soft\Red Spider"
cd /d C:\Program Files (x86)\3000soft\Red Spider
rmdir /s/q "C:\Program Files (x86)\3000soft\Red Spider"
cd /d C:\Program Files(x86)\3000soft\Red Spider
rmdir /s/q "C:\Program Files(x86)\3000soft\Red Spider"

goto start
