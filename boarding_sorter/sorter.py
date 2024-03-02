def sort_boarding_passes(boarding_passes):
    sorted_passes = []
    starting_pass = next(pass_ for pass_ in boarding_passes if pass_.origin not in [p.destination for p in boarding_passes])
    current_pass = starting_pass

    while current_pass:
        sorted_passes.append(current_pass)
        next_pass = next((pass_ for pass_ in boarding_passes if pass_.origin == current_pass.destination), None)
        current_pass = next_pass

    return sorted_passes