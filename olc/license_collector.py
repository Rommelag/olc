# pylint: disable=line-too-long
"""Detect Open Source Licenses in multiple eco systems (i.e. operating systems, programming languages)"""
import os
import subprocess


class LicenseCollector():
    """Collect Licenses"""

    def __init__(self, component_name):
        self.component_name = component_name

    def get_licenses_debian(self):
        """See https://www.debian.org/doc/packaging-manuals/copyright-format/1.0/ """
        print('Collecting Debian licenses..')
        licenses = {
            'component': self.component_name,
            'eco-system': 'debian',
            'licenses': []
        }
        doc_path = '/usr/share/doc'
        for package in next(os.walk(doc_path))[1]:
            copyright_path = "{}/{}/copyright".format(doc_path, package)
            if os.path.isfile(copyright_path):
                with open(copyright_path, "r", encoding="utf-8") as file:
                    data = file.read()
                licenses['licenses'].append({'name': package, 'license_text': data})
        return licenses

    def get_licenses_alpine(self):
        """Alpine"""
        print('Collecting Alpine licenses..')
        licenses = {
            'component': self.component_name,
            'eco-system': 'alpine',
            'licenses': []
        }
        output = subprocess.check_output(['apk', 'info'], encoding="utf-8")
        for package in output.splitlines():
            lic_output = subprocess.check_output(['apk', 'info', '-e', '--license', package], encoding="utf-8")
            lic_output = lic_output.strip().splitlines()
            # Make sure we fail if apk output doesn't conform to our interpretation
            assert len(lic_output) <= 2
            if len(lic_output) < 2:
                print("Alpine: No license found for package {}, skipping.".format(package))
                continue
            license = lic_output[1].strip().split(" ")
            licenses['licenses'].append({'name': package, 'license_names': license})
        return licenses

    def get_licenses_python(self):
        """Python"""
        pass
        # Looks like this isn't so easy - you can read "License" from 'PKG-INFO' or rip off
        # https://github.com/raimon49/pip-licenses/blob/master/piplicenses.py
        # But the license texts themselves aren't always part of the python package,
        # and License name is not SPDX compatible (e.g 'GPL', 'LGPL')

    def get_licenses_node(self):
        """ Javacript """
        pass
        # via https://stackoverflow.com/questions/16274841/output-all-licenses-of-installed-node-js-libraries
        # cd {project}/node_modules
        # ls | sed 's/$/\/package.json/' | xargs grep '"license[s]*"' -A 3
