from setuptools import setup

setup(
    name='django-zerorpc-api',
    version='0.1.1dev',
    author='Gabriel Grant',
    packages=['zerorpc_api'],
    license='LGPL',
    long_description=open('README').read(),
    install_requires=[
        'django',
        'zerorpc',
    ],
)
