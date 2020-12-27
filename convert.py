#!/usr/bin/env python3
# -*- coding: utf-8 -*
# 
# S11, S12, S21, S22を含んだs2pファイルを作成する
# 2020 @tommie_nico
#
# Usage:
#
# python3 convert.py file1.s2p file2.s2p >file2.s2p
#
# or
#
# ./convert.py file1.s2p file2.s2p >file2.s2p
#
import sys
if len(sys.argv) != 3:
	print( "usage: python3 convert.py file1.s2p file2.s2p >file2.s2p")
	sys.exit()

ld1 = open(sys.argv[1])
ld2 = open(sys.argv[2])

while True:
	line1 = ld1.readline()
	if not line1:
		break
	word1 = line1.strip().split()

	line2 = ld2.readline()
	if not line2:
		break
	word2 = line2.strip().split()
	if word1[0].startswith("#"):
		print( line1[:-1])
	elif len(word1) >= 5 and len(word2) >= 9:
		#print( "line1="+line1)
		#print( "line2="+line2)
		print(  word1[0]+" "+word1[1]+" "+word1[2]+" "+word1[3]+" "+word1[4]
			        +" "+word2[3]+" "+word2[4]+" "+word2[1]+" "+word2[2])

ld1.close()
ld2.close()

