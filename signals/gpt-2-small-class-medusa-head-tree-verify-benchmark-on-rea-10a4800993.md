# GPT-2-small-class Medusa head tree-verify benchmark on real text

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `gpt-2-small-class-medusa-head-tree-verify-benchmark-on-rea-10a4800993`
Run ID: `gpt-2-small-class-medusa-head-tree-verify-benchmark-on-rea-10a4800993-20260630T183617207982+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Self-Speculative Decoding via Medusa Heads with Tree Verify: enoch://control-plane/projects/self-speculative-decoding-via-medusa-heads-with-tree-verify-cb9bb2d46bb9/runs/self-speculative-decoding-via-medusa-heads-with-tree-verify-cb9bb2d46bb9-20260630T181606907350+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/98573a40af07

## What looked useful

The tested cheap linear-head variant never accepted future-head tokens beyond the guaranteed base-model next token: mean accepted draft length was 1.0, mean max accepted draft length was 1.0, and the Medusa-style path was about 4.17x slower than cached greedy decode on the bounded run.

## Boundaries and scale limits

Only 128 training blocks, one training epoch, horizons 2-4, top-1 draft chain, simple PyTorch verifier, and no optimized tree attention or full Medusa architecture. The aborted 512-block run produced no metrics and is not evidence.

## Claim scope

Bounded GPT-2-small-class benchmark: frozen gpt2 with linear Medusa-style future-token heads trained on WikiText-2 real-token targets and evaluated by greedy tree verification on held-out WikiText-2 prompts.

## Why it stopped

Bounded real-text early falsification: the tested linear future heads had near-zero future-token accuracy and produced no verifier-accepted lookahead, so this exact setup is not worth scaling or paper writing.

## Recommended next action

Stop this variant; if continuing, run a bounded follow-up that trains heads on base-model greedy continuations and evaluates a top-k tree before any larger scaling.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Distilled GPT-2-small Medusa heads with top-k tree verification on real text
- Success threshold: Mean accepted draft length >= 1.5, all verifier-gated outputs match greedy decode, and wall time is no worse than 1.2x cached greedy in the unoptimized harness or shows a model-call reduction that justifies optimization.
- Stop condition: Stop if mean accepted draft length remains <= 1.1 after a bounded distilled-head run of at least 512 training blocks and 16 held-out prompts.

## Evidence references

- Artifact root: `<local-path>/projects/gpt-2-small-class-medusa-head-tree-verify-benchmark-on-rea-10a4800993`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
