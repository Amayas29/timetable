
from prettytable import PrettyTable


def toprettytable(table, days, time):
    pt = PrettyTable()

    pt.field_names = ["Jour", *time]

    spaces = [""] * len(time)

    for day in days:
        daylist = table[day]

        resday = []
        for hour in daylist:
            resday.append("\n".join(map(lambda x: str(x), hour)))

        pt.add_row([day, *resday])
        for _ in range(2):
            pt.add_row(["", *spaces])

    return pt


def tomarkdowntable(table, days, time):

    max_len = 16
    header = ["Jour", *time]
    result = "|"
    line = "|"

    for e in header:
        result += " " + str(e).center(max_len, " ") + " |"
        line += ":" + "-" * max_len + ":|"

    result += "\n" + line + "\n"

    for day in days:

        result += "| " + str(day).center(max_len, " ") + " |"

        for hour in table[day]:

            result += " " + \
                str("\n".join(map(lambda x: str(x), hour))).center(
                    max_len, " ") + " |"

        result += "\n"

    return result
