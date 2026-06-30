# Local Cache Retrieval Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `local-cache-retrieval-speculative-decoding-7b01554f5000`
Run ID: `local-cache-retrieval-speculative-decoding-7b01554f5000-20260619T210802042211+0000`

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

- Provider-backed Research Facility batch: hf:MiniMaxAI/MiniMax-M3: enoch://research-facility/provider/hf:MiniMaxAI/MiniMax-M3/de473bf63e78

## What looked useful

Across 10 seeds, LocalSuffixCache reduced cycles by 70.98% on synthetic templated logs, stayed near zero on random tokens, and reduced cycles by 11.03% on the project prompt while a simple online bigram baseline reached 27.80% there.

## Boundaries and scale limits

Proxy simulator only; no real LM target, no GPU inference, no tokenizer/model logits, no KV-cache overhead, no batching, and no wall-clock serving validation.

## Claim scope

Causal local suffix-cache retrieval can reduce speculative-decoding verification cycles on locally repetitive token streams under oracle verification-cycle accounting.

## Why it stopped

Proxy evidence supports a workload-dependent mechanism but is not a direct/full validation and is mixed against the bigram baseline.

## Recommended next action

Run a bounded direct LM follow-up with a GPT-2-small-class target and real tokenizer to measure wall-clock latency, target forward-pass reduction, cache overhead, and workload sensitivity.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct small-LM latency test for local-cache retrieval speculative decoding
- Success threshold: At least 20% wall-clock latency reduction and at least 30% target forward-pass reduction on repeated workloads, with less than 5% latency regression on non-repeated controls and exact output equivalence.
- Stop condition: Stop if cache lookup overhead eliminates latency gains, if acceptance is below 10% on repeated workloads, or if output equivalence fails.

## Evidence references

- Artifact root: `<local-path>/projects/local-cache-retrieval-speculative-decoding-7b01554f5000`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
