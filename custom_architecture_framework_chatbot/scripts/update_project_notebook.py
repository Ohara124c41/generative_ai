from pathlib import Path

import nbformat
from nbformat.v4 import new_code_cell, new_markdown_cell


PROJECT_NOTEBOOK = Path("project.ipynb")


def update_notebook() -> None:
    nb = nbformat.read(PROJECT_NOTEBOOK, as_version=4)

    nb.cells[1].source = (
        "I curated a 78-row dataset covering DoDAF 2.02, MODAF 1.2, the NATO Architecture Framework v4, "
        "OMG's Unified Architecture Framework 1.2, TOGAF Standard 10, FEAF 2.3, the Zachman Framework 3.0, "
        "NIST's Cyber-Physical Systems Architecture Framework 1.0, and The Open Group ArchiMate 3.2. "
        "Each record captures the artifact name, version, and a short description that I validated against "
        "the official specifications listed in `scripts/create_architecture_dataset.py`, so the chatbot has accurate "
        "ground truth when reasoning about capability planning or compliance questions."
    )

    nb.cells[2].source = (
        "## Data Wrangling\n\n"
        "The cells below load `data/architecture_framework_knowledge.csv`, ensure the `text` column is clean, "
        "and summarize the mix of frameworks so the dataset can be fed directly into a retrieval workflow."
    )

    nb.cells[3].source = (
        "from pathlib import Path\n\n"
        "import pandas as pd\n\n"
        "DATA_PATH = Path(\"data/architecture_framework_knowledge.csv\")\n\n"
        "knowledge_df = (\n"
        "    pd.read_csv(DATA_PATH)\n"
        "    .dropna(subset=[\"text\"])\n"
        "    .assign(text=lambda df: df[\"text\"].astype(str).str.strip())\n"
        ")\n\n"
        "print(f\"Loaded {len(knowledge_df):,} knowledge rows from {DATA_PATH}\")\n"
        "knowledge_df.head()\n"
    )

    nb.cells[4].source = (
        "framework_summary = (\n"
        "    knowledge_df.groupby(\"framework\")\n"
        "    .agg(\n"
        "        rows=(\"text\", \"count\"),\n"
        "        versions=(\"version\", lambda values: \", \".join(sorted(set(values))))\n"
        "    )\n"
        "    .sort_values(\"rows\", ascending=False)\n"
        ")\n\n"
        "framework_summary\n"
    )

    nb.cells[5].source = (
        "knowledge_df = knowledge_df.assign(\n"
        "    text_lower=knowledge_df[\"text\"].str.lower()\n"
        ")\n\n"
        "knowledge_df.sample(5, random_state=7)[[\"framework\", \"object\", \"version\", \"text\"]]\n"
    )

    nb.cells[6].source = (
        "## Custom Query Completion\n\n"
        "I use a lightweight retrieval-augmented prompt: keywords from the user's question score each row, "
        "the top entries become the context block, and that block is prepended to the OpenAI Completion request. "
        "Comparing this grounded response with a baseline completion (no custom context) shows how much the "
        "architecture knowledge base helps."
    )

    nb.cells[7].source = (
        "import re\n"
        "from textwrap import dedent\n\n"
        "import openai\n\n"
        "# Replace this placeholder with your actual Vocareum/OpenAI API key before running the notebook.\n"
        "openai.api_base = \"https://openai.vocareum.com/v1\"\n"
        "openai.api_key = \"YOUR API KEY\"\n\n"
        "MODEL_NAME = \"gpt-3.5-turbo-instruct\"\n"
        "DEFAULT_TOP_K = 4\n"
    )

    nb.cells[8].source = (
        "def score_text(text, keywords):\n"
        "    lowered = text.lower()\n"
        "    return sum(lowered.count(keyword) for keyword in keywords)\n\n"
        "\n"
        "def build_context(question, top_k=DEFAULT_TOP_K):\n"
        "    tokens = re.findall(r\"[a-z0-9]+\", question.lower())\n"
        "    keywords = {token for token in tokens if token}\n"
        "    if not keywords:\n"
        "        keywords = set(question.lower().split())\n"
        "\n"
        "    scored = (\n"
        "        knowledge_df.assign(\n"
        "            relevance=knowledge_df[\"text_lower\"].apply(lambda txt: score_text(txt, keywords))\n"
        "        )\n"
        "        .sort_values(\"relevance\", ascending=False)\n"
        "    )\n"
        "\n"
        "    if scored[\"relevance\"].max() == 0:\n"
        "        scored = scored.sample(n=min(top_k, len(scored)), random_state=42)\n"
        "    else:\n"
        "        scored = scored.head(top_k)\n"
        "\n"
        "    return \"\\n\\n\".join(scored[\"text\"].tolist())\n"
    )

    nb.cells[9].source = (
        "def call_completion(prompt, temperature=0.2, max_tokens=350):\n"
        "    response = openai.Completion.create(\n"
        "        model=MODEL_NAME,\n"
        "        prompt=prompt,\n"
        "        temperature=temperature,\n"
        "        max_tokens=max_tokens,\n"
        "    )\n"
        "    return response[\"choices\"][0][\"text\"].strip()\n\n"
        "\n"
        "def ask_basic_completion(question):\n"
        "    prompt = dedent(\n"
        "        f\"\"\"\n"
        "        You are a helpful enterprise architecture assistant.\n"
        "        Question: {question}\n"
        "        Answer:\n"
        "        \"\"\"\n"
        "    ).strip()\n"
        "    return call_completion(prompt, temperature=0.4)\n\n"
        "\n"
        "def ask_custom_completion(question, top_k=DEFAULT_TOP_K, context=None):\n"
        "    if context is None:\n"
        "        context = build_context(question, top_k=top_k)\n"
        "\n"
        "    prompt = dedent(\n"
        "        f\"\"\"\n"
        "        You are an enterprise architecture copilot. Use only the provided context to answer the question, and cite the relevant framework names when possible.\n"
        "\n"
        "        Context:\n"
        "        {context}\n"
        "\n"
        "        Question: {question}\n"
        "        Answer:\n"
        "        \"\"\"\n"
        "    ).strip()\n"
        "    return call_completion(prompt, temperature=0.2)\n"
    )

    nb.cells[10].source = (
        "sample_context = build_context(\n"
        "    \"How do capability taxonomies relate to project timelines?\",\n"
        "    top_k=3,\n"
        ")\n"
        "sample_context\n"
    )

    nb.cells[11].source = (
        "def evaluate_question(question, top_k=DEFAULT_TOP_K):\n"
        "    context = build_context(question, top_k=top_k)\n"
        "    return {\n"
        "        \"question\": question,\n"
        "        \"context\": context,\n"
        "        \"basic_answer\": ask_basic_completion(question),\n"
        "        \"custom_answer\": ask_custom_completion(question, top_k=top_k, context=context),\n"
        "    }\n"
    )

    nb.cells[12].source = (
        "## Custom Performance Demonstration\n\n"
        "The next sections ask multiple enterprise-architecture questions. Each captures the baseline completion (no context) "
        "and the grounded completion (with the curated knowledge base) so it is easy to see the improvement."
    )

    question_texts = [
        "How do DoDAF CV-2 and CV-5 differ when aligning capability gaps with responsible organizations?",
        "What guidance do TOGAF ADM Phase D, the NIST CPS AF Physical Viewpoint, and the ArchiMate Technology Layer provide when designing an edge sensor platform?",
        "How can human-in-the-loop governance be maintained when mapping MODAF OpV-5 activities to UAF Projects Viewpoint milestones while addressing NIST CPS AF Crosscutting Concerns for safety-critical missions?",
        "Which architecture viewpoints best align AIoT edge analytics with enterprise services, and how do the NIST CPS AF Functional Viewpoint, TOGAF ADM Phase C, and the ArchiMate Application Layer complement one another?",
        "Where should technical-debt remediation be captured when combining the TOGAF Architecture Requirements Specification, the ArchiMate Implementation & Migration Layer, and Zachman Row 5 component assemblies?",
    ]

    tail_cells = []
    for idx, question_text in enumerate(question_texts, start=1):
        question_literal = repr(question_text)
        question_var = f"question_{idx}"
        answers_var = f"answers_q{idx}"

        tail_cells.append(
            new_markdown_cell(f"### Question {idx}\n\nQuestion: {question_text}")
        )

        tail_cells.append(
            new_code_cell(
                f"{question_var} = {question_literal}\n"
                f"{answers_var} = evaluate_question({question_var})\n\n"
                f"print({question_var})\n"
                "print(\"\\n--- Basic completion ---\\n\")\n"
                f"print({answers_var}[\"basic_answer\"])\n"
                "print(\"\\n--- Custom completion ---\\n\")\n"
                f"print({answers_var}[\"custom_answer\"])\n"
            )
        )

        tail_cells.append(new_code_cell(f"{answers_var}[\"context\"]\n"))

    nb.cells = nb.cells[:13] + tail_cells

    nbformat.write(nb, PROJECT_NOTEBOOK)
    print("Updated project.ipynb with architecture chatbot content.")


if __name__ == "__main__":
    update_notebook()
