# Binary Weights with Dense Residual Adapter Path

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `binary-weights-with-dense-residual-adapter-path-de73ef69c812`
Run ID: `binary-weights-with-dense-residual-adapter-path-de73ef69c812-20260621T195512242535+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/59f15e12bd75

## What looked useful

Binary-only validation MSE was 2.7906x dense; binary plus dense residual adapter reduced validation MSE to 0.3244x of binary-only and 0.9054x of dense. The adapter was effectively dense, with 99.38% of entries above 1e-3, adapter norm 92.69% of the binary base norm, and storage accounting slightly exceeding dense baseline bits.

## Boundaries and scale limits

Only synthetic MLP regression was tested: 5 seeds, 2048 train examples, 1024 validation examples, 32 input dimensions, 64 hidden units, 240 epochs. No transformer, language-model, packed binary inference, low-rank adapter, sparse adapter, or GPT-2-small-class baseline was run.

## Claim scope

In a small NumPy teacher-student two-layer MLP regression probe, an unconstrained same-shape dense residual adapter path repairs most of the validation loss penalty from sign-binarized weights, but it does not preserve a compression advantage.

## Why it stopped

No-paper useful signal: the local mechanism works as an accuracy repair, but the tested unconstrained dense residual path is not a compression-positive method and the evidence is a small synthetic proxy rather than direct model-scale validation.

## Recommended next action

Run a bounded residual-budget sweep using low-rank or sparse adapters and require a real storage advantage versus dense while preserving most of the binary-to-dense accuracy repair.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Budget-capped residual adapters for binary-weight MLPs
- Success threshold: At least one budgeted adapter setting achieves validation MSE no worse than binary_mlp - 0.70 * (binary_mlp - dense_mlp) while using less than 50% of dense baseline inference bits including bias.
- Stop condition: Stop if all budgeted adapters either use at least 50% of dense inference bits or recover less than 50% of the binary-to-dense validation-loss gap.

## Evidence references

- Artifact root: `<local-path>/projects/binary-weights-with-dense-residual-adapter-path-de73ef69c812`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
