# Prompt-Lookup + N-gram Hybrid Speculative Decoding on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `prompt-lookup-n-gram-hybrid-speculative-decoding-on-cpu-73b618f741df`
Run ID: `prompt-lookup-n-gram-hybrid-speculative-decoding-on-cpu-73b618f741df-20260527T041903782600+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/48a9fd9eca41

## What looked useful

Hybrid drafting reduced simulated target verification calls by 52.70% aggregate versus 48.76% for prompt-only and 43.35% for n-gram-only. Gains were strong on synthetic repetition and structured Node documentation, modest on code-like traces, and weak on license/legal text. Tie-breaking affected workload performance.

## Boundaries and scale limits

No real transformer verifier, tokenizer/model distribution, KV-cache behavior, batching overhead, or end-to-end latency was measured; corpora are local documentation/license/code-like files plus synthetic repetition, not a broad serving workload.

## Claim scope

Bounded CPU trace benchmark of prompt-lookup, generated-history n-gram, and two hybrid tie-break policies over 37 local/synthetic documents, using exact future-token acceptance and target-call reduction as a proxy for speculative decoding benefit.

## Why it stopped

This run closes as no-paper useful signal because the evidence is trace-proxy mechanism support, not direct end-to-end CPU speculative decoding validation.

## Recommended next action

Run a bounded end-to-end CPU follow-up with a small real transformer target model to measure wall-clock latency, verifier batching overhead, and acceptance under the model tokenizer.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end CPU hybrid speculative decoding with a small transformer target
- Success threshold: Hybrid shows >=20% median wall-clock latency reduction versus greedy decoding and >=5% median latency reduction versus the best single-source drafter on at least two workload families.
- Stop condition: Stop as negative if hybrid fails to beat the best single-source drafter by 5% median latency or if verifier/drafter overhead erases target-call savings on two or more workload families.

## Evidence references

- Artifact root: `<local-path>/projects/prompt-lookup-n-gram-hybrid-speculative-decoding-on-cpu-73b618f741df`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
