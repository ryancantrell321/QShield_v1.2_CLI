import shutil
from textwrap import fill

terminal_width = shutil.get_terminal_size().columns

def justify_text(text, width):
    lines = text.splitlines()
    justified_lines = []
    for line in lines:
        if not line.strip():  # Preserve empty lines
            justified_lines.append("")
        else:
            wrapped = fill(line, width=width)
            justified_lines.extend(wrapped.splitlines())
    return "\n".join(justified_lines)
