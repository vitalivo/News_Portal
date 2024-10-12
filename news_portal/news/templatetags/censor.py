from django import template
import re

register = template.Library()

# Список нецензурных слов
PROFANITIES = ['редиска', 'плохое_слово']  # Добавьте свои ругательства сюда


@register.filter(name='censor')
def censor(value):
    if not isinstance(value, str):
        raise ValueError("Фильтр цензуры применяется только к строковым переменным.")

    for word in PROFANITIES:
        pattern = re.compile(re.escape(word), re.IGNORECASE)
        value = pattern.sub(word[0] + '*' * (len(word) - 1), value)

    return value
