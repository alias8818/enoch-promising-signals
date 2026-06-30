# Entropy-driven dynamic KV eviction for long local inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `entropy-driven-dynamic-kv-eviction-for-long-local-inference-2c7ebc38b65d`
Run ID: `entropy-driven-dynamic-kv-eviction-for-long-local-inference-2c7ebc38b65d-20260528T013521037003+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/0baf61e57fbd

## What looked useful

Keeping high-entropy tokens retained more future attention than random or recency in distilgpt2 and gpt2, while keeping low-entropy tokens was consistently poor. The signal was strongly confounded by position: an oldest-token baseline beat high entropy at 10-20% budgets and roughly tied it at 40%.

## Boundaries and scale limits

No real KV-cache was evicted during generation; no long-context task accuracy, latency, memory, 7B+ model, GQA/MQA model, or serving-engine integration was tested.

## Claim scope

Small GPT-style mechanism probe only: token-level predictive entropy was compared with fixed-horizon future attention mass in tiny-gpt2, distilgpt2, and gpt2, with equal-budget retention policies.

## Why it stopped

Proxy mechanism evidence was mixed: high entropy is a useful candidate signal, but it did not separate cleanly from a simple position baseline, so this is not a direct validation of entropy-driven KV eviction.

## Recommended next action

Stop this run as no-paper useful signal; next direct test should patch an online generation loop and require entropy or entropy+age eviction to beat the best age baseline on long-context quality-memory tradeoff.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Online entropy-plus-age KV eviction in a real generation loop
- Success threshold: At two or more KV budgets, entropy-plus-age must improve task quality or retained logprob by at least 5% relative over the best age-only baseline while matching the same memory budget and adding less than 10% generation overhead.
- Stop condition: Stop if entropy-plus-age fails to beat the best age-only baseline on both quality and overhead in two representative long-context tasks or if online entropy computation erases the memory/latency benefit.

## Evidence references

- Artifact root: `<local-path>/projects/entropy-driven-dynamic-kv-eviction-for-long-local-inference-2c7ebc38b65d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
