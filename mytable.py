from parser import parse
import sys
from printer import toprettytable, tomarkdowntable

if len(sys.argv) < 1:
    print("Usage: mytable.py <filename>")
    exit(1)

COMPAR = ('LU3IN032', 'COMPAR')
DATA = ('LU3IN026', 'DATA')
IA = ('LU3IN025', 'IA')
CRYPTO = ('LU3IN024', 'CRYPTO')
CALC = ('LU3IN030', 'CALC')
PRECH = ('LU3IN013-rech', 'PRECH')
WEB = ('LU3IN017', 'WEB')
COMPIL = ('LU3IN018', 'COMPIL')
GL = ('LU3IN012', 'GL')
ECO = ('LU3IN027', 'ECO')
ARCHI = ('LU3IN031', 'ARCHI')
PAPPL = ('LU3IN013-app', 'PAPPL')
SYS = ('LU3IN010', 'SYS')

# TODO : choose your units and groups
UNITS = [DATA[0], CRYPTO[0], WEB[0], GL[0], SYS[0]]

GROUPS = {
    DATA[0]: 2,
    CRYPTO[0]: 2,
    WEB[0]: 4,
    GL[0]: 2,
    SYS[0]: 6
}


tobj = parse(sys.argv[1])
table = tobj.table


result = {}

for day in table:

    nday = []
    for hour in table[day]:

        nhour = []

        for s in hour:
            if s.code not in UNITS:
                continue

            if s.group == None or s.group == GROUPS[s.code]:
                nhour.append(s)

        nday.append(nhour)

    result[day] = nday

DAYS = ["lundi", "mardi", "mercredi", "jeudi", "vendredi"]
TIME = ["8h45 - 10h30", "10h45-12h30",
        "---", "14h - 15h45", "16h - 17h45", "18h - 19h45"]

# print(str(toprettytable(result, DAYS, TIME)))
print(tomarkdowntable(result, DAYS, TIME))
