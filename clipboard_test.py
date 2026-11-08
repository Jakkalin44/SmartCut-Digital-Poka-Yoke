
import pyperclip

job_code = "Abcdf2221"

# Copy Job Code to Windows Clipboard
pyperclip.copy(job_code)

# Read the value back from Clipboard
copied_text = pyperclip.paste()

print("Original Job Code:", job_code)
print("Clipboard Content:", copied_text)

if copied_text == job_code:
    print("Clipboard Test PASSED!")
else:
    print("Clipboard Test FAILED!")

