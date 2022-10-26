#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    j = list(dir(hidden_4))
    for i in j:
        if i(1) == "_":
            continue
        else:
            print(f"{i}")
