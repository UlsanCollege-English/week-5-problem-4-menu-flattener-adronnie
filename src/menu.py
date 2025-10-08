# src/menu.py

def flatten_menu(node):
    if not node or "type" not in node:
        return []

    if node["type"] == "item":
        name = node.get("name")
        return [name] if name else []

    if node["type"] == "category":
        items = []
        for child in node.get("children", []):
            items.extend(flatten_menu(child))
        return items

    # Unknown node type
    return []
