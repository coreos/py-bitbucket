from setuptools import setup

version = "0.2"
install_requires = ['requests', 'requests-oauthlib']

setup(name='py-bitbucket',
    version=version,
    description="A python client for the BitBucket API V1",
    long_description=open('README.md').read(),
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers"
    ],
    keywords='bitbucket api',
    author='Joseph Schorr',
    author_email='joseph.schorr@coreos.com',
    url='http://github.com/coreos/py-bitbucket',
    license=open('LICENSE').read(),
    packages=['bitbucket'],
    install_requires=install_requires,
)