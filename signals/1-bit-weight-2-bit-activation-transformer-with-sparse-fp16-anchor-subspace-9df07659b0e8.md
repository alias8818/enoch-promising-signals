# 1-bit weight + 2-bit activation transformer with sparse FP16 anchor subspace

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `1-bit-weight-2-bit-activation-transformer-with-sparse-fp16-anchor-subspace-9df07659b0e8`
Run ID: `1-bit-weight-2-bit-activation-transformer-with-sparse-fp16-anchor-subspace-9df07659b0e8-20260610T014302838484+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b44fd0375346

## What looked useful

Sensitivity-selected 6.25% FP16 anchors reduced W1A2 relative MSE by 6.0% on Gaussian inputs and 23.7% on heavy-tailed inputs versus no-anchor W1A2; on heavy-tailed inputs the same anchors were 21.8% better than random 6.25% anchors.

## Boundaries and scale limits

No training, no language-model perplexity, no learned anchor policy, no kernel benchmark, no GPT-2-small-class or larger validation.

## Claim scope

In a synthetic single-block transformer forward-fidelity probe, sparse FP16 input anchors improve W1A2 reconstruction error, especially when activation and weight salience is heavy-tailed.

## Why it stopped

Proxy-only useful signal; the run directly tested forward fidelity but not trainability, perplexity, or hardware efficiency, so it is not paper-ready.

## Recommended next action

Run a bounded trained tiny autoregressive transformer follow-up comparing W1A2, W1A2 plus learned/sensitivity anchors, and tuned W2A2 at matched memory budget.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny trained LM validation for sparse FP16 anchors in W1A2 transformers
- Success threshold: W1A2 plus sensitivity or learned anchors improves validation loss by at least 5% versus W1A2 no-anchor and beats random anchors at the same anchor ratio without exceeding the matched memory budget.
- Stop condition: Stop if anchor variants fail to improve validation loss over W1A2 no-anchor after three seeds, diverge more often than the no-anchor control, or require anchor ratios that erase the low-bit memory advantage.

## Evidence references

- Artifact root: `<local-path>/projects/1-bit-weight-2-bit-activation-transformer-with-sparse-fp16-anchor-subspace-9df07659b0e8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
