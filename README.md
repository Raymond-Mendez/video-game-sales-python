# Video Game Sales Analysis — Python Fundamentals

Core Python worked through on a real dataset instead of toy examples: the 20 best-selling video games
of all time, analysed with nothing but the standard library — no pandas. Each script covers one
building block and prints a small report.

Sales figures are **millions of units sold**, not dollars.

## Findings

From the top-20 list:

| Question | Answer |
|---|---|
| Combined global sales | 586.61M units |
| Average per title | 29.33M units |
| Wii Sports' share of the total | **14.1%** — one title is a seventh of the entire list |
| Best-selling genre | Sports, 138.46M units |
| Titles published by Nintendo | **17 of 20** (85%) |
| Released before 2000 | 6 of 20 |
| North America vs Japan | NA outsells Japan 3.8× (295.75M vs 78.72M) |

The headline takeaway is concentration: Nintendo holds 85% of the all-time top 20, and a single
pack-in title (Wii Sports, 82.74M) accounts for 14% of the combined total.

## Scripts

| File | Concepts | What it prints |
|---|---|---|
| [`data.py`](data.py) | Module-level constants | The shared dataset and column-index constants |
| [`task1_variables.py`](task1_variables.py) | Variables, arithmetic, f-string formatting | Dataset size, total and average global sales, the #1 title's share |
| [`task2_strings.py`](task2_strings.py) | Slicing, `.strip()`, `.title()` | A franchise name sliced out of a title, plus messy names normalised |
| [`task3_lists.py`](task3_lists.py) | Lists, comprehensions, `sorted()`, tuples | Column extraction, adding a record with ranks rebuilt, dataset metadata |
| [`task4_loops.py`](task4_loops.py) | `for`, `if/else`, accumulators | Blockbusters above 25M, pre-2000 count, NA vs JP totals, Nintendo's catalogue |
| [`task5_dictionaries.py`](task5_dictionaries.py) | Dicts, `.get()`, `.items()`, sorting | Sales by genre, titles per publisher, one game as a labelled record |
| [`task6_functions.py`](task6_functions.py) | Functions, default arguments, returns | Regional vs global sales reconciliation, genre filtering, formatted summaries |

## Design notes

Three decisions worth calling out, since they were fixes to an earlier version:

- **The dataset lives in one place.** It was originally copy-pasted into all six scripts. It now sits
  in `data.py` and is imported, so a correction to one row propagates everywhere.
- **Ranks are recalculated after an insert.** `task3` adds Animal Crossing: New Horizons (31.18M),
  which belongs at **#6**, not #21. Appending a row without rebuilding the rank column would leave the
  data self-contradictory.
- **Units are labelled consistently.** These are millions of *units sold*; an earlier version
  formatted one of them with a dollar sign.

Each script is import-safe (`if __name__ == "__main__"`), so importing a helper does not trigger a
wall of printed output.

## Running

Python 3.8+, no dependencies:

```bash
python task1_variables.py
```

## Data

20 rows × 10 columns: rank, name, platform, year, genre, publisher, and sales for North America,
Europe, Japan and globally. Adapted from [VGChartz](https://www.vgchartz.com/) global sales estimates
(public domain). Regional columns do not sum to the global figure — the global total also includes
other regions, which the dataset does not break out (`task6` quantifies the gap).

## License

[MIT](LICENSE)
