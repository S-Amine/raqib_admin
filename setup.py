from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in raqib_admin/__init__.py
from raqib_admin import __version__ as version

setup(
	name="raqib_admin",
	version=version,
	description="Raqib App administration",
	author="saidi.amine.p@gmail.com",
	author_email="saidi.amine.p@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
