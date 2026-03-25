# Incident Report: Suspected Brute-Force Login Attempt

## 1. Summary

A potential brute-force attack was detected on a Windows endpoint after multiple failed login attempts occurred within a short timeframe. The activity triggered a high-severity custom alert in Wazuh.

---

## 2. Alert Details

- **Alert Name:** Custom Alert: Possible brute-force attack (multiple failed logins)
- **Rule ID:** 100003
- **Severity Level:** 12 (High)
- **MITRE ATT&CK:** T1110 (Brute Force)
- **Agent:** windows-lab
- **Timestamp:** 2026-03-25T01:08:20.309Z

---

## 3. Investigation Steps

### Step 1: Review Alert
- Observed multiple alerts for failed login attempts (Rule 100002)
- Correlation rule (100003) triggered after repeated failures

### Step 2: Analyze Event Data
- Event ID: 4625 (failed login)
- Log source: Windows Security Event Log
- Multiple login failures occurred within a short time period

### Step 3: Validate Behavior
- Activity pattern matches brute-force behavior:
  - Repeated authentication failures
  - Occurring rapidly within seconds

---

## 4. Findings

- Multiple failed login attempts were recorded on the system
- Behavior is consistent with a brute-force login attempt
- No successful login was observed following the attempts

---

## 5. Impact Assessment

- No confirmed compromise
- However, repeated failed logins indicate a potential attack attempt
- System may be vulnerable to password guessing if protections are weak

---

## 6. Response Actions

- No containment required (lab environment)
- In real environment:
  - Investigate source IP
  - Consider account lockout policies
  - Monitor for further suspicious activity

---

## 7. Conclusion

This activity was identified as a simulated brute-force attempt. Detection was successfully performed using custom Wazuh rules with correlation logic. The alert demonstrates the ability to detect repeated authentication failures and escalate severity appropriately.

---

## 8. Key Learnings

- Single failed logins are low-risk events
- Multiple failures indicate potential attack patterns
- Correlation rules improve detection accuracy
- SIEM tuning is essential for meaningful alerts

## 9. Threat Intelligence Enrichment

The source IP associated with the failed login attempts was analyzed during the investigation.

- **IP Address:** 127.0.0.1
- **Abuse Confidence Score:** N/A
- **Country:** N/A
- **ISP:** N/A
- **Total Reports:** N/A

### Analysis

The source IP is a localhost address (127.0.0.1), which indicates the activity originated from the same system. In this lab scenario, this confirms that the brute-force activity was simulated locally rather than coming from an external attacker.

### Impact on Investigation

Since the IP is local, external threat intelligence enrichment was not applicable. However, the behavior (multiple failed login attempts) still accurately represents a brute-force attack pattern. This demonstrates the importance of understanding context before applying enrichment.