import json

def get_candidates_from_json(path):
    """Возвращает нам список кандидатов"""
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def get_candidate(candidate_id):
    """Возвращает кандидата по id"""
    candidates = get_candidates_from_json("candidates.json")
    for candidate in candidates:
        if candidate['id'] == candidate_id:
            return candidate


def get_candidates_by_name(candidate_name):
    """Возвращает кандидатов по имени"""
    candidates = get_candidates_from_json("candidates.json")
    matches = []
    for candidate in candidates:
        if candidate_name.lower() in candidate['name'].lower():
            matches.append(candidate)
    return matches


def get_candidates_by_skill(skill_name):
    """Возвращает кандидатов по навыку/навыкам"""
    candidates = get_candidates_from_json("candidates.json")
    matches = []
    for candidate in candidates:
        if skill_name.lower() in candidate['skills'].lower():
            matches.append(candidate)
    return matches


