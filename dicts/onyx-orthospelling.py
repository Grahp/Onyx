## Onyx Orthospelling

from plover.steno import Stroke as PloverStroke

LONGEST_KEY = 1

def lookup(outline):
    stroke = parse_stroke(outline[0])
    return lookup_stroke(stroke)

def lookup_stroke(stroke):
    if is_valid(stroke):
        print("valid")
        return ortho(stroke)

def is_valid(stroke):
    return stroke >= CHORD or stroke >= SPACE_CHORD

def ortho(stroke):
    ## clean up this horrendous function lol
    starters = stroke & STARTER_KEYS
    vowels = stroke & VOWEL_KEYS
    enders = stroke & ENDER_KEYS
    translation = STARTERS[starters] + VOWELS[vowels] + ENDERS[enders]
    if stroke >= SPACE_CHORD:
        translation = "{^ ^}" + translation
    else:
        translation = "{^}" + translation
    if stroke & {"-D", "-Z"}:
        translation = translation + "e"
    return translation


def parse_stroke(raw_steno_stroke):
    return frozenset(PloverStroke(raw_steno_stroke).keys())

## type hint
def with_stroke_keys(dict):
    return {parse_stroke(k): v for k, v in dict.items()}

CHORD = parse_stroke("+^-")
# INCLUDE_SPACE = lambda stroke: "+" not in stroke
SPACE_CHORD = parse_stroke("^-")
STARTER_KEYS = {"K-", "S-", "P-", "T-", "R-", "L-"}
VOWEL_KEYS = {"J", "E", "I", "U", "-V"}
ENDER_KEYS = {"-R", "-L", "-N", "-F", "-G", "-P", "-T", "-S"}
STARTERS = with_stroke_keys({
    "": "",
    "S": "s",
    "ST": "st",
    "STR": "str",
    "STL": "w",
    "T": "t",
    "K": "k",
    })

VOWELS = with_stroke_keys({
    "": "",
    "JE": "a",
    "I": "i",
    "E": "e",
    })

ENDERS = with_stroke_keys({
    "": "",
    "-R": "r",
    "-N": "n",
    "-NG": "ng",
    "-FG": "b",
    "-VFG": "v",
    })
