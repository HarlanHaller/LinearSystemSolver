
#helper functions
def convert_to_float(frac_str):
    """converts inputed fraction or number as string to float"""
    try:
        return float(frac_str)
    except ValueError:
        num, denom = frac_str.strip().split('/')
        if " " in num:
            raise ValueError
        else:
            return float(num) / float(denom)


def checkEoP(x1, x2, y1, y2, c1, c2):
    """returns 2 if Parellel, 1 if Equal, and 0 if nethier"""
    if x1 == x2 and y1 == y2:
        if c1 != c2:
            return 2
        return 1
    return 0


def gen_equation_temps(Frame, tk):
    Ref_contianer = {}

    a = tk.Entry(width=3, master=Frame, justify=tk.RIGHT)
    a.grid(column=0, row=0)
    Ref_contianer["X"] = a
    tk.Label(text="x +", master=Frame).grid(column=1, row=0)

    b = tk.Entry(width=3, master=Frame, justify=tk.RIGHT)
    b.grid(column=2, row=0)
    Ref_contianer["Y"] = b
    tk.Label(text="y =", master=Frame).grid(column=3, row=0)

    e = tk.Entry(width=3, master=Frame, justify=tk.RIGHT)
    e.grid(column=4, row=0)
    Ref_contianer["C"] = e

    return Ref_contianer

def log(message, output):
    """logs message to output box"""
    output["text"] = message

#errors
class noInput(Exception):
    """Raised when expeted input is not provided"""
    pass
