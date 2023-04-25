from setuptools import setup

def long_readme():
	with open('README.md', 'r')  as f:
		return f.read() 

def short_readme():
	with open('README.txt', 'r')  as f1:
		return f1.read()
    	
setup(name='vision',
	version='1.0.1',
	description = short_readme(), 
	long_description = long_readme() ,
	url='https://github.com/amiehe-essomba/vision',
	author='Iréné Amiehe-Essomba ',
	keywords = 'mamba cython python c++ c javascript julia ruby R',
	install_requires = [
	'markdown',
	],
	classifier = [
	'Licence :: OSI Approved :: IPCMS Licence',
	'Operating System :: MacOS :: MacOS X',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: POSIX',
	'Program Language :: Python :: version >= 3.8',
	'Topic :: VISION code editor',
	],   
	test_suite = 'nose.collector',
	include_package_data = True, 
	author_email='amieheessomba@etu.unistra.fr',
	license='MIT License',
	packages=['vision'],
	zip_safe=False)