#!/bin/pwsh

if (Get-Command pip -ErrorAction SilentlyContinue) {
    Write-Host "Installing Python dependencies..."
    pip install -r requirements.txt
}
else {
    Write-Host "pip is not installed"
    Write-Host "Installing pip"
    Invoke-WebRequest -Uri https://bootstrap.pypa.io/get-pip.py -OutFile get-pip.py
    python get-pip.py
    Write-Host "Installing Python dependencies..."
    pip install -r requirements.txt
}

if (Get-Command pytest -ErrorAction SilentlyContinue) {
    Write-Host "Running tests..."
    pytest --version
    pytest
}
else {
    Write-Host "pytest is not installed"
    Write-Host "installing pytest"
    pip install pytest
    pytest --version
    pytest
}