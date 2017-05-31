import re
acronymTable = []

def abbreviate(acronym):
    acronymTable = re.split(r'\s|-', acronym)
    return ''.join([x[0] for x in acronymTable]).upper()
