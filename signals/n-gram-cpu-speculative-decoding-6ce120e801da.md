# N-gram CPU speculative decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-cpu-speculative-decoding-6ce120e801da`
Run ID: `n-gram-cpu-speculative-decoding-6ce120e801da-20260528T223653636455+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/3af9a9903689

## What looked useful

The mechanism works when repetition is present and costs roughly 1.5-2.1 microseconds per output token in the Python prototype, but real continuation traces accept only about 3.3-4.1% of drafted tokens; accepted-token yield, not CPU overhead, is the likely bottleneck.

## Boundaries and scale limits

No neural verifier or end-to-end serving runtime was run. The evidence is limited to token-trace replay on two public-domain/proxy text corpora plus synthetic controls, with at most 200k tokens per trace.

## Claim scope

Trace-level BPE-token replay on Tiny Shakespeare and Alice in Wonderland shows CPU n-gram speculative drafting is cheap and control-sensitive, but produces only modest real-corpus target-call reduction of 1.11x to 1.17x.

## Why it stopped

No-paper useful signal: trace replay supports the mechanism but real-corpus gains are modest and proxy-only, not a full validation.

## Recommended next action

Stop paper work for this run; the only warranted next step is a bounded end-to-end small-model runtime test on prompt-copy-heavy tasks to see whether wall-clock decode speedup exceeds 1.25x.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end prompt-copy n-gram speculation with a small local verifier
- Success threshold: At least 1.25x median wall-clock decode speedup on prompt-copy-heavy tasks with exact output preservation for deterministic decoding and no worse than 1.05x slowdown on non-copy controls.
- Stop condition: Stop if integrated acceptance remains below 8% drafted-token acceptance or median wall-clock speedup is below 1.10x on two prompt-copy-heavy task sets.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-cpu-speculative-decoding-6ce120e801da`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
