"""Task 3 - Lists and tuples.

Extracting a column, adding a record while keeping the rank column consistent,
and packing dataset metadata into a tuple.
"""

from data import GLOBAL_SALES, NAME, video_game_sales


def ranked(games):
    """Return the rows re-sorted by global sales with the rank column rewritten.

    The rank column has to be recalculated after any insert - otherwise a new row
    tacked onto the end claims a rank its sales do not support.
    """
    ordered = sorted(games, key=lambda game: game[GLOBAL_SALES], reverse=True)
    return [[position] + game[1:] for position, game in enumerate(ordered, start=1)]


def main():
    # a) Pull one column out into its own list
    game_names = [game[NAME] for game in video_game_sales]
    print(f"First five titles: {game_names[:5]}")

    # b) Add a newer release. Working on a copy leaves the shared dataset untouched.
    games = [row[:] for row in video_game_sales]
    games.append(
        [0, 'Animal Crossing: New Horizons', 'NS', 2020, 'Simulation', 'Nintendo',
         7.45, 5.21, 7.37, 31.18]
    )

    # 31.18M would place it 6th, so ranks are rebuilt rather than left as appended.
    games = ranked(games)
    print(f"Rows after append: {len(games)}")

    new_position = next(g[0] for g in games if g[NAME].startswith('Animal Crossing'))
    print(f"Animal Crossing: New Horizons ranks #{new_position} on global sales")

    # c) Dataset metadata as an immutable tuple: (rows, columns, name)
    dataset_info = (len(games), 10, 'Video Game Sales')
    print(f"Dataset info: {dataset_info}")


if __name__ == "__main__":
    main()
