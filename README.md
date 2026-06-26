# IntrusionTrie-Scan

A pure Python pattern scanner built for embedded firewall log inspection. By indexing blacklisted malware payload keywords inside a prefix **Trie Data Structure**, this intrusion detection tool drops pattern matching complexities down to constant limits independent of signature library size.

## ⚡ Data Structure Properties
* **Data Layout:** Advanced Prefix Trie tree maps tracking character branch routes.
* **Time Complexity:** Constant lookup bounds $O(L)$, where $L$ defines the length of incoming network strings, completely bypassing iterative search operations.
