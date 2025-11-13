# Udacity Generative AI Portfolio

A collection of four hands-on projects completed as part of the Udacity Generative AI Nanodegree. Each project tackles a different applied AI challenge, from computer vision to multimodal retrieval, and showcases practical tooling around LLMs, vector databases, and model fine-tuning.

## Projects

### 1. AI Photo Editing & Inpainting (`ai_photo_editing_inpainting`)
- **Goal**: Build an interactive app that performs targeted inpainting and style edits on user-uploaded photos.
- **Highlights**: Streamlit UI, image masking workflow, integration with Stable Diffusion / inpainting checkpoints, reproducible runs saved under `starter/outputs/`.
- **Tech**: Python, Streamlit, diffusers / Stable Diffusion inpainting, Pillow, OpenCV.

### 2. Custom Architecture Framework Chatbot (`custom_architecture_framework_chatbot`)
- **Goal**: Create an LLM-powered assistant that answers questions about a proprietary architecture governance framework using retrieval-augmented generation (RAG).
- **Highlights**: Knowledge base stored in CSV (`data/architecture_framework_knowledge.csv`), embeddings + vector search, LangChain pipeline wired into a Jupyter demo notebook and CLI scripts.
- **Tech**: LangChain, OpenAI GPT via Vocareum, ChromaDB (or FAISS), pandas, Python scripts/notebooks.

### 3. Lightweight Fine-Tuning of a Foundational Model (`lightweight_fine-tuning_foundational_model`)
- **Goal**: Fine-tune DistilBERT for sentiment classification using LoRA/PEFT techniques to keep training lightweight.
- **Highlights**: `LightweightFineTuning.ipynb` walks through dataset prep, LoRA adapter training, evaluation, and saving the adapter under `distilbert-sst2-lora/`.
- **Tech**: Hugging Face Transformers, PEFT/LoRA, PyTorch, datasets, scikit-learn metrics.

### 4. HomeMatch ? Personalized Real Estate Agent (`personalized_real-estate_agent`)
- **Goal**: Generate synthetic listings for Berlin & Tokyo, store them in both text and image vector databases, collect buyer preferences, and deliver GPT-personalized property narratives.
- **Highlights**: Multimodal retrieval (text embeddings + CLIP image embeddings), LangChain personalization, placeholder listing imagery, and a fully executed `HomeMatch.ipynb` notebook.
- **Tech**: LangChain, LangChain-OpenAI, ChromaDB, CLIP (transformers), Sentence Transformers, Pillow, pandas.

## Getting Started
```bash
# create / activate virtualenv of your choice
pip install -r personalized_real-estate_agent/requirements.txt
# repeat per-project requirement files as needed
```

Each project directory contains its own notebook(s), scripts, and READMEs with deeper instructions.

## Notes
- Vocareum-issued OpenAI keys are required for the LangChain/GPT demos. Export `OPENAI_API_KEY` and `OPENAI_API_BASE=https://openai.vocareum.com/v1` before running notebooks.
- Some notebooks save outputs/artifacts in `listings/`, `distilbert-sst2-lora/`, or `starter/outputs/`; use as needed to reproduce results.

Happy building!
