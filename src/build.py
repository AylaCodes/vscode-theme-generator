import argparse
from pathlib import Path

import themes

def main(args: argparse.Namespace):
    try:
        builder = getattr(themes, args.theme)()
    except Exception as e:
        print(f"Unable to select {args.theme}: {e}")
        print("Falling back to default theme...")
        builder = themes.Theme()

    builder.build_theme(args.template, args.output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t",
        "--template",
        default=Path("template.json"),
        help="Template file to be used (template.json)",
        type=Path,
    )
    parser.add_argument(
        "-T", "--theme", default="Theme", help="The theme to generate (Theme)", type=str
    )
    parser.add_argument(
        "-o",
        "--output",
        default=Path("output.json"),
        help="The file to output the generated theme to (output.json)",
        type=Path,
    )

    args = parser.parse_args()
    main(args)
