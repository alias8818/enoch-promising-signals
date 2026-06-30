# Ternary weights with structured residual projection at sub-1-bit

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `ternary-weights-with-structured-residual-projection-at-sub-1-bit-3db5111fa8ca`
Run ID: `ternary-weights-with-structured-residual-projection-at-sub-1-bit-3db5111fa8ca-20260620T120531984578+0000`

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

DCT residual k=2 at 0.8117 aggregate bpp improved medium MLP accuracy over the 0.5708 bpp d=0.10 ternary base (0.2068 vs 0.1766) and over a random k=2 basis at the same bpp (0.1854), but ternary-only d=0.15-0.17 at 0.7617-0.8295 bpp achieved 0.2452-0.2514 accuracy. Smooth matrix relative MSE improved from 0.5753 to 0.5491 with DCT k=2, while Gaussian controls barely improved.

## Boundaries and scale limits

No real language model, no GPT-2-small-class baseline, no packed inference kernel, no perplexity benchmark, no quantization-aware retraining, and only one deterministic synthetic teacher/student task plus matrix controls.

## Claim scope

Bounded post-training synthetic MLP and 512x512 matrix approximation probe: fixed DCT residual projection under a sub-1-bit aggregate accounting improves over the same sparse ternary base on structured residuals, but does not beat matched-bit ternary-only allocation on downstream accuracy.

## Why it stopped

Moderate proxy evidence found a mechanism but falsified the practical fixed-basis claim against a simpler matched-bit ternary allocation; this is not full validation and not paper-ready.

## Recommended next action

Stop this fixed-DCT residual variant as no-paper evidence; the next bounded test should evaluate learned or data-derived residual bases against matched-bpp ternary-only baselines on real small language-model layers.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned residual subspaces for sub-1-bit ternary compression
- Success threshold: At least one learned/data-derived residual variant below 1.0 aggregate bpp must beat matched-bpp ternary-only by at least 5% relative perplexity or accuracy degradation reduction on a real small language-model evaluation while preserving reconstruction improvements across most compressed layers.
- Stop condition: Stop if learned/data-derived residual bases fail to beat matched-bpp ternary-only on both reconstruction and downstream metrics, or if honest storage accounting exceeds 1.0 bpp for the layers under test.

## Evidence references

- Artifact root: `<local-path>/projects/ternary-weights-with-structured-residual-projection-at-sub-1-bit-3db5111fa8ca`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
