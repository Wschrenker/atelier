@echo off
setlocal
cd /d "%~dp0"

title Brautkleid-Messmodul (dieses Fenster offen lassen)

set PORT=3301
set URL=http://127.0.0.1:%PORT%/brautkleid-messmodul.html

echo ============================================
echo   Brautkleid-Messmodul
echo ============================================
echo.

REM --- 1) Ist Node.js installiert? ---
where node >nul 2>nul
if errorlevel 1 (
  echo [Fehler] Node.js wurde nicht gefunden.
  echo Bitte Node.js installieren: https://nodejs.org
  echo.
  pause
  exit /b 1
)

REM --- 2) Immer frisch: einen evtl. alten Server auf dem Port beenden ---
echo Pruefe auf alten Server und beende ihn, falls vorhanden...
powershell -NoProfile -Command "Get-NetTCPConnection -LocalPort %PORT% -State Listen -ErrorAction SilentlyContinue | ForEach-Object { Stop-Process -Id $_.OwningProcess -Force -ErrorAction SilentlyContinue }; Start-Sleep -Milliseconds 500"

REM --- 3) Browser-Oeffner im Hintergrund: wartet, bis der frische Server bereit ist ---
start "" /b powershell -NoProfile -Command "for($i=0;$i -lt 60;$i++){try{$c=New-Object Net.Sockets.TcpClient;$c.Connect('127.0.0.1',%PORT%);$c.Close();Start-Process '%URL%';exit}catch{Start-Sleep -Milliseconds 250}}"

echo Server startet frisch... der Browser oeffnet sich automatisch, sobald er bereit ist.
echo.
echo (Zum Beenden dieses Fenster schliessen.)
echo.

REM --- 4) Server im Vordergrund: dieses Fenster IST das laufende Programm ---
node server.js

echo.
echo Der Server wurde beendet.
pause
endlocal
