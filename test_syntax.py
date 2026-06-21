import ast
import sys

with open("src/fletSource.ts", "r") as f:
    content = f.read()
    start_idx = content.find("`") + 1
    end_idx = content.rfind("`")
    code = content[start_idx:end_idx]
    
    try:
        ast.parse(code)
        print("Syntax OK")
    except SyntaxError as e:
        print(f"SyntaxError: {e.msg} at line {e.lineno}")
        sys.exit(1)
