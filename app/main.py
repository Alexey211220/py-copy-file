def copy_file(command: str) -> None:

    parts = command.split()

    if len(parts) == 3 and parts[0] == "cp":
        if parts[1] != parts[2]:
            try:
                with open(parts[1], "r") as new, open(parts[2], "w") as old:
                    for line in new:
                        old.write(line)
            except (FileNotFoundError):
                pass
