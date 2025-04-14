# Append this logic after runner finishes to extract and save fact-check log
try:
    output_topic_dir = os.path.join(args.output_dir, "_".join(topic.lower().split()))
    os.makedirs(output_topic_dir, exist_ok=True)
    verification_output_path = os.path.join(output_topic_dir, "fact_check_log.json")

    fact_checks = info_result[1]["fact_checks"]
    with open(verification_output_path, "w") as f:
        json.dump(fact_checks, f, indent=2)
    print(f"[✅] Fact-check results saved to {verification_output_path}")
except Exception as e:
    print(f"[⚠️] Failed to export fact-check log: {e}")
