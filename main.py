
import sys
from parser import parse
from logger import Logger
from plateform import clear
from core import filtertimetable, reducetimetable
from printer import toprettytable

log = Logger()


def choose(opt_units, number_units):

    if number_units > len(opt_units):
        log.log(
            "\nNumber of units is greater than the number of optional units", Logger.WARNING)
        return []

    units = []
    curr = 0
    while curr < number_units:

        log.log(
            f"\n\t Choose {number_units} units that you want to add to your timetable.", Logger.HEADER)

        log.log("\n", Logger.TEXT)

        delimiter = "\t+" + "-" * 38 + "+"
        log.log(delimiter, Logger.TEXT, True)

        for i, unit in enumerate(opt_units):
            log.log(f"\t|{i:15d} - {unit[1]:20s}|", Logger.TEXT, True)

        log.log(delimiter, Logger.TEXT, True)

        try:
            index_unit = int(
                input(f"\n\t * Choose the unit N° {curr} : "))

            if index_unit < 0 or index_unit >= len(opt_units):
                raise ValueError(f"Unit index out of range")

            log.log(
                f"\n\t --> SUCCES : {opt_units[index_unit][1]} is chosen", Logger.SUCCES)

            curr += 1

            units.append(opt_units[index_unit])
            opt_units.pop(index_unit)

        except ValueError as e:
            log.log(f"\n\t --> Error : {e}", Logger.FAIL)

        log.log("\n\t [Press enter to continue...]", Logger.TEXT)
        input()

        clear()

    return units


if len(sys.argv) < 3:
    print(
        f"Usage: python3 {sys.argv[0]} <filename : String> <number of optinals units : Int> <required units codes : List>")
    exit(1)

try:
    NUMBER_OF_OPT = int(sys.argv[2])
except ValueError:
    print(f"Invalid number of optional units: {sys.argv[2]}")
    exit(1)

required_units = sys.argv[3:]
tobj = parse(sys.argv[1], required_units)

if tobj is None:
    exit(1)

timetable = tobj.table
ALL_UNITS = tobj.ALL_UNITS

UNITS = choose(tobj.OPT_UNITS, NUMBER_OF_OPT)


for unit in ALL_UNITS:

    if unit in UNITS:
        continue

    if unit[0] in required_units and unit not in UNITS:
        UNITS.append(unit)


timetable = filtertimetable(timetable, UNITS)

DAYS = ["lundi", "mardi", "mercredi", "jeudi", "vendredi"]
TIME = ["8h45 - 10h30", "10h45-12h30",
        "---", "14h - 15h45", "16h - 17h45", "18h - 19h45"]

timetables = reducetimetable(timetable, UNITS)
if timetables is None:
    exit(0)

str_u = ", ".join([u[1] for u in UNITS])
log.log(
    f"The timetables for the units : {str_u} are saved in results.txt file\n", Logger.HEADER)

with open("results.txt", "w") as f:
    for table in timetables:
        f.write(str(toprettytable(table, DAYS, TIME)))
        f.write("\n\n")
