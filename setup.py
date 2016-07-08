from setuptools import setup

setup(
    name="Memt",
    version="1.0",
    py_modules=['memt'],
    install_requires=[
        'Memt',
    ],
    entry_points='''
        [console_scripts]
        memt=memt:cli
    '''
)
