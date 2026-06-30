# ResidualChannel-1Bit

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residualchannel-1bit-a908184542ab`
Run ID: `residualchannel-1bit-a908184542ab-20260525T163001744879+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/27448e2fdc40

## What looked useful

Residual 1-bit validation loss was 2.0346 mean over 3 seeds versus 2.0510 for pure 1-bit, a 0.0164 nat / 0.80% improvement, with about 10.2% more trainable parameters. Dense baseline was 1.8558, showing a large remaining quality gap.

## Boundaries and scale limits

Local proxy only: 241k-266k parameter toy character model, 3 seeds, 2000 optimization steps, no parameter-matched widened 1-bit control, no GPT-2-small-class run, no optimized 1-bit inference kernel or downstream benchmark.

## Claim scope

In a tiny 2-layer character-level Transformer on Tiny Shakespeare, a rank-8 full-precision residual path added to STE 1-bit linear layers modestly improved 2000-step validation loss versus pure 1-bit linear layers, but remained much worse than a dense baseline.

## Why it stopped

No-paper useful signal: bounded local evidence supports a modest mechanism effect, but the effect is small, parameter-overhead-confounded, and far from dense quality; this is not full validation.

## Recommended next action

Run a bounded parameter-matched deepen test comparing rank-8 residual 1-bit against widened pure 1-bit and residual ranks 2/4/8/16 at the same trainable-parameter budget.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Parameter-Matched Residual Channel 1-Bit Ablation
- Success threshold: Residual 1-bit beats the parameter-matched widened pure 1-bit control by at least 1% mean validation loss over 3 seeds, with paired improvement on at least 2 of 3 seeds.
- Stop condition: Stop if the parameter-matched residual gain is below 0.5% mean validation loss or inconsistent across seeds, because the current effect is too small for a larger LM run.

## Evidence references

- Artifact root: `<local-path>/projects/residualchannel-1bit-a908184542ab`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
