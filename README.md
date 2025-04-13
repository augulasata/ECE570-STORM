# ECE570-STORM

## STORM Extension: Fact-Checked Article Verification

This repository extends the original STORM framework with claim verification, semantic trust scoring, and trust-based source analysis. It enhances traceability and reliability of the information used in generated articles.

## Features Added

- Claim verification using semantic similarity and domain-based trust metrics  
- Automatic export of `fact_check_log.json` with trust scores and explanations  
- Source-level scoring and filtering capability (you receive URL-wise metadata, not a filtered article)  
- Compatible with STORM’s original pipeline stages: research → outline → article → polish

## Prerequisites

### API Keys Required

You must provide API access to:

- OpenAI API Key: for GPT-4o model inference  
- Bing, Brave, Tavily, or Serper API Key: for search queries  

**Cost Warning**: OpenAI GPT-4o usage requires a minimum credit of ~$5 USD.

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

## Step 3: Set API Keys

You can set them in your shell using:

```bash
export OPENAI_API_KEY="your-openai-key"
export OPENAI_API_TYPE="openai"
export BING_SEARCH_API_KEY="your-bing-key"
```

For alternatives:

```bash
export BRAVE_API_KEY="..."
export SERPER_API_KEY="..."
export TAVILY_API_KEY="..."
```

## Step 4: Add These Modified Files

Replace or add the following files into the STORM repository:

- `knowledge_storm/storm_wiki/modules/claim_verification.py`  
- `knowledge_storm/storm_wiki/modules/knowledge_curation.py`  
- `knowledge_storm/storm_wiki/modules/engine.py`  
- `examples/storm_examples/run_storm_wiki_gpt.py`  
- `test_claim_verification.py` *(optional standalone verification tester)*

These include the custom functionality for verifying information and generating `fact_check_log.json`.

## Step 5: Test Claim Verifier (Optional)

```bash
python test_claim_verification.py
```

You’ll get output showing:

- `trust_score`: a float from 0.0 to 1.0  
- `reason`: explanation for score  
- `matching_snippets`: evidence retrieved

## Step 6: Run the Pipeline

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

Enter a topic when prompted (e.g., `manhattan`, `japan`, `ai ethics`).

## Output (Per Topic)

Under `.output/<your_topic>/`, you’ll find:

- `conversation_log.json` — Full turn-by-turn information-seeking dialogue  
- `raw_search_results.json` — Unfiltered source information from retrieval  
- `fact_check_log.json` — List of claims + associated trusted sources with trust score & reasoning  
- `storm_gen_article.txt` — Generated article using all curated information  
- `storm_gen_outline.txt` — Article structure used for writing  
- `storm_gen_article_polished.txt` — Final version after polishing module

**Note**: While we provide trust scores per URL, we do not generate a filtered article based only on "credible" URLs.

## Citation

This implementation builds on [STORM (NAACL 2024)](https://arxiv.org/abs/2402.14207). Please cite the original work if you use this project for research purposes.
