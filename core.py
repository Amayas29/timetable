from copy import copy
from logger import Logger
import itertools


def dict_product(dicts):
    return (dict(zip(dicts, x)) for x in itertools.product(*dicts.values()))


class Timetable:

    def __init__(self):
        self.table = {}
        self.ALL_UNITS = []
        self.OPT_UNITS = []

    def __str__(self):
        s = ""
        for day in self.table:
            s += day + " : \n"
            for hour in self.table[day]:
                s += "\t" + "-" * 10 + "\n"
                s += "\t" + "\n\t".join([str(e)
                                        for e in hour]) + ("\n\t" if hour else "")

                s += "-" * 10 + "\n\n"

            s += "\n"
        return s


class Entry:

    def __init__(self, etype, value, group):
        self.etype = etype
        self.name = value[1]
        self.code = value[0]
        self.group = group

    def __str__(self):
        g = f" - {str(self.group)}" if self.group is not None else ""
        return f"{self.etype} : {self.name}{g}"

    def __repr__(self):
        return self.__str__()

    def tojson(self):
        return self.__dict__


def contains(entry, units, groups=None):

    contained = len(
        list(filter(lambda x: x[0] == entry.code, units))) != 0

    if not contained:
        return False

    if groups is None:
        return True

    return (entry.group is None or entry.group in groups[entry.code])


def filtertimetable(table, units, groups=None):

    table = table.copy()

    for day in table:

        filtered_day = []
        for hour in table[day]:
            filtered_day.append(
                list(filter(lambda x: contains(x, units, groups), hour)))

        table[day] = filtered_day

    return table


def remove_by_uniqueness(table, unique, groups, unique_list):

    for day in table:
        for hour in table[day]:

            if len(list(filter(lambda x: x.code == unique, hour))) == 0:
                continue

            for entry in hour:
                if entry.code == unique:
                    continue

                try:

                    groups[entry.code].remove(entry.group)

                    if len(groups[entry.code]) == 0:
                        unique_list.add(entry.code)

                except KeyError:
                    pass


def clean_uniqueness(table, groups, units):
    table = filtertimetable(table, units, groups)
    unique_list = set(filter(lambda x: len(groups[x]) == 1, groups))

    while unique_list:
        unique = unique_list.pop()
        remove_by_uniqueness(table, unique, groups, unique_list)
        table = filtertimetable(table, units, groups)

    return table


def reducetimetable(table, units):

    log = Logger()
    groups = {u[0]: set() for u in units}

    for day in table:
        for hour in table[day]:
            for entry in hour:
                if entry.group is not None:
                    groups[entry.code].add(entry.group)

    # Delete those that overlap with the courses
    for day in table:
        for hour in table[day]:

            if(len(
                    list(filter(lambda x: x.etype == "Cours", hour))) == 0):
                continue

            for entry in hour:
                if entry.group is not None and entry.etype != "Cours":

                    try:
                        groups[entry.code].remove(entry.group)
                    except KeyError:
                        pass

    table = clean_uniqueness(table, groups, units)

    if len(list(filter(lambda x: groups[x] == set(), groups))) != 0:
        log.log("Error : The choice of units is an impossible combination", Logger.FAIL)
        return None

    tables = []
    groups = list(dict_product(groups))
    for gr in groups:

        for k, v in gr.items():
            gr[k] = set([int(v)])

        t = copy(table)
        t = clean_uniqueness(t, gr, units)

        if len(list(filter(lambda x: gr[x] == set(), gr))) != 0:
            continue

        tables.append(t)

    if len(tables) == 0:
        log.log("Error : The choice of units is an impossible combination", Logger.FAIL)
        return None

    return tables
