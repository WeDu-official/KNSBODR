"""
KNSBODR - kinda not sane but okayish dice roller – A tiny CLI tool for rolling dice.
made by WEDUXOX/WEDUOFFICIAL as a joke for god sake- https://github.com/WeDu-official
Usage:
    python dice_roller.py roll 2d6
    python dice_roller.py roll 1d20+5
"""

import argparse
import random
import re
import sys


# ---- Core Logic ----
def parse_dice_notation(notation: str) -> tuple[int, int, int]:
    """
    Parse dice notation like '2d6', '1d20+5', '3d8-2'.
    Returns: (num_dice, sides, modifier)
    """
    pattern = r'^(\d+)d(\d+)([+-]\d+)?$'
    match = re.match(pattern, notation.lower().strip())

    if not match:
        raise ValueError(
            f"Invalid dice notation: {notation}. "
            "Use format like '2d6' or '1d20+5'."
        )

    num_dice = int(match.group(1))
    sides = int(match.group(2))
    mod_str = match.group(3)
    modifier = int(mod_str) if mod_str else 0

    if num_dice <= 0 or sides <= 0:
        raise ValueError("Number of dice and sides must be positive like your avg mood morning before you remember you slept too long.. or maybe world is too early.")
    if num_dice > 1000:
    	 raise ValueError("too many dice ~ pookie ;) (max 1,000).")
    if modifier > 100000:
    	 raise ValueError("too big modifer (max 100 apples multipled by 1k baskets(don't worry that max value of human brain was 2^17 as i heard)).")
    if sides > 10000:
        raise ValueError("Sides too large (max 10,000(go and open file and see python code for first time in your life my pookie)).")

    return num_dice, sides, modifier


def roll_dice(
    num_dice: int,
    sides: int,
    modifier: int = 0
) -> tuple[list[int], int]:
    """
    Rolls dice and returns (individual_rolls, total).
    """
    rolls = [random.randint(1, sides) for _ in range(num_dice)]
    total = sum(rolls) + modifier
    return rolls, total


def format_roll_output(
    notation: str,
    rolls: list[int],
    total: int,
    modifier: int = 0
) -> str:
    """Pretty-print the roll result."""
    if modifier > 0:
        mod_str = f"+{modifier}"
    elif modifier < 0:
        mod_str = f"-{abs(modifier)}"
    else:
        mod_str = ""

    rolls_str = " + ".join(str(r) for r in rolls)

    if mod_str:
        calc = f"({rolls_str}) {mod_str}"
    else:
        calc = rolls_str

    return f"🎲 {notation} → {calc} = **{total}**"


# ---- CLI ----
def main():
    parser = argparse.ArgumentParser(
        description="KNSBODR - kinda not sane but okayish dice roller.",
        epilog="Examples:\n  roll 2d6\n  roll 1d20+5"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
        help="Subcommands"
    )

    # Roll command
    roll_parser = subparsers.add_parser(
        "roll",
        help="Roll dice (e.g., 2d6, 1d20+5)"
    )
    roll_parser.add_argument(
        "notation",
        type=str,
        help="Dice notation like 2d6 or 1d20+5"
    )

    args = parser.parse_args()

    if args.command == "roll":
        try:
            num_dice, sides, modifier = parse_dice_notation(args.notation)
            rolls, total = roll_dice(num_dice, sides, modifier)

            print(
                format_roll_output(
                    args.notation,
                    rolls,
                    total,
                    modifier
                )
            )

        except ValueError as e:
            print(f"❌ Error: {e}", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()
