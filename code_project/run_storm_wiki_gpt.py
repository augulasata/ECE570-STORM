# Append this logic right above def main
from knowledge_storm.storm_wiki.modules import claim_verification

def run_fact_check_pipeline(url_to_info_path, output_path="fact_check_log.json"):
    with open(url_to_info_path, "r") as f:
        data = json.load(f)

    fact_check_log = []
    for url, info_list in data.items():
        for entry in info_list:
            claim = entry if isinstance(entry, str) else entry.get("content", "")
            if not claim.strip():
                continue
            result = claim_verification.verify_claim(claim, info_list)
            fact_check_log.append({
                "url": url,
                "claim": claim,
                "trust_score": None,
                "reason": result
            })

    with open(output_path, "w") as f:
        json.dump(fact_check_log, f, indent=2)
    print(f"[GOOD] Fact-check results written to {output_path}")
