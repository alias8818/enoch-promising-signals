# Sub-2-bit weights with per-layer learned residual channels

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `sub-2-bit-weights-with-per-layer-learned-residual-channels-543bd4d49e6e`
Run ID: `sub-2-bit-weights-with-per-layer-learned-residual-channels-543bd4d49e6e-20260613T200151956251+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/63c9cb3c594b

## What looked useful

Across two seeds, frozen 1-bit validation loss averaged 2.9454 versus dense 2.3917. Rank-1 residual channels at 1.2545 effective bits recovered 66.6% of the 1-bit gap; rank-2 at 1.5089 effective bits recovered 73.8%. Rank-4 and rank-8 recovered more but exceeded 2 effective bits.

## Boundaries and scale limits

Only a tiny character LM, 600 dense training steps, 300 residual adaptation steps, two seeds, no GPT-2-small-class baseline, no packed-kernel runtime, and bit accounting only for quantized linear weights plus residual parameters.

## Claim scope

On a two-layer width-96 character-level causal Transformer trained briefly on Tiny Shakespeare, frozen 1-bit per-output-channel linear weights plus learned low-rank residual channels recover much of the validation-loss gap versus the dense baseline while rank-1 and rank-2 variants remain below 2 effective bits per quantized linear weight.

## Why it stopped

Useful mechanism signal, but this is a small proxy validation and not direct publication-grade evidence for sub-2-bit weight architectures at realistic model scale.

## Recommended next action

Run a deeper bounded follow-up on a token-level nanoGPT or GPT-2-small-class setup with equal-memory baselines, full model bit accounting, and at least three seeds before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Token-level residual-channel sub-2-bit validation against equal-memory baselines
- Success threshold: Rank-1 or rank-2 residual-channel model remains below 2 effective bits for quantized linear weights, recovers at least 50% of the frozen 1-bit validation-loss gap, and is competitive with an equal-memory low-bit baseline.
- Stop condition: Stop if residual-channel variants recover less than 50% of the 1-bit gap in two consecutive seeds or are dominated by equal-memory low-bit baselines after matched adaptation budget.

## Evidence references

- Artifact root: `<local-path>/projects/sub-2-bit-weights-with-per-layer-learned-residual-channels-543bd4d49e6e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
