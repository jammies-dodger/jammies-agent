# Feature Improvement: Parentheses Support

## Current State
The calculator evaluates infix expressions (`+`, `-`, `*`, `/`) using a two-stack
shunting-yard approach, but it cannot handle grouped sub-expressions. Expressions
like `(3 + 5) * 2` fail because `(` and `)` are treated as invalid tokens.

## Proposed Improvement
Add support for parentheses so users can control evaluation order:
- `(` pushes onto the operator stack and blocks operator popping.
- `)` pops and applies operators until the matching `(` is found.
- Unmatched `(` or `)` raises a clear `ValueError`.

## Why This Matters
Grouping is a core expectation of any calculator. It enables expressions like
`(10 - 4) * 3`, `2 * (3 + 5)`, and nested groups like `((2 + 3) * 4)`.

## Implementation Notes
- Modify `pkg/calculator.py` `_evaluate_infix` to handle `(` and `)` tokens.
- Add unit tests covering grouped, nested, and unmatched parentheses.
