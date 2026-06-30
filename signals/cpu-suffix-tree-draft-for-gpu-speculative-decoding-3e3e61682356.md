# CPU Suffix-Tree Draft for GPU Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-suffix-tree-draft-for-gpu-speculative-decoding-3e3e61682356`
Run ID: `cpu-suffix-tree-draft-for-gpu-speculative-decoding-3e3e61682356-20260527T202521382020+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/80d69c8860f5

## What looked useful

Order-16 suffix lookup reached 7.13 accepted tokens per position for 8-token drafts on copy-heavy synthetic streams at about 200k proposed tokens/sec, but only 0.157 accepted tokens per position on the natural Shakespeare stream.

## Boundaries and scale limits

50k-token proxy streams, regex tokenization, Python implementation, no target GPU model, no BPE tokenizer, no end-to-end speculative decoding latency measurement.

## Claim scope

A CPU rolling suffix/prompt-lookup drafter can propose exact-match drafts quickly and with high acceptance on copy-heavy token streams, but not on ordinary Shakespeare-like natural prose in this proxy benchmark.

## Why it stopped

Closed as no-paper useful signal: the proxy supports workload-specific promise but early-falsifies a broad natural-language CPU suffix-drafter claim without direct GPU validation.

## Recommended next action

Run a bounded native drafter plus real tokenizer/GPU target-model integration on copy-heavy prompts and compare end-to-end tokens/sec against no-draft and simple n-gram baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Native suffix drafter with real GPU speculative decoding on copy-heavy prompts
- Success threshold: At least 20% end-to-end tokens/sec improvement on copy-heavy prompt suites, no more than 5% p95 latency regression, and no claimed improvement on prose unless directly measured.
- Stop condition: Stop if accepted tokens per position is below 1.0 or end-to-end throughput improvement is below 10% on copy-heavy prompts after native integration.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-suffix-tree-draft-for-gpu-speculative-decoding-3e3e61682356`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
