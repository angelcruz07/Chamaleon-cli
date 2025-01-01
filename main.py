import json
import os
import click

THEMES_DIR = os.path.expanduser("~/.config/qtile/themes")
CURRENT_THEME_FILE = os.path.expanduser("~/.config/qtile/config.json")


@click.group()
def cli():
    pass


@click.command()
def list_themes():
    """List avaible Qtile themes."""
    themes = [
        f.replace(".json", "") for f in os.listdir(THEMES_DIR) if f.endswith(".json")
    ]
    for theme in themes:
        print(theme)


@click.command()
@click.argument("theme_name")
def apply_qtile_theme(theme_name):
    """Apply  theme to Qtile"""
    theme_path = os.path.join(THEMES_DIR, f"{theme_name}.json")
    if not os.path.isfile(theme_path):
        print(f"Error: The theme {theme_path} does not exist.")
        return

    theme_data = {"theme": theme_name}

    try:
        with open(CURRENT_THEME_FILE, "w") as f:
            json.dump(theme_data, f, indent=4)
        print(f"Theme '{theme_name}' applied succesfully to Qtile.")
    except Exception as e:
        print(f"Error applying the theme '{theme_name}' : {e}")


cli.add_command(list_themes)
cli.add_command(apply_qtile_theme)


def main():
    print("Chamaleon-cli Welcome!")
    cli()


if __name__ == "__main__":
    main()
