# Suffix-Tree Drafter Speculative Decoding with Exact-Output Baseline

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-drafter-speculative-decoding-with-exact-output-baseline-27c18ab1b31f`
Run ID: `suffix-tree-drafter-speculative-decoding-with-exact-output-baseline-27c18ab1b31f-20260628T105135530821+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/92970d39d153

## What looked useful

Medium sweep over 17k-21k token streams found exact output in all cases. Best serial-pass speedups were 10.28x on repeated boilerplate and 15.03x on code templates with max_draft=32; markovish prose reached only 1.29x and unique adversarial text stayed at 1.00x.

## Boundaries and scale limits

Synthetic token streams only; no transformer target, tokenizer integration, GPU latency measurement, batching effects, KV-cache accounting, or real benchmark corpus was tested. Serial-pass speedup is a compute proxy, not measured LLM serving throughput.

## Claim scope

A causal prefix suffix-copy drafter with exact verification preserves the baseline output and reduces serial target verification passes on synthetic repetitive and code-template token streams, but provides little or no benefit on low-repetition or adversarial streams.

## Why it stopped

No-paper useful signal: this run is a synthetic mechanism benchmark and does not provide direct LLM serving evidence.

## Recommended next action

Run a bounded direct follow-up using a real tokenizer and small transformer-generated traces, measuring wall-clock latency and target forward-pass cost against standard speculative decoding controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-token trace validation for suffix-copy speculative decoding
- Success threshold: At least 1.5x measured wall-clock speedup on a repeated/code-like real-token corpus with exact output equality and no regression worse than 5% on prose/adversarial controls.
- Stop condition: Stop if accepted draft spans remain below 0.5 tokens per verification pass or drafter overhead erases pass-count savings on both code-like and prose real-token traces.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-drafter-speculative-decoding-with-exact-output-baseline-27c18ab1b31f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
