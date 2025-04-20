#!/usr/bin/env -S uv run --script
import polars as pl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import argparse
import os


def plot(csv_path, svg_path, title, x_date):
    try:
        df = pl.read_csv(csv_path, has_header=True)
        if x_date:
            df = df.with_columns(
                pl.col(df.columns[0]).str.strptime(pl.Date, "%Y-%m-%d")
            )
        x_data = df[:, 0]
        y_data = df[:, 1]

        plt.figure(figsize=(10, 6))
        ax = plt.gca()
        if x_date:
            ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
            ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
            plt.setp(ax.get_xticklabels(), rotation=45, ha="right")
        plt.plot(x_data, y_data, linewidth=2)

        plt.ylim(bottom=0, top=1.20 * max(y_data))

        plt.xlabel(df.columns[0])
        plt.ylabel(df.columns[1])
        if len(title) != 0:
            plt.title(title)

        plt.grid(True)
        plt.tight_layout()

        plt.savefig(svg_path, format="svg")
        print(f"wrote plot to {svg_path}")

    except FileNotFoundError:
        print(f"Error: The file {csv_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Create a line graph from a CSV file and save it as an SVG."
    )
    parser.add_argument("csv", help="Input CSV filepath")
    parser.add_argument(
        "--svg",
        help="Output SVG filepath (defaults to CSV filepath with .csv extension replaced with .svg)",
    )
    parser.add_argument("--title", help="Output graph's title")
    parser.add_argument(
        "--x_date",
        action="store_true",
        help="Treat the x-axis as dates",
    )
    args = parser.parse_args()
    if args.svg:
        svg_path = args.svg
    else:
        base = os.path.splitext(args.csv)[0]
        svg_path = base + ".svg"
    if args.title:
        title = args.title
    else:
        title = ""
    plot(args.csv, svg_path, title, args.x_date)
