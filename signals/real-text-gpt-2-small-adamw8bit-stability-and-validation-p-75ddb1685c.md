# Real-text GPT-2-small AdamW8bit stability and validation-perplexity check on GB10

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-text-gpt-2-small-adamw8bit-stability-and-validation-p-75ddb1685c`
Run ID: `real-text-gpt-2-small-adamw8bit-stability-and-validation-p-75ddb1685c-20260610T163829376389+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: 8-bit AdamW vs full AdamW on GPT-2-small, gb10: enoch://control-plane/projects/8-bit-adamw-vs-full-adamw-on-gpt-2-small-gb10-d7f5b2a6f68c/runs/8-bit-adamw-vs-full-adamw-on-gpt-2-small-gb10-d7f5b2a6f68c-20260610T125214723069+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/021ea2559543

## What looked useful

AdamW8bit met the bounded Tier 1 threshold: final validation perplexity 864.9 versus 847.7 for AdamW, ratio 1.0203, with finite losses/gradients throughout and lower observed CUDA peak allocation in this short run.

## Boundaries and scale limits

Only 40 steps per optimizer, batch size 1, sequence length 128, 16 validation batches, one dataset, one seed, pretrained GPT-2-small. This does not establish long-run convergence, multi-seed robustness, or publication-grade optimizer equivalence.

## Claim scope

On GB10, a single-seed 40-step GPT-2-small fine-tuning run on real WikiText-2 text completed with bitsandbytes AdamW8bit without non-finite loss/gradients and finished within 1.10x the matched AdamW validation perplexity.

## Why it stopped

Tier 1 direct test met the stability/perplexity threshold but remains no-paper evidence because it is short, single-seed, and narrow in dataset/hyperparameter coverage.

## Recommended next action

Run a bounded deepen follow-up with 3 seeds and 200-500 steps per optimizer, checkpointed validation curves, and explicit optimizer-state memory accounting.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-seed longer GPT-2-small AdamW8bit validation curve check
- Success threshold: All AdamW8bit runs finite, median final validation perplexity <= 1.10x matched AdamW, and no seed worse than 1.15x matched AdamW after at least 200 steps.
- Stop condition: Stop if any AdamW8bit seed has non-finite loss/gradients or exceeds 1.15x matched AdamW validation perplexity at the final checkpoint.

## Evidence references

- Artifact root: `<local-path>/projects/real-text-gpt-2-small-adamw8bit-stability-and-validation-p-75ddb1685c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
