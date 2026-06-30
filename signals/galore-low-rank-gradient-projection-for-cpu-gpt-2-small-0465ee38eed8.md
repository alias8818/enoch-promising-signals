# GaLore low-rank gradient projection for CPU GPT-2-small

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `galore-low-rank-gradient-projection-for-cpu-gpt-2-small-0465ee38eed8`
Run ID: `galore-low-rank-gradient-projection-for-cpu-gpt-2-small-0465ee38eed8-20260628T135322027394+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/5b6138e20214

## What looked useful

Calibrated run reduced optimizer state from 705.71 MB to 9.56 MB, but increased wall time from 1.87 s to 17.99 s and ended 108.27 loss points above AdamW after two steps.

## Boundaries and scale limits

Synthetic data, reduced vocab 4096, batch 1, sequence length 16, two calibrated steps, minimal local GaLore-style optimizer; not a full GPT-2-small corpus/tokenizer convergence result.

## Claim scope

On a bounded CPU GPT-2-small-shaped synthetic probe, exact-SVD GaLore-style projection greatly reduces optimizer-state memory but is much slower and shows worse two-step loss movement than AdamW.

## Why it stopped

Proxy/early falsification for the simple exact-SVD CPU GaLore hypothesis: memory compression works, but runtime and early optimization behavior are not practical in the bounded GPT-2-small-shaped CPU probe.

## Recommended next action

Stop this run as no-paper useful evidence; next bounded test should replace exact SVD with randomized or much less frequent projection and require <2x AdamW wall time while preserving most state-memory savings.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Randomized-projector GaLore CPU GPT-2-small-shaped probe
- Success threshold: GaLore variant optimizer-state bytes <= 10% of AdamW, wall time <= 2x AdamW, and final synthetic loss within 5% of AdamW after the bounded step budget.
- Stop condition: Stop if overhead remains >2x AdamW after projector changes or if loss remains clearly worse than AdamW under matched learning-rate tuning.

## Evidence references

- Artifact root: `<local-path>/projects/galore-low-rank-gradient-projection-for-cpu-gpt-2-small-0465ee38eed8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
