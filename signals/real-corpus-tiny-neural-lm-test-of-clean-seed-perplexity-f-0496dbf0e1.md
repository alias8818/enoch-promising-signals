# Real-Corpus Tiny Neural LM Test of Clean-Seed Perplexity Filtering

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `real-corpus-tiny-neural-lm-test-of-clean-seed-perplexity-f-0496dbf0e1`
Run ID: `real-corpus-tiny-neural-lm-test-of-clean-seed-perplexity-f-0496dbf0e1-20260523T075542798481+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Perplexity-Filtered Tiny Pretraining on CPU: enoch://control-plane/projects/perplexity-filtered-tiny-pretraining-on-cpu-82b8fe8565ea/runs/perplexity-filtered-tiny-pretraining-on-cpu-82b8fe8565ea-20260523T074954489467+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/5c3a1e9f2dce

## What looked useful

The seed scorer successfully separated candidate lines by seed NLL, but the low seed-perplexity subset produced worse final validation perplexity than random same-budget training: 287.60 mean valid PPL versus 268.33 for random (+7.18% worse), and 288.60 mean test PPL versus 267.98 (+7.69% worse). High seed-PPL was also worse than random but slightly better than low seed-PPL, so the expected monotonic quality relationship was absent.

## Boundaries and scale limits

Not WikiText-2 due corpus hosting failures/hang; not transformer or GPT-2-small scale; 8k train lines, 1k validation/test lines, 2 epochs, 3 final-model initialization repeats; tests pure low-perplexity selection rather than hybrid quality/diversity filtering.

## Claim scope

Tier-1 small direct real-corpus test: on an 8k-line Project Gutenberg public-domain mix with a word-level tiny LSTM seed scorer and final tiny LSTM language models, pure lowest clean-seed perplexity filtering did not improve held-out perplexity versus a token-budget-matched random subset.

## Why it stopped

Direct Tier-1 real-corpus evidence falsified the success threshold: low seed-perplexity filtering was required to improve validation PPL by at least 3% versus random, but it was 7.18% worse on validation and 7.69% worse on test.

## Recommended next action

Stop this clean-seed lowest-perplexity filtering branch as a no-paper negative result; do not scale it as-is unless a future bounded rerun changes the filter to include diversity or known-noise rejection and beats the same random same-budget control.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-tiny-neural-lm-test-of-clean-seed-perplexity-f-0496dbf0e1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
