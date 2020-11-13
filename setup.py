from distutils.core import setup

setup(
  name = 'TOPSIS_Chahat_101803580', 
  packages = ['TOPSIS_Chahat_101803580'], 
  version = '1.0.0',  
  license='MIT', 
  description = 'Topsis score calculator',
  long_description=open("README.txt").read(),
  author = 'Chahat',               
  author_email = 'cchahat_be18@thapar.edu', 
  url = 'https://github.com/chahat2002/TOPSIS_Chahat_101803580',
  download_url = 'https://github.com/chahat2002/TOPSIS_Chahat_101803580/archive/v_1.0.0.tar.gz', 
  keywords = ['topsis', 'thapar', 'rank', 'topsis score'], 
  install_requires=["pandas"],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers', 
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.7',
  ],
)
