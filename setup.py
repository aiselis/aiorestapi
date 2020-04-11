#
#    Copyright 2019 Alessio Pinna <alessio.pinna@aiselis.com>
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

import os
import re
import sys
import pathlib
from setuptools import setup

if sys.version_info < (3, 6):
    raise RuntimeError("aiorestapi 4.x requires Python 3.6+")


HERE = pathlib.Path(__file__).parent


txt = (HERE / 'aiorestapi' / '__init__.py').read_text('utf-8')
try:
    version = re.findall(r"^__version__ = '([^']+)'\r?$",
                         txt, re.M)[0]
except IndexError:
    raise RuntimeError('Unable to determine version.')


with open(os.path.join(HERE, 'README.md')) as f:
    README = f.read()


setup(
    name='aiorestapi',
    version=version,
    description='Rapid rest resources for aiohttp',
    long_description=README,
    long_description_content_type='text/markdown',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Development Status :: 3 - Alpha',
        'Operating System :: POSIX',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Topic :: Internet :: WWW/HTTP',
        'Framework :: AsyncIO',
    ],
    author='Alessio Pinna',
    author_email='alessio.pinna@aiselis.com',
    maintainer='Alessio Pinna <alessio.pinna@aiselis.com>',
    url='https://github.com/aiselis/aiorestapi',
    project_urls={
        'Bug Reports': 'https://github.com/aiselis/aiorestapi/issues',
        'Source': 'https://github.com/aiselis/aiorestapi',
    },
    license='Apache 2',
    packages=['aiorestapi'],
    python_requires='>=3.6',
    install_requires=[
        'aiohttp'
    ],
    include_package_data=True,
)
