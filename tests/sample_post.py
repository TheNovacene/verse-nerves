import requests, json

def demo_post(base="http://localhost:8787"):
    payload = {
        "token_entropy": 4.1,
        "branch_factor": 2,
        "retrieval_hit_rate": 0.7,
        "state_drift": 0.1,
        "belief_change_rate": 0.05,
        "sentiment_var": 0.1,
        "roundtrip_latency_ms": 250,
        "queue_depth": 1,
        "tool_error_rate": 0.0,
        "handoff_count": 1,
        "policy_hits": 0,
        "off_distribution": 0.05,
        "auth_failures": 0,
        "repetition_score": 0.1,
        "hallucination_prob": 0.05,
        "compute_budget": 0.7,
        "coherence_internal": 0.75,
        "connections": 2,
        "recursion_depth": 1
    }
    r = requests.post(f"{base}/vn/observe", json=payload, timeout=10)
    print(r.json())

if __name__ == "__main__":
    demo_post()
