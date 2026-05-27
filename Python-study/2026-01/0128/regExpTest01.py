import re

pattern = r"^01[016789]-\d{3,4}-\d{4}$"

phones = [
    "010-1234-5678",
    "011-234-5678",
    "019-9999-9999",
    "01054562123"
    "02-215-8444"
]

for p in phones:
    if re.match(pattern, p):
        print(p, "→ 올바른 번호")
    else:
        