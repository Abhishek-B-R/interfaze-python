from __future__ import annotations

from typing import Any, Dict

JSONSchema = Dict[str, Any]


def empty_task_schema(name: str = "empty_schema") -> Dict[str, Any]:
    return {"type": "json_schema", "json_schema": {"name": name, "schema": {}}}


def response_format(schema: JSONSchema, name: str = "response") -> Dict[str, Any]:
    return {"type": "json_schema", "json_schema": {"name": name, "schema": _ensure_object_root(schema)}}


def _ensure_object_root(schema: JSONSchema) -> JSONSchema:
    if isinstance(schema, dict) and schema.get("type") == "object":
        return schema
    return {
        "type": "object",
        "properties": {"result": schema},
        "required": ["result"],
        "additionalProperties": False,
    }
