# GaLore-Rank-Scheduled vs Adafactor on 125M Transformer

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `galore-rank-scheduled-vs-adafactor-on-125m-transformer-3e2d2d55ff41`
Run ID: `galore-rank-scheduled-vs-adafactor-on-125m-transformer-3e2d2d55ff41-20260621T045112256123+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/41fa2e2055c3

## What looked useful

The mechanism was not falsified as an optimizer because rank-scheduled GaLore reduced short-run synthetic loss slightly more than Adafactor, but the practical replacement hypothesis is not supported: mean loss-delta advantage was 0.0093 while mean step time was 46.4x slower, optimizer state was 241x larger, and CUDA peak allocation was 1.91x larger.

## Boundaries and scale limits

Synthetic data only; two seeds; short 20-30 step horizon; local approximate GaLore implementation rather than a fully optimized reference implementation; no natural-language perplexity or long-horizon stability evidence.

## Claim scope

On a local 123.75M-parameter GPT-style Transformer trained for 20-30 CUDA steps on a deterministic synthetic next-token task, the tested SVD-based rank-scheduled GaLore approximation showed only a tiny short-run loss-delta advantage over PyTorch Adafactor while being much slower and using substantially more optimizer state and CUDA memory.

## Why it stopped

Bounded local evidence is an early practical falsification of the naive SVD-based rank-scheduled GaLore variant versus Adafactor, not a full validation of all GaLore implementations.

## Recommended next action

Stop this run as no-paper useful signal; only revisit with a bounded optimized-projection GaLore implementation that must beat Adafactor on both loss-per-token and wall-clock or memory at the same 125M scale.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Optimized rank-scheduled GaLore projection versus Adafactor at 125M
- Success threshold: At equal token budget, optimized rank-scheduled GaLore must improve final loss by at least 0.02 over Adafactor while staying within 2x Adafactor wall-clock and within 1.25x Adafactor peak CUDA allocation, or show at least 25% lower optimizer-state memory at no worse loss.
- Stop condition: Stop if projection overhead remains above 2x Adafactor wall-clock or peak CUDA allocation remains above 1.25x without a loss improvement of at least 0.02 after the matched runs.

## Evidence references

- Artifact root: `<local-path>/projects/galore-rank-scheduled-vs-adafactor-on-125m-transformer-3e2d2d55ff41`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
