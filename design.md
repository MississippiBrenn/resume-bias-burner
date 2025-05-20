# Design Plan

## Goal

Create an AI-powered tool that screens resumes while:

- Highlighting non-linear or "hidden" strengths (e.g. caregiver gaps, volunteer roles)
- Flagging biased rejections (e.g. against employment gaps, non-college paths)
- Giving an 'Equity Score' on each resume's likelihood of being unfairly judged

## Input

- A resume (text or parsed data from PDF)
- Optional: A job description

## Process

1. Extract key entities (skills, roles, dates gaps)
2. Identify  patterns like:
   - Gaps in employment
   - Caregiving or volunteer signals
   - Freelance/undocumented labor
3. Score resumes based on:
   - Alignment with job description
   - Risk of bias (e.g. unexplained gaps, age-related language)
4. Output:
   - Match Score
   - Equity warning (if risk of bias is high)
   - Summary of hidden strengths

### Output

- Clean JSON or readable report
