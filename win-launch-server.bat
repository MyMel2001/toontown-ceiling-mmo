@echo off
color 0a
title Toontown Ceiling Server Launcher
cd %~dp0
start python.exe server/server.py
pause
