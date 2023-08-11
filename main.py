from typer import Typer
from typing import List
from webbrowser import open


# PROJECT OO
# Electronics Toolset
# Ohms Law calculator
# Resistance Finder


OO_TITLE = """
 ██████╗  ██████╗       ███████╗██╗     ███████╗ ██████╗
██╔═══██╗██╔═══██╗      ██╔════╝██║     ██╔════╝██╔════╝
██║   ██║██║   ██║█████╗█████╗  ██║     █████╗  ██║     
██║   ██║██║   ██║╚════╝██╔══╝  ██║     ██╔══╝  ██║     
╚██████╔╝╚██████╔╝      ███████╗███████╗███████╗╚██████╗
 ╚═════╝  ╚═════╝       ╚══════╝╚══════╝╚══════╝ ╚═════╝
"""


RESFIND_TITLE = """
██████╗ ███████╗███████╗███████╗██╗███╗   ██╗██████╗ 
██╔══██╗██╔════╝██╔════╝██╔════╝██║████╗  ██║██╔══██╗
██████╔╝█████╗  ███████╗█████╗  ██║██╔██╗ ██║██║  ██║
██╔══██╗██╔══╝  ╚════██║██╔══╝  ██║██║╚██╗██║██║  ██║
██║  ██║███████╗███████║██║     ██║██║ ╚████║██████╔╝
╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝
--------------------------------------------------------------------
"""


res_color_code = {
        "black":  {"value": 0, "multiplier": 1, "tolerance": 0},
        "brown":  {"value": 1, "multiplier": 10, "tolerance": 0.01},
        "red":    {"value": 2, "multiplier": 100, "tolerance":0.02},
        "orange": {"value": 3, "multiplier": 1_000, "tolerance": 0},
        "yellow": {"value": 4, "multiplier": 10_000, "tolerance": 0},
        "green":  {"value": 5, "multiplier": 100_000, "tolerance": 0.005},
        "blue":   {"value": 6, "multiplier": 1_000_000, "tolerance": 0.0025},
        "purple": {"value": 7, "multiplier": 10_000_000, "tolerance": 0.001},
        "gray":   {"value": 8, "multiplier": 100_000_000, "tolerance": 0},
        "white":  {"value": 8, "multiplier": 100_000_000, "tolerance": 0},
        "gold":   {"value": 0, "multiplier": 0.1, "tolerance": 5},
        "silver": {"value": 0, "multiplier": 0.01, "tolerance": 10},
        "none":   {"value": 0, "multiplier": 0, "tolerance": 20},
}

def band_calc_5():
    colors = list()
    while len(colors) < 5:
        color_input = input(f"Enter band-{len(colors) + 1} color: ").strip().lower()
        if color_input == "q":
            raise SystemExit
        elif color_input not in res_color_code.keys():
            print("\nERROR: color not found")
            print("available colors")
            print("------------------------------")
            [print(x) for x in res_color_code.keys()]
        else:
            colors.append(color_input)
    
    color_values = [res_color_code[c]["value"] for c in colors ]
    digits = int("".join(map(str, color_values[:3])))
    multiplier = res_color_code[colors[3]]["multiplier"]
    tolerance = res_color_code[colors[4]]["tolerance"]

    print(f"Calculation: {digits} X {multiplier} = {digits * multiplier} ohms +- {tolerance * 100}%")

    print(digits)



app = Typer()

@app.command()
def resfind():
    print(RESFIND_TITLE)
    try:
        bands = int(input("Enter NO. bands: "))
        if bands == 5:
            band_calc_5()
    except ValueError:
        print("ERROR: non-numeric input")

@app.command()
def datasheet(part: List[str]):
    url = f"https://google.com/search?q={'+'.join(part)}+datasheet"
    open(url)

if __name__ == "__main__":
    app()

# Datasheet lookup

#
