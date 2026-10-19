
"""Command-line weather application."""

import argparse
import os
import sys
from pathlib import Path

try:
    from .favorites import FavoritesManager
    from .weather_api import (
        WeatherAPI,
        format_current_weather,
        format_forecast
    )
except ImportError:
    from favorites import FavoritesManager
    from weather_api import (
        WeatherAPI,
        format_current_weather,
        format_forecast
    )


FAVORITES_FILE = Path(__file__).with_name("favorites.json")



def load_api_key():
    key = os.environ.get("WEATHER_API_KEY")

    if key:
        return key

    try:
        from importlib import import_module

        config = import_module("week08.config")

        return (
            getattr(config, "API_KEY", None)
            or getattr(config, "WEATHER_API_KEY", None)
        )

    


    except ImportError:
        return None


def build_parser():
    parser = argparse.ArgumentParser(
        description="Check weather and manage saved locations"
    )

    commands = parser.add_subparsers(
        dest="command",
        required=True
    )

    current = commands.add_parser(
        "current",
        help="Show current weather"
    )
    current.add_argument("location")

    forecast = commands.add_parser(
        "forecast",
        help="Show weather forecast"
    )
    forecast.add_argument("location")
    forecast.add_argument(
        "--days",
        type=int,
        default=3
    )

    favorites = commands.add_parser(
        "favorites",
        help="Manage favorite locations"
    )

    favorites_commands = favorites.add_subparsers(
        dest="favorites_command",
        required=True
    )

    add = favorites_commands.add_parser("add")
    add.add_argument("name")
    add.add_argument("location")

    favorites_commands.add_parser("list")

    remove = favorites_commands.add_parser("remove")
    remove.add_argument("name")

    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)

    favorites = FavoritesManager(FAVORITES_FILE)

    if args.command == "favorites":

        if args.favorites_command == "add":
            if not favorites.add(args.name, args.location):
                print(
                    f"Favorite '{args.name}' already exists",
                    file=sys.stderr
                )
                return 1

            print(f"Added {args.name}: {args.location}")
            return 0

        if args.favorites_command == "remove":
            if not favorites.remove(args.name):
                print(
                    f"Favorite '{args.name}' not found",
                    file=sys.stderr
                )
                return 1

            print(f"Removed {args.name}")
            return 0

        if args.favorites_command == "list":
            for name, location in favorites.list_all().items():
                print(f"{name}: {location}")

            return 0

    api_key = load_api_key()

    if not api_key:
        print(
            "Error: API key is missing",
            file=sys.stderr
        )
        return 1

    location = (
        favorites.get_location(args.location)
        or args.location
    )

    client = WeatherAPI(api_key)

    try:
        if args.command == "current":
            data = client.get_current_weather(location)
            formatter = format_current_weather

        else:
            data = client.get_forecast(
                location,
                days=args.days
            )
            formatter = format_forecast

        if data is None:
            print(
                "Error: Weather request failed",
                file=sys.stderr
            )
            return 1

        print(formatter(data))
        return 0

    except (ValueError, KeyError, TypeError) as exc:
        print(
            f"Error: {exc}",
            file=sys.stderr
        )
        return 1


if __name__ == "__main__":
    sys.exit(main())
