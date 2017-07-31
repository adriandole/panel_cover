import configparser
import os
from typing import Union


def config(file: Union[os.path.abspath, str]
           = 'panel_cover_config.ini') -> configparser.ConfigParser:
    cfg = configparser.ConfigParser(interpolation=None)
    if not os.path.isfile(file):
        config_file = open(file, 'w')
        cfg['Files'] = {
            'image directory':
                r'\\elshares.el.nist.gov\netzero\Pics_Automated\NZERTF Arrays',
            'output path': 'data.csv',
            'mask image': 'mask.jpg', 'image name format':
                'Cam226PTZ-NZERTFarrays--%Y-%m-%d--%H-%M-%S.jpg'}
        cfg['Parameters'] = {'start date': '', 'end date': ''}
        cfg.write(config_file)
        config_file.close()
    cfg.read(file)
    return cfg

