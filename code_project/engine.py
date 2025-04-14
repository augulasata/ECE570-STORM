# RUN_KNOWLEDGE_CURATION_MODULE OLD CODE
'''
def run_knowledge_curation_module(
    self,
    ground_truth_url: str = "None",
    callback_handler: BaseCallbackHandler = None,
) -> StormInformationTable:
    (
        information_table,
        conversation_log,
    ) = self.storm_knowledge_curation_module.research(
        topic=self.topic,
        ground_truth_url=ground_truth_url,
        callback_handler=callback_handler,
        max_perspective=self.args.max_perspective,
        disable_perspective=False,
        return_conversation_log=True,
    )

    FileIOHelper.dump_json(
        conversation_log,
        os.path.join(self.article_output_dir, "conversation_log.json"),
    )
    information_table.dump_url_to_info(
        os.path.join(self.article_output_dir, "raw_search_results.json")
    )
    return information_table
'''

# APPLY THE FOLLOWING
# RUN_KNOWLEDGE_CURATION_MODULE NEW CODE

def run_knowledge_curation_module(
        self,
        ground_truth_url: str = "None",
        callback_handler: BaseCallbackHandler = None,
    ) -> StormInformationTable:
        log_data = {"conversation_log": [], "fact_checks": []}
        
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

        return information_table

# POST_RUN OLD CODE
'''
def post_run(self):
    """
    Post-run operations, including:
    1. Dumping the run configuration.
    2. Dumping the LLM call history.
    """
    config_log = self.lm_configs.log()
    FileIOHelper.dump_json(
        config_log, os.path.join(self.article_output_dir, "run_config.json")
    )

    llm_call_history = self.lm_configs.collect_and_reset_lm_history()
    with open(
        os.path.join(self.article_output_dir, "llm_call_history.jsonl"), "w"
    ) as f:
        for call in llm_call_history:
            if "kwargs" in call:
                call.pop(
                    "kwargs"
                )  # All kwargs are dumped together to run_config.json.
            f.write(json.dumps(call) + "\n")
'''

# APPLY THE FOLLOWING
# POST_RUN NEW CODE

def post_run(self):
    config_log = self.lm_configs.log()
    FileIOHelper.dump_json(
        config_log, os.path.join(self.article_output_dir, "run_config.json")
    )

    llm_call_history = self.lm_configs.collect_and_reset_lm_history()
    with open(
        os.path.join(self.article_output_dir, "llm_call_history.jsonl"), "w"
    ) as f:
        for call in llm_call_history:
            call.pop("kwargs", None)
            f.write(json.dumps(call) + "\n")

    if hasattr(self, "fact_checks") and self.fact_checks:
        FileIOHelper.dump_json(
            self.fact_checks,
            os.path.join(self.article_output_dir, "fact_check_log.json"),
        )
