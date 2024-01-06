# Infernal XL LoRA

An Infernal LoRA generation &amp; management project for SDXL!

## Model Extraction

```
python .\scripts\convert_original_stable_diffusion_to_diffusers.py --checkpoint_path .\revAnimated_v122EOL.safetensors --from_safetensors --dump_path revAnimated/ --from_safetensors
```

## References

- https://civitai.com/articles/771/tutorial-konyconi-style-lora-update
- https://medium.com/mlearning-ai/using-civitai-models-with-diffusers-package-45e0c475a67e
- https://www.reddit.com/r/StableDiffusion/comments/118spz6/captioning_datasets_for_training_purposes/
- https://aituts.com/sdxl-lora/

> ### Michael P. Stanich
> I would only use AI images to assist if you already have a dataset
> So for enhancing concepts or expanding the flexibility of the dataset.
> Typically you want to use as many high quality images of your concepts as possible, with good tagging/training method
> Too many AI images will have negative effects since they have added noise and other strange factors we may not notice but the AI will notice as a pattern.

> ### rockerBOO
> SD doesn't support transparency so it will take some other value (like setting the BG to white or black). 

## Image References

### Video Games

- Diablo
- DOOM

## Image Generation

### Negative Prompt

```
embedding:easynegative
```

And on some characters:

```
((((ugly)))), (((duplicate))), ((morbid)), ((mutilated)), [out of frame], extra fingers, mutated hands, ((poorly drawn hands)), ((poorly drawn face)), (((mutation))), (((deformed))), blurry, ((bad anatomy)), (((bad proportions))), ((extra limbs)), cloned face, (((disfigured))), gross proportions, (malformed limbs), ((missing arms)), ((missing legs)), (((extra arms))), (((extra legs))), (fused fingers), (too many fingers), (((long neck)))
```

Everything else was copied from the images on the InfernalAI CivitAI page, except for using `dpmpp_sde_gpu karras` in ComfyUI.

### Sick Prompts

- timepiece
- assault rifle
- armor
- ancient
