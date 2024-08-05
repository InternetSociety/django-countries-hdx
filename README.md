# django-countries-regions

Adds region and subregion data to django-countries.

## Installation

Install this library using `pip`:
```bash
pip install django-countries-regions
```
## Usage

This is a simple module that extends [django-countries](https://pypi.org/project/django-countries/) to add region and sub-region data (as defined by the [UN M49 Standard](https://en.wikipedia.org/wiki/UN_M49)).

It also contains helper methods to retrieve the countries in a region or sub-region, and get a region or sub-region's name.


```shell
In [1]: from django_countries.fields import Country
In [2]: from django_countries_regions import regions

In [3]: Country("NZ").region
Out[3]: '009'

In [4]: Country("NZ").subregion
Out[4]: '053'

In [5]: regions.region_name("009")
Out[5]: 'Oceania'

In [6]: regions.subregion_name("053")
Out[6]: 'Australia and New Zealand'

In [7]: regions.countries_by_region("009")
Out[7]:
['AS','AU',
 'CK',
# …
]

In [8]: regions.countries_by_subregion("053")
Out[8]: ['AU', 'NZ', 'NF']
```


## Development

To contribute to this library, first checkout the code. Then create a new virtual environment:
```bash
cd django-countries-regions
python -m venv venv
source venv/bin/activate
```
Now install the test dependencies:
```bash
pip install -e '.[test]'
```
To run the tests:
```bash
pytest
```
