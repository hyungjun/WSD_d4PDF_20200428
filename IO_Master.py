from numpy import *
import os, sys

def IO_Master(cfg, prj, model, run, res):
    if prj=="JRA55":
        import IO_JRA55
        iom  = IO_JRA55.IO_Jra55(model, run, res)
   
    elif prj=="HAPPI":
        import IO_HAPPI
        iom  = IO_HAPPI.IO_Happi(model, run, res)

    elif prj=="d4PDF":
        import IO_d4PDF
        iom  = IO_d4PDF.IO_d4pdf(cfg, run) 

    else:
        print "check prj, model, run, res="
        print "prj, model, run, res"
        sys.exit()
    return iom


