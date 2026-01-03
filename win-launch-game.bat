@echo off
color 0a
title Toontown Ceiling Launcher
cd %~dp0
set /p IP="Host IP:"
start "thirdparty/Panda3D-1.10.11/python/ppython.exe" launch.py
pause
