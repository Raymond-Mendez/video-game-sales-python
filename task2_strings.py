"""Task 2 - String methods and f-strings.

Slicing, cleaning inconsistent user-entered names, and formatting a summary line.
"""

from data import GLOBAL_SALES, NAME, YEAR, video_game_sales

# Deliberately messy input, the way names often arrive from a form or scraped page
MESSY_NAMES = ['  Wii Sports  ', 'TETRIS', '  mario kart WII']


def main():
    # a) Slice the franchise name out of a longer title
    game_name = video_game_sales[4][NAME]   # 'Pokemon Red/Blue'
    franchise = game_name[0:7]              # 'Pokemon'
    print(f"Franchise sliced from '{game_name}': {franchise}")

    # b) Normalise messy names: strip whitespace, then title-case them consistently
    print("\nCleaned names:")
    for name in MESSY_NAMES:
        cleaned_name = name.strip().title()
        print(f"  {name!r} -> {cleaned_name!r}")

    # c) Format the best seller as a report line.
    # Units are millions of COPIES SOLD, so no dollar sign here.
    best_name = video_game_sales[0][NAME]
    best_year = video_game_sales[0][YEAR]
    best_global = video_game_sales[0][GLOBAL_SALES]

    print(f"\n#1 Best Seller: {best_name} ({best_year}) - {best_global}M units sold globally")


if __name__ == "__main__":
    main()
