import re
tx = "To be, or not to be, that is the question"
samogloski = re.findall('[aeyiou]',tx)
l = len(samogloski)
print(f"Liczba samogłosek w tekście: {l}")