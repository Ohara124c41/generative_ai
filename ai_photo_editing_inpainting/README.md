# AI Photo Editing Inpainting

An interactive Gradio app and companion notebook for experimenting with SAM-based segmentation and SDXL inpainting. Users can upload an image, click on the subject to generate a mask via the Segment Anything Model, and then describe new backgrounds/subjects that are generated with a Stable Diffusion XL inpainting pipeline. The notebook walks through each step (SAM, mask visualization, inpainting, interactive UI) and stores the latest app results for easy review.

---

## Project Structure

```
ai_photo_editing_inpainting/
├── starter/
│   ├── app.py               # Gradio UI using the notebook helpers
│   ├── starter.ipynb        # Guided project notebook with SAM + SDXL sections
│   ├── car.png / *.jpeg     # Sample assets for quick experimentation
│   └── .gradio/             # Runtime artifacts created by Gradio
├── README.md                # (this file)
├── LICENSE.txt
└── CODEOWNERS
```

All development happens inside `starter/starter.ipynb`. The notebook produces helper functions consumed by `app.py`, so the order of execution matters (run the notebook before launching the app).

---

## Environment & Dependencies

The project targets the Udacity-provided “base” conda env (Python 3.11.4) with GPU access. Required libraries:

- `torch` 2.6.0+cu124, `torchvision`, `torchaudio`
- `transformers` ≥ 4.57 (for `SamModel`/`SamProcessor`)
- `diffusers` ≥ 0.35 with `accelerate`, `safetensors`
- `gradio` 5.x, `anyio` 3.7.x
- `Pillow`, `numpy`, `pandas` 2.x (for smoother Gradio analytics)

If you are recreating the environment manually:

```bash
conda create -n ai-inpaint python=3.11
conda activate ai-inpaint
pip install torch==2.6.0+cu124 torchvision==0.21.0+cu124 torchaudio==2.6.0+cu124 --index-url https://download.pytorch.org/whl/cu124
pip install transformers diffusers accelerate safetensors gradio pandas
```

> **GPU note:** Both SAM and SDXL inpainting use several GB of VRAM. Close unused GPU apps, and call `torch.cuda.empty_cache()` between long runs if you’re tight on memory.

---

## Running the Notebook

1. **Launch Jupyter Lab/Notebook** in `ai_photo_editing_inpainting/starter`.
2. **Run each section in order:**
   - Imports and device checks.
   - SAM model/processor loading (`facebook/sam-vit-base` on CUDA).
   - `get_processed_inputs` mask helper and visualization cell (should show the car mask overlay).
   - SDXL inpainting pipeline setup (`diffusers/stable-diffusion-xl-1.0-inpainting-0.1`).
   - Cached inpaint cell (creates `outputs/car_mars.png` on first run, reuses it afterwards).
3. **Interactive App cells** (last section):
   - `import app` and optional `importlib.reload(app)` when editing.
   - `my_app = app.generate_app(get_processed_inputs, inpaint)` launches Gradio without blocking.
   - Use the Gradio UI (local or public URL), then call `my_app.close()` when finished.
4. **Latest result viewer**: rerun the “Latest Gradio result” cell to display the cached PNG and metadata saved under `outputs/app_runs`.

> The notebook now caches heavy operations:
> - The SDXL inpaint example writes to `outputs/car_mars.png`.
> - Each Gradio run stores `outputs/app_runs/latest.png` plus a JSON metadata summary.

---

## Using the Gradio App

1. Upload or drag/drop an input image (non-square images get padded to 512×512).
2. Click on the subject multiple times until the SAM mask looks good (green background, white subject).
3. Provide a prompt (and optional negative prompt), CFG scale, random seed, and whether to invert the mask.
4. Click **Run inpaint** and wait for the SDXL pipeline to finish (1–3 minutes on a 6 GB GPU).
5. Download the result, or rerun with new ideas. Reset clears the image, mask, prompts, checkbox, and stored points.


---

## Testing & Verification

There are no automated tests because the core of the project is interactive. Verification is manual:

- **SAM section**: run the mask visualization cell and confirm the rendered 128×128 RGBA preview matches the rubric (white subject, green background).
- **Inpainting section**: run the cached SDXL cell once; the follow-up `make_image_grid` cell must show the 3-panel comparison.
- **Interactive App**: launch Gradio, segment the sample car, and generate at least one background swap. The notebook’s “Latest Gradio result” cell must display the saved output/metadata for submission evidence.

If an output cell is missing (e.g., due to kernel restart), rerun the relevant section so the notebook contains the required visual evidence.

---

## Tips & Troubleshooting

- **CUDA OOM**: restart the kernel, run `torch.cuda.empty_cache()`, enable `pipeline.enable_vae_slicing()` and `pipeline.enable_sequential_cpu_offload()` if needed, or temporarily keep SAM on CPU.
- **Gradio queue TypeError (`infer_objects copy`)**: upgrade `pandas` to ≥2.1 to silence the analytics warning.
- **App never returns**: we launch with `prevent_thread_lock=True`, so the notebook cell finishes. Always call `my_app.close()` before shutting down the kernel.
- **Result syncing**: the notebook viewer only shows what’s stored in `outputs/app_runs`. If the image looks stale, refresh that cell after your latest Gradio run.

Enjoy swapping backgrounds, replacing subjects, and experimenting with prompts/CFG scales! Include screenshots from the Gradio runs (or the cached notebook cell) when you submit to satisfy the rubric’s “Interactive App” requirement.
