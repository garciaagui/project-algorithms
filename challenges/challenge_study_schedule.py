def study_schedule(permanence_period, target_time):
    counter = 0

    if type(target_time) != int:
        return None

    for entry, exit in permanence_period:
        if type(entry) != int or type(exit) != int:
            return None

        if target_time >= entry and target_time <= exit:
            counter += 1

    return counter
