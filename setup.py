from setuptools import setup

setup(
    name="Mem",
    version="1.0",
    py_modules=['mem'],
    install_requires=[
        'Mem',
    ],
    entry_points='''
        [console_scripts]
        mem=mem:cli
    '''
)
