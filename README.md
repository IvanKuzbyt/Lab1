# Warehouse Manager

Laboratory project for the course "Professional Python" (Variant 10: Система обліку складських запасів).

## Description
Console application for tracking warehouse inventory, managing stock levels, calculating total asset values, and identifying low-stock items.

## Requirements
- Python 3.11+

## Installation
python -m venv .venv
# Activate the virtual environment (.venv\Scripts\activate on Windows)
python -m pip install -e .

## Run
python -m warehouse_manager.main

or via console command:
warehouse-manager

## Project Structure
- `src/warehouse_manager/models.py` — Data models (`WarehouseItem`)
- `src/warehouse_manager/services.py` — Business logic (stock operations, search, evaluation)
- `src/warehouse_manager/main.py` — Console menu entry point

## Author
Student: Кузбит Іван  
Group: ФЕП-32