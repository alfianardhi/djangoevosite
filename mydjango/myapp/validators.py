from django.core.exceptions import ValidationError

def validate_author_comment(value):
    author_comment = value
    if author_comment == '-':
        message = "Please input your name"
        raise ValidationError(message)