from unittest import TestCase
from django_countries_regions import regions

world_regions = ["AQ", "BV", "IO", "CX", "CC", "TF", "HM", "GS", "UM"]
au_nz_subregions = ["AU", "NZ", "NF"]


class TestCountry(TestCase):
    # TODO: How to test methods that extend an external app?
    def test_country_region(self):
        return True

    def test_country_subregion(self):
        return True


class TestRegions(TestCase):
    def test_countries_by_region(self):
        query = regions.countries_by_region("XA")
        self.assertCountEqual(world_regions, query)

    def test_countries_by_subregion(self):
        query = regions.countries_by_subregion("QP")
        self.assertCountEqual(au_nz_subregions, query)

    def test_region_name(self):
        query = regions.region_name("XA")
        self.assertEqual(query, "World")

    def test_subregion_name(self):
        query = regions.subregion_name("QP")
        self.assertEqual(query, "Australia and New Zealand")