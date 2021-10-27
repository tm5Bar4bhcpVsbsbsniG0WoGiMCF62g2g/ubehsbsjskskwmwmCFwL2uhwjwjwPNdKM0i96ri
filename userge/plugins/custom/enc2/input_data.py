import os
import random
import string

list = [0]
link = [0]
custom_name = [0]


def run():
    pattern = ""
    last = int(input("Enter Last episode number:"))
    filename = input("Enter file name(blank if want default name):-")
    while "{i}" not in pattern:
        pattern = input("Enter Custom Name Pattern: with {i}:")
        pattern = os.path.splitext(pattern)[0]
    if filename == "":
        filename = "enc2_data.py"
    else:
        filename += os.path.split(filename)[0] + ".py"
    for i in range(1, last + 1):
        ip = input(f"Enter ep{i} link:")
        if ip != "":
            a = pattern.replace("{i}", f"{i}")
            ran = "".join(random.choices(string.ascii_uppercase + string.digits, k=6))
            a += f" [{str(ran)}]" + ".mkv"
            ip = ip.replace("?a=view", "")
            link.append(ip)
            custom_name.append(a)
            list.append(f"/ddl {ip} | {a}")
            data = open(filename, "w")
            data.write(f"list={list}\n\nlink={link}\n\ncustom_name={custom_name}")
            data.close()
    for i in list:
        print(i)


if __name__ == "__main__":
    run()
