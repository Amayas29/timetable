from logger import Logger
import json
from core import Timetable, Entry


def cours(e, group=None):
    return Entry("Cours", e, group)


def td(e, group=None):
    return Entry("Td", e, group)


def tme(e, group=None):
    return Entry("Tme", e, group)


def __get_entry__(type, name, code, group):
    if type == "Cours":
        return cours((code, name), group)

    if type == "Td":
        return td((code, name), group)

    if type == "Tme":
        return tme((code, name), group)

    return None


def parse(filename, required_units=None):
    log = Logger()
    tobj = Timetable()

    table = {}
    units = {}
    opt_units = {}

    with open(filename, "r") as f:
        readed_data = json.load(f)

    for day in readed_data:
        dl = []

        for hour in readed_data[day]:
            hl = []

            for e in hour:

                units[e["code"]] = e["name"]

                if required_units is not None and e["code"] not in required_units:
                    opt_units[e["code"]] = e["name"]

                u = __get_entry__(e["etype"], e["name"], e["code"], e["group"])

                if u is None:
                    log.log("Parse Error : uknown type", Logger.FAIL)
                    return None

                hl.append(u)

            dl.append(hl)

        table[day] = dl

    tobj.table = table
    tobj.ALL_UNITS = [u for u in units.items()]
    tobj.OPT_UNITS = [u for u in opt_units.items()]

    return tobj
