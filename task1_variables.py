"""Task 1 - Variables and arithmetic.

Dataset size, average global sales, and how much of the total the #1 title represents.
All sales figures are in millions of units.
"""

from data import GLOBAL_SALES, video_game_sales


def main():
    # a) How many games are in the dataset?
    total_games = len(video_game_sales)
    print(f"Games in dataset: {total_games}")

    # b) Average global sales across all games
    total_global_sales = 0
    for game in video_game_sales:
        total_global_sales += game[GLOBAL_SALES]

    avg_global_sales = total_global_sales / total_games
    print(f"Total global sales: {total_global_sales:.2f} million units")
    print(f"Average global sales: {avg_global_sales:.2f} million units")

    # c) Share of total sales held by the top-selling game
    top_game_global_sales = video_game_sales[0][GLOBAL_SALES]
    top_game_share = (top_game_global_sales / total_global_sales) * 100
    print(f"Top game's share of total global sales: {top_game_share:.1f}%")


if __name__ == "__main__":
    main()
