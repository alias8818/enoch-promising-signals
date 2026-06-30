# Layer-Shared Adam States for Transformer Blocks

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `layer-shared-adam-states-for-transformer-blocks-8d3bf81fc44f`
Run ID: `layer-shared-adam-states-for-transformer-blocks-8d3bf81fc44f-20260526T101631174142+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/1a4d425f5a56

## What looked useful

Layer-shared Adam states are mechanically viable and give large optimizer-state savings, but the naive shared m/v formulation loses convergence quality versus AdamW. Higher LR partially mitigates the gap: at lr=0.003 over 300 steps, shared AdamW reached mean val loss 0.231 versus AdamW 0.074 while retaining 81.1% estimated state reduction.

## Boundaries and scale limits

Proxy task only; tiny Transformer; no natural-language corpus, GPT-2-small-class run, long-horizon stability test, distributed training, or full memory-pressure validation. Tested one sharing rule: averaged homologous gradients updating shared m/v tensors for all block layers.

## Claim scope

On a 6-layer, d_model=128 causal Transformer trained on a synthetic arithmetic next-token task, sharing AdamW first/second moment tensors across homologous Transformer block parameters reduced estimated optimizer-state memory by 81.1% but underperformed standard AdamW after matched 300-step training, including after a small shared-optimizer learning-rate sweep.

## Why it stopped

The bounded Transformer proxy produced a mixed result: substantial optimizer-state reduction but consistently worse validation loss than AdamW, so the naive layer-shared Adam-state idea is not paper-ready.

## Recommended next action

Stop this run as no-paper useful evidence; next bounded test should evaluate a different variant such as per-layer first moments with shared/compressed second moments on a small real-token LM benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Per-layer first moments with shared second moments for Transformer Adam memory reduction
- Success threshold: A variant retains at least 40% optimizer-state memory reduction while final validation loss is within 5% relative of tuned AdamW on the bounded benchmark across three seeds.
- Stop condition: Stop if all variants exceed AdamW validation loss by more than 10% relative after LR tuning or if memory savings fall below 25%.

## Evidence references

- Artifact root: `<local-path>/projects/layer-shared-adam-states-for-transformer-blocks-8d3bf81fc44f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
