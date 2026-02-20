def copy_file(command: str) -> None:

    parts = command.split()

    if len(parts) == 3 and parts[0] == "cp":
        old_file, new_file = parts[1], parts[2]
        if parts[1] != parts[2]:
            try:
                with open(old_file, "r") as new, open(new_file, "w") as old:
                    for line in new:
                        old.write(line)
            except (FileNotFoundError):
                pass
