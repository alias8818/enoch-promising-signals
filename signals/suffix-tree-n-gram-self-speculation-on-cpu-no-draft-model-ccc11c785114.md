# Suffix-tree n-gram self-speculation on CPU (no draft model)

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-n-gram-self-speculation-on-cpu-no-draft-model-ccc11c785114`
Run ID: `suffix-tree-n-gram-self-speculation-on-cpu-no-draft-model-ccc11c785114-20260613T191102124889+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/fee21034b133

## What looked useful

Suffix-history self-speculation works when exact repetition is present: code boilerplate reached 0.913 proposal coverage, 0.722 acceptance, median accepted span 8, and a 5.54x ideal target-call upper bound. It failed on one-pass prose and random control with zero proposals, and templated logs were brittle with 0.306 acceptance and median accepted span 1.

## Boundaries and scale limits

Single-process CPU replay benchmark only; streams are small and mostly synthetic or embedded; ideal speedup is a target-call upper bound, not measured wall-clock model acceleration.

## Claim scope

Bounded replay evidence for suffix-history n-gram proposal coverage and exact-token acceptance on embedded/synthetic streams; no real transformer latency was measured.

## Why it stopped

Proxy replay evidence is mixed and insufficient for a paper or broad speedup claim; it is an early bounded mechanism test, not full validation.

## Recommended next action

Stop this run as no-paper useful mechanism evidence; next run should wrap the proposer around a small CPU transformer and compare latency against greedy decoding on repetitive code/log prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Measure suffix n-gram self-speculation latency on a small CPU transformer
- Success threshold: At least 1.25x measured tokens/sec improvement over greedy decoding on repetitive code/log prompts, with no improvement claim on controls unless observed, and identical greedy-token outputs under deterministic decoding.
- Stop condition: Stop if measured CPU latency is below 1.05x greedy after implementation overheads, or if accepted draft spans do not persist under real model tokenization and verification.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-n-gram-self-speculation-on-cpu-no-draft-model-ccc11c785114`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
