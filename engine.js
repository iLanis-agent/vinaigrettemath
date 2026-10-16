// Vinaigrette Math engine - oil-to-vinegar ratio, batch and emulsion honesty.
// Every norm is a labeled kitchen norm; the app never judges doneness or safety.

function assertPositive(value, label) {
  if (!Number.isFinite(value) || value <= 0) {
    throw new Error(label + " must be above zero");
  }
}

function tenths(x) {
  return Math.floor(x * 10 + 0.5) / 10;
}

function fixed1(x) {
  return tenths(x).toFixed(1);
}

// Labeled norm: the classic vinaigrette is 3 parts oil to 1 part vinegar.
function ratioTruth(oilTbsp, vinegarTbsp) {
  assertPositive(oilTbsp, "the oil");
  assertPositive(vinegarTbsp, "the vinegar");
  const ratio = tenths(oilTbsp / vinegarTbsp);
  let band;
  if (ratio < 2.5) {
    band = "sharper than the classic 3-to-1";
  } else if (ratio <= 3.5) {
    band = "right at the classic 3-to-1";
  } else {
    band = "softer and richer than the classic 3-to-1";
  }
  return fixed1(oilTbsp) + " tablespoons of oil against " + fixed1(vinegarTbsp) +
    " tablespoons of vinegar reads " + fixed1(ratio) + " to 1, " + band + " honestly.";
}

// Labeled norm: a side salad takes 1 tablespoon of dressing, a main salad takes 2.
function dressTruth(sideSalads, mainSalads) {
  assertPositive(sideSalads + mainSalads, "the salad count");
  if (!Number.isFinite(sideSalads) || sideSalads < 0 || !Number.isFinite(mainSalads) || mainSalads < 0) {
    throw new Error("the salad counts cannot be negative");
  }
  const tbsp = tenths(sideSalads + mainSalads * 2);
  const cups = tenths(tbsp / 16);
  const side = sideSalads === 1 ? "side salad" : "side salads";
  const main = mainSalads === 1 ? "main salad" : "main salads";
  return sideSalads + " " + side + " and " + mainSalads + " " + main + " ask " + fixed1(tbsp) +
    " tablespoons, " + fixed1(cups) + " cups, of dressing honestly.";
}

// Labeled norm: a teaspoon of Dijon per half cup of dressing holds the emulsion.
function emulsifyTruth(dressingTbsp) {
  assertPositive(dressingTbsp, "the dressing");
  const tsp = tenths(dressingTbsp / 8);
  return fixed1(dressingTbsp) + " tablespoons of dressing wants " + fixed1(tsp) +
    " teaspoons of Dijon to hold the emulsion honestly.";
}

if (typeof module !== "undefined") {
  module.exports = { ratioTruth, dressTruth, emulsifyTruth, tenths, fixed1 };
}
