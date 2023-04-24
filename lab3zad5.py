def tower_hanoi(n, from_rod, to_rod, aux_rod):
    stack = [(n, from_rod, to_rod, aux_rod)]
    while stack:
        n, from_rod, to_rod, aux_rod = stack.pop()
        if n == 1:
            print(f"Move disk {n} from rod {from_rod} to rod {to_rod}")
        else:
            stack.append((n-1, aux_rod, to_rod, from_rod))
            stack.append((1, from_rod, to_rod, aux_rod))
            stack.append((n-1, from_rod, aux_rod, to_rod))
n = 5
tower_hanoi(n, 'A', 'C', 'B')