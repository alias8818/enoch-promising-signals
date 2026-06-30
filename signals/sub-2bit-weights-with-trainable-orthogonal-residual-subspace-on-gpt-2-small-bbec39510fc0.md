# Sub-2bit weights with trainable orthogonal residual subspace on GPT-2-small

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sub-2bit-weights-with-trainable-orthogonal-residual-subspace-on-gpt-2-small-bbec39510fc0`
Run ID: `sub-2bit-weights-with-trainable-orthogonal-residual-subspace-on-gpt-2-small-bbec39510fc0-20260621T224752273477+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/5d3a42f703b2

## What looked useful

Ternary-only Conv1D GPT-2-small degraded WikiText-2 validation loss from 4.04 to 10.40. Orthogonal residuals recovered much of that damage, reaching loss 5.83 at rank 8 with 2.9% trainable parameters and loss 5.82 at rank 32 with 10.7% trainable parameters, but neither approached dense loss. The mechanism is real but insufficient in this bounded configuration.

## Boundaries and scale limits

Only 4096 validation tokens and short residual-only training runs were used. This is not a full-corpus fine-tune, not a quantized embedding/LM-head test, and not evidence for production compression or paper-grade GPT-2-small parity.

## Claim scope

Bounded GPT-2-small WikiText-2 probe: all GPT-2 Conv1D transformer weights were replaced by a 1.55 entropy-bit ternary base plus trainable low-rank residuals constrained columnwise orthogonal to the ternary base; embeddings and tied LM head remained dense.

## Why it stopped

No-paper useful signal: direct held-out GPT-2-small proxy evidence shows partial recovery but persistent large loss gap versus dense, so this is not publication-grade support for sub-2-bit GPT-2-small weights with orthogonal residuals.

## Recommended next action

Stop the paper path for this configuration; only continue with a bounded control study comparing orthogonal residuals against unconstrained LoRA-style residuals at matched parameter budgets and longer training.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Matched residual-control study for sub-2-bit GPT-2-small Conv1D weights
- Success threshold: A follow-up earns support only if the orthogonal residual reaches within 0.5 nats of dense validation loss and beats matched unconstrained/control residuals, or if the control identifies a clearly better residual formulation under the same sub-2-bit base.
- Stop condition: Stop if rank 32 remains above 5.0 validation loss after the longer bounded adaptation or fails to improve over matched unconstrained residual controls.

## Evidence references

- Artifact root: `<local-path>/projects/sub-2bit-weights-with-trainable-orthogonal-residual-subspace-on-gpt-2-small-bbec39510fc0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
