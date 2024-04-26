# Copyright (c) 2021 LupLab
# SPDX-License-Identifier: AGPL-3.0-only

from dominate.tags import *
from dominate.util import raw

import lupbook_filter
import matching_schema
import panflute


#
# Component generation
#

class LupbookMatching(lupbook_filter.LupbookComponent):
    @staticmethod
    def _yaml_validator():
        return matching_schema.matching_validator

    @staticmethod
    def activity_id():
        return "matching"

    def _activity_name(self):
        return "Matching activity"

    def _gen_choice_block(self, choice):
        div_attrs = {
            "id": f"matching-{self.args['id']}-choice-{choice['id']}",
            "cls": "matching-c-choice border rounded m-2 p-2 d-flex",
            "data-match": f"{choice['match']}"
        }
        with div(**div_attrs):
            text = choice['text']
            formatted_text = panflute.convert_text(text, output_format = 'html')
            # TODO: fix this in CSS (the last paragraph of the parent div should
            # not have a bottom margin)
            modified_text = formatted_text.replace('<p>', '<p class = "m-1">')
            raw(modified_text)

    def _gen_answer_block(self, answer):
        div_attrs = {
            "id": f"matching-{self.args['id']}-answer-{answer['id']}",
            "cls": "matching-c-answer border rounded m-2 p-2 d-flex flex-column",
        }
        with div(**div_attrs):
            text = answer['text']
            formatted_text = panflute.convert_text(text, output_format = 'html')
            # TODO: see above
            modified_text = formatted_text.replace('<p>', '<p class = "m-1">')
            raw(modified_text)

    def _gen_activity(self):
        # Generate containers and blocks
        with div(cls = "card-body p-2 m-0 row"):
            with div(cls = "col"):
                div("Drag items from here...",
                    cls = "small fst-italic text-secondary")
                with div(id = f"matching-{self.args['id']}-choices",
                         cls = "matching-l-choices border"):
                    for i, block in enumerate(self.args["choices"]):
                        self._gen_choice_block(block)

            with div(cls = "col"):
                div("...and drop them here (click to remove)",
                    cls = "small fst-italic text-secondary")
                with div(id = f"matching-{self.args['id']}-answers",
                         cls = "matching-l-answers border"):
                    for i, block in enumerate(self.args['answers']):
                        self._gen_answer_block(block)

    def _gen_controls(self):
        with div(cls = "card-body border-top"):
            with div(cls = "d-flex align-items-center"):
                with div(cls = "px-1"):
                    button("Submit",
                           id = f"matching-{self.args['id']}-submit",
                           cls = "btn btn-primary")
                    button("Reset",
                           id = f"matching-{self.args['id']}-reset",
                           cls = "btn btn-secondary")

                with div(cls = "px-1 flex-grow-1"):
                    div(cls = "d-none")

                with div(cls = "px-1"):
                    button(id = f"matching-{self.args['id']}-feedback-btn",
                           cls = "matching-c-feedback__toggle collapsed d-none",
                           data_bs_target = f"#matching-{self.args['id']}-feedback",
                           data_bs_toggle = "collapse", type = "button")

    def _gen_feedback(self):
        with div(id = f"matching-{self.args['id']}-feedback", cls = "collapse"):
            with div(cls = "card-body border-top"):
                div(id = f"matching-{self.args['id']}-correct",
                    cls = "matching-c-feedback-correct d-none")
                for i, choice in enumerate(self.args["choices"]):
                    formatted_text = panflute.convert_text(
                            choice["feedback"], output_format = 'html')
                    div(raw(formatted_text),
                        id = f"matching-{self.args['id']}-feedback-{choice['id']}",
                        cls = "matching-c-feedback-item d-none")
