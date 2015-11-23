def single_match_probs(team1, team2):
    """ input: team1 general winning P, team2 general winning P
        return: team1 winning probability versus team2.
    """
    ability_1 = team1/(1-team1)
    ability_2 = team2/(1-team2)
    return ability_1 / (ability_1+ability_2)

def multiple_match_probs(single_P1, max_matches, winning_require_matches):
    """ Given the winning P of a team in a single match,
        returns the winning P in a max Y matches serie which requires winning X matches to win the serie.
    """

def drunk_probability(drunk_ratio, device_error_chance, alarm_while_drunk_P=1):
    """Police have a device, which can test if a driver is drunk.
       It will never failed when you are drunk.
       But, sometimes, it will mis-indicate a sober dirver drunk.
       Given a ratio of drunk driver among all dirvers and the device_error_chance,
       We can tell you when police randomly pick a dirver, and the device indicates him drunk， the chance that he is really drunk.
    """
    device_alarm_P = drunk_ratio*alarm_while_drunk_P + (1-drunk_ratio)*device_error_chance
    drunk_while_alarm_P = (drunk_ratio*alarm_while_drunk_P) / device_alarm_P
    return drunk_while_alarm_P
