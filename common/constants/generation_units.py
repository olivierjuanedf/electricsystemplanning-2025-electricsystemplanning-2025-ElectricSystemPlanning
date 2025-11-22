from common.constants.countries import set_country_trigram


UNIT_NAME_SEP = '_'


def set_gen_unit_name(country: str, agg_prod_type: str) -> str:
    country_trigram = set_country_trigram(country=country)
    return f'{country_trigram}{UNIT_NAME_SEP}{agg_prod_type}'


def get_country_from_unit_name(prod_unit_name: str) -> str:
    return prod_unit_name.split(UNIT_NAME_SEP)[0]


def get_prod_type_from_unit_name(prod_unit_name: str) -> str:
    """
    ATTENTION tricky cases if '_' in prod type... the rule is to take the str after country name + separator
    Args:
        prod_unit_name:

    Returns:
    """
    country = get_country_from_unit_name(prod_unit_name=prod_unit_name)
    return prod_unit_name[len(country) + len(UNIT_NAME_SEP):]


STORAGE_COL_SUFFIX = {'prod': 'prod', 'cons': 'cons'}


def add_suffix_to_storage_unit_col(col: str, col_type: str) -> str:
    """
    Suffix added when both prod. and cons. for storage are put in a same df -> to distinguish the 2 columns 
    for a same prod unit
    Args:
        col: 
        col_type: either prod/cons

    Returns:

    """
    if col_type not in STORAGE_COL_SUFFIX:
        raise Exception(f'Suffix cannot be added to storage column {col}; unknown type {col_type} '
                        f'(it must be in {list(STORAGE_COL_SUFFIX)})')
    return col + UNIT_NAME_SEP + STORAGE_COL_SUFFIX[col_type]
