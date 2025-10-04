import json

def read_variable(variable_name):

    """Reads a specific variable from a JSON file.

  Args:
    file_path: The path to the JSON file.
    variable_name: The name of the variable to read.

  Returns:
    The value of the variable, or None if the variable is not found.
    """

    with open('settings.json', 'r') as f:
        data = json.load(f)

    if variable_name in data:
        return data[variable_name]
    else:
        return None
