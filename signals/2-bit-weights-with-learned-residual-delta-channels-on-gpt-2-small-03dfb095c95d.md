# 2-bit weights with learned residual delta channels on GPT-2-small

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `2-bit-weights-with-learned-residual-delta-channels-on-gpt-2-small-03dfb095c95d`
Run ID: `2-bit-weights-with-learned-residual-delta-channels-on-gpt-2-small-03dfb095c95d-20260620T122543709007+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/4a28c0fcbf95

## What looked useful

Naive 2-bit projection quantization collapsed GPT-2-small validation loss from 3.8662 to 36.3028. Learned residual delta channels improved loss to 7.5793 at 3.125% residual channels and 7.0612 at 12.5%, showing a real recovery mechanism but not practical competitiveness in this setup.

## Boundaries and scale limits

Short bounded CUDA run only: one seed, 32,768 training tokens, 16,384 validation tokens, 40 residual-only steps, embeddings and lm_head left dense, no packed inference kernels, no full-corpus validation, no comparison to modern production PTQ baselines.

## Claim scope

On GPT-2-small with Conv1D projection matrices replaced by naive per-output-channel 2-bit weights, sparse learned residual delta channels trained for 40 local steps on WikiText-2 recover a large fraction of the collapse but remain much worse than dense GPT-2-small on a 16,384-token validation slice.

## Why it stopped

Bounded direct evidence supports partial recovery but early-falsifies the practical claim that simple learned residual delta channels make naive 2-bit GPT-2-small projection weights competitive with dense quality.

## Recommended next action

Stop this run as no-paper useful signal; a bounded deepen follow-up should test smarter channel selection or lower-rank residual parameterization against GPTQ/AWQ/NF4-style baselines before any scale-up.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Smarter residual channel selection for 2-bit GPT-2-small projections
- Success threshold: At equal or lower residual storage than 12.5% dense residual channels, reduce validation loss to within 1.0 nat of dense GPT-2-small and outperform the quantization-error-selected residual baseline by at least 0.5 nat.
- Stop condition: Stop if task-sensitivity or low-rank residual variants remain above 6.0 validation loss or fail to beat the current 12.5% residual-channel loss by at least 0.5 nat under the same evaluation protocol.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-weights-with-learned-residual-delta-channels-on-gpt-2-small-03dfb095c95d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
