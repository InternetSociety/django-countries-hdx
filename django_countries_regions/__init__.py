from django_countries_regions.country_regions import COUNTRY_REGIONS
from django_countries_regions.regions import REGIONS, SUBREGIONS


class Regions:
    """
    An object that can query a UN M49 list of geographical regions and subregions and return a list of countries in
    that region.
    """

    def country_region(self, country_code: str, region: bool = True) -> str | None:
        """Return a UN M49 region code for a country.

        Extends django-countries by adding a .region method to the Country field.

        :param country_code: Two-letter ISO country code.
        :param region: Boolean. Region lookup if True, Sub-region if False.
        :return: String. UN M49 region code.
        """
        code_to_use = "un_region_code" if region else "un_subregion_code"
        try:
            return COUNTRY_REGIONS[country_code][code_to_use]
        except KeyError:
            return None

    def country_region_name(self, country_code: str) -> str | None:
        """Return the region name for a country

        :param country_code: Two-letter ISO country code.
        :return: String
        """
        region_code = self.country_region(country_code)

        if region_code:
            try:
                return self.region_name(region_code)
            except KeyError:
                return None
        return None

    def country_subregion(self, country_code: str) -> str | None:
        """Return a UN M49 sub-region code for a country.

        Extends django-countries by adding a .subregion method to the Country field.

        :param country_code: Two-letter ISO country code.
        :return: String. UN M49 sub-region code.
        """
        try:
            return self.country_region(country_code, region=False)
        except KeyError:
            return None

    def country_subregion_name(self, country_code: str) -> str | None:
        """Return the sub-region name for a country

        :param country_code: Two-letter ISO country code.
        :return: String
        """
        region_code = self.country_subregion(country_code)

        if region_code:
            try:
                return self.subregion_name(region_code)
            except KeyError:
                return None
        return None

    def countries_by_region(self, region_code: str, region: bool = True) -> str | None:
        """Return a list of country codes found within a region.

        :param region_code: UN M49 region code.
        :param region: Boolean. Region lookup if True, Sub-region if False.
        :return: List of two-letter ISO country codes.
        """
        if region_code:
            if region:
                try:
                    return REGIONS[region_code]["countries"]
                except KeyError:
                    return None
            else:
                return SUBREGIONS[region_code]["countries"]
        return None

    def countries_by_subregion(self, region_code: str) -> str | None:
        """Return a list of country codes found within a sub-region

        :param region_code: UN M49 sub-region code.
        :return: List of two-letter ISO country codes.
        """
        if region_code:
            try:
                return self.countries_by_region(region_code, region=False)
            except KeyError:
                return None
        return None

    def region_name(self, region_code: str) -> str | None:
        """Return the region name

        :param region_code: UN M49 region code.
        :return: String
        """
        if region_code:
            try:
                return REGIONS[region_code]["name"]
            except KeyError:
                return None
        return None

    def subregion_name(self, region_code: str) -> str | None:
        """Return the region name

        :param region_code: UN M49 sub-region code.
        :return: String
        """
        if region_code:
            try:
                return SUBREGIONS[region_code]["name"]
            except KeyError:
                return None
        return None


regions = Regions()
