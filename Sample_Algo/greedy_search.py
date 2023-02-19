def state_coverage_problem():
    """ Set of stated needed to cover"""
    states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])
    
    """Hash table (dictionary) used to store key-value pair.
    Format: stations[str: 'station']: set(list(str('name'), str('name')))"""
    stations = {}
    stations["kone"] = set(["id", "nv", "ut"])
    stations["ktwo"] = set(["wa", "id", "mt"])
    stations["kthree"] = set(["or", "nv", "ca"])
    stations["kfour"] = set(["nv", "ut"])
    stations["kfive"] = set(["ca", "az"])

    """Set to store the final stations that we need to rent to cover
    the area selected in states_needed"""
    final_stattions = set()

    best_station = None
    while states_needed:
        best_station = None
        states_covered = set()
        for station, states in stations.items():
            covered = states_needed & states
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered
        
        states_needed -= states_covered
        final_stattions.add(best_station)

    print(final_stattions)