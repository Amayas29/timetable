
# *I need my timetable for the second semester of my L3 !*

Generate timetables from a general timetable, according to the optional units chosen and taking into account the overlapping of sessions.

*Linux and Mac* ~~Windows~~

## How to use

Clone the project with the following command:

```sh
git clone https://github.com/Amayas29/timetable
```

* make sure you are in the timetable directory (with cd command)

then start the program with the following command:

```sh
python3 main.py <filename : String> <number of optinals units : Int> <required units codes : List>
```

for instance

```sh
python3 main.py l3_info.json 4 LU3IN010
```

A results.txt file will then be created with the different schedules generated.

## Example

```'
+----------+---------------+----------------+-----+-----------------+------------------+------------------+
|   Jour   |  8h45 - 10h30 |  10h45-12h30   | --- |   14h - 15h45   |   16h - 17h45    |   18h - 19h45    |
+----------+---------------+----------------+-----+-----------------+------------------+------------------+
|  lundi   |  Cours : SYS  | Cours : COMPAR |     | Td : COMPAR - 1 | Tme : COMPAR - 1 |                  |
|          |               |                |     |                 |                  |                  |
|          |               |                |     |                 |                  |                  |
|  mardi   |               |  Td : IA - 2   |     |   Tme : IA - 2  |                  |                  |
|          |               |                |     |                 |                  |                  |
|          |               |                |     |                 |                  |                  |
| mercredi |  Cours : CALC | Cours : CRYPTO |     |                 | Td : CRYPTO - 2  | Tme : CRYPTO - 2 |
|          |               |                |     |                 |                  |                  |
|          |               |                |     |                 |                  |                  |
|  jeudi   |               |                |     |    Cours : IA   |                  |                  |
|          |               |                |     |                 |                  |                  |
|          |               |                |     |                 |                  |                  |
| vendredi | Td : CALC - 2 | Tme : CALC - 2 |     |   Td : SYS - 6  |  Tme : SYS - 6   |                  |
|          |               |                |     |                 |                  |                  |
|          |               |                |     |                 |                  |                  |
+----------+---------------+----------------+-----+-----------------+------------------+------------------+

```
