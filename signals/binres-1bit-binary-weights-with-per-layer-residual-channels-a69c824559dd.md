# BinRes-1bit: Binary Weights with Per-Layer Residual Channels

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `binres-1bit-binary-weights-with-per-layer-residual-channels-a69c824559dd`
Run ID: `binres-1bit-binary-weights-with-per-layer-residual-channels-a69c824559dd-20260628T065032102782+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/5c84415f6acd

## What looked useful

Residual channels monotonically improved relative weight MSE, but even rank 32 at 2.38x fp16 compression left relative logit MSE of 0.339 on gaussian teachers and 0.240 on structured-lowrank teachers, with top-1 agreement of 57.3% and 67.0%.

## Boundaries and scale limits

No trained model, no transformer, no real checkpoint, no language-model perplexity, no learned residual-channel SGD, no GPU/kernel measurement; residual channels were favorable SVD approximations on synthetic weights.

## Claim scope

CPU-only NumPy proxy on synthetic dense MLP teachers: scaled 1-bit sign weights plus optimal per-layer low-rank residual channels reduce matrix reconstruction error but do not strongly preserve random-input logits at the tested compression budgets.

## Why it stopped

Proxy early falsification of paper-readiness: mechanism improves reconstruction but does not provide direct/full validation or strong functional preservation.

## Recommended next action

Stop this run as a proxy-only useful signal; next bounded test should train or compress a small transformer with dense and pure-binary controls before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Train a Small Transformer with BinRes 1-bit Layers
- Success threshold: At least 4x fp16 storage compression with less than 5% relative validation-loss degradation versus dense and a clear improvement over pure binary weights.
- Stop condition: Stop if BinRes does not beat pure binary validation loss by at least 10% relative gap reduction or cannot maintain at least 4x fp16 storage compression.

## Evidence references

- Artifact root: `<local-path>/projects/binres-1bit-binary-weights-with-per-layer-residual-channels-a69c824559dd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
