# Ternary Main Weights with Learned Low-Rank Residual Correction Channels

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `ternary-main-weights-with-learned-low-rank-residual-correction-channels-01e939aad111`
Run ID: `ternary-main-weights-with-learned-low-rank-residual-correction-channels-01e939aad111-20260525T042901525077+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/5a872fbb1a46

## What looked useful

Rank-8 residual channels improved ternary-only validation loss in all three 800-step seeds, reducing mean validation loss from 2.17720 to 2.16933, while dense remained much better at 2.07514. In the 1200-step run, rank-8 improved ternary-only from 2.07711 to 2.06234 at about 24.3% of the dense storage proxy. A seed-7 rank sweep improved from rank-4 2.16730 to rank-16 2.13906 and rank-32 2.13649.

## Boundaries and scale limits

Evidence is limited to a toy char-LM, 800-1200 optimizer steps, one small transformer shape, three 800-step seeds for rank-8, and a seed-7 rank sweep. It does not validate GPT-2-small-class models, subword corpora, convergence-scale training, actual ternary inference kernels, or training-memory savings.

## Claim scope

On a small Tiny Shakespeare character-level transformer, learned ternary projection weights with low-rank residual correction channels train stably and consistently improve validation loss over ternary-only weights, with rank-dependent gains under a simple inference storage proxy.

## Why it stopped

The local evidence supports a mechanism but remains a toy/proxy validation with small rank-8 gains and a clear dense quality gap, so this run should close as no-paper useful signal rather than positive paper evidence.

## Recommended next action

Do not write a paper from this run; run a bounded follow-up on a standard subword LM corpus with storage-matched dense/ternary/ternary+residual controls and residual rank ablations.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Storage-Matched Subword LM Validation for Ternary Weights with Low-Rank Residuals
- Success threshold: Ternary-plus-residual recovers at least 25% of the dense-to-ternary validation loss gap in mean final loss across seeds, remains below 50% of dense estimated inference storage, and beats a storage-matched reduced dense control.
- Stop condition: Stop if rank-16 or rank-32 residuals fail to recover at least 10% of the dense-to-ternary gap after the planned training budget or if a storage-matched dense control dominates the residual approach.

## Evidence references

- Artifact root: `<local-path>/projects/ternary-main-weights-with-learned-low-rank-residual-correction-channels-01e939aad111`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
