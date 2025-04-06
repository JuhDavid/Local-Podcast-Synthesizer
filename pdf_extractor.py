import os
import traceback
import PyPDF2

def extract_text_from_pdf(pdf_path):
    abs_pdf_path = os.path.abspath(pdf_path)
    print(f"Attempting to access PDF at absolute path: {abs_pdf_path}")
    if not os.path.exists(abs_pdf_path) or not os.path.isfile(abs_pdf_path):
        print(f"Error: File not found or not a file: {abs_pdf_path}")
        return ""

    try:
        with open(abs_pdf_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            print(f"Number of pages found: {len(reader.pages)}")

            if reader.is_encrypted:
                try:
                    if reader.decrypt('') != PyPDF2.PasswordType.NOT_DECRYPTED:
                        print("PDF decrypted with empty password.")
                except Exception as decrypt_e:
                    print(f"Decryption attempt failed: {decrypt_e}")

            text = ""
            for i, page in enumerate(reader.pages):
                try:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
                except Exception as page_e:
                    print(f"Error extracting text from page {i + 1}: {page_e}")

        return text.strip()
    except Exception as e:
        print(f"An error occurred reading PDF: {e}")
        traceback.print_exc()
        return ""
