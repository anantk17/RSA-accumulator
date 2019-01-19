from setuptools import setup

setup(name='rsa-accumulator',
      version='0.1',
      description='Cryptographic dynamic accumulators based on strong RSA assumption',
      url='https://github.com/oleiba/RSA-accumulator',
      author='Oded Leiba',
      author_email='odedlei@post.bgu.ac.il',
      license='MIT',
      packages=['rsa-accumulator'],
      install_requires=[
            'matplotlib',
            'secrets',
            'hippiehug',
            'merkletools'
      ],
      zip_safe=False)
