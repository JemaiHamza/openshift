from setuptools import setup

setup(name='openerpapp', version='1.0',
      description='OpenERP Python-2.7 Community Cartridge based application',
      author='jha', author_email='jha@pcsol.tn',
      url='http://www.python.org/sigs/distutils-sig/',

      #  Uncomment one or more lines below in the install_requires section
      #  for the specific client drivers/modules your application needs.
      install_requires=['greenlet', 'postgresql-9.2',
                        #  'MySQL-python',
                        #  'pymongo',
                        #  'psycopg2',
      ],
     )
