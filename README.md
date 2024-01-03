# Infernal LoRA
An Infernal LoRA generation &amp; management project!

## Model Extraction

```
python .\scripts\convert_original_stable_diffusion_to_diffusers.py --checkpoint_path .\revAnimated_v122EOL.safetensors --from_safetensors --dump_path revAnimated/ --from_safetensors
```

## References

- https://civitai.com/articles/771/tutorial-konyconi-style-lora-update
- https://medium.com/mlearning-ai/using-civitai-models-with-diffusers-package-45e0c475a67e

## Image Generation

### Negative Prompt

```
embedding:easynegative
```

And on some characters:

```
((((ugly)))), (((duplicate))), ((morbid)), ((mutilated)), [out of frame], extra fingers, mutated hands, ((poorly drawn hands)), ((poorly drawn face)), (((mutation))), (((deformed))), blurry, ((bad anatomy)), (((bad proportions))), ((extra limbs)), cloned face, (((disfigured))), gross proportions, (malformed limbs), ((missing arms)), ((missing legs)), (((extra arms))), (((extra legs))), (fused fingers), (too many fingers), (((long neck)))
```

Everything else was copied from the images on the CivitAI page, except for using `dpmpp_sde_gpu karras` in ComfyUI.

### Sick Prompts

- timepiece
- assault rifle
- armor
- ancient
