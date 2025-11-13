# HomeMatch · Multimodal Real Estate Personalization

Future Homes Realty’s **HomeMatch** blends synthetic listing generation, vector search, and GPT-powered personalization to help high-tech buyers find Berlin and Tokyo properties that fit their lifestyle. The workflow lives in `HomeMatch.ipynb` (with `HomeMatch.py` as a starter script) and demonstrates the full rubric requirements from the Udacity project brief.

## Features
- **Synthetic listings**: 12 GPT-authored entries covering Berlin innovation corridors and Tokyo bay districts (`listings/listings.json`).
- **Image placeholders**: Gradient PNGs per listing, rendered locally and embedded into the CLIP pipeline (`listings/images/`).
- **Dual vector indexes**  
  - Text embeddings via `HuggingFaceEmbeddings` stored in Chroma (`listings/vectorstores/text-chroma/`).  
  - Image embeddings via CLIP (`ImageVectorIndex`) for multimodal search (`listings/vectorstores/image-chroma/`).
- **Preference capture**: `PreferenceSurvey` encodes a “Neo-Urban Researcher” persona centered on transit, culture, and maker amenities.
- **Multimodal retrieval**: Combines semantic similarity with CLIP image scores for ranked recommendations.
- **Personalized narratives**: LangChain `ChatOpenAI` rewrites top listings so they highlight the buyer’s transit, culture, and tech priorities.

## Project Structure
```
personalized_real-estate_agent/
├── HomeMatch.ipynb          # Primary notebook (executed with outputs)
├── HomeMatch.py             # Optional starter script
├── listings/
│   ├── listings.json        # Cached GPT-generated listings (12 entries)
│   ├── images/              # Placeholder PNGs used by CLIP
│   └── vectorstores/        # Persisted Chroma + CLIP indices
├── requirements.txt         # Environment specification
└── README.md                # This document
```

## Environment
- Python 3.12+ (Jupyter kernel uses `.venv`)
- Key packages: `langchain`, `langchain-openai`, `langchain-community`, `chromadb`, `sentence-transformers`, `transformers`, `pillow`, `numpy`, `pandas`.

Install everything:
```bash
pip install -r requirements.txt
```

## OpenAI / Vocareum Setup
HomeMatch relies on Vocareum-routed API keys. Before launching Jupyter (or running `HomeMatch.py`), export:
```bash
export OPENAI_API_KEY="voc-…"
export OPENAI_API_BASE="https://openai.vocareum.com/v1"
```
On Windows PowerShell:
```powershell
$env:OPENAI_API_KEY = "voc-…"
$env:OPENAI_API_BASE = "https://openai.vocareum.com/v1"
```
The notebook currently contains a temporary hard-coded key block for testing—remove it before sharing and rely on environment variables instead.

## Running the Notebook
1. Open `HomeMatch.ipynb`.
2. Ensure `REGENERATE_LISTINGS = False` unless you intentionally want to overwrite `listings.json`. If you do regenerate:
   - Set it to `True`.
   - Run the listing generation cell (it auto-retries parsing errors).
   - Set it back to `False` for later runs/grading.
3. Execute all cells (or use `python -m nbconvert --to notebook --execute --inplace HomeMatch.ipynb` to confirm reproducibility).
4. Inspect outputs:
   - Preview table of listings.
   - Multimodal ranking dataframe and image previews.
   - Personalized narratives referencing buyer preferences.

## Regenerating Assets
- **Listings**: Flip `REGENERATE_LISTINGS = True` and re-run the generation cell. The fallback images will be recreated automatically.
- **Vector stores**: Re-running the “Run the complete HomeMatch pipeline” section rebuilds both text and image indexes. The code automatically switches to UUID-suffixed directories if Windows file locks prevent deletion.

## Verification Checklist
- ≥10 synthetic listings exist in `listings/listings.json`.
- Vector-store directories contain the latest Chroma data.
- Notebook outputs show:
  - Survey answers.
  - Ranking table with text/image scores.
  - Image previews.
  - GPT-personalized narratives.

## Optional Enhancements
- Swap placeholder PNGs with real imagery or DALL·E renders.
- Extend `PreferenceSurvey` with interactive widgets for multiple personas.
- Deploy the core logic (`HomeMatch.py`) as a Streamlit or FastAPI app.

Enjoy matching buyers to their perfect cyberpunk-meets-green sanctuary!
