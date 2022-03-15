from setuptools import setup, find_packages

setup(
    name='Sublist3r',
    version='1.0',
    python_requires='>=2.7',
    install_requires=['os','colorama','termcolor'],
    packages=find_packages()+['.'],
    include_package_data=True,
    url='https://github.com/yogesh-hack/Burnfile_viruse.git',
    license='GPL-2.0',
    description='Subdomains enumeration tool for penetration testers',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Telecommunications Industry',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Security',
    ],
    keywords='subdomain dns detection',
    entry_points={
        'console_scripts': [
            'burnfile_viruse = burnfile_viruse:interactive',
        ],
    },
)
