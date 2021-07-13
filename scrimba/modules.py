# common modules to import: datetime, random, string, os, math, browser
# https://docs.python.org/3/py-modindex.html

#dir command prints all of the methods the module can use
import platform
print(platform.python_version())

#can import and change as an alias. after the alias is created you cannot use the previous name. 
#in this example 'pl' must be used moving forward
import platform as pl

#rather than typing platform out the new alias is pl
print(pl.python_version())

#if you are using one module method then you can use that as well

from platform import python_version, system
print(python_version(), system())

#can alias the imported module here as well

from platform import python_version as pv
print(pv())