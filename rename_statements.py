import os
import PyPDF2
import re

def process_pdf(input_file_path):
    """
    1) Open the first page of the PDF.
    2) Look for "FOR THE PERIOD" (case-insensitive).
    3) From the next line onward, stop if line starts with "STE".
    4) Skip lines that start with certain keywords.
    5) If a line has "Tax ID", remove that substring.
    6) Return the joined lines as the account name (or None if not found).
    """
    try:
        with open(input_file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            first_page = pdf_reader.pages[0]
            text = first_page.extract_text() or ""
            lines = text.split('\n')

        for i, line in enumerate(lines):
            # case-insensitive check for "FOR THE PERIOD"
            if "FOR THE PERIOD" in line.upper():
                account_name_parts = []
                for j in range(i + 1, len(lines)):
                    next_line = lines[j].strip()

                    # stop if line starts with "STE"
                    if next_line.upper().startswith("STE"):
                        break

                    # skip lines with these starters
                    skip_starters = [
                        'Number', 'Tax ID', 'For Client',
                        'Visit', 'For 24-hour', 'PNC Bank'
                    ]
                    # if line starts with any of the skip_starters, ignore it
                    if next_line and not any(next_line.startswith(x) for x in skip_starters):
                        # remove everything after 'Tax ID' if present
                        if 'Tax ID' in next_line:
                            next_line = next_line.split('Tax ID')[0].strip()
                        account_name_parts.append(next_line)

                if account_name_parts:
                    return text, ' '.join(account_name_parts)

        return text, None

    except Exception as e:
        print(f"Error processing PDF '{input_file_path}': {str(e)}")
        return None, None


def clean_string(input_string):
    """
    Remove non-alphanumeric punctuation, but KEEP spaces.
    (No longer converting spaces to underscores).
    """
    input_string = input_string or ""
    # remove punctuation except spaces
    cleaned = re.sub(r"[^\w\s]", "", input_string)
    cleaned = cleaned.strip()
    # Note: We do NOT replace spaces with underscores here.
    return cleaned


def rename_file(original_path, destination_folder, account_name):
    """
    Prepend the account_name (or "Unlabeled") to 
    the original file's entire name, including extension.
    """
    if not os.path.exists(original_path):
        print(f"Error: file not found -> {original_path}")
        return

    original_file_name = os.path.basename(original_path)
    if account_name:
        # Keep spaces as is
        account_name = clean_string(account_name)
        new_file_name = f"{account_name} {original_file_name}"
    else:
        new_file_name = f"Unlabeled {original_file_name}"

    new_full_path = os.path.join(destination_folder, new_file_name)
    print(f"Renaming:\n  From -> {original_path}\n  To   -> {new_full_path}")
    try:
        os.rename(original_path, new_full_path)
        print(f"Renamed to: {new_file_name}")
    except Exception as e:
        print(f"Error renaming file: {str(e)}")


def main():
    input_folder = r"C:\Users\Owner\Desktop\BankStatementAutomation\input_statements"
    processed_folder = r"C:\Users\Owner\Desktop\BankStatementAutomation\processed_statements"

    os.makedirs(input_folder, exist_ok=True)
    os.makedirs(processed_folder, exist_ok=True)

    print("DEBUG: Starting PDF rename script...")
    print(f"DEBUG: Checking input folder -> {input_folder}")
    
    all_files = os.listdir(input_folder)
    if not all_files:
        print("No files found in the input folder.")
        return
    
    print(f"DEBUG: Found {len(all_files)} file(s) in {input_folder}:")
    for f in all_files:
        print(f"  - {f}")

    print("\nDEBUG: Filtering for PDFs:")
    pdf_files = [f for f in all_files if f.lower().endswith('.pdf')]
    for pdf in pdf_files:
        print(f"  - PDF: {pdf}")
    non_pdfs = [f for f in all_files if not f.lower().endswith('.pdf')]
    for np in non_pdfs:
        print(f"  - Not a PDF, skipping: {np}")

    if not pdf_files:
        print("No PDF files found. Exiting.")
        return

    for filename in pdf_files:
        file_path = os.path.join(input_folder, filename)
        _, account_name = process_pdf(file_path)
        print(f"\nDEBUG: For file '{filename}', extracted account name -> {account_name}")
        rename_file(file_path, processed_folder, account_name)


if __name__ == "__main__":
    main()