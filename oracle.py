import json, math

def tenths(x):
    return math.floor(x * 10 + 0.5) / 10

def fixed1(x):
    return f"{tenths(x):.1f}"

def ratio_truth(oil, vinegar):
    if oil <= 0:
        raise ValueError("the oil must be above zero")
    if vinegar <= 0:
        raise ValueError("the vinegar must be above zero")
    ratio = tenths(oil / vinegar)
    if ratio < 2.5:
        band = "sharper than the classic 3-to-1"
    elif ratio <= 3.5:
        band = "right at the classic 3-to-1"
    else:
        band = "softer and richer than the classic 3-to-1"
    return (f"{fixed1(oil)} tablespoons of oil against {fixed1(vinegar)} tablespoons of vinegar "
            f"reads {fixed1(ratio)} to 1, {band} honestly.")

def dress_truth(sides, mains):
    if sides + mains <= 0:
        raise ValueError("the salad count must be above zero")
    if sides < 0 or mains < 0:
        raise ValueError("the salad counts cannot be negative")
    tbsp = tenths(sides + mains * 2)
    cups = tenths(tbsp / 16)
    side = "side salad" if sides == 1 else "side salads"
    main = "main salad" if mains == 1 else "main salads"
    return (f"{sides} {side} and {mains} {main} ask {fixed1(tbsp)} tablespoons, "
            f"{fixed1(cups)} cups, of dressing honestly.")

def emulsify_truth(tbsp):
    if tbsp <= 0:
        raise ValueError("the dressing must be above zero")
    tsp = tenths(tbsp / 8)
    return f"{fixed1(tbsp)} tablespoons of dressing wants {fixed1(tsp)} teaspoons of Dijon to hold the emulsion honestly."

cases = []

def add(fn_name, args):
    try:
        fn = {"ratioTruth": ratio_truth, "dressTruth": dress_truth, "emulsifyTruth": emulsify_truth}[fn_name]
        cases.append({"fn": fn_name, "args": args, "result": fn(*args)})
    except ValueError as e:
        cases.append({"fn": fn_name, "args": args, "error": str(e)})

# ratioTruth
add("ratioTruth", [9, 3])       # 3.0 classic
add("ratioTruth", [3, 1])       # 3.0 classic
add("ratioTruth", [6, 3])       # 2.0 sharper
add("ratioTruth", [8, 2])       # 4.0 softer
add("ratioTruth", [7, 2])       # 3.5 edge -> classic
add("ratioTruth", [2, 1])       # 2.0 sharper
add("ratioTruth", [9, 2])       # 4.5 softer
add("ratioTruth", [0, 3])       # error
add("ratioTruth", [9, 0])       # error
# dressTruth
add("dressTruth", [4, 2])       # 8 tbsp, 0.5 cups
add("dressTruth", [1, 0])       # singular side
add("dressTruth", [0, 1])       # singular main
add("dressTruth", [1, 1])       # both singular
add("dressTruth", [6, 3])       # 12 tbsp, 0.8 cups
add("dressTruth", [0, 0])       # error
add("dressTruth", [-1, 2])      # error
# emulsifyTruth
add("emulsifyTruth", [8])       # 1.0 tsp
add("emulsifyTruth", [12])      # 1.5 tsp
add("emulsifyTruth", [10])      # 1.25 -> 1.3 tsp
add("emulsifyTruth", [4])       # 0.5 tsp
add("emulsifyTruth", [0])       # error

with open("expected.json", "w") as f:
    json.dump(cases, f, indent=2)
    f.write("\n")
print(f"{len(cases)} cases written")
for c in cases:
    print(c["fn"], c["args"], "->", c["result"] if "result" in c else "ERR: " + c["error"])
