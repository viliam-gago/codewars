def tower_builder(n_floors):
    tower = []
    for floor in range(0,n_floors):
        tower.append('*'*(2*floor + 1))

    tower_shifted = [f'{floor:^{len(tower[-1])}}' for floor in tower]

    return tower_shifted
    # for floor in tower_shifted:
    #     print(floor)

tower_builder(3)
