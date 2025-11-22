from common.constants.countries import set_country_trigram


UNIT_NAME_SEP = '_'


def set_gen_unit_name(country: str, agg_prod_type: str) -> str:
    country_trigram = set_country_trigram(country=country)
    return f'{country_trigram}{UNIT_NAME_SEP}{agg_prod_type}'


def get_country_from_unit_name(prod_unit_name: str) -> str:
    return prod_unit_name.split(UNIT_NAME_SEP)[0]


def get_prod_type_from_unit_name(prod_unit_name: str) -> str:
    return prod_unit_name.split(UNIT_NAME_SEP)[1]


