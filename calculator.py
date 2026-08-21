"""weduxox bla bla"""
"""An unnecessarily dramatic calculator like my aunts except that they are not that good at math.. or anything... besides drama"""

import argparse
import ast
import operator


OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.FloorDiv: operator.floordiv,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}


def evaluate(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value

    if isinstance(node, ast.UnaryOp) and type(node.op) in OPERATORS:
        return OPERATORS[type(node.op)](evaluate(node.operand))

    if isinstance(node, ast.BinOp) and type(node.op) in OPERATORS:
        left = evaluate(node.left)
        right = evaluate(node.right)
        return OPERATORS[type(node.op)](left, right)

    raise ValueError("Unsupported mathematical expression.")


def calculate(expression: str):
    tree = ast.parse(expression, mode="eval")
    return evaluate(tree.body)


def main():
    parser = argparse.ArgumentParser(
        description="Perform unnecessarily dramatic arithmetic."
    )
    parser.add_argument("expression", help="Expression such as 2+2 or (8*7)-3")
    args = parser.parse_args()

    try:
        print("🧮 Initializing arithmetic subsystem...")
        print("🔍 Parsing mathematical structure...")
        print("📡 Establishing numerical communication...")
        print("🧠 Consulting the computational authorities...")
        print("⚙️ Performing highly sophisticated calculations...")

        result = calculate(args.expression)

        print()
        print(f"🎯 RESULT: {result}")

    except (SyntaxError, ValueError, ZeroDivisionError) as e:
        print()
        print(f"❌ Mathematical catastrophe: {e}")


if __name__ == "__main__":
    main()

