import json
from copy import copy


def clean_version(notebook_path: str, version: str = "teacher"):
    """
    Removes all cells with corresponding tag and replace the notebook

    Args:
        notebook_path: path to the notebook to modify
        version: version to be kept. Must be chosen in ['teacher', 'student']
    """
    possible_versions = ["teacher", "student"]
    if version not in possible_versions:
        raise ValueError(f"Version must be chosen in ['teacher', 'student']\n"
                         f"Current value is {version}.")
    possible_versions.remove(version)
    opposite_tag = possible_versions[0]

    with open(notebook_path, "r") as f:
        data = json.load(f)

    cells = copy(data["cells"])
    for idx, cell in enumerate(data["cells"]):
        if "metadata" in cell and "tags" in cell["metadata"]:
            tags = cell["metadata"]["tags"]
            if opposite_tag in tags and version not in tags:
                del cells[idx]

    data["cells"] = cells
    json_data = json.dumps(data)
    with open(notebook_path, "w") as f:
        f.write(json_data)
