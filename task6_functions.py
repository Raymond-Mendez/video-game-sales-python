"""Task 6 - Functions.

Reusable helpers with default arguments and return values, replacing the
inline loops used in the earlier tasks.
"""

from data import (EU_SALES, GENRE, GLOBAL_SALES, JP_SALES, NAME, NA_SALES,
                  YEAR, video_game_sales)


def regional_sales_total(game):
    """Sum the three regional sales columns for one game.

    Note this will not equal global_sales: the global figure also includes
    'other regions', which the dataset does not break out.
    """
    return game[NA_SALES] + game[EU_SALES] + game[JP_SALES]


def filter_by_genre(games, genre='Platform'):
    """Return every game in a given genre. Defaults to Platform titles."""
    return [game for game in games if game[GENRE] == genre]


def summarize(game):
    """Format one game as a single report line (sales in millions of units)."""
    return f"{game[NAME]} ({game[YEAR]}) - {game[GENRE]} - {game[GLOBAL_SALES]}M units"


def main():
    top_game = video_game_sales[0]
    regional = regional_sales_total(top_game)
    unaccounted = top_game[GLOBAL_SALES] - regional
    print(f"{top_game[NAME]}: {regional:.2f}M across NA/EU/JP, "
          f"{unaccounted:.2f}M in other regions")

    print("\nPlatform games (default argument):")
    for game in filter_by_genre(video_game_sales):
        print(f"  {summarize(game)}")

    print("\nSports games (explicit argument):")
    for game in filter_by_genre(video_game_sales, 'Sports'):
        print(f"  {summarize(game)}")

    print(f"\nFull list ({len(video_game_sales)} titles):")
    for game in video_game_sales:
        print(f"  {summarize(game)}")


if __name__ == "__main__":
    main()
