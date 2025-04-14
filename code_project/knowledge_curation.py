# Imported verification module
from knowledge_storm.storm_wiki.modules.claim_verification import verify_claim

# Append this to research method to return fact-check logs
if return_conversation_log:
    fact_checks = []
    for persona, history in conversations:
        for turn in history:
            for info in turn.search_results:
                if info.meta and "verification" in info.meta:
                    fact_checks.append(info.meta["verification"])
    return information_table, {
        "conversation_log": StormInformationTable.construct_log_dict(conversations),
        "fact_checks": fact_checks,
    }
