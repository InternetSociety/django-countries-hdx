from unittest import TestCase
from django_countries_regions import regions
from django_countries.fields import Country
from django.conf import settings

settings.configure()


# Test data
world_regions = ["AQ", "BV", "IO", "CX", "CC", "TF", "HM", "GS", "UM"]
au_nz_subregions = ["AU", "NZ", "NF"]


class TestCountry(TestCase):
    def test_country_region(self):
        query = Country("AF").region
        self.assertEqual(query, "XD")

    def test_country_subregion(self):
        query = Country("AF").subregion
        self.assertEqual(query, "XT")


class TestRegions(TestCase):
    def test_countries_by_region(self):
        query = regions.countries_by_region("XA")
        self.assertCountEqual(query, world_regions)

    def test_countries_by_subregion(self):
        query = regions.countries_by_subregion("QP")
        self.assertCountEqual(query, au_nz_subregions)

    def test_region_name(self):
        query = regions.region_name("XA")
        self.assertEqual(query, "World")

    def test_subregion_name(self):
        query = regions.subregion_name("QP")
        self.assertEqual(query, "Australia and New Zealand")
