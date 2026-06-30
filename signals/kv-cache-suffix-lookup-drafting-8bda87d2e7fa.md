# KV-Cache Suffix Lookup Drafting

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-suffix-lookup-drafting-8bda87d2e7fa`
Run ID: `kv-cache-suffix-lookup-drafting-8bda87d2e7fa-20260530T002811831594+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/766a0e159b49

## What looked useful

Natural WikiText exact lookup produced low accepted tokens per probe: best self-history row was 0.0914 accepted tokens/probe, and suffix-8 draft-4 was 0.0140. A distilgpt2 greedy verifier accepted only 2 draft tokens across 118 lookup-hit samples. Repetitive synthetic text and degenerate model loops were easy wins, showing the mechanism works mainly when repetition is already extreme.

## Boundaries and scale limits

No production KV-cache pointer reuse, serving-engine latency, cache eviction policy, multi-request workload, approximate matching, or large instruction-tuned model validation was tested. The positive model-generated result is confounded by repeated newline collapse.

## Claim scope

Exact token-suffix lookup was evaluated on bounded local corpora: 120k GPT-2 tokens from WikiText-2, synthetic repeated and shuffled controls, a 192-hit-cap distilgpt2 greedy-verifier probe, and a 2048-token distilgpt2 greedy-generated stream. It supports drafting only in highly repetitive or degenerate streams, not as a broad standalone natural-text drafting mechanism.

## Why it stopped

Bounded local evidence is mixed and mostly negative for natural text: exact suffix lookup has too little accepted draft yield, while the strongest positive result is a degenerate-loop artifact rather than robust drafting behavior.

## Recommended next action

Stop this project as no-paper evidence; if continuing, run a bounded follow-up on targeted repetitive workloads with a real speculative verifier and an explicit latency baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Targeted Repetitive-Workload KV Suffix Drafting
- Success threshold: On at least two targeted repetitive datasets, achieve at least 1.2x end-to-end decode throughput versus no drafting and outperform a simple n-gram draft baseline at matched verifier settings, while the natural-text control is reported separately.
- Stop condition: Stop if accepted tokens/probe remain below 0.25 or end-to-end throughput is below 1.05x on the targeted workloads after a correct verifier and baseline are implemented.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-suffix-lookup-drafting-8bda87d2e7fa`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
