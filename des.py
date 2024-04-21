import easyocr
import re
from datetime import datetime

# Load the image
image_path = r"C:\Users\durga\Expiry date\test expiry\7.jpeg"  # Update with your image path

# Create an EasyOCR reader
reader = easyocr.Reader(lang_list=['en'])  # Specify the language(s) you want to detect

# Perform text detection and recognition
result = reader.readtext(image_path, detail=0)  # Use detail=0 to get only the recognized text

# Define your own date patterns here
date_patterns = [
    r"(\d{1,2}/\d{1,2}/\d{2,4})",
    r"(\d{1,2}\s+(?:JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)\s+\d{4})",
    r"(\d{2,4}-\d{1,2}-\d{1,2})",
    r"(\d{1,2}-\d{1,2}-\d{2,4})",
    r"(\d{1,2}-\s+(?:JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)\s+-\d{4})",
    r"(\d{1,2}.\d{1,2}.\d{2,4})",
    r"(\d{1,2}-[A-Za-z]{3,4}-\d{2,4})",
]

# Initialize a list to store detected dates
detected_dates = []
detected_numbers = []
# Iterate through the recognized text
for text in result:
    for pattern in date_patterns:
        # Search for date patterns in the recognized text
        dates_found = re.findall(pattern, text)
        if dates_found:
            for date_str in dates_found:
                try:
                    detected_date = None  # Initialize the variable before the try block
                    if '/' in date_str:
                        date_parts = date_str.split('/')
                        if len(date_parts) == 3:
                            if date_parts[1].isdigit():
                                if date_parts[0].isdigit() and len(date_parts[0]) in {1, 2}:
                                    detected_date = datetime.strptime(date_str, '%d/%m/%y'if len(date_parts[2]) == 2 else '%d/%m/%Y')
                                elif date_parts[0].isdigit() and len(date_parts[0]) in {2, 4}:
                                    detected_date = datetime.strptime(date_str, '%Y/%m/%d')
                            elif date_parts[1].upper() in ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]:
                                if date_parts[0].isdigit() and len(date_parts[0]) in {1, 2}:
                                    detected_date = datetime.strptime(date_str, '%d/%b/%y'if len(date_parts[2]) == 2 else '%d/%b/%Y')
                                elif date_parts[0].isdigit() and len(date_parts[0]) in {2, 4}:
                                    detected_date = datetime.strptime(date_str, '%Y/%b/%d')
                             
                    elif '-' in date_str:
                        date_parts = date_str.split('-')
                        if len(date_parts) == 3:
                            if date_parts[1].isdigit():
                                if date_parts[0].isdigit() and len(date_parts[0]) in {1, 2}:
                                    detected_date = datetime.strptime(date_str, '%d-%m-%y'if len(date_parts[2]) == 2 else '%d-%m-%Y')
                                elif date_parts[0].isdigit() and len(date_parts[0]) in {2, 4}:
                                    detected_date = datetime.strptime(date_str, '%Y-%m-%d')
                            elif date_parts[1].upper() in ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]:
                                if date_parts[0].isdigit() and len(date_parts[0]) in {1, 2}:
                                    detected_date = datetime.strptime(date_str, '%d-%b-%y'if len(date_parts[2]) == 2 else '%d-%b-%Y')
                                elif date_parts[0].isdigit() and len(date_parts[0]) in {2, 4}:
                                    detected_date = datetime.strptime(date_str, '%Y-%b-%d')
                               
                           
                    elif '.' in date_str:
                        date_parts = date_str.split('.')
                        if len(date_parts) == 3:
                            if date_parts[1].isdigit():
                                if date_parts[0].isdigit() and len(date_parts[0]) in {1, 2}:
                                    detected_date = datetime.strptime(date_str, '%d.%m.%y'if len(date_parts[2]) == 2 else '%d.%m.%Y')
                                elif date_parts[0].isdigit() and len(date_parts[0]) in {2, 4}:
                                    detected_date = datetime.strptime(date_str, '%Y.%m.%d')
                            elif date_parts[1].upper() in ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]:
                                if date_parts[0].isdigit() and len(date_parts[0]) in {1, 2}:
                                    detected_date = datetime.strptime(date_str, '%d.%b.%y'if len(date_parts[2]) == 2 else '%d.%b.%Y')
                                elif date_parts[0].isdigit() and len(date_parts[0]) in {2, 4}:
                                    detected_date = datetime.strptime(date_str, '%Y.%b.%d')
                           
                    elif ' ' in date_str:
                        date_parts = date_str.split(' ')
                        if len(date_parts) == 3:
                            if date_parts[1].isdigit():
                                if date_parts[0].isdigit() and len(date_parts[0]) in {1, 2}:
                                    detected_date = datetime.strptime(date_str, '%d %m %y'if len(date_parts[2]) == 2 else '%d %m %Y')
                                elif date_parts[0].isdigit() and len(date_parts[0]) in {2, 4}:
                                    detected_date = datetime.strptime(date_str, '%Y %m %d')
                            elif date_parts[1].upper() in ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]:
                                detected_date = datetime.strptime(date_str, '%d %b %y'if len(date_parts[2]) == 2 else '%d %b %Y')
                                if date_parts[0].isdigit() and len(date_parts[0]) in {1, 2}:
                                    detected_date1 = datetime.strptime(date_str, '%d %b %Y')
                                elif date_parts[0].isdigit() and len(date_parts[0]) in {2, 4}:
                                    detected_date = datetime.strptime(date_str, '%Y %b %d')
                               
                   
                    if detected_date is not None:
                        detected_dates.append(detected_date)  # Convert and append to the list
                except ValueError:
                    pass
    six_digit_numbers = re.findall(r"\d{6}", text)
    if six_digit_numbers:
        detected_numbers.extend(six_digit_numbers)
# If at least one date is detected
if detected_dates or detected_numbers:
    for num_str in detected_numbers:
        try:
            if len(num_str) == 6:
                day = int(num_str[:2])
                month = int(num_str[2:4])
                year = int(num_str[4:])
                if year < 100:
                    year += 2000
                else:
                    year += 1900
                detected_date = datetime(year, month, day)
                detected_dates.append(detected_date)
            elif len(num_str) == 8:
                day = int(num_str[:2])
                month = int(num_str[2:4])
                year = int(num_str[4:])
                detected_date = datetime(year, month, day)
                detected_dates.append(detected_date)  
        except ValueError:
            pass
    # If multiple dates are detected, take the maximum date
    if len(detected_dates) > 1:
        expiry_date = max(detected_dates)
    else:
        expiry_date = detected_dates[0]

    # Calculate the difference between the current date and the detected date
    current_date = datetime.now()
    date_difference = expiry_date - current_date
    print("Expiry date:", expiry_date.strftime('%d/%m/%Y'))
    if date_difference.days < 0:
        print("Expired")
    else:
        print(date_difference.days,"days left")
else:
    print("No dates found")