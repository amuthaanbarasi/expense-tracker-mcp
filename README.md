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

## Setup Instructions

1. Open a terminal in the project folder.
2. Activate the Python virtual environment.
3. Install the required dependencies:

   ```bash
   pip install "mcp<2" httpx
   ```

4. Start the existing FastAPI Expense Tracker API.
5. Set the `EXPENSE_API_TOKEN` environment variable in MCP Inspector using a valid API token.
6. Configure MCP Inspector to run `mcp_server.py` with the project's virtual environment Python interpreter.
7. Connect to the MCP server and test the tools, resource, and prompt.

**Note:** The FastAPI Expense Tracker API must be running for the MCP tools to work.

## Testing

The following tests were completed using MCP Inspector:

- Added an expense successfully.
- Calculated monthly spending successfully.
- Summarized spending by category successfully.
- Rejected an invalid month.
- Rejected a negative expense amount.
- Tested the `expense://summary` resource.
- Tested the `budget_summary` prompt.

## Project Status

Three MCP tools, one resource, and one prompt have been implemented and tested using MCP Inspector.


## Project Status
The three tools, one resource, and one prompt were tested using MCP Inspector.
