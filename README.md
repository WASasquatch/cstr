# cstr
Provides a method for printing colored messages to console with preset tags.

# Installation

`pip install https://github.com/WASasquatch/cstr.git`

# Example usage
```python
from cstr import *

p = cstr()

#! MESSAGE TEMPLATES
p.color.add_code("msg", f"{cstr.color.BLUE}MyProject: {cstr.color.END}")
p.color.add_code("warning", f"{cstr.color.BLUE}MyProject {cstr.color.LIGHTYELLOW}Warning: {cstr.color.END}")
p.color.add_code("error", f"{cstr.color.RED}MyProject {cstr.color.END}Error: {cstr.color.END}")

#! EXAMPLE USAGE
p("This is a message").msg.print()
p("This is a warning").warning.print()
p("This is a error").error.print()

#! JUST USE COLOR
print(f"{p.color.RED}Red text{p.color.END}")
```
