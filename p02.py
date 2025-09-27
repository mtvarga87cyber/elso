# 2. alkalom
from curses.ascii import isdigit

szam = (input("Kérek egy számot:"))
if isdigit(szam):
    szam = int(szam)

if szam > 0:
    print("Pozitív")
elif szam < 0:
    print("Negatív")
else:
    print("Nulla")
