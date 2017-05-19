from setuptools import setup

setup(
    name="mem",
    version="1.0",
    py_modules=['mem'],
    install_requires=[
        'mem',
    ],
    entry_points='''
        [console_scripts]
        mem=mem:cli
    '''
)
