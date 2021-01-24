import keepclean
from setuptools import setup, find_packages

setup(
	name = 'keepclean',
	packages = find_packages(),
	version = keepclean.__version__,
	python_requires='>=3.6',
	classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Utilities"
    ],
	platforms = 'any',
	zip_safe=True,
    include_package_data = True,
    install_requires=open('requirements.txt').readlines()
)