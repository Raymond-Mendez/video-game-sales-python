"""Task 4 - Loops and conditionals.

Filtering by threshold, counting by era, comparing regional totals, and
collecting a publisher's catalogue.
"""

from data import GLOBAL_SALES, JP_SALES, NAME, NA_SALES, PUBLISHER, YEAR, video_game_sales

BLOCKBUSTER_THRESHOLD = 25  # million units


def main():
    # a) Blockbusters above the threshold
    print(f"Games above {BLOCKBUSTER_THRESHOLD}M units:")
    for game in video_game_sales:
        if game[GLOBAL_SALES] > BLOCKBUSTER_THRESHOLD:
            print(f"  {game[NAME]}: {game[GLOBAL_SALES]}M")

    # b) How many titles predate 2000?
    pre_2000_count = 0
    for game in video_game_sales:
        if game[YEAR] < 2000:
            pre_2000_count += 1
    print(f"\nReleased before 2000: {pre_2000_count} of {len(video_game_sales)}")

    # c) North America vs Japan
    total_na_sales = 0
    total_jp_sales = 0
    for game in video_game_sales:
        total_na_sales += game[NA_SALES]
        total_jp_sales += game[JP_SALES]

    print(f"\nNorth America total: {total_na_sales:.2f}M units")
    print(f"Japan total:         {total_jp_sales:.2f}M units")

    if total_na_sales > total_jp_sales:
        ratio = total_na_sales / total_jp_sales
        print(f"North America leads Japan by {ratio:.1f}x on this top-20 list.")
    else:
        ratio = total_jp_sales / total_na_sales
        print(f"Japan leads North America by {ratio:.1f}x on this top-20 list.")

    # d) One publisher's share of the list
    nintendo_games = []
    for game in video_game_sales:
        if game[PUBLISHER] == 'Nintendo':
            nintendo_games.append(game[NAME])

    share = len(nintendo_games) / len(video_game_sales) * 100
    print(f"\nNintendo titles: {len(nintendo_games)} ({share:.0f}% of the list)")
    for name in nintendo_games:
        print(f"  {name}")


if __name__ == "__main__":
    main()
