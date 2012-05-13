from setuptools import setup

setup(
    name='django-zerorpc-api',
    version='0.1.2dev',
    author='Gabriel Grant',
    packages=['zerorpc_api', 'zerorpc_api.management.commands'],
    license='LGPL',
    long_description=open('README').read(),
    install_requires=[
        'django',
        'zerorpc-legacy',
    ],
)
