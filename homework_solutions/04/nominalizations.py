"""One possible solution for finding nominalizations in a text."""

import re

from assignment_04_text import nom_text


nominalizations = []

patterns = [('Gerund',    r'\b[-\w]*\wing\b'),  # The hyphen for "copy-editing"
            ('Agent',     r'\b\w{2,}[eo]r\b'),  # 2+ \w to avoid "for"
            ('Recipient', r'\b\w{2,}ee\b'),
            ('Other',     r'\b\w{2,}(?:[ts]ion|ment|[ae]nce)\b'),
            ('Zero',      r'$^'),  # Purposefully cannot match anything
            ]

total = 0
for name, regex in patterns:
    matches = re.findall(regex, nom_text, flags=re.I)
    count = len(matches)
    total += count
    print(f'{name}:', count)
    nominalizations.extend(matches)

print('Total nominalizations:', total)
print(nominalizations)
