# Ternary GPT-2 with FP16 Attention Head Residual

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `ternary-gpt-2-with-fp16-attention-head-residual-3174513ec594`
Run ID: `ternary-gpt-2-with-fp16-attention-head-residual-3174513ec594-20260628T173651946513+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ca36c73b2e4f

## What looked useful

Dense mean best validation loss was 2.3613; pure ternary was 2.4021; ternary plus FP16 attention residual was 2.4076. The residual arm added 32,770 parameters, trained nonzero residual weights with mean gate sigmoid 0.1248, but was worse than pure ternary on average and won only 1 of 6 paired seeds.

## Boundaries and scale limits

2-layer 128-hidden byte model, 128-token context, 500 optimizer steps, six seeds, Tiny Shakespeare only. This does not validate GPT-2-small-scale behavior, tokenizer/corpus robustness, long-run convergence, downstream quality, or deployment compression/performance.

## Claim scope

In a tiny GPT-2-style byte-level causal LM on Tiny Shakespeare, STE ternary attention/MLP projections were consistently worse than a dense control, and adding a zero-initialized trainable FP16 attention-output residual path did not improve pure ternary validation loss across six seeds.

## Why it stopped

Bounded local proxy produced an early falsification of the claimed residual benefit: the FP16 attention residual did not beat pure ternary validation loss despite training and adding parameters. This is not a full-scale validation.

## Recommended next action

Stop this formulation as no-paper evidence; only revisit with a parameter-matched residual/control redesign before spending larger GPT-2-small-scale compute.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/ternary-gpt-2-with-fp16-attention-head-residual-3174513ec594`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
