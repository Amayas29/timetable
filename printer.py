
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
