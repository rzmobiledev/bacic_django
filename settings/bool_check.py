list_of_bools = ("True", "true", "tRue", "TRue", "TRUE", "TrUE", "TRuE")


def str_to_boolean(bool_name: str) -> bool:
    """return boolean from string check"""
    if bool_name in list_of_bools:
        return True
    return False
