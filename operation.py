import subprocess
import logging
import logging.config

logging.config.fileConfig('logging.conf')

def exec_command(command):
    try:
        logging.info("[START] execute " + command)
        p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        out, err = p.communicate()

        if out is not None:
            logging.info("stdout : " + out)
        if err is not None or p.returncode != 0:
            raise Exception(err)
        logging.info("[FINISH] execute " + command)
        return p.returncode
    except:
        logging.error("[FAIL] execute " + command, exc_info=True)
        raise


def deploy_file(path, **kwargs):
    try:
        for key in kwargs.keys():
            value = kwargs[key]

    except:
        logging.error("[FAIL] deploy file :" + path, exc_info=True)
        raise


def edit_file(path, **kwargs):
    with open(path) as f:
        lines = f.readlines()

    with open(path, "w") as f:
        for line in lines:
            line.trip


def get_pattern(path):
    if path in ["ifcfg-eth", "network"]:
        return {"pattern": "kv", "separator": "="}
    elif path in ["route-eth"]:
        return {"pattern": "route", "separator": " via "}


