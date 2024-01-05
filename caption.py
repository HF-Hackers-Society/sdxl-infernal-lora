from glob import glob
import os
from os import path
from shutil import make_archive


data_dir = 'dataset'


for img in glob('{}/*.png'.format(data_dir)):
	# Fix the name given by ComfyUI
	parts = img.split('_')
	i = len(parts)-2
	parts[i] = parts[i].replace('0', '')
	parts = '_'.join(parts)

	if not path.isfile(parts):
		os.rename(img, parts)

	caption_fname = path.splitext(parts)[0] + '.txt'
	caption = []

	for i, part in enumerate(path.basename(img).split('_')):
		if not part:
			break
		caption.append(part)

	caption = ' '.join(caption)

	if not path.isfile(caption_fname):
		with open(caption_fname, 'w') as f:
			f.write(caption)

if not path.isfile('{}.zip'.format(data_dir)):
	make_archive(data_dir, 'zip', data_dir)
