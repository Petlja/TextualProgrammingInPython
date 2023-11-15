@echo off
IF EXIST .venv (
    echo .venv exists, updating it...
    start cmd /k ".venv\Scripts\activate && pip install -r requirements.txt && cls"
) ELSE (
    echo .venv does not exist, creating it...
    python -m venv .venv
    start cmd /k ".venv\Scripts\activate && pip install -r requirements.txt && cls"
)