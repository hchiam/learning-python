import re


def get_pattern_match(regex_string, text):
    pattern = re.compile(regex_string)
    return pattern.findall(text)[0]
