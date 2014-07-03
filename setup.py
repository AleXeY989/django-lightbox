
from setuptools import setup

setup(
    name='django-lightbox',
    version='2.7.1',
    url='http://lokeshdhakar.com/projects/lightbox2/',
    description='Django package for jquery-lightbox: A lightweight customizable lightbox plugin for jQuery',
    author='Lokesh Dhakar',
    maintainer='AleXeY989',
    maintainer_email='alex1chupahin@ya.ru',
    license='MIT License',
    keywords=['django', 'jquery', 'lightbox'],
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
    packages=['django_lightbox'],
    package_data={'django_lightbox': ['static/js/django_lightbox/*.js', 'static/css/django_lightbox/*.css', 'static/img/django_lightbox/*.png']}
)
