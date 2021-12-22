
class Logger:
    HEADER = '\033[95m'

    SUCCES = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    TEXT = ''

    ENDC = '\033[0m'
    BOLD = '\033[1m'

    def log(self, msg, mode, is_bold=False):

        if is_bold:
            mode = f"{mode}{self.BOLD}"

        print(f"{mode}{msg}{self.ENDC}")
