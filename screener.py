import re 
import json 
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
            
    #  scan for date ranges and calculate missing years
    data["gaps"] = detect_year_gaps(text)

    return data

def detect_year_gaps(text): 
    # Find all 4-digit years 
    years = sorted(set(int(y) for y in 
re.findall(r"\b(19|20)\d{2}\b", text)))
    years = sorted([y for y in years if 1970 <= y <= 2030]) 

    gaps = []
    for i in range(1, len(ears)): 
        if years[i] - years[i-1] > 1: 
            gaps.append((years[i-1], years[i]))

    return gaps
    
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
    strengths = []
    if data["caregiving_signals"]:
        strengths.append("Demonstrated caregiving responsibilities, which reflect compassion, time management, and multitasking.")

    if data["volunteer_roles"]:
        strengths.append("Engaged in vounteer or unpaid work, showing community involvement and initiative.")
    if len(data.get("gaps", [])) > 0:
            strengths.append("Resilience through non-linear work hitory-likely adaptability and self-direction.")
    return strenghts

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
    Volunteer at a local shelter 2016-2017, Caregiver for parent 2018-2020. Freelance writing 2021-2022.
    """
    result = process_resume(resume_text)
    print("\n--- Hidden Strengths Summary ---")
    for s in result["strengths_summary"]: 
        print(f"- {s}")
    print(json.dumps(result, indent=2))
