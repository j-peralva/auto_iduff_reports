from pathlib import Path


def project_root() -> Path:
    """Return project path"""
    path = Path.cwd()
    while path.name != 'auto_iduff_reports':
        path = path.parent
    return path


def read_input() -> list:
    """Read input file and returns each line in a list"""
    with open(project_root().joinpath('input', 'input_data.txt'), 'r') as file:
        data = []
        while line := file.readline().rstrip('\n'):
            data.append(line)
    return data


if __name__ == '__main__':
    print(project_root())
    print(read_input())
