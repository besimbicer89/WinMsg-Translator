#!/usr/bin/env python
import json, sys

if len(sys.argv) != 2:
	print "How to use: python2 " + sys.argv[0] + " <wm_hex_id>"
	print "Example: python2 " + sys.argv[0] + " 202"
	print "Output: WM_LBUTTONUP"

wm_list = json.loads(open(sys.argv[0]+"/../wm.json").read())
for wm in wm_list:
	if wm["id_hex"] == sys.argv[1].zfill(4):
		print wm["wm"]
		break