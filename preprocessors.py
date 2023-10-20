import re

def correct_zarate_term(statement):
    """
    Converts all variations of terminologies to E. Zarate Hospital (case-insensitive)
    """
    corrections = {
        "e. zarate": "E. Zarate Hospital",
        "zarate": "E. Zarate Hospital",
        "zarate hospital": "E. Zarate Hospital",
        "hospital": "E. Zarate Hospital"
    }

    # Use regular expression to find whole words and replace them (case-insensitive)
    pattern = r'\b(?:' + '|'.join(map(re.escape, corrections.keys())) + r')\b'
    corrected_sentence = re.sub(pattern, lambda x: corrections[x.group().lower()], statement.text, flags=re.IGNORECASE)

    # Ensure that "E. Zarate Hospital" is not repeated
    corrected_sentence = re.sub(r'(e\. zarate hospital\s+)+', 'E. Zarate Hospital ', corrected_sentence)

    statement.text = corrected_sentence
    return statement
