# /usr/bin/env python
# _*_ coding:utf-8 _*_
# Author = "Shi Lu"

"""
import logging

logging.basicConfig(filename="app.log", level=logging.WARNING)  # 包含本身的级别信息

logging.debug("debug test")
logging.info("info test")
logging.warning("warning test")
logging.error("error test")
logging.critical("critical test")
"""

import logging

logging.basicConfig(filename="app.log",
                    level=logging.WARNING,
                    format="%(asctime)s %(filename)s : %(lineno)d %(funcName)s - %(levelname)s : %(message)s",
                    datefmt="%m/%d/%Y %I:%M:%S %p")

logging.debug("debug test")
logging.info("info test")
logging.warning("warning test")
logging.error("error test")
logging.critical("critical test")


def app_run():
    logging.warning("the app is beening running for a long time...")

app_run()
