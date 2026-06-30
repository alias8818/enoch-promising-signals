# N-gram suffix-tree speculative decoding on CPU without draft-model VRAM

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-suffix-tree-speculative-decoding-on-cpu-without-draft-model-vram-f441727c9192`
Run ID: `n-gram-suffix-tree-speculative-decoding-on-cpu-without-draft-model-vram-f441727c9192-20260613T153558890276+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/032f66016b8b

## What looked useful

The proposer reached 10.629x idealized target-call speedup on a repeated-template control, but only 1.070x on Tiny Shakespeare and 1.116x on local project text; a low-repeat control showed 1.000x. This supports a narrow repetitive-output mechanism but not a general draft-model replacement.

## Boundaries and scale limits

No neural target model was run; results use exact-match oracle acceptance over token traces with up to 12000 tokens per corpus and 64 CPU-only configurations. End-to-end inference latency, model-tokenizer behavior, batching, cache effects, and target quality were not measured.

## Claim scope

Bounded trace-level evidence for an online CPU n-gram/suffix-index proposer without a draft model: strong idealized target-call reduction on highly repetitive streams, weak reduction on natural/project text.

## Why it stopped

Proxy/early falsification of the broad general-acceleration claim: natural/project traces showed only 6.95% to 11.59% idealized target-call reduction before real inference overhead.

## Recommended next action

Stop this run as no-paper useful-signal evidence; if pursued, integrate the proposer into a small CPU target-LM decode loop and require at least 1.20x end-to-end speedup on repetitive/code-like prompts with safe bypass on ordinary prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end CPU target-LM validation for suffix speculative decoding on repetitive outputs
- Success threshold: At least 1.20x end-to-end tokens/sec or latency improvement on repetitive/code-like prompts, no output mismatch under deterministic decoding, and less than 5% slowdown on low-repeat ordinary prompts with bypass enabled.
- Stop condition: Stop if real target-model integration shows under 1.10x end-to-end speedup on repetitive/code-like prompts or more than 5% slowdown on ordinary prompts after adding the acceptance-rate bypass.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-suffix-tree-speculative-decoding-on-cpu-without-draft-model-vram-f441727c9192`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
