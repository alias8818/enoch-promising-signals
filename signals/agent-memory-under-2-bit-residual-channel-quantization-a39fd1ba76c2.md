# Agent memory under 2-bit residual-channel quantization

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `agent-memory-under-2-bit-residual-channel-quantization-a39fd1ba76c2`
Run ID: `agent-memory-under-2-bit-residual-channel-quantization-a39fd1ba76c2-20260620T204852117115+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a257891428a7

## What looked useful

Residual-channel ternary reached top1 accuracy 0.9716 at noise 0.10 and 0.4190 at noise 0.20, versus 0.6614/0.1660 for sign_1bit and 0.8110/0.2500 for 2-bit uniform. This supports a channel-aware compression mechanism under favorable clustered-memory assumptions, but not a paper-ready agent-memory claim.

## Boundaries and scale limits

Synthetic vectors only; 4,096 memory items, 128 dimensions, 32 generated channels, 5 seeds, 4 noise levels, 2,048 queries per condition. No real LLM agent, real embeddings, real replay traces, or long-horizon memory updates were tested.

## Claim scope

In a deterministic clustered synthetic repeated-agent memory retrieval benchmark, a shared-channel-centroid plus ternary residual encoding preserved exact top-k retrieval better than 1-bit sign and generic 2-bit uniform baselines while using about 1.837 effective bits per scalar in the main configuration.

## Why it stopped

Stopped after a bounded CPU proxy run: the mechanism looks promising in synthetic retrieval, but the result is not direct/full validation of agent memory quality.

## Recommended next action

Run a bounded deepen test on real replay-task embeddings with observed session/topic/user channels and a noisy-channel ablation before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual-channel memory quantization on real replay embeddings with noisy channel labels
- Success threshold: Residual-channel encoding remains below 2 effective bits/scalar and achieves at least 90% of dense top1 retrieval at low/moderate noise or improves top1 by at least 10 percentage points over generic 2-bit uniform on real replay embeddings without reducing downstream answer accuracy by more than 5 percentage points.
- Stop condition: Stop if residual-channel encoding fails to beat generic 2-bit uniform by at least 3 percentage points top1 on real embeddings or if channel-label noise erases the advantage before realistic noise levels.

## Evidence references

- Artifact root: `<local-path>/projects/agent-memory-under-2-bit-residual-channel-quantization-a39fd1ba76c2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
