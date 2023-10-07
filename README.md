# cstr
Provides a method for printing colored messages to console with preset tags.

# Installation

`pip install https://github.com/WASasquatch/cstr.git`

# Example usage
```python
from cstr import cstr

#! MESSAGE TEMPLATES
cstr.color.add_code("msg", f"{cstr.color.BLUE}MyProject: {cstr.color.END}")
cstr.color.add_code("warning", f"{cstr.color.BLUE}MyProject {cstr.color.LIGHTYELLOW}Warning: {cstr.color.END}")
cstr.color.add_code("error", f"{cstr.color.RED}MyProject {cstr.color.END}Error: {cstr.color.END}")

#! EXAMPLE USAGE
cstr("This is a message").msg.print()
cstr("This is a warning").warning.print()
cstr("This is a warning").error.print()
```
