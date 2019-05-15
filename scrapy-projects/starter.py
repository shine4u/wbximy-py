# encoding=utf8

import sys
import os
from logging.handlers import RotatingFileHandler
import logging
import importlib

from scrapy.settings import Settings
from scrapy.spiderloader import SpiderLoader
from scrapy.crawler import CrawlerProcess
from scrapy.utils.log import configure_logging


def set_logger(settings):
    configure_logging(install_root_handler=False)
    log_format = '%(asctime)s - %(name)s - %(filename)s:%(lineno)d - %(levelname)s - %(threadName)s - %(message)s'
    log_level = settings['LOG_LEVEL']

    if settings["LOG_DIR"]:
        logging.info(settings["LOG_DIR"])
        logdir = settings['LOG_DIR']
        if not os.path.exists(logdir):
            os.mkdir(logdir)
        logfile = os.path.join(logdir, "crawler.log")
        rotating_file_log = RotatingFileHandler(logfile, maxBytes=1024 * 1024 * 1024, backupCount=5)
        rotating_file_log.setFormatter(logging.Formatter(log_format))
        rotating_file_log.setLevel(log_level)

        logging.root.setLevel(log_level)
        logging.root.addHandler(rotating_file_log)


def load_conf(module_name, env=''):
    conf_path = 'mods.%s.settings' % module_name
    if env:
        conf_path += '_' + env
    module = importlib.import_module(conf_path)
    settings = Settings()
    settings.setmodule(module)
    set_logger(settings)
    return settings


def main(argv):
    module_name = argv[1]
    spider_name = argv[2]
    env = ''
    if len(sys.argv) > 3:
        env = argv[3]
    settings = load_conf(module_name, env)
    spider_loader = SpiderLoader(settings)
    crawler = CrawlerProcess(settings)
    spider = spider_loader.load(spider_name)
    crawler.crawl(spider)
    crawler.start()


if __name__ == '__main__':
    main(sys.argv)
