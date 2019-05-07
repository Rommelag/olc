from itertools import chain, compress
import re
from pkg_resources import get_distribution


def get_pkg_licenses(pkg):
    distribution = get_distribution(pkg)
    try:
        lines = distribution.get_metadata_lines('METADATA')
    except:
        lines = distribution.get_metadata_lines('PKG-INFO')
    lines = list(lines)
    licenses = _filter(lines, 'License:') + _filter(lines, 'Classifier: License')
    return licenses


def _filter(lines, prefix):
    results = []
    for line in lines:
        match = re.search(r'{} (.*)'.format(prefix), line)
        if match:
            results.append(match.group(1))
    return results
