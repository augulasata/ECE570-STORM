# Create a this file and copy and paste the below code as a whole 

DOMAIN_TRUST_LEVELS = {
    ".gov": 1.0,
    ".edu": 0.95,
    "cnn.com": 0.75,
    "medium.com": 0.4,
    "blogspot.com": 0.3,
    "wordpress.com": 0.3,
    "default": 0.5
}

def get_domain_trust(url: str) -> float:
    try:
        domain = urlparse(url).netloc
        for trusted in DOMAIN_TRUST_LEVELS:
            if trusted in domain:
                return DOMAIN_TRUST_LEVELS[trusted]
    except:
        pass
    return DOMAIN_TRUST_LEVELS["default"]

def score_relevance(claim: str, snippets: List[str], model: SentenceTransformer) -> float:
    if not snippets:
        return 0.0
    claim_emb = model.encode([claim])
    snippet_embs = model.encode(snippets)
    sims = cosine_similarity(claim_emb, snippet_embs)[0]
    return float(np.max(sims))

def verify_claim(claim: str, info_dict: Dict[str, Dict], model: SentenceTransformer = None) -> Dict:
    if model is None:
        model = SentenceTransformer("paraphrase-MiniLM-L6-v2")

    if not info_dict:
        return {
            "trust_score": 0.0,
            "reason": "No information provided for verification."
        }

    all_snippets = []
    domain_scores = []

    for info in info_dict.values():
        url = info.get("url", "")
        snippets = info.get("snippets", [])
        all_snippets.extend(snippets)
        domain_scores.append(get_domain_trust(url))

    relevance_score = score_relevance(claim, all_snippets, model)
    domain_score = max(domain_scores) if domain_scores else 0.5
    trust_score = round(0.7 * relevance_score + 0.3 * domain_score, 3)

    reason_snippet = "\n".join(all_snippets[:3]) if all_snippets else "No supporting text found."
    reason = f"Claim assessed using semantic similarity and source reliability.\nTop snippet(s):\n{reason_snippet}"

    return {
        "trust_score": trust_score,
        "reason": reason
    }
