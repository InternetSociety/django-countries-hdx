from django_countries_regions.country_regions import COUNTRY_REGIONS
from django_countries_regions.regions import REGIONS, SUBREGIONS


# TODO: Would returning `(region_code, region_name)` be more useful?
def get_country_region(country_code, region=True):
    code_to_use = "iso_region_alpha2_code" if region else "iso_subregion_alpha2_code"
    return COUNTRY_REGIONS[country_code][code_to_use]


def get_country_subregion(country_code):
    return get_country_region(country_code, region=False)


class Regions():
    """
    An object that can query an ISO list of geographical regions and subregions and return a list of countries in
    that region.
    """

    def get_countries_by_region(self, region_code, region=True):
        if region:
            return REGIONS[region_code]["countries"]
        else:
            return SUBREGIONS[region_code]["countries"]

    def get_countries_by_subregion(self, region_code):
        return self.get_countries_by_region(region_code, region=False)

    def get_region_name(self, region_code):
        if region_code:
            return REGIONS[region_code]["name"]
        return None

    def get_subregion_name(self, region_code):
        if region_code:
            return SUBREGIONS[region_code]["name"]
        return None


regions = Regions()
