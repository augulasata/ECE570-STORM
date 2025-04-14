# RESEARCH OLD CODE
'''
def research(
    self,
    topic: str,
    ground_truth_url: str,
    callback_handler: BaseCallbackHandler,
    max_perspective: int = 0,
    disable_perspective: bool = True,
    return_conversation_log=False,
) -> Union[StormInformationTable, Tuple[StormInformationTable, Dict]]:
    """
    Curate information and knowledge for the given topic

    Args:
        topic: topic of interest in natural language.

    Returns:
        collected_information: collected information in InformationTable type.
    """

    # identify personas
    callback_handler.on_identify_perspective_start()
    considered_personas = []
    if disable_perspective:
        considered_personas = [""]
    else:
        considered_personas = self._get_considered_personas(
            topic=topic, max_num_persona=max_perspective
        )
    callback_handler.on_identify_perspective_end(perspectives=considered_personas)

    # run conversation
    callback_handler.on_information_gathering_start()
    conversations = self._run_conversation(
        conv_simulator=self.conv_simulator,
        topic=topic,
        ground_truth_url=ground_truth_url,
        considered_personas=considered_personas,
        callback_handler=callback_handler,
    )

    information_table = StormInformationTable(conversations)
    callback_handler.on_information_gathering_end()
    if return_conversation_log:
        return information_table, StormInformationTable.construct_log_dict(
            conversations
        )
    return information_table
'''

# APPLY THE FOLLOWING
# RESEARCH NEW CODE
def research(
        self,
        topic: str,
        ground_truth_url: str,
        callback_handler: BaseCallbackHandler,
        max_perspective: int = 0,
        disable_perspective: bool = True,
        return_conversation_log=False,
        ) -> Union[StormInformationTable, Tuple[StormInformationTable, Dict]]:
        """
        Curate information and knowledge for the given topic.
        """
        # Step 1: Identify personas
        callback_handler.on_identify_perspective_start()
        considered_personas = [""] if disable_perspective else self._get_considered_personas(
        topic=topic, max_num_persona=max_perspective
        )
        callback_handler.on_identify_perspective_end(perspectives=considered_personas)

        # Step 2: Simulate conversations
        callback_handler.on_information_gathering_start()
        conversations = self._run_conversation(
        conv_simulator=self.conv_simulator,
        topic=topic,
        ground_truth_url=ground_truth_url,
        considered_personas=considered_personas,
        callback_handler=callback_handler,
        )
        callback_handler.on_information_gathering_end()

        information_table = StormInformationTable(conversations)
        
        # APPENDED/UPDATED SECTION
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
        return information_table
