#!/usr/bin/env python
import ROOT
from DataFormats.FWLite import Handle, Events, Runs
import sys

"""
Author: Nick Smith, U. Wisconsin -- Madison
Created: 13/02/2016
With additions by Kenneth Long, U. Wisconsin -- Madison
"""
def getWeightIDs(edm_file_name) :
    if "/store/" in edm_file_name :
        edm_file_name = "/".join(["root://cmsxrootd.fnal.gov/",
            edm_file_name])
    elif not os.path.isfile(edm_file_name) :
        raise FileNotFoundException("File %s was not found." % edm_file_name)
    runs = Runs(edm_file_name)
    runInfoHandle = Handle("LHERunInfoProduct")
    runInfoLabel = "externalLHEProducer"
    run = runs.__iter__().next()
    run.getByLabel(runInfoLabel, runInfoHandle)
    lheStuff = runInfoHandle.product()

    lines = []
    for i, h in enumerate(lheStuff.headers_begin()) :
        if i == lheStuff.headers_size() :
            break
        hlines = []
        isWeights = False
        for line in h.lines() :
            hlines.append(line)
            if 'weightgroup' in line :
                isWeights = True
        if isWeights :
            lines.extend(hlines)
            break
    return ''.join(lines)
