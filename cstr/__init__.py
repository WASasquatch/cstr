def cstr_colors():
    class color:
        END = '\33[0m'
        BOLD = '\33[1m'
        ITALIC = '\33[3m'
        UNDERLINE = '\33[4m'
        BLINK = '\33[5m'
        BLINK2 = '\33[6m'
        SELECTED = '\33[7m'

        BLACK = '\33[30m'
        RED = '\33[31m'
        GREEN = '\33[32m'
        YELLOW = '\33[33m'
        BLUE = '\33[34m'
        VIOLET = '\33[35m'
        BEIGE = '\33[36m'
        WHITE = '\33[37m'

        BLACKBG = '\33[40m'
        REDBG = '\33[41m'
        GREENBG = '\33[42m'
        YELLOWBG = '\33[43m'
        BLUEBG = '\33[44m'
        VIOLETBG = '\33[45m'
        BEIGEBG = '\33[46m'
        WHITEBG = '\33[47m'

        GREY = '\33[90m'
        LIGHTRED = '\33[91m'
        LIGHTGREEN = '\33[92m'
        LIGHTYELLOW = '\33[93m'
        LIGHTBLUE = '\33[94m'
        LIGHTVIOLET = '\33[95m'
        LIGHTBEIGE = '\33[96m'
        LIGHTWHITE = '\33[97m'

        GREYBG = '\33[100m'
        LIGHTREDBG = '\33[101m'
        LIGHTGREENBG = '\33[102m'
        LIGHTYELLOWBG = '\33[103m'
        LIGHTBLUEBG = '\33[104m'
        LIGHTVIOLETBG = '\33[105m'
        LIGHTBEIGEBG = '\33[106m'
        LIGHTWHITEBG = '\33[107m'
        
        @staticmethod
        def add_code(name, code):
            if not hasattr(color, name.upper()):
                setattr(color, name.upper(), code)
            else:
                raise ValueError(f"'color' object already contains a code with the name '{name}'.")
    return color

class _Cstr(str):        
    def __new__(cls, text='', color_class=None):
        instance = super().__new__(cls, text)
        instance.color = color_class or cstr_colors()
        return instance


    def __getattr__(self, attr):
        if attr.lower().startswith("_cstr"):
            code = getattr(self.color, attr.upper().lstrip("_cstr"))
            modified_text = self.replace(f"__{attr[1:]}__", f"{code}")
            return _Cstr(modified_text)
        elif attr.upper() in dir(self.color):
            code = getattr(self.color, attr.upper())
            modified_text = f"{code}{self}{self.color.END}"
            return _Cstr(modified_text)
        elif attr.lower() in dir(_Cstr):
            return getattr(_Cstr, attr.lower())
        else:
            raise AttributeError(f"'_Cstr' object has no attribute '{attr}'")

    def print(self, **kwargs):
        print(self, **kwargs)

    def add_code(self, name, code):
        self.color.add_code(name, code)

class cstr:
    def __new__(cls, text=''):
        color_class = cstr_colors()
        class CstrInstance(_Cstr):
            def __call__(self, new_text):
                return CstrInstance(new_text, color_class=color_class)
        return CstrInstance(text, color_class=color_class)

    @staticmethod
    def add_code(instance, name, code):
        instance.add_code(name, code)
