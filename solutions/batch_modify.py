import os
import re


def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.readlines()

    main_block_start = None
    for i, line in enumerate(content):
        if re.match(r"if\s+__name__\s*==\s*['\"]__main__['\"]\s*:", line):
            main_block_start = i
            break
    else:
        raise NotImplementedError(
            f"if __name__ == '__main__' not found in {file_path}"
            )

    if main_block_start is None:
        return  # Skip files without `if __name__ == '__main__':`

    # Extract indentation
    indent_match = re.match(
        r"(\s*)if\s+__name__\s*==\s*['\"]__main__['\"]\s*:",
        content[main_block_start])
    indent = indent_match.group(1) if indent_match else ""

    # Collect lines inside `if __name__ == '__main__':`
    main_code = []
    main_block_end = None
    for i in range(main_block_start + 1, len(content)):
        if content[i].strip() == "":
            main_code.append(content[i])  # Preserve blank lines
            continue
        # Stop when indentation level changes
        if not content[i].startswith(indent + "    "):
            main_block_end = i
            break
        # Remove one level of indentation
        main_code.append(content[i][len(indent):])

    if not main_code:
        return  # Skip if there's no meaningful content

    # Construct new content
    # Keep everything before the `if __name__`
    new_content = content[:main_block_start]
    new_content.append("def main():\n")
    new_content.append("    '''Main code of module.'''\n")
    new_content.extend(main_code)
    new_content.append("if __name__ == '__main__':\n")
    new_content.append("    main()\n")

    # Add the remaining content after the `if __name__` block
    if main_block_end is not None:
        new_content.append("\n\n")
        new_content.extend(content[main_block_end:])

    with open(file_path.lower(), 'w', encoding='utf-8') as f:
        f.writelines(new_content)


def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file == 'batch_modify.py':
                continue
            if file.endswith('.py'):
                process_file(os.path.join(root, file))


# process_file("problem_001F.py")
process_directory('C:/Users/a3592/OneDrive - INSTRUMENTACION Y COMPONENTES SA'
                  + '/Documentos/Python/ProjectEuler/solutions')
