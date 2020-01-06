from setuptools import setup, find_packages

setup(
    name='ming',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click', 'psutil', 'PyYAML', 'paramiko'
    ],
    entry_points='''
        [console_scripts]
        yourscript=yourpackage.scripts.yourscript:cli
    ''',
)
