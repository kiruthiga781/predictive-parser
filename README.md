# predictive-parser
A predictive parser for arithmetic expressions using LL(1) grammar implemented in Python.
## Features

- LL(1) predictive parser
- Supports `+`, `-`, `*`, `/` and parentheses
- Computes FIRST and FOLLOW sets
- Minimal and modular Python implementation
- ## Grammar
- E → T E'
E' → + T E' | ε
T → F T'
T' → * F T' | ε
F → (E) | id
