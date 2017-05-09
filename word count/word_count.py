from string import punctuation, maketrans
import re

def word_count(input):
    myTable = maketrans(punctuation, " " * len(punctuation))
    formatted = decode_if_needed(input.translate(myTable).lower())
    pattern = re.compile(
        u"(\ud83d[\ude00-\ude4f])|"  # emoticons
        u"(\ud83c[\udf00-\uffff])|"  # symbols & pictographs (1 of 2)
        u"(\ud83d[\u0000-\uddff])"  # symbols & pictographs (2 of 2)
        "+", flags=re.UNICODE)
    sanitized = pattern.sub(r' ', formatted)
    result = {}
    for thing in sanitized.split():
        result[thing] = result.get(thing, 0) + 1
    return result

def decode_if_needed(obj, encoding='utf-8'):
    if isinstance(obj, basestring):
        if not isinstance(obj, unicode):
            obj = unicode(obj, encoding)
    return obj
