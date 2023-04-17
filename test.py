import os, sys
import platform
import mainLinux
import mainWin
from configure	  import clear, moveCursor
from pathlib		import Path
from fileType	   import fileType as FT
from fileType	   import readfile as RT


def visionEditor():
	# get root path 
	root	= os.path.abspath(os.curdir)

	# path parent
	s = Path(__file__).resolve().parents[2]
	
	# get system name
	system  = platform.system()
	
	# get arguments 
	arg	 = sys.argv
	
	# coustomized terminal 
	terminal = "monokai"
	
	# 
	writeData = {"data" : [], "FileName" : None, "action" : False}
		
	if system in ['Windows', "Linux", "MacOS"]: 
		if   len(arg) == 1 : 
			termios, language   = "none", "unknown"
			data				= {}
		elif len(arg) == 2 : 
			if arg[1]: 
				ext = FT.file(arg[1])
				if ext is not None : 
					termios, language = terminal, ext
					if system == "Windows" :  name = root + f"\\{arg[1]}"
					else:  name = root + f"/{arg[1]}"
					
					#if os.stat(name) == 0 :  data = RT.readFile(fileName=name, termios=termios, language=language)
					#else:  data = {} 
					
					data					= RT.readFile(fileName=name, termios=termios, language=language)
					writeData["FileName"]   = arg[1]
					writeData["data"]	   = data['string'].copy()
					writeData["action"]	 = True
					
				else: termios, language = "none", "unknown"
			else : termios, language = "none", "unknown"
		elif len(arg) == 3 : pass 
		
		if   system == "Windows"	: mainWin.IDE(termios=termios, lang=language).VISION(importation=data, writeData =  writeData, path = root)
		elif system == "Linux"	  : mainLinux.IDE(termios=termios, lang=language).VISION(importation=data, writeData =  writeData, path = root)
		else: pass 
		
	else: pass
	
	
if __name__ == '__main__':
	sys.stdout.write(clear.clear.screen(2)+moveCursor.cursor.TO(0,0))
	visionEditor()
