# Sink-token sensitivity for 40% GPT-2 KV cache eviction

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `sink-token-sensitivity-for-40--gpt-2-kv-cache-eviction-e5e2c49c5d`
Run ID: `sink-token-sensitivity-for-40--gpt-2-kv-cache-eviction-e5e2c49c5d-20260607T055928214688+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: KV Eviction Policy Reduces Cache 40pct on GPT2 Small: enoch://control-plane/projects/kv-eviction-policy-reduces-cache-40pct-on-gpt2-small-d1bbb0182424/runs/kv-eviction-policy-reduces-cache-40pct-on-gpt2-small-d1bbb0182424-20260607T033338838596+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ae5d5ea133b6

## What looked useful

Recent-only 40% eviction was catastrophic (mean NLL 7.8735, PPL 2626.72), while preserving 1-8 sink tokens reduced mean NLL to 3.9515-3.9995 (PPL 52.01-54.57) against a full-cache control of NLL 3.6599 (PPL 38.86). Too many sink tokens hurt recency: 64 sinks had PPL 97.10.

## Boundaries and scale limits

GPT-2 small only; 12 selected Wikitext-2 test examples of 256 tokens; one seed; one eviction fraction; offline loss scoring only, not generation quality, serving throughput, longer contexts, larger models, or multi-dataset robustness.

## Claim scope

In a small direct GPT-2 Wikitext-2 sequential scoring test with 40% KV-cache eviction and 256-token sequences, preserving a small number of initial sink tokens materially reduces next-token loss versus recent-only eviction.

## Why it stopped

Tier 1 direct test produced a useful mechanism signal but not enough breadth or robustness for paper readiness.

## Recommended next action

Run a bounded deepen test at 512-1024 token contexts with bootstrap intervals, a second corpus, and GPT-2 medium if local GPU memory permits; stop paper consideration until robustness holds beyond this Tier 1 result.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Robust sink-token optimum for GPT-2 KV eviction at longer contexts
- Success threshold: Best 1-8 sink-token setting improves mean NLL by at least 0.25 over 0-sink recent-only eviction at both lengths and on both corpora, with no more than 0.50 mean NLL degradation versus full cache.
- Stop condition: Stop if 0-sink recent-only eviction is not significantly worse than 1-8 sink retention on either corpus or if the best sink count varies so widely that no bounded recommendation remains.

## Evidence references

- Artifact root: `<local-path>/projects/sink-token-sensitivity-for-40--gpt-2-kv-cache-eviction-e5e2c49c5d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
