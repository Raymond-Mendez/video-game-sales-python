"""Task 5 - Dictionaries.

Aggregating sales by genre, counting titles per publisher, and building a
labelled record for a single game.
"""

from data import GENRE, GLOBAL_SALES, NAME, PUBLISHER, YEAR, video_game_sales


def main():
    # a) Total global sales per genre
    sales_by_genre = {}
    for game in video_game_sales:
        genre = game[GENRE]
        sales_by_genre[genre] = sales_by_genre.get(genre, 0) + game[GLOBAL_SALES]

    print("Global sales by genre (millions of units):")
    for genre, sales in sorted(sales_by_genre.items(), key=lambda item: item[1], reverse=True):
        print(f"  {genre:<13} {sales:6.2f}M")

    # b) Number of titles per publisher
    games_per_publisher = {}
    for game in video_game_sales:
        publisher = game[PUBLISHER]
        games_per_publisher[publisher] = games_per_publisher.get(publisher, 0) + 1

    print("\nTitles per publisher:")
    for publisher, count in sorted(games_per_publisher.items(), key=lambda item: item[1], reverse=True):
        print(f"  {publisher:<10} {count}")

    # c) A single game as a labelled record instead of a positional row
    top_game_row = video_game_sales[0]
    top_game = {
        'name': top_game_row[NAME],
        'year': top_game_row[YEAR],
        'genre': top_game_row[GENRE],
        'publisher': top_game_row[PUBLISHER],
        'global_sales_millions': top_game_row[GLOBAL_SALES],
    }

    print("\nTop game record:")
    for key, value in top_game.items():
        print(f"  {key}: {value}")


if __name__ == "__main__":
    main()
