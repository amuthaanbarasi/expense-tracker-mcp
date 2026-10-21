
import os
import httpx
from datetime import datetime
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Expense Tracker")

API_URL = "http://127.0.0.1:8000"


def get_headers():
    token = os.getenv("EXPENSE_API_TOKEN")

    if not token:
        raise ValueError("Please configure EXPENSE_API_TOKEN.")

    return {"Authorization": f"Bearer {token}"}


@mcp.tool()
def add_expense(
    title: str,
    amount: float,
    category: str,
    description: str = ""
) -> str:
    """Add an expense to the logged-in user's expense tracker."""

    if amount <= 0:
        return "Error: Amount must be greater than zero."

    data = {
        "title": title,
        "amount": amount,
        "category": category,
        "description": description,
        "expense_date": datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    }

    try:
        response = httpx.post(
            f"{API_URL}/expenses/",
            json=data,
            headers=get_headers(),
            timeout=10
        )

        if response.status_code == 401:
            return "Error: Login token is invalid or expired."

        response.raise_for_status()
        expense = response.json()

        return (
            f"Expense saved successfully. "
            f"ID: {expense['id']}, "
            f"Title: {expense['title']}, "
            f"Amount: Rs. {expense['amount']}"
        )

    except httpx.HTTPError:
        return "Error: Could not save the expense. Check the API server."


@mcp.tool()
def monthly_total(year: int, month: int) -> str:
    """Calculate the total expenses for a given month."""

    if month < 1 or month > 12:
        return "Error: Month must be between 1 and 12."

    try:
        response = httpx.get(
            f"{API_URL}/expenses/",
            params={"skip": 0, "limit": 1000},
            headers=get_headers(),
            timeout=10
        )

        if response.status_code == 401:
            return "Error: Login token is invalid or expired."

        response.raise_for_status()
        expenses = response.json()

        total = 0
        count = 0

        for expense in expenses:
            expense_date = datetime.fromisoformat(
                expense["expense_date"]
            )

            if expense_date.year == year and expense_date.month == month:
                total += expense["amount"]
                count += 1

        return (
            f"Month: {year}-{month:02d}, "
            f"Number of expenses: {count}, "
            f"Total: Rs. {total:.2f}"
        )

    except httpx.HTTPError:
        return "Error: Could not retrieve expenses. Check the API server."
    
@mcp.tool()
def top_categories() -> str:
    """Show the total spending for each expense category."""

    try:
        response = httpx.get(
            f"{API_URL}/expenses/",
            params={"skip": 0, "limit": 1000},
            headers=get_headers(),
            timeout=10
        )

        if response.status_code == 401:
            return "Error: Login token is invalid or expired."

        response.raise_for_status()
        expenses = response.json()

        totals = {}

        for expense in expenses:
            category = expense["category"]
            amount = expense["amount"]

            if category not in totals:
                totals[category] = 0

            totals[category] += amount

        if not totals:
            return "No expenses found."

        result = []

        for category, total in sorted(
            totals.items(),
            key=lambda item: item[1],
            reverse=True
        ):
            result.append(f"{category}: Rs. {total:.2f}")

        return "\n".join(result)

    except httpx.HTTPError:
        return "Error: Could not retrieve expenses. Check the API server."
    
@mcp.resource("expense://summary")
def expense_summary() -> str:
    """Provide a summary of the user's expenses."""

    try:
        response = httpx.get(
            f"{API_URL}/expenses/",
            params={"skip": 0, "limit": 1000},
            headers=get_headers(),
            timeout=10
        )

        if response.status_code == 401:
            return "Error: Login token is invalid or expired."

        response.raise_for_status()
        expenses = response.json()

        total = sum(expense["amount"] for expense in expenses)

        return (
            f"Number of expenses: {len(expenses)}\n"
            f"Total spending: Rs. {total:.2f}"
        )

    except httpx.HTTPError:
        return "Error: Could not retrieve expenses. Check the API server."

@mcp.prompt()
def budget_summary(month: str) -> str:
    """Create a prompt for summarizing expenses and planning a budget."""

    return (
        f"Review the user's expenses for {month}. "
        "Summarize total spending by category, identify the highest "
        "spending category, and suggest three practical ways to save money. "
        "Ask for a budget limit if one is not provided. "
        "Do not invent expense amounts; use the available expense data."
    )




if __name__ == "__main__":
    mcp.run()
