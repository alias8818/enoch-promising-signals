# Tiny Transformer Dynamic Anchor Reset Confirmation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tiny-transformer-dynamic-anchor-reset-confirmation-97b870418a`
Run ID: `tiny-transformer-dynamic-anchor-reset-confirmation-97b870418a-20260601T074843541629+0000`

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

- Parent run decision: Learned Tiny-Model Dynamic Anchor Reset Probe: enoch://control-plane/projects/learned-tiny-model-dynamic-anchor-reset-probe-9c3a0aa1ee/runs/learned-tiny-model-dynamic-anchor-reset-probe-9c3a0aa1ee-20260601T014326214944+0000
- Parent run decision: Dynamic Anchor State Reset for CPU Long-Context: enoch://control-plane/projects/dynamic-anchor-state-reset-for-cpu-long-context-9d03cf7a5256/runs/dynamic-anchor-state-reset-for-cpu-long-context-9d03cf7a5256-20260531T192750821344+0000

## What looked useful

Dynamic anchor reset achieved 0.6327 mean held-out long content accuracy versus 0.1343 for the standard absolute-position baseline, 0.1387 for periodic reset, and 0.1422 for no-position over seeds 101/202/303. The effect is aligned with anchor-relative position rather than generic positional ablation.

## Boundaries and scale limits

Synthetic mechanism benchmark only; 48-wide 2-layer transformer; 150 training steps for the complete comparison; no natural-language corpus, GPT-2-small-class model, long training, or large-scale validation.

## Claim scope

In a tiny dense causal transformer on synthetic anchor-delimited codebook next-token prediction, resetting positional IDs at anchor tokens substantially improves content-token accuracy versus an absolute-position baseline and reset ablations over three fixed seeds.

## Why it stopped

No-paper closure: the local Tier 2 synthetic mechanism confirmation supports the anchor-reset mechanism, but the evidence is not publication-grade because it is synthetic, tiny-model, and short-training only.

## Recommended next action

Run a bounded deepen test on a real or semi-real anchored retrieval/text benchmark with a GPT-2-small-class or parameter-matched dense baseline before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Dynamic Anchor Reset on Semi-Real Anchored Retrieval Text
- Success threshold: Dynamic reset must improve held-out anchored-span accuracy by at least 10 absolute percentage points or reduce anchored-token loss by at least 5% versus the dense baseline, with no worse than 1% degradation in overall validation loss, consistently across at least 2 of 3 seeds.
- Stop condition: Stop if dynamic reset fails to beat the dense baseline on anchored-span accuracy/loss in at least 2 of 3 seeds, or if gains appear only on synthetic codebook data and vanish on semi-real text.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-transformer-dynamic-anchor-reset-confirmation-97b870418a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
