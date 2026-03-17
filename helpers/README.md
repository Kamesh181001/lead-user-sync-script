# Lead User Sync Script

This project contains a Python script that synchronizes lead records with user accounts using GraphQL APIs.

The script retrieves lead mobile numbers, checks if a corresponding user exists with the same mobile number, and updates the lead record with the correct user ID.

## Features

- Fetch all lead mobile numbers from the database
- Query user records using GraphQL
- Map users to leads based on mobile numbers
- Update lead records with user IDs
- Batch processing to handle large datasets efficiently

## Tech Stack

- Python
- GraphQL API
- Requests library

## How It Works

1. Fetch all lead mobile numbers from the leads table.
2. Query users with matching mobile numbers.
3. Create a mapping between mobile numbers and user IDs.
4. Update the lead records with the corresponding user IDs.
5. Process records in batches to avoid overloading the API.

## Project Structure

- `main.py` – Entry point of the script
- `repo.py` – Contains GraphQL queries and mutations
- `hasura_client.py` – Handles GraphQL API requests


## Notes

This project demonstrates backend data processing using Python and GraphQL APIs.  
Sensitive credentials are managed through environment variables.


