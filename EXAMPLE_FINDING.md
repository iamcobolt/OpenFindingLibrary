# Documentation for JSON Expected Data

- **Finding Title:** `finding_title`  
  - _Type:_ String  
  - _Description:_  Represents the primary title or name associated with the specific security finding. Ensure it is concise yet informative enough to provide a clear context about the nature of the identified issue.  
  - _Required:_ TRUE

- **Risk Rating:** `risk_rating`  
  - _Type:_ int  
  - _Description:_  Quantitative representation of the potential severity or impact of the identified security finding. The rating is scaled from 1 to 5, where:
    - **1**: Informational - No immediate threat, mainly for awareness.
    - **2**: Low - Minor vulnerabilities that may have limited impact.
    - **3**: Medium - Vulnerabilities that could lead to some data exposure or potential misuse.
    - **4**: High - Serious vulnerabilities that can cause significant damage if exploited.
    - **5**: Critical - Severe vulnerabilities that pose immediate threats and could lead to extensive system compromise or data breaches.  
  - _Required:_ TRUE


- **CVSS Score** 'cvss_score'  
  - _Type:_ float  
  - _Description:_  
  - _Required:_ TRUE

- **Risk Rating Notes:** `risk_rating_notes`  
   - _Type:_ String  
   - _Format:_ Markdown Language  
   - _Description:_ Provide a detailed explanation for the chosen risk rating. If the risk rating is influenced by specific circumstances or variables, please clarify the reason and/or circumstances under which the rating applies.  
  - _Required:_ TRUE

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
  - _Required:_ TRUE

- **Mitre ATT&CK Tactic/Technique:** `tactic`  
   - _Type:_ String  
   - _Format:_ PlainText  
   - _Description:_     
   - _Required:_ TRUE

- **Finding Description:** `description`  
   - _Type:_ String  
   - _Format:_ HTML  
   - _Description:_    
   - _Required:_ TRUE

- **Executive Remediation Details:** `remediation_details_nontechnical`  
   - _Type:_ String  
   - _Format:_ HTML  
   - _Description:_    
   - _Required:_ TRUE

- **Technical Remediation Details:** `remediation_details_technical`  
   - _Type:_ String  
   - _Format:_ HTML  
   - _Description:_    
   - _Required:_ TRUE

- **References:** `reference_list`  
   - _Type:_ Array  
      - **URL:** `url`  
         - _Type:_ Link  
         - _Required:_ TRUE 
      - **Description:** `description`  
         - _Type:_ String  
         - _Format:_ Markdown Language  
         - _Description:_   
         - _Required:_ TRUE 
      - **CVE ID:** `cve_ID`  
         - _Type:_ String  
         - _Description:_   
         - _Required:_ FALSE 
      - **Title:** `title`  
         - _Type:_ String   
         - _Description:_   
         - _Required:_ TRUE
  - _Required:_ TRUE

- **Author:** `author`  
  - _Type:_ UserName  
  - _Description:_   
  - _Required:_ TRUE 

- **Editor 1:** `editor_1`  
   - _Type:_ UserName  
   - _Description:_   
   - _Required:_ FALSE  

- **Editor 2:** `editor_2`  
   - _Type:_ UserName  
   - _Description:_  
   - _Required:_ FALSE  

- **Active:**   
   - _Type:_ bool  
   - _Description:_ This flag is used for limiting searches to only findings that have been through PR and are community accessible.  
   - _Required:_ TRUE 

- **Beta:** `beta`  
   - _Type:_ bool  
   - _Description:_    
   - _Required:_ TRUE 

- **Deprecated:** `deprecated`  
   - _Type:_ bool  
   - _Description:_    
   - _Required:_ TRUE 

- **Editing Notes:** `editing_notes`  
   - _Type:_ Array  
      - **Note:** `note`  
         - _Type:_ String    
         - _Required:_ TRUE 
      - **Date:** `date`  
         - _Type:_ Date  
         - _Required:_ TRUE 
      - **Author:** `author`  
         - _Type:_ UserName  
         - _Required:_ TRUE 
      - **Note:** `note`  
         - _Type:_ String  
         - _Required:_ TRUE 
  - _Required:_ FALSE 

- **Key Words:**  `key_words`  
   - _Type:_ String  
   - _Format:_ PlainText  
   - _Description:_  Keywords that can be used for search or tagging purposes within the documentation.  
  - _Required:_ FALSE
