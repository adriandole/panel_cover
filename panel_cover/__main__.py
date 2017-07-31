import os
import argparse
import csv
from datetime import datetime
from skimage.io import imread
from panel_cover.config import config
from panel_cover.algorithm import algorithm
from panel_cover.utils import ProgressBar

parser = argparse.ArgumentParser()
parser.add_argument('-cfg', '--config_file', type=str, dest='cfg',
                    default='panel_cover_config.ini',
                    help='Config file to use')
parser.add_argument('-s', '--start_date', type=str, dest='s',
                    help='Start date of images to process. Format:'
                         'YYYY-MM-DDThh:mm:ss')
parser.add_argument('-e', '--end_date', type=str, dest='e',
                    help='End date of images to process.')
in_args = parser.parse_args()
cfg=config(in_args.cfg)

start_date = datetime.strptime(in_args.s, '%Y-%m-%dT%H:%M:%S')
end_date = datetime.strptime(in_args.e, '%Y-%m-%dT%H:%M:%S')

source_dir = os.path.abspath(cfg['Files']['image directory'])
images = os.listdir(source_dir)

image_dates = []
for image_name in images:
    try:
        image_dates += [datetime.strptime(image_name,
                                          cfg['Files']['image name format'])]
    except:
        continue
image_dates = sorted(filter(lambda x: start_date <= x <= end_date, image_dates))
image_paths = map(lambda x: os.path.join(source_dir, datetime.strftime(x, cfg[
    'Files']['image name format'])), image_dates)

output_file = open(cfg['Files']['output path'], 'w')
writer = csv.writer(output_file, dialect='excel', quoting=csv.QUOTE_ALL)

progress = ProgressBar()
mask = imread(cfg['Files']['mask image'])
total = len(image_dates)
for index, path in enumerate(image_paths):
    progress.update((index+1)/total)
    cover = algorithm(imread(path), mask)
    writer.writerow([image_dates[index], cover])

output_file.close()
