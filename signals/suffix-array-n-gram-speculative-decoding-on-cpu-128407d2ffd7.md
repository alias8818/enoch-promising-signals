# Suffix-Array N-Gram Speculative Decoding on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-array-n-gram-speculative-decoding-on-cpu-128407d2ffd7`
Run ID: `suffix-array-n-gram-speculative-decoding-on-cpu-128407d2ffd7-20260525T075558981644+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/8a852442b9b4

## What looked useful

Suffix arrays make exact n-gram lookup far faster than recent-window scanning and can produce accepted draft tokens on highly repetitive traces, but a simple hash n-gram recency index matched or exceeded acceptance while building and querying faster in all local tests.

## Boundaries and scale limits

No real LLM verifier, no real prompt/output traces, no concurrent serving, no tokenizer/model cache effects, and no end-to-end speculative decoding throughput measurement.

## Claim scope

Single-threaded CPU benchmark of exact n-gram draft proposers on held-out synthetic token traces up to 200k training tokens and 50k queries.

## Why it stopped

Moderate proxy evidence, not full validation: suffix-array lookup beat scanning but did not beat the simpler hash baseline on CPU lookup/build metrics, and acceptance was useful only for highly repetitive synthetic traces.

## Recommended next action

Stop this run as no-paper evidence; the concrete next bounded test is trace replay on real LLM prompt/output tokens against an equal-memory hash n-gram baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-Replay Suffix-Array N-Gram Speculative Decoding
- Success threshold: At equal or lower measured RSS, suffix-array proposer achieves at least 95% of hash baseline accepted tokens/query and at least 2x lower lookup latency than recent-window scan on real traces.
- Stop condition: Stop if real-trace acceptance is below 0.25 accepted tokens/query or if suffix-array lookup is slower than both hash and scan at equal memory.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-array-n-gram-speculative-decoding-on-cpu-128407d2ffd7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
