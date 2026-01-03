@echo off
color 0a
title Toontown Ceiling Launcher
cd %~dp0
start "thirdparty/Panda3D-1.10.11/python/ppython.exe" server/server.py
start "thirdparty/Panda3D-1.10.11/python/ppython.exe" launch.py
pause
