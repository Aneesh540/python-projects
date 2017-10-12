""" 
os.getcwd()      --> 	give current working directory

os.path.join()   -->    takes multiple argument and 
					    makes a path accn'ng to operating sys.

os.makedirs()    -->    makedirs() is more efficient then makedir()
						bcoz it can create multiple folders

os.listdir()     -->    list of all folders and file in 
						(my laptop Desktop @ that time)
				i.e. ['gdk', 'mypro', 'location.png', '.idea', 'my_app']
 						

SKIPPED : Handling absolute and relative path on page 177 of book
automate the boring stuff 
"""
import os

print(os.getcwd())

os.chdir(os.path.join('/home/ldrago','Desktop'))

cwd=os.getcwd()
print('current working directory is: %s \n' %cwd)

print(os.listdir(cwd))


def makeNewDirectory():

	name = input('enter name of directory or press enter to skip:')

	location = os.path.join(os.getcwd(),name)

	if name is not '':
		
		try:
			os.makedirs(location)
			print('making file at location :',location)


		except:
			print("file already exist at that location")	


class FilePath:
	"""File path, directory name, basename,split-full-path"""

	def __init__(self,current_wd):
		self.cwd=current_wd

	def split(self):
		print(os.path.split(self.cwd))

	def dirname(self):
		"""name of directory/folder in which file is present"""
		print(os.path.dirname(self.cwd))

	def basename(self):
		print(os.path.basename(self.cwd))

	def full_split(self):
		"""split fill path in linux and mac start with ['',..] """
		print(self.cwd.split(os.path.sep))	
		# print('root/home/ldrago/aneesh/bar'.split(os.path.sep))


if __name__ == '__main__':
	

	makeNewDirectory()
	print('\n')

	one=FilePath(cwd)
	one.full_split()
	one.split()
	one.dirname()
	one.basename()
