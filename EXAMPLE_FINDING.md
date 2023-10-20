# Documentation for JSON Expected Data

- **Finding Title:** `finding_title`  
  - _Type:_ String  
  - Represents the primary title or name associated with the specific security finding. Ensure it is concise yet informative enough to provide a clear context about the nature of the identified issue.

- **Risk Rating:** `risk_rating`  
  - _Type:_ Integer  
  - Quantitative representation of the potential severity or impact of the identified security finding. The rating is scaled from 1 to 5, where:
    - **1**: Informational - No immediate threat, mainly for awareness.
    - **2**: Low - Minor vulnerabilities that may have limited impact.
    - **3**: Medium - Vulnerabilities that could lead to some data exposure or potential misuse.
    - **4**: High - Serious vulnerabilities that can cause significant damage if exploited.
    - **5**: Critical - Severe vulnerabilities that pose immediate threats and could lead to extensive system compromise or data breaches.


- **CVSS Score** 'cvss_score'

- **Risk Rating Notes:** `risk_rating_notes`  
  _Type:_ String, _Format:_ Markdown Language  
  Provide a detailed explanation for the chosen risk rating. If the risk rating is influenced by specific circumstances or variables, please clarify the reason and/or circumstances under which the rating applies.

- **Impacted Domain:** `impact`
  - _Type:_ String
  - _Recommended Values:_ 
    - **API Security**: Issues related to exposed, misconfigured, or vulnerable APIs, leading to potential data breaches or unauthorized actions.
    - **Application-level DoS**: Vulnerabilities that allow attackers to exhaust application resources, making the application unusable.
    - **Authentication**: Issues where unauthorized users can gain access or authorized users can escalate privileges.
    - **Authorization**: Failures in verifying what actions or resources the user is permitted to access.
    - **Business Logic**: Exploits that make use of the application's functionality, such as race conditions, or flaws in the application's core logic.
    - **Cloud Configuration**: Security risks stemming from misconfigured cloud services or platforms.
    - **Code Quality**: Vulnerabilities derived from poor code practices, like hard-coded credentials or inadequate error-checking.
    - **Configuration Management**: Vulnerabilities arising from improperly configured systems, potentially leading to unintended access or exposures.
    - **Container Security**: Vulnerabilities associated with Docker, Kubernetes, or other containerization technologies.
    - **Cryptography**: Flaws in implementing or using cryptographic functions, potentially leading to data exposure or system compromise.
    - **Data Protection**: Flaws related to confidentiality and privacy, such as exposing sensitive information or not encrypting data properly.
    - **Database Security**: Flaws in database setup or configuration, including weak authentication or lack of encryption.
    - **DNS Security**: Attacks that target DNS servers, including DNS poisoning or spoofing.
    - **Endpoint Protection**: Issues at the endpoints, like unprotected client-side data or vulnerable client-side code.
    - **Error Handling**: Situations where error messages disclose too much information about the system's internals, aiding attackers.
    - **File Upload Vulnerabilities**: Security flaws allowing attackers to upload malicious files to a system.
    - **Insecure Deserialization**: Flaws allowing attackers to execute arbitrary code through serialized objects.
    - **Insecure Direct Object References (IDOR)**: Vulnerabilities where attackers can bypass authorization and directly access resources.
    - **Input Validation**: Problems with how user inputs are processed and validated, potentially leading to issues like SQL injection or cross-site scripting (XSS).
    - **Legacy System Vulnerabilities**: Security flaws associated with outdated or no longer supported hardware or software.
    - **Logging and Monitoring**: Insufficient or misconfigured logging that doesn't capture or alert on malicious activities.
    - **Network Configuration**: Misconfigured firewalls, exposed services, or other network-related vulnerabilities.
    - **Output Encoding**: Issues where data is output without proper encoding, often related to XSS vulnerabilities.
    - **Patch Management**: Risks associated with outdated software or systems lacking critical security patches.
    - **Physical Security**: Vulnerabilities associated with the physical protection of hardware or data.
    - **Resource Management**: Issues with how an application or system handles its resources, potentially leading to resource exhaustion or leaks.
    - **Server Configuration**: Flaws in server settings, including exposed admin interfaces or unnecessary services running.
    - **Server-level DoS**: Vulnerabilities targeting the server resources directly, rather than the application.
    - **Session Management**: Weaknesses in how user sessions are managed and maintained, e.g., session hijacking or session fixation.
    - **Social Engineering**: Manipulative actions targeting humans, trying to trick them into revealing sensitive information or performing certain actions.
    - **Third-party Components**: Vulnerabilities related to the use of third-party libraries, plugins, or tools.

- **Mitre ATT&CK Tactic/Technique:** `tactic`  
  _Type:_ String

- **Finding Description:** `description`  
  _Type:_ String, _Format:_ Markdown Language

- **Executive Remediation Details:** `remediation_details_nontechnical`  
  _Type:_ String, _Format:_ Markdown Language

- **Technical Remediation Details:** `remediation_details_technical`  
  _Type:_ String, _Format:_ Markdown Language

- **References:** `reference_list`
    - **URL:** `url`
    _Type:_ Link 
    - **Description:** `description`
        - **CVE ID:** `cve_ID`
        - **Title:** `title`

- **Author:** `author`

- **Editor 1:** `editor_1`

- **Editor 2:** `editor_2`

- **Active:** This flag is used for limiting searches to only findings that have been through PR and are community accessible.

- **Beta:** `beta`

- **Deprecated:** `deprecated`

- **Editing Notes:** `editing_notes`
    - **Note:** `note`
        - **Date:** `date`
        - **Author:** `author`
        - **Note:** `note`

- **Key Words:**  `key_words`
  Keywords that can be used for search or tagging purposes within the documentation.
