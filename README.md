# Open Finding Library

The Open Finding Library is a managed and maintained library of findings with the goal of centralising security reporting finding templates avliable for use at any consultancy or for any orgonization usage.

# Finding Formatting
Findings are submitted and retrieved from the API formatted in JSON. Storage is maintained by OFL and paid for by enterprise licences.

# Orgonisation Structure
- Mobile_Application_Findings -
- Network_Findings -
- Purple_Team_Findings -
- Red_Team_Findings -
- Social_Engineering_Findings -
- Thick_Client_Findings -
- Thin_Client_Findings -
- Web_Application_Findings -

# Quality Assurance Process
1. Finding is written
    - All Fields are required to be submitted to QA or finding will be rejected
    - Follow Style Writing Guidelines for quickest approval.
2. Push Finding in branch
3. Create Merge Request
4. Technical Editor will review technical accuracy of the finding.
    - Technical editor may request revisions
5. Technical Writer will QA and review for quality and consistancy.
6. Finding will be reviewed by review board member for final merge

# Methodology
- CVSS Scores - CVSS scores are not used by all users and are different based on situation. Therefore OFL takes no responsibility for providing these scores, instead users should set the CVSS score when the finding is used based on environment variables.
