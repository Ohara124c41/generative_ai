# Custom Architecture Framework Chatbot

This project extends Udacity's “Build Your Own Custom Chatbot” assignment with a professional scenario: a retrieval-augmented assistant for enterprise/system architects. The chatbot answers questions about DoDAF, MODAF, NATO NAF, UAF, TOGAF, FEAF, Zachman, NIST CPS AF, and ArchiMate viewpoints using a curated CSV knowledge base.

## Repository Layout

- `project.ipynb` – Primary notebook with scenario description, data wrangling, retrieval/helper functions, and five baseline vs. custom Q&A comparisons.
- `data/architecture_framework_knowledge.csv` – 78-row dataset generated for this project (see `scripts/create_architecture_dataset.py` for provenance).
- `scripts/` – Utility helpers, including the dataset generator and a notebook-updater that can rebuild the evaluation cells.
- `requirements.txt` – Minimal dependency set (`openai`, `pandas`, `python-dotenv`, `ipykernel`) tested on Python 3.10–3.12.

## Setup

1. Create/activate a virtual environment (Conda `base` works too).
2. Install dependencies:
   ```bash
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   ```
3. Launch Jupyter and open `project.ipynb`.
4. Replace `openai.api_key = "YOUR API KEY"` (cell ~105) with your Vocareum key **only while running the notebook**; revert to the placeholder before submission or version control.

## Running the Notebook

Execute the notebook top-to-bottom:

1. Data wrangling cells load and summarize the CSV while creating a `text` column that satisfies the rubric.
2. The retrieval helper builds context windows using keyword scoring; `DEFAULT_TOP_K` can be tuned to trade recall vs. precision.
3. Five evaluation blocks print baseline (no context) and custom (context-grounded) answers plus the snippets that were retrieved, satisfying the requirement for ≥2 Q&A comparisons.
4. The concluding cell documents observed improvements and next steps.

## Offline / Limited-Network Deployment

For a local concurrent engineering team with restricted connectivity, replace the OpenAI API call in `call_completion` with a locally hosted instruction-following model (e.g., a fine-tuned Llama 3 or GPT4All instance). The rest of the pipeline—CSV loading, keyword scoring, prompt construction—runs entirely offline, so swapping the completion function allows the chatbot to operate on isolated networks while retaining the curated knowledge.

## Design Decisions & Value

- **Domain-Specific Dataset:** Instead of the stock Udacity CSVs, the project builds a 78-row architecture glossary validated against official framework specifications. This ensures the model actually needs the custom data to answer accurately.
- **Transparent Retrieval:** A simple keyword scorer keeps the logic easy to inspect and avoids additional dependencies, aligning with the project goal of understanding RAG “under the hood.”
- **Evaluation Coverage:** Five architect-centric questions (capability ownership, edge platform design, HITL governance, AIoT alignment, technical debt) show clear differences between the base model and the grounded responses, demonstrating the value of customization.
- **Extensibility:** `scripts/create_architecture_dataset.py` can regenerate or extend the dataset with additional frameworks, and `scripts/update_project_notebook.py` keeps the notebook structure reproducible.

## Requirements & Submission Notes

- Ensure `requirements.txt` accompanies the submission so reviewers can replicate the environment quickly.
- Before submitting, run the notebook with your API key, capture the outputs, then scrub the key (set back to `"YOUR API KEY"` or load via environment variables).
- The rubric items (“Data Wrangling,” “Custom Query Completion,” “Scenario Explanation,” “Performance Demonstration”) are addressed in the notebook sections noted above; no additional files are required.
