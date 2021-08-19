#!/usr/bin/env python3

from Utils.dbg import ERR, WARN, DiagStdErr, PrettyPrintTracebackDiagnostics

from sys import stdout, stderr
from html import escape, unescape
from urllib.parse import quote

def Str(t, checknonempty=True):
	assert isinstance(t, str),  f"exected string but got type='{type(t)}'"
	assert (not checknonempty) or (len(t)>0), f"string is empty, and this was unexpected"
	return t

def Bool(t):
	assert isinstance(t, bool), f"exected bool but got type='{type(t)}'"
	return t

def Int(t, minval=0):
	assert isinstance(t, int), f"exected int but got type='{type(t)}'"
	assert t>=minval
	return t
	
def List(t):
	assert isinstance(t, list), f"exected list but got type='{type(t)}'"
	return t

def Dict(t):
	assert isinstance(t, dict), f"exected dict but got type='{type(t)}'"
	return t

def Tuple(t, expectedlen=2):
	assert isinstance(t, tuple),f"exected tuple but got type='{type(t)}'"
	assert len(t)==Int(expectedlen, 1)
	return t

def Check(expr, msg):
	Str(msg)
	if not Bool(expr):
		ERR("EXPRESSION NOT FULLFILLED: " + msg)
		return False
	return True

def Trim(s, checknonempty=True):
	s = Str(s, Bool(checknonempty)).replace("\t"," ")
	s = s.strip()
	return s

def SuffixFrom(s, splitstr):
	n = Str(s).rfind(Str(splitstr))
	if n<0: 
		ERR(f"string '{s}' does not contain split string '{splitstr}' at all")
	return s[n+len(splitstr):]

def Dbg(verbose, msg, level=1):
	Str(msg)
	if Int(level) <= Int(verbose):
		print(msg, file=stderr)
		
def Warn(msg):
	WARN(msg)

def Outputfile(outputfile):
	assert outputfile is not None
	outputfile = Str(outputfile).replace(" ", "_")	
	f = stdout if (outputfile is None or len(outputfile)==0 or outputfile=="None") else open(outputfile, 'w')
	return f

def LoadText(filename, timeout=4000, split=True):
	#if preprocess:
	#	import subprocess
	#	output = call(["g++","-E", filename])
	#	return output
		
	with open(Str(filename), 'r', timeout) as f:
		c = f.read()
		if split:
			c = c.split("\n")		
		return c

def HtmlEncode(s): 
	# for text in html page
	t=escape(Str(s, False))
	#assert t==escape(t)
	return t

def HtmlDecode(s):
	t=unescape(Str(s, False))
	assert t==unescape(t)
	return t

def UrlQuote(s): 
	# for file names in urls
	t = quote(Str(s, False), safe='')
	#assert t==quote(t, safe='')
	assert t.find("'") < 0
	assert t.find('"') < 0
	assert t.find(" ") < 0
	return t

def MkHtmlPage(htmlcontent):
	assert Str(htmlcontent).find("DOCTYPE")<0 and htmlcontent.find("<html>")<=0 and htmlcontent.find("<body>")<=0	
	meta      = "<meta http-equiv='Content-Type' content='text/html; charset=utf-8'/>\n"
	meta 	 += "<meta http-equiv='Cache-Control' content='no-cache, no-store, must-revalidate' />\n"
	meta     += "<meta http-equiv='Pragma' content='no-cache' />\n"
	meta     += "<meta http-equiv='Expires' content='0' />"
	comment   = "<!-- AUTOGENERATED HTML from CourseBuilder, CEF -->"
	bodystyle = "style='font-family: times new roman, times, serif;font-size: 12pt;color: #000000;'" # org BS "style='font-family: Verdana;font-size: 12pt;color: #494c4e;'"	
	return f"<!DOCTYPE html>\n<html>\n{comment}\n{meta}\n<body {bodystyle}>\n" + htmlcontent + "\n</body>\n</html>"  

def HandleException(ex):
	try:
		assert isinstance(ex, Exception)
		DiagStdErr(stderr)
		PrettyPrintTracebackDiagnostics(ex)
	except:
		print(f"EXCEPTION: {ex} (and exception in exceptions handling)")
		
	exit(-1)