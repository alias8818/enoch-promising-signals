# RAM-Resident Tiny Distilled Draft for CPU Spec Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `ram-resident-tiny-distilled-draft-for-cpu-spec-decoding-9560e6b1216a`
Run ID: `ram-resident-tiny-distilled-draft-for-cpu-spec-decoding-9560e6b1216a-20260620T025701137097+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/1c521c1789c1

## What looked useful

RAM residency alone did not make speculative decoding useful. The proxy showed that high acceptance is the gating condition: full coverage and 1.0 acceptance barely cleared the 1.05x threshold, while 0.1488 acceptance at half coverage produced only 0.2885x greedy throughput.

## Boundaries and scale limits

Not a transformer or LLM benchmark; no real neural draft model, KV cache, tokenizer, sampling, long context, or multi-prompt corpus was tested. The only positive case used full state coverage in a first-order proxy.

## Claim scope

Bounded deterministic NumPy proxy for greedy CPU speculative decoding: a RAM-resident exact next-token table improved throughput by 1.0544x with exact output match, while partial low-acceptance draft tables were much slower than greedy decoding.

## Why it stopped

Proxy result is mixed and not publication-grade: it supports the mechanism only under exact full-state coverage and early-falsifies low-coverage tiny drafts for this CPU proxy.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should use a real small transformer target and a RAM-resident draft/cache with exact-output or valid sampling equivalence checks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small Transformer CPU Speculative Decoding With RAM-Resident Draft
- Success threshold: Mean throughput at least 1.10x greedy target baseline with no output-equivalence failures and lower-bound acceptance above the measured break-even point.
- Stop condition: Stop if acceptance remains below 0.50 or throughput remains below 1.00x after two draft sizes or prompt sets.

## Evidence references

- Artifact root: `<local-path>/projects/ram-resident-tiny-distilled-draft-for-cpu-spec-decoding-9560e6b1216a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
