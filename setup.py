from setuptools import setup

setup(
	name = 'hasher'
	version = '0.1.0'
	packages = ['pycli']
	entry_points = {
		'console_scripts': [
			'hasher = hasher.__main__:main'
		]
	})

