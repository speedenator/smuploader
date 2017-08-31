from setuptools import setup

setup(name='smuploader',
      version='0.3',
      description='A SmugMug uploader and downloader. Uses SmugMug API v2.0',
      url='http://github.com/speedenator/smuploader',
      author='Marek Rei. Packaged by Erik Selberg',
      author_email='erik@selberg.org',
      license='MIT',
      packages=['smuploader'],
      scripts=['bin/smuploader', 'bin/smdownloader', 'bin/smregister', 'bin/smregtest'],
      zip_safe=False)