from distutils.core import setup

setup(
    name='pitop',
    version='1.0',
    url='https://github.com/maximumG/pitop',
    download_url='https://github.com/maximumG/pitop/archive/master.zip',
    license='Apache Version 2.0',
    author='maximumG',
    author_email='',
    description='Itop REST API interaction',
    keywords=['Itop', 'REST', 'API'],
    requires='requests',
    py_modules=['pitop']
)
