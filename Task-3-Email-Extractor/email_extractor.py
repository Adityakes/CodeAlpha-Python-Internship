# ==========================================================
# Project Name : Email Address Extractor
# Description  : This program reads a text file, extracts all
#                email addresses using Regular Expressions,
#                removes duplicate emails, and saves the
#                extracted emails into another text file.
#
# Concepts Used:
# - File Handling
# - Functions
# - Regular Expressions (re)
# - Exception Handling
# - List & Set
# ==========================================================

# Import Regular Expression module
import re


# ==========================================================
# File Names
# ==========================================================
# Input file contains the text from which emails are extracted.
# Output file will store the extracted email addresses.

INPUT_FILE = "input.txt"
OUTPUT_FILE = "emails.txt"


# ==========================================================
# Function: read_file()
# Purpose : Reads the content of the input file.
# Returns : Complete text if file exists, otherwise None.
# ==========================================================

def read_file(file_name):
    try:
        with open(file_name, "r") as file:
            return file.read()

    except FileNotFoundError:
        print(f"\nError: '{file_name}' not found.")
        print("Please make sure the input file exists.\n")
        return None


# ==========================================================
# Function: extract_emails()
# Purpose : Extracts all valid email addresses from text.
# Returns : A sorted list of unique email addresses.
# ==========================================================

def extract_emails(text):

    # Regular Expression Pattern for Email Validation
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    # Find all email addresses
    emails = re.findall(email_pattern, text)

    # Remove duplicate email addresses
    unique_emails = set(emails)

    # Sort emails alphabetically
    sorted_emails = sorted(unique_emails)

    return sorted_emails


# ==========================================================
# Function: save_emails()
# Purpose : Saves all extracted emails into output file.
# ==========================================================

def save_emails(file_name, emails):

    with open(file_name, "w") as file:

        file.write("=====================================\n")
        file.write("      Extracted Email Addresses\n")
        file.write("=====================================\n\n")

        # Check whether emails are found
        if emails:

            # Write each email with serial number
            for index, email in enumerate(emails, start=1):
                file.write(f"{index}. {email}\n")

        else:
            file.write("No Email Addresses Found.")


# ==========================================================
# Function: display_result()
# Purpose : Displays extracted emails on the terminal.
# ==========================================================

def display_result(emails):

    print("\n=====================================")
    print("        Extraction Result")
    print("=====================================")

    print(f"\nTotal Email Addresses Found : {len(emails)}")

    if emails:

        print("\nExtracted Email Addresses:\n")

        for email in emails:
            print(f"• {email}")

    else:
        print("\nNo Email Addresses Found.")

    print(f"\nOutput saved successfully in '{OUTPUT_FILE}'")


# ==========================================================
# Main Function
# Program execution starts from here.
# ==========================================================

def main():

    print("=" * 45)
    print("        EMAIL ADDRESS EXTRACTOR")
    print("=" * 45)

    # Step 1 : Read data from input file
    content = read_file(INPUT_FILE)

    # Stop execution if file is missing
    if content is None:
        return

    # Step 2 : Extract email addresses
    emails = extract_emails(content)

    # Step 3 : Save emails into output file
    save_emails(OUTPUT_FILE, emails)

    # Step 4 : Display the final result
    display_result(emails)


# ==========================================================
# Driver Code
# This ensures that main() runs only when this file
# is executed directly.
# ==========================================================

if __name__ == "__main__":
    main()