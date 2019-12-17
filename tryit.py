#!/usr/bin/env python
from __future__ import print_function
from irods.models import DataObject
from irods.models import DataObjectMeta
from irods.models import Resource
from irods.models import ResourceMeta
from datetime import datetime, timedelta
import time

import sys,os
sys.path.insert(0,os.environ['HOME'])
import irodsess
ses = irodsess.main()

now = datetime.utcnow()

age = int(sys.argv[1]) if sys.argv[1:] else 0

cutoff = now - timedelta(seconds = abs(age))


def convert_int():
    try:    i = int( sys.argv[1] )
    except: pass
    return locals().get('i')

def print_cheatsheet():

    print("{r:-^20} {c:-^20} {m:-^20} {n:-^20} {v:-^20}".format(r='resc name',c='create age',m='modify age', n='name', v='value'))
    for x in ses.query(ResourceMeta,Resource):
        resc_name = x[Resource.name]
        t_create =  x[ResourceMeta.create_time]
        t_modify =  x[ResourceMeta.modify_time]
        name =   x[ResourceMeta.name]
        value =  x[ResourceMeta.value]
        c_age =  now - t_create
        m_age =  now - t_modify
        print("{r:>20} {c:>20} {m:>20} {n:>20} {v:>20}".format(
            r = resc_name,
            c = c_age.total_seconds(), 
            m = m_age.total_seconds(), 
            n = name, 
            v = value))


arg = convert_int()

if arg is None:
    print_cheatsheet()
else:
    for x in ses.query(ResourceMeta,Resource).filter (  ResourceMeta.modify_time >= cutoff,
                                                        ResourceMeta.modify_time <  now,
                                                        Resource.name != "" ):
        print( x[Resource.name], "-", x[ResourceMeta.name] )
