from setuptools import setup, find_packages


setup(
    name='myqr',
    version='0.1',
    install_requires=[
        'imageio',
        'numpy',
        'Pillow',
    ],
    entry_points='''
        [console_scripts]
        myqr=myqr.cli
    ''',
    packages=find_packages(),
)