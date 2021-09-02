# E21

all:
	@ echo "Doing nothing!"

check:
	@ grep itundervisining L??/* -R || echo "OK, no 'itundervisining'.." $(VERBOSE)
	@ grep "BB-Cou-UUVA-"  L??/* -R || echo "OK, no 'BB-Cou-UUVA-'.."    $(VERBOSE)
	@ grep "blackboard.au.dk" L??/* -R  
	@ #grep "p\." L01/*.ipynb -R
	@ # 2021-08-02| CEF, update to E21 ITMAL.
	@ # https://itundervisning.ase.au.dk/GITMAL/		
# F21
#
#DAV = /mnt/Dav/ITMAL
#DIR = $(DAV)/Fildeling
#TEXDIR=/home/cef/ASE/ITMAL/TeX
#EXCLUDEPAT=--exclude='*~' --exclude='.ipynb*' --exclude='__pycache__'
#VERBOSE=
#
#tree:
#	Etc/MkHtmlFileTree.py
#
#pub: clean
#	@ echo "CP lessons, local.."
#	@ #cp -v -u $(TEXDIR)/lesson01.pdf L01/lesson01.pdf
#	@ #cp -v -u $(TEXDIR)/lesson02.pdf L02
#	@ #cp -v -u $(TEXDIR)/lesson03.pdf L03/
#	@ #cp -v -u $(TEXDIR)/lesson07.pdf L07/
#	@ #cp -v -u $(TEXDIR)/lesson08.pdf L08/
#	@ cp -v -u $(TEXDIR)/lesson09.pdf L09/
#	@ echo "CP lessons, remote.."
#	@ cp -v -u -r L?? $(DIR)
#	@ #echo  cp -v -u -r `ls L??| grep -v ".ipynb" | grep -v "__pychache__"` $(DIR)
#	@ echo "CP libitmal, remote.."
#	@ cp -v -u -r Etc libitmal $(DIR)
#
##update:
##	@ git status
##	@ echo -n "Server itu git pull.." && (ssh itu "cd F20_itmal && git pull") || echo "failed"
##	@ echo "ALL OK"
#
#check:
#	@ grep itundervisining     L??/* -R || echo "OK, no 'itundervisining'.."   $(VERBOSE)
#	@ grep "BB-Cou-UUVA-91831" L??/* -R || echo "OK, no 'BB-Cou-UUVA-91831'.." $(VERBOSE)
#	@#grep "blackboard.au.dk" L??/* -R	
#	@#grep "p\." L01/*.ipynb -R
#
#hasDAV:
#	@ cat /proc/mounts | grep $(DAV) >/dev/null || mount $(DAV) 
#	@# cat /proc/mounts | grep $(DAV) >/dev/null || (echo "ERROR: DAV dir $(DAV) not mounted" && false)	
#
#diff: hasDAV
#	diff -dwqr -x '*~' -x '.git*' -x 'Makefile' -x 'Solutions' -x 'Old' -x 'Src' -x 'datasets' . $(DIR) || echo "DIFFS(1)!"
#	@#diff  $(TEXDIR)/lesson01.pdf L01/lesson01.pdf || echo "DIFFS(2)!"
#	@#diff  $(TEXDIR)/lesson02.pdf L02/lesson02.pdf || echo "DIFFS(3)!"
#	@ echo "OK"
#
#cleanremote: hasDAV
#	@ find $(DIR) -iname '.ipynb_checkpoints' -exec rm -rf {} \; 2>/dev/null || true
#	@ find $(DIR) -iname '__pycache__' -exec rm -rf {} \;        2>/dev/null || true
#	@ find $(DIR) -iname '*~' -exec rm -rf {} \;                 2>/dev/null || true
#
#clean: cleanremote
#	@ find . -iname '.ipynb_checkpoints' -exec rm -rf {} \; || true
#	@ find . -iname '__pycache__' -exec rm -rf {} \; || true
#	@ find . -iname '*~' -exec rm -rf {} \; || true
		