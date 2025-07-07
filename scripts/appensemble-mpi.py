#!/usr/bin/env python
""" 
    A high-level code for running the SYSNet software

    Take a look into the config file under the directory 'scripts'
    to learn about the input parameters.
    
    Mehdi Rezaie, mr095415@ohio.edu
    December 2020
"""
import sysnet

if __name__ == '__main__':
    debug = False
    if debug:
        sysnet.detect_anomaly() # this will slow down

    config = sysnet.parse_cmd_arguments('config.yaml')
    pipeline = sysnet.SYSNetSnapshotMPI(config)
    pipeline.config.scheduler_kwargs.update(T_0=5, T_mult=1)  # FIXME: it does not show up in the log!
    pipeline.run()
