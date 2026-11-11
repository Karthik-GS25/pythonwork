"""51. Safe file and directory management demonstration using os and time."""

import os, time


def manage(base="My_Project"):
    path = os.path.join(base, "assignments", "task1")
    os.makedirs(path, exist_ok=True)
    file_path = os.path.join(path, "sample.py")
    with open(file_path, "w", encoding="utf8") as file:
        file.write("print('Python Assignment')\n")
    total = sum(
        os.path.getsize(os.path.join(root, name))
        for root, _, names in os.walk(base)
        for name in names
    )
    return {
        "cwd": os.getcwd(),
        "cwd_bytes": os.getcwdb(),
        "directory_exists": os.path.isdir(path),
        "total_size": total,
        "access_time": time.ctime(os.path.getatime(file_path)),
        "modified_time": time.ctime(os.path.getmtime(file_path)),
        "contents": os.listdir(path),
    }


print(manage())
