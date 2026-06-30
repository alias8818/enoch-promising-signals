# CPU Cascaded Speculative Decoding with N-gram Draft

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-cascaded-speculative-decoding-with-n-gram-draft-4ec66f74ecd0`
Run ID: `cpu-cascaded-speculative-decoding-with-n-gram-draft-4ec66f74ecd0-20260622T013034588550+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/c48d07e29ef3

## What looked useful

Cascade acceptance was 0.926 on structured_repeat, 0.794 on mixed_repeat, and 0.029 on low_repeat. Exact output matching held for all cascaded runs. Mean target batch call reduction was 0.626 and mean modeled speedup was 2.503x under the recorded cost model.

## Boundaries and scale limits

Synthetic n-gram corpora only; no real CPU LLM forward passes, tokenizer effects, hardware counters, multithread serving, or production text workloads were tested.

## Claim scope

In a bounded deterministic n-gram verifier, cascaded n-gram speculative drafting preserved exact greedy target output and reduced target batch calls on synthetic repeated-context streams, but acceptance collapsed on low-repeat streams under target/draft data mismatch.

## Why it stopped

Closed as no-paper useful signal because this run is a synthetic/proxy validation, not direct publication-grade CPU LLM evidence.

## Recommended next action

Run a bounded direct CPU LLM validation with a GPT-2-small-class target, real text corpora, exact-output checks, direct latency, and hardware counters; stop if low-repeat text still has poor acceptance or latency regresses.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct CPU LLM validation for cascaded n-gram speculative decoding
- Success threshold: At least 1.20x direct median decode speedup on repeated-context real text with exact output equality and no more than 5% slowdown on low-repeat real text.
- Stop condition: Stop if exact output diverges, repeated-context speedup is below 1.05x, or low-repeat workloads regress by more than 5%.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-cascaded-speculative-decoding-with-n-gram-draft-4ec66f74ecd0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
