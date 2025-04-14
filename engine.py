# Add initialization
self.fact_checks = []

# Modify run_knowledge_curation_module to store logs
result = self.storm_knowledge_curation_module.research(
    topic=self.topic,
    ground_truth_url=ground_truth_url,
    callback_handler=callback_handler,
    max_perspective=self.args.max_perspective,
    disable_perspective=False,
    return_conversation_log=True,
)

if isinstance(result, tuple):
    information_table, log_data = result
    self.conversation_log = log_data.get("conversation_log", [])
    self.fact_checks = log_data.get("fact_checks", [])
else:
    information_table = result
    self.conversation_log = []
    self.fact_checks = []

if self.conversation_log:
    FileIOHelper.dump_json(
        self.conversation_log,
        os.path.join(self.article_output_dir, "conversation_log.json"),
    )
information_table.dump_url_to_info(
    os.path.join(self.article_output_dir, "raw_search_results.json")
)

# Add to post_run to save fact-check log
if hasattr(self, "fact_checks") and self.fact_checks:
    FileIOHelper.dump_json(
        self.fact_checks,
        os.path.join(self.article_output_dir, "fact_check_log.json"),
    )
