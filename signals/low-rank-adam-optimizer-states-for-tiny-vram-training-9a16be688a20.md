# Low-Rank Adam Optimizer States for Tiny-VRAM Training

Status: `useful_signal`
Project ID: `low-rank-adam-optimizer-states-for-tiny-vram-training-9a16be688a20`
Run ID: `low-rank-adam-optimizer-states-for-tiny-vram-training-9a16be688a20-20260518T093706257823+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/6c6ccfa4c7b7

## What looked useful

Persistent low-rank moment storage gives real byte savings, but pure low-rank second moments create denominator coverage/conditioning problems and exact SVD recompression dominates runtime. A viable tiny-VRAM optimizer likely needs a hybrid diagonal or factored second-moment residual rather than pure low-rank Adam states.

## Boundaries and scale limits

Tested only synthetic low-rank and full-rank matrix regression on a single GB10 with dense transient moment reconstruction; no transformer, real corpus, GPT-2-small-class baseline, production low-memory kernel, or constrained-VRAM peak-memory validation was run.

## Claim scope

On synthetic 256x256 matrix-regression probes, truncated-SVD Adam moment states reduce persistent optimizer-state bytes by 4-16x but are slower, less accurate than Adam, numerically fragile at standard Adam epsilon, and do not demonstrate end-to-end peak-VRAM savings.

## Why it stopped

Medium synthetic evidence is a proxy early falsification of the straightforward pure low-rank Adam-state formulation, not a full validation of all possible low-rank optimizer-state designs.

## Recommended next action

Stop this pure SVD-truncated Adam-state line as no-paper evidence; the bounded next test is a hybrid low-rank first moment plus diagonal or row-column second-moment residual on a tiny transformer language-model task.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Hybrid Low-Rank First Moment with Diagonal Second-Moment Residual
- Success threshold: At least 4x persistent optimizer-state reduction versus Adam, no SVD/conditioning failures, final validation loss within 5% of the best memory-efficient baseline, and measured peak CUDA memory reduction on the constrained task.
- Stop condition: Stop if the hybrid variant still requires dense moment reconstruction, remains more than 3x slower than Adam/Adafactor at equal task size, or misses the validation-loss threshold across two seeds.

## Evidence references

- Artifact root: `<local-path>/projects/low-rank-adam-optimizer-states-for-tiny-vram-training-9a16be688a20`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
