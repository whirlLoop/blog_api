"""Contains validation for various data types."""
import string
import re


def is_empty(value):
    """Checks whether value provided is empty or whitespace, tabs or newlines

    Arguments:
        value {string} -- value to check
    Returns:
        boolean -- true if empty, else false
    """
    stripped_value = value.strip()
    if stripped_value:
        return False
    return True


def is_alphabet_only(value):
    """Check string contains alphabets only

    Arguments:
        value {string} -- value to validate
    """
    is_alpha = value.translate({ord(c): None for c in string.whitespace})
    if not is_alpha.isalpha():
        return False
    return True


def is_valid_post(value):
    """Validates a post

    Arguments:
        value {string} -- post to validate

    Returns:
        boolean -- true if valid
    """
    pattern = '^[a-zA-Z0-9,.!? ()]*$'
    if re.match(pattern, value):
        return True
    return False

# if __name__ == '__main__':
# #     empty_string = "not        "
# #     # print(is_empty(empty_string))
# #     is_alpha_bet = "qwerty suei serer"
# #     print(is_alphabet(is_alpha_bet))
#     post = "My name, as you well know, (sic) is Peter."
#     print(is_valid_post(post))
