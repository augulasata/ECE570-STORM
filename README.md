# ECE570-STORM

## STORM Extension: Fact-Checked Article Generation

This repository extends the original STORM framework with claim verification, semantic trust scoring, and source filtering. It enhances article generation by using only verified, trustworthy information.

## What You’ll Get

- Semantic similarity + trust score-based claim verification  
- Automatic `fact_check_log.json` export after each run  
- Filtered article output using only sources with `trust_score >= 0.5`  
- Seamless integration with STORM’s research → outline → article pipeline  

## Prerequisites

### API Keys Required

You must provide API access to:

- OpenAI API Key: For GPT-4o model inference  
- Bing, Brave, Tavily, or Serper API Key: For real-time search results  

**Cost Warning**: You will likely need to spend at least $5 USD on GPT-4o usage.

## Step 1: Clone STORM Codebase

```bash
git clone https://github.com/stanfordnlp/storm.git
cd storm
```

## Step 2: Setup Python Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install sentence-transformers
```

## Step 3: Set Your API Keys

Use shell environment variables:

```bash
export OPENAI_API_KEY="your-openai-key"
export OPENAI_API_TYPE="openai"
export BING_SEARCH_API_KEY="your-bing-key"
```

Or if using alternatives:

```bash
export BRAVE_API_KEY="..."
export SERPER_API_KEY="..."
export TAVILY_API_KEY="..."
```

## Step 4: Add or Replace These Files

Add or replace the following files inside the STORM repo:

- `knowledge_storm/storm_wiki/modules/claim_verification.py`  
- `knowledge_storm/storm_wiki/modules/knowledge_curation.py`  
- `knowledge_storm/storm_wiki/modules/engine.py`  
- `examples/storm_examples/run_storm_wiki_gpt.py`  
- `test_claim_verification.py` *(optional test script)*

These files modify STORM to support fact-checking and trust-based article filtering.

## Step 5: (Optional) Test Claim Verifier

```bash
python test_claim_verification.py
```

This prints:

- A trust_score between 0.0 and 1.0  
- Matched snippet scores  
- Reasoning for trustworthiness

## Step 6: Run Full Pipeline

```bash
PYTHONPATH=. python examples/storm_examples/run_storm_wiki_gpt.py \
  --output-dir .output \
  --retriever you \
  --do-research \
  --do-generate-outline \
  --do-generate-article \
  --do-polish-article \
  --max-conv-turn 2 \
  --max-perspective 3 \
  --search-top-k 3 \
  --retrieve-top-k 2
```

Enter a topic when prompted (e.g., `princeton`, `japan`, `ai safety`).

## Outputs Per Topic

The following files are created under `.output/<topic>/`:

- `conversation_log.json`  
- `raw_search_results.json`  
- `fact_check_log.json`  
- `storm_gen_article.txt`  
- `storm_gen_article_trusted_only.txt`

## Citation

This project builds on the [STORM (NAACL 2024)](https://arxiv.org/abs/2402.14207) framework. Please cite it if you use this work in research.
