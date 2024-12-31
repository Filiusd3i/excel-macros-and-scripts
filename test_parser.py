import os
import PyPDF2

def process_pdf(input_file_path):
    try:
        with open(input_file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            first_page = pdf_reader.pages[0]
            text = first_page.extract_text() or ""
            lines = text.split('\n')

        for i, line in enumerate(lines):
            if "FOR THE PERIOD" in line.upper():
                account_name_parts = []
                for j in range(i + 1, len(lines)):
                    next_line = lines[j].strip()
                    
                    if next_line.startswith('STE'):
                        break
                        
                    if next_line and not any(next_line.startswith(x) for x in 
                        ['Number', 'Tax ID', 'For Client', 'Visit', 'For 24-hour', 'PNC Bank']):
                        # Remove Tax ID if present
                        if 'Tax ID' in next_line:
                            next_line = next_line.split('Tax ID')[0].strip()
                        account_name_parts.append(next_line)
                
                if account_name_parts:
                    return text, ' '.join(account_name_parts)
                
        return text, None

    except Exception as e:
        print(f"Error: {str(e)}")
        return None, None

def test_statements():
    """
    Test function that scans the 'input_statements' folder
    and prints out the extracted account name for each PDF.
    """
    input_folder = r"C:\Users\Owner\Desktop\BankStatementAutomation\input_statements"
    
    print("\n--- TESTING ACCOUNT NAME EXTRACTION ---")
    if not os.path.exists(input_folder):
        print(f"Input folder not found: {input_folder}")
        return

    files_in_folder = os.listdir(input_folder)
    if not files_in_folder:
        print("No files in the input folder.")
        return

    for filename in files_in_folder:
        if filename.lower().endswith('.pdf'):
            file_path = os.path.join(input_folder, filename)
            _, account_name = process_pdf(file_path)
            print(f"\nRESULT for '{filename}':")
            print(f"  Account Name: {account_name}")
        else:
            print(f"Skipping non-PDF file: {filename}")

if __name__ == "__main__":
    test_statements()