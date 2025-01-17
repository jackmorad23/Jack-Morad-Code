import os
import re
import pandas as pd
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from bs4 import BeautifulSoup
import logging

from google_auth_oauthlib.flow import InstalledAppFlow

def connect_gmail():
    # Define the scope of the Gmail API, limiting access to read-only Gmail data
    SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

    # Check if token.json exists, which stores the user's access and refresh tokens
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    else:
        # If there are no (valid) credentials available, let the user log in.
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    # Return the Gmail API service object
    service = build('gmail', 'v1', credentials=creds)
    return service


def fetch_emails(service):
    """Fetch emails containing donor data."""
    try:
        # Search for emails with the subject "Weekly Let's Go Red Gift Email"
        results = service.users().messages().list(userId='me', q='subject:"Weekly Let\'s Go Red Gift Email"').execute()
        
        # Retrieve all matching email messages
        messages = results.get('messages', [])
        email_data = []

        # Iterate through each email message and extract the HTML parts
        for msg in messages:
            message = service.users().messages().get(userId='me', id=msg['id']).execute()
            
            for part in message['payload']['parts']:
                # If the part is an HTML message, add its data to the email_data list
                if part['mimeType'] == 'text/html':
                    email_data.append(part['body']['data'])

        # Return the collected email data
        return email_data
    except Exception as e:
        logging.error(f"Error fetching emails: {e}")
        return []

def parse_table_from_email(email_body):
    """Extract the donor table from the email body."""
    try:
        # Use BeautifulSoup to parse the HTML email body
        parser = BeautifulSoup(email_body, 'html.parser')
        
        # Find all the tables in the email
        tables = parser.find_all('table')

        # If tables exist, process the first one as the donor data table
        if tables:
            donor_table = tables[0]
            rows = donor_table.find_all('tr')

            # Extract column headers from the first row (assumed to be header row)
            headers = [header.text.strip() for header in rows[0].find_all('th')]
            data = []

            # Iterate over each row (skipping the header row) and extract donor information
            for row in rows[1:]:
                cols = [col.text.strip() for col in row.find_all('td')]

                # Extract graduation year from the donor name (e.g., "Mr. Chris Thomas '73")
                donor_name = cols[0]  # Assuming "Donor Name" is in the first column
                grad_year = None
                match = re.search(r"'(\d{2})", donor_name)
                if match:
                    # Determine full graduation year based on the last two digits
                    grad_year = "19" + match.group(1) if int(match.group(1)) > 50 else "20" + match.group(1)

                # Append data with extracted graduation year
                data.append(cols + [grad_year])

            # Add a new "Graduation Year" column to the header
            headers.append('Graduation Year')
            
            # Return the parsed data as a Pandas DataFrame
            return pd.DataFrame(data, columns=headers)

        # Return an empty DataFrame if no donor table is found
        logging.warning("No donor table found in email body.")
        return pd.DataFrame()

    except Exception as e:
        logging.error(f"Error parsing email body: {e}")
        return pd.DataFrame()

def update_master_sheet(master_path, new_data):
    """Update the master Excel sheet with new donor data."""
    try:
        # Load the existing master Excel sheet
        master_df = pd.read_excel(master_path)

        # Iterate through the new donor data and update the master sheet
        for _, row in new_data.iterrows():
            donor_email = row['Email']
            
            # Check if there is an existing row with the same donor email in the master sheet
            matching_row = master_df[master_df['Email Address'] == donor_email]

            # Extract the "In Memory Of" column from the email table
            in_memory_of = row.get('In Memory Of', '')  # Default to an empty string if the column doesn't exist

            if not matching_row.empty:
                # If a matching row is found, update the existing donor's data
                idx = matching_row.index[0]
                master_df.at[idx, 'Home Address1'] = row['Address']
                master_df.at[idx, 'Contact Number'] = row['Phone']
                
                # Update the FY25 donation amount by adding the new gift amount
                master_df.at[idx, 'FY25'] += float(row['Gift Amount'].replace('$', '').replace(',', ''))

                # Update "Notes" column with "In Memory Of" if it exists
                if in_memory_of:
                    current_notes = master_df.at[idx, 'Notes'] or ''  # Handle if "Notes" is empty
                    master_df.at[idx, 'Notes'] = f"{current_notes} | In Memory Of: {in_memory_of}".strip('| ')
            else:
                # If no matching row is found, add a new donor entry
                new_entry = {
                    'First Name': row['Donor Name'].split()[1],
                    'Last Name': row['Donor Name'].split()[-1],
                    'Graduation Year': row['Graduation Year'],
                    'Email Address': row['Email'],
                    'Home Address1': row['Address'],
                    'Contact Number': row['Phone'],
                    'FY25': float(row['Gift Amount'].replace('$', '').replace(',', '')),
                    'Notes': f"In Memory Of: {in_memory_of}" if in_memory_of else '',
                }
                
                # Append the new donor entry to the master sheet
                master_df = master_df.append(new_entry, ignore_index=True)

        # Save the updated master sheet to the same file
        master_df.to_excel(master_path, index=False)
        logging.info(f"Master sheet updated successfully: {master_path}")
    except Exception as e:
        logging.error(f"Error updating master sheet: {e}")

# Main script
def main():
    try:
        # Connect to Gmail using the API
        gmail_service = connect_gmail()

        # Fetch the emails containing donor data
        email_data = fetch_emails(gmail_service)

        # Path to the master Excel sheet that tracks donor data
        master_sheet_path = 'master_donations.xlsx'

        # Process each email and update the master sheet with new donor data
        for email in email_data:
            email_body = re.sub('-+', '', email)  # Remove encoding artifacts from the email body
            new_donor_data = parse_table_from_email(email_body)

            # If new donor data is found, update the master sheet
            if not new_donor_data.empty:
                update_master_sheet(master_sheet_path, new_donor_data)
            else:
                logging.warning("No new donor data found in email.")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

# Run the main script if this file is executed
if __name__ == "__main__":
    main()
