def validat_nums_only(text):
    if text.isdigit():
        return True
    else:
        return "Value must be num!"

def validat_chars_only(text):
    if text.isalpha():
        return True
    else:
        return "value must be chars!"
