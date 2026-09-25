import re
from app.database.repository import get_part, get_by_category

def answer_question(question: str) -> str:
    q = question.strip().lower()

    if not q:
        return "Please ask a question about the inventory."

    # "List all items in [category]"
    match = re.search(r"list.*items? in (.+)", q)
    if match:
        category = match.group(1).strip(" ?.")
        items = get_by_category(category)
        if not items:
            return f"I couldn't find any items in the category '{category}'."
        lines = [f"- {i['name']} (qty: {i['quantity']}, location: {i['location']})" for i in items]
        return f"Items in category '{category}':\n" + "\n".join(lines)

    # "Where is the [item]?"
    match = re.search(r"where (?:is|are) (?:the )?(.+)", q)
    if match:
        item_name = match.group(1).strip(" ?.")
        if not item_name:
            return "Please tell me which item you're looking for."
        part = get_part(item_name)
        if not part:
            return f"I couldn't find '{item_name}' in the inventory. Check the spelling or try a shorter name."
        return f"{part['name']} is stored in {part['location']}."

    # "How many [item] do we have?"
    match = re.search(r"how many (.+?) do we have", q)
    if match:
        item_name = match.group(1).strip(" ?.")
        if not item_name:
            return "Please specify which item you're asking about, e.g. 'how many brake pads do we have?'."
        part = get_part(item_name)
        if not part:
            return f"I couldn't find '{item_name}' in the inventory. Check the spelling or try a shorter name."
        return f"We have {part['quantity']} {part['name']}."

    return (
        "I didn't understand that. Try asking things like:\n"
        "- 'How many brake pads do we have?'\n"
        "- 'Where is the ECU?'\n"
        "- 'List all items in Electrical.'"
    )