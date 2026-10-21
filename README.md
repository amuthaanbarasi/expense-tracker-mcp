# Expense Tracker MCP Server

## Overview
This project connects an MCP server to an existing Expense Tracker API built with FastAPI. It allows an AI application to add expenses, calculate monthly spending, and summarize spending by category.

## Technologies
- Python
- Model Context Protocol (MCP)
- FastMCP
- FastAPI
- HTTPX
- SQLite

## Tools
1. `add_expense` — Adds a new expense.
2. `monthly_total` — Calculates the total expenses for a selected month.
3. `top_categories` — Groups expenses by category and sorts by spending amount.

## Resource
- `expense://summary` — Returns the number of expenses and total spending.

## Prompt
- `budget_summary` — Generates instructions for reviewing spending and suggesting ways to save money.

## Setup
1. Activate the project's Python virtual environment.
2. Install dependencies: `pip install "mcp<2" httpx`
3. Start the existing FastAPI Expense Tracker API.
4. Configure the `EXPENSE_API_TOKEN` environment variable in MCP Inspector.
5. Configure the MCP server to run `mcp_server.py`.

## Testing
- Added an expense successfully.
- Calculated the monthly total successfully.
- Summarized spending by category successfully.
- Confirmed that an invalid month is rejected.
- Confirmed that a negative expense amount is rejected.

## Project Status
The three tools, one resource, and one prompt were tested using MCP Inspector.
