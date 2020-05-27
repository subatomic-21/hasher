from setuptools import setup


setup(
	name='hasher',
	version='0.1.0',
	py_modules=[],
	packages=['hasher'],
	install_requires=[
		'click', 'colorama', 'hashlib', 'pyfiglet'
	],
	entry_points='''
		[console_scripts]
		hasher=hasher:main

	''',

	)
