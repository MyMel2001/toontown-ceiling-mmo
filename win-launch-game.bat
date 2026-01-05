@echo off
color 0a
title Toontown Ceiling Launcher
cd %~dp0
set /p IP="Host IP:"
start python.exe launch.py
pause
