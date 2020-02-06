# -*- coding: utf-8 -*-

#
# Joe Richards (nospam-github@disconformity.net)
# 2020-01-04
#

from modules import cbpi
import logging
from modules.fermenter import FermenterView

def get_config():
    config = {}
    config['auto_start_fermenter_enabled'] = get_param("auto_start_fermenter_enabled", "YES", "select", "Autostart fermenters on CBPi startup?", ["YES", "NO"])
    config['auto_start_fermenter_list'] = get_param("auto_start_fermenter_list", "1", "text", "Autostart fermenters in this list (comma separated list)")
    return config

def get_param(param_name, default_value, param_type, param_desc, param_opts=None):
    value = cbpi.get_config_parameter(param_name, None)
    if value is None:
        cbpi.add_config_parameter(param_name, default_value, param_type, param_desc, param_opts)
        return default_value
    return value

def log(s):
    print(s)
    cbpi.app.logger.info(s)

@cbpi.initalizer(order=9999)
def init(cbpi):
    log("Auto Starting Fermenters...")
    config = get_config()
    if config['auto_start_fermenter_enabled'] != 'YES':
        log("\tAuto Start not enabled.")
        return

    if 'auto_start_fermenter_list' not in config or len(config['auto_start_fermenter_list'].strip()) == 0:
        log("\tFermenter list is empty. Please set the auto_start_fermenter_list parameter.")
        return

    fermenter_ids = [int(fid.strip()) for fid in config['auto_start_fermenter_list'].split(',')]

    for fid in fermenter_ids:
        fermenter = FermenterView().get_fermenter(fid)
        if not fermenter:
            log("No fermenter id [{}] could be found, skipping.".format(fid))
            continue
        log("Toggling fermenter, Name: {}, CURRENT STATE: {}".format(fermenter.name, fermenter.state))
        FermenterView().toggle(fid)
        log("Toggling fermenter, Name: {}, CURRENT STATE: {}".format(fermenter.name, fermenter.state))
        if fermenter.state == True:
            log("Auto start fermenter [{}], id [{}] success!".format(fermenter.name, fid))
            cbpi.notify("auto_start_fermentation", "Auto start fermenter [{}], id [{}] success!".format(fermenter.name, fid), type="success", timeout=None)
        else:
            log("Auto start fermenter [{}], id [{}] failed!".format(fermenter.name, fid))
            cbpi.notify("auto_start_fermentation", "Auto start fermenter [{}], id [{}] failed!".format(fermenter.name, fid), type="danger", timeout=None)
