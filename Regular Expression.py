import re

sentence = "Call me at 0928-987-6543 tomorrow."
phone_pattern = r"\d{4}-\d{3}-\d{4}"

found = re.search(phone_pattern, sentence)

if found:
    print("Phone number found:", found.group())
else:
    print("No phone number in the text.")
