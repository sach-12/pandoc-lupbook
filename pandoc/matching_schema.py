# Copyright (c) 2021 LupLab
# SPDX-License-Identifier: AGPL-3.0-only

import lupbook_schema

_matching_schema = {
    "title": "Lupbook Matching",
    "description": "Schema for Lupbook's matching interactive activity",
    "type": "object",
    "properties": {
        "id": {
            "type": "string",
            "format": "lupbook_id",
        },
        "title":{
            "type": "string"
        },
        "prompt": {
            "type": "string",
        },
        "random": {
            "type": "boolean",
            "default": False
        },
        "choices": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "string"
                    },
                    "match": {
                        "type": "string"
                    },
                    "text": {
                        "type": "string"
                    },
                    "feedback": {
                        "type": "string"
                    }
                },
                "required": ["id", "match", "text"],
                # XXX:
                # 1. we could remove `id` for choices and just use a simple
                # enumeration in the filter
                # 2. we could otherwise remove `id` for answers and have them
                # list the correct choice ids (this would also allow a choice to
                # match multiple answers).
                "additionalProperties": False
            }
        },
        "answers": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "string"
                    },
                    "text": {
                        "type": "string"
                    },
                },
                "required": ["id", "text"],
                "additionalProperties": False
            }
        }
    },
    "required": ["id", "title", "prompt", "choices", "answers"],
    "additionalProperties": False
}

matching_validator = lupbook_schema.LupbookValidator(
        _matching_schema,
        format_checker = lupbook_schema.lupbook_format_checker)