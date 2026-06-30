# Adafactor-2D vs 8-bit AdamW vs CAME at matched 4GB peak VRAM

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `adafactor-2d-vs-8-bit-adamw-vs-came-at-matched-4gb-peak-vram-5438e35550be`
Run ID: `adafactor-2d-vs-8-bit-adamw-vs-came-at-matched-4gb-peak-vram-5438e35550be-20260614T105658093813+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8e64d1d89fb2

## What looked useful

Activation memory dominated the 4 GiB peak in this setup, so optimizer state savings did not increase calibrated batch size. CAME and 8-bit AdamW were stronger at a shared lr=2e-4; tuned Adafactor lr=0.01 recovered much of the loss drop with near-zero factored persistent state.

## Boundaries and scale limits

Synthetic data only, one seed, 30 optimizer steps, small local model, no real corpus, no long-run convergence, no larger model where optimizer state dominates the 4 GiB budget.

## Claim scope

On a GB10 CUDA host, for an 8-layer BF16 GPT-style synthetic next-token task calibrated to approximately 4 GiB peak CUDA allocation, all three optimizers fit the same microbatch. CAME gave the largest 30-step loss drop at lr=2e-4, 8-bit AdamW gave the highest throughput, and Adafactor-2D required a higher learning rate to approach their short-horizon loss reduction while using far less persistent optimizer state.

## Why it stopped

Closed as a no-paper useful signal because the evidence is a short synthetic matched-memory proxy, not a real-data or long-run validation of the optimizer comparison.

## Recommended next action

Run a bounded real-dataset GPT-2-small-class follow-up at matched 4 GiB peak with per-optimizer learning-rate tuning, multiple seeds, and equal token budgets; stop if tuned Adafactor cannot get within 5% of CAME or 8-bit AdamW validation loss-per-token.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-data matched-4GB optimizer comparison with per-optimizer LR tuning
- Success threshold: Tuned Adafactor-2D reaches validation loss-per-token within 5% of the best of CAME or 8-bit AdamW at matched 4 GiB peak while preserving at least 5x lower persistent optimizer state.
- Stop condition: Stop if Adafactor-2D remains more than 5% worse in validation loss-per-token after the tuning grid or if all optimizers again fit identical batches because activations dominate memory.

## Evidence references

- Artifact root: `<local-path>/projects/adafactor-2d-vs-8-bit-adamw-vs-came-at-matched-4gb-peak-vram-5438e35550be`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
