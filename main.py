from trie_scanner import NetworkSignatureTrie
from packet_parser import extract_clean_payload

if __name__ == "__main__":
    print("🧠 Launching IntrusionTrie-Scan Network Threat Inspector...\n")

    firewall_database = NetworkSignatureTrie()
    
    # Pre-load known malicious signature exploit arrays
    firewall_database.black_list_exploit("shellcode_exec")
    firewall_database.black_list_exploit("sql_inject")

    # Simulate a suspicious inbound network packet payload
    incoming_packet = "get /index.php?id=1;sql_inject;-- payload"
    cleaned_frame = extract_clean_payload(incoming_packet)

    # Sliding window scanner search pass using the Trie
    threat_flagged = False
    for start_idx in range(len(cleaned_frame)):
        substring_window = cleaned_frame[start_idx:]
        if firewall_database.scan_string_segment(substring_window):
            threat_flagged = True
            break

    print(f"📝 Raw Monitored Payload String: \"{incoming_packet}\"")
    print(f"🔮 Packet Deep Inspection Verdict: {'🚨 MALICIOUS INTRUSION BLOCKED' if threat_flagged else '✅ SECURE PACKET ROUTE PASS'}")
