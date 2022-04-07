#
# Copyright (c) 2021 Airbyte, Inc., all rights reserved.
#


from setuptools import find_packages, setup

MAIN_REQUIREMENTS = [
    "airbyte-cdk~=0.1",
    "smart-open==5.2.*",
    "pyarrow==7.0.*",
    "wcmatch==8.2",
    "dill==0.3.4",
    "pytz",
]

TEST_REQUIREMENTS = [
    "pytest~=6.1",
    "pandas==1.3.1",
    "psutil",
    "pytest-order",
    "netifaces~=0.11.0",
    "docker",
]

setup(
    name="source_files_abstract",
    description="Source implementation for Files Abstract.",
    author="Airbyte",
    author_email="contact@airbyte.io",
    packages=find_packages(),
    install_requires=MAIN_REQUIREMENTS,
    package_data={"": ["*.json"]},
    extras_require={
        "tests": TEST_REQUIREMENTS,
    },
)
