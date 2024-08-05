from django_countries_regions.country_regions import COUNTRY_REGIONS
from django_countries_regions.regions import REGIONS, SUBREGIONS


def country_region(country_code, region=True):
    """Return a UN M49 region code for a country.

    Extends django-countries by adding a .region method to the Country field.

    :param country_code: Two-letter ISO country code.
    :param region: Boolean. Region lookup if True, Sub-region if False.
    :return: String. UN M49 region code.
    """
    code_to_use = "un_region_code" if region else "un_subregion_code"
    return COUNTRY_REGIONS[country_code][code_to_use]


def country_subregion(country_code):
    """Return a UN M49 sub-region code for a country.

    Extends django-countries by adding a .subregion method to the Country field.

    :param country_code: Two-letter ISO country code.
    :return: String. UN M49 sub-region code.
    """
    return country_region(country_code, region=False)


class Regions():
    """
    An object that can query a UN M49 list of geographical regions and subregions and return a list of countries in
    that region.
    """

    def countries_by_region(self, region_code, region=True):
        """Return a list of country codes found within a region.

        :param region_code: UN M49 region code.
        :param region: Boolean. Region lookup if True, Sub-region if False.
        :return: List of two-letter ISO country codes.
        """
        if region_code:
            if region:
                return REGIONS[region_code]["countries"]
            else:
                return SUBREGIONS[region_code]["countries"]
        return None

    def countries_by_subregion(self, region_code):
        """Return a list of country codes found within a sub-region

        :param region_code: UN M49 sub-region code.
        :return: List of two-letter ISO country codes.
        """
        if region_code:
            return self.countries_by_region(region_code, region=False)
        return None

    def region_name(self, region_code):
        """Return the region name

        :param region_code: UN M49 region code.
        :return: String
        """
        if region_code:
            return REGIONS[region_code]["name"]
        return None

    def subregion_name(self, region_code):
        """Return the region name

        :param region_code: UN M49 sub-region code.
        :return: String
        """
        if region_code:
            return SUBREGIONS[region_code]["name"]
        return None


regions = Regions()
