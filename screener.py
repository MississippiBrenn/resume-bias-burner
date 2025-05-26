import re 
def extract_resume_data(text):
    data = {
        "skills": [],
        "gaps": [],
        "volunteer_roles": [],
        "caregiving_signals": []
    }

    # Example caregiving keywords
    caregiving_keywords = ["maternity leave", "paternity leave", "caregiver", "raising children", "stay-at-home", "mom", "dad", "son", "daughter", "child", "parent"]

    # Example volunteer roles
    volunteer_keywords = ["volunteer", "nonprofit", "community work", "unpaid", "community"]

    # Search for caregiving indicators
    for word in caregiving_keywords:
        if word in text.lower():
            data["caregiving_signals"].append(word)

    # Search for volunteer indicators
    for word in volunteer_keywords:
        if word in text.lower():
            data["volunteer_roles"].append(word)

    # TODO: Detect employment gaps (placeholder)
    #  scan for date ranges and calculate missing years

    return data

def score_bias_risk(data):
    score = 0
    flags = []

    if data["caregiving_signals"]:
        score += 1
        flags.append("Possible caregiving-related gap")

    if data["volunteer_roles"]:
        score += 1
        flags.append("Volunteer or unpaid labor")

    if len(data.get("gaps", [])) > 0:
        score += len(data["gaps"])
        flags.append("Employment gap(s) detected")

    return {
        "bias_risk_score": score,
        "risk_flags": flags
    }

def summarize_hidden_strengths(data):
    # TODO: Highlight underrepresented strengths
    return []

def process_resume(text):
    data = extract_resume_data(text)
    bias_info = score_bias_risk(data)
    summary = summarize_hidden_strengths(data)
    return {
        "parsed": data,
        "bias_assessment": bias_info,
        "strenths_summary": summary
    }

if __name__ == "__main__":
    # Example usage
    resume_text = """
    John Doe
    Software Engineer
    Skills: Python, JavaScript, SQL
    Experience: 5 years as a software engineer
    """
    result = process_resume(resume_text)
    print(result)
