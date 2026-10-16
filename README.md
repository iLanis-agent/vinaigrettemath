# Vinaigrette Math

Vinaigrette ratio honesty. Everyone quotes three to one, and nobody measures the one. Vinaigrette Math does the oil-to-vinegar, batch and emulsifier arithmetic a salad dressing depends on, with every norm labeled.

## What it computes

- **The ratio truth** - oil against vinegar in tablespoons, read to tenths and judged: sharper than the classic 3-to-1, right at it, or softer and richer (labeled kitchen norm).
- **The batch truth** - side salads at 1 tablespoon of dressing and main salads at 2 (labeled kitchen norm), totaled in tablespoons and cups.
- **The emulsion truth** - a teaspoon of Dijon per half cup of dressing (labeled kitchen norm) to hold the emulsion, scaled to your batch.

## Boundary

Illustrative arithmetic only. Every norm is a labeled kitchen norm; your recipe and your taste win every tie.

## Files

- `index.html` - landing page with the honesty pitch and the boundary.
- `app.html` - the interactive calculator.
- `engine.js` - the arithmetic, shared by the app and the tests.
- `oracle.py` - the Python mirror that generates `expected.json`.
- `test.js` - compares every engine output against `expected.json` (21 cases).
- `expected.json` - the golden answers.

## Test

```
python3 oracle.py
node test.js
```

Live: https://ilanis-agent.github.io/vinaigrettemath/
Repo: https://github.com/iLanis-agent/vinaigrettemath
