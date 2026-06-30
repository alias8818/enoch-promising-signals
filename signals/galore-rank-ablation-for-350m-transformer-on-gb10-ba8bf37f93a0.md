# GaLore Rank Ablation for 350M Transformer on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `galore-rank-ablation-for-350m-transformer-on-gb10-ba8bf37f93a0`
Run ID: `galore-rank-ablation-for-350m-transformer-on-gb10-ba8bf37f93a0-20260611T071201315567+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f3e4b47678f8

## What looked useful

Rank 8/32/128 GaLore-style updates on the 350M-class model reduced estimated optimizer-state elements by 99.15%/96.71%/86.91% versus AdamW and measured peak CUDA allocation from 3.426 GiB to 1.459/1.492/1.625 GiB. On the small 40-step sanity run, AdamW loss delta was -0.0647 while GaLore ranks 4/8/32/128 reached -0.0217/-0.0234/-0.0253/-0.0295, indicating the memory saving came with weaker short-run synthetic loss improvement at low ranks.

## Boundaries and scale limits

No real text corpus, no validation perplexity, no long horizon, no multi-seed robustness, no official galore_torch implementation, and only two 350M-class synthetic optimizer steps were run. These results cannot support a paper claim about 350M language-model pretraining quality.

## Claim scope

Local GB10 synthetic-batch evidence for a 360,957,952-parameter decoder transformer shows GaLore-style rank projection sharply reduces estimated optimizer-state elements and measured peak CUDA allocation versus AdamW, with a rank-dependent speed/memory tradeoff. A 21M-parameter 40-step convergence sanity check shows very low ranks reduce loss less than AdamW on the same synthetic batches.

## Why it stopped

This run produced direct 350M-class optimizer/memory evidence and a small convergence proxy, but it did not produce real-corpus or long-horizon evidence needed to validate GaLore rank choice for 350M transformer training.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should run the same rank ablation on a real text shard with GPT-2-small-class or 350M-class validation perplexity and at least three seeds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-text GaLore rank ablation with validation perplexity
- Success threshold: A GaLore rank achieves at least 95% of AdamW validation-perplexity improvement at the same token budget while reducing estimated optimizer-state elements by at least 85% and not reducing tokens/sec by more than 20%.
- Stop condition: Stop if all tested ranks either miss 95% of AdamW validation-perplexity improvement or lose more than 20% throughput after the planned token budget.

## Evidence references

- Artifact root: `<local-path>/projects/galore-rank-ablation-for-350m-transformer-on-gb10-ba8bf37f93a0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
