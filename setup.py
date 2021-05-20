import setuptools

setuptools.setup(
    name='hyrule-compendium-cli',
    version='3.0.2',
    author='Aarav Borthakur',
    author_email='gadhaguy13@gmail.com',
    description='The official CLI for the Hyrule Compendium API',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/gadhagod/Hyrule-Compendium-CLI',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'pyrule-compendium==2.4.1',
        'click',
        'Pygments',
        'termcolor'
    ],
    scripts=['./bin/compendium'],
    python_requires='>=3.6'
)