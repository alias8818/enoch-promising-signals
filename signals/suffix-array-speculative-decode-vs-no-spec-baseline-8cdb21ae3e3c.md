# Suffix-Array Speculative Decode vs No-Spec Baseline

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-array-speculative-decode-vs-no-spec-baseline-8cdb21ae3e3c`
Run ID: `suffix-array-speculative-decode-vs-no-spec-baseline-8cdb21ae3e3c-20260628T054932339685+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d2b982979355

## What looked useful

Suffix-array drafts can produce 4.47x-7.57x tokens per target validation call on repeated/local text proxies while staying at 1.00x on a random control.

## Boundaries and scale limits

No real transformer target, no logits validation, no GPU/KV-cache serving path, no wall-clock model tokens/sec measurement, and only small bounded corpora.

## Claim scope

Offline token-stream proxy: suffix-array drafting reduced target validation calls on deterministic repeated-text and local scaffold-text corpora, with no benefit on a random low-repetition control.

## Why it stopped

Proxy-only useful signal; not full validation and not paper-ready.

## Recommended next action

Run a bounded real-model follow-up with a small transformer target to measure exact-output speculative decoding speed, acceptance, and suffix lookup overhead.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real small-transformer validation of suffix-array speculative decoding
- Success threshold: At least 1.25x wall-clock tokens/sec improvement on repeated/noisy prompt families, no regression below 0.95x on low-repetition controls, and exact output equivalence to the target baseline.
- Stop condition: Stop if suffix lookup overhead or low acceptance keeps wall-clock throughput under 1.05x on repeated/noisy prompts.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-array-speculative-decode-vs-no-spec-baseline-8cdb21ae3e3c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
