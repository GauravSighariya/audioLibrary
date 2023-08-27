from django import template

register = template.Library()

@register.filter
def convert_to_minutes_seconds(seconds):
    """
    Custom template filter to convert seconds to "min, sec" format.

    This filter takes a duration in seconds and converts it to a human-readable format
    representing minutes and seconds, such as "3 min, 20 sec".

    """
    minutes, seconds = divmod(seconds, 60)
    return f"{int(minutes)} min, {int(seconds)} sec"
