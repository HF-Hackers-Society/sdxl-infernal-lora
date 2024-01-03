import sys
sys.dont_write_bytecode = True

import os
from os import path
import torch
from diffusers import *


def load_torch() -> (str, torch.dtype):
	if torch.cuda.is_available():
		return 'cuda', torch.float16
	else:
		return 'cpu', torch.float32


def main(cache_dir:str = 'data'):
	os.makedirs(cache_dir, exist_ok=True)

	device, dtype = load_torch()
	model_id = path.join(cache_dir, 'revAnimated')

	pipe = StableDiffusionPipeline.from_pretrained(
		model_id,
		torch_dtype=dtype,
		safety_checker=None,
		#feature_extractor=feature_extractor
	).to(device)
	# 20 concepts, 4 images per concept

	pipe.load_lora_weights(path.join(cache_dir, 'InfernalAIv8.safetensors'))

	image = pipe(
		prompt='coffee machine',
		cfg_scale=6.5,
		clip_skip=2,
		num_inference_steps=45
	).images[0]

	image.save('test.png')

if __name__ == '__main__':
	main()
