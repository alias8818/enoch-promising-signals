# Perplexity-ordered curriculum vs shuffled pretraining data for GPT-2-small

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `perplexity-ordered-curriculum-vs-shuffled-pretraining-data-for-gpt-2-small-d955468a3d14`
Run ID: `perplexity-ordered-curriculum-vs-shuffled-pretraining-data-for-gpt-2-small-d955468a3d14-20260622T000902227315+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ef97128d263b

## What looked useful

The direct short-run GPT-2-small probe produced mixed seed outcomes: curriculum won 2/3 seeds by validation PPL, but the largest effect favored shuffled and mean curriculum-minus-shuffled delta was +0.00962 eval loss / +14.67 PPL. Simple pretrained-perplexity easy-to-hard ordering should not be treated as a free early-training improvement without stronger replication.

## Boundaries and scale limits

This is not full GPT-2-small pretraining: only 61,440 tokens per condition per seed, first WikiText-2 blocks, short context, one easy-to-hard schedule, and no longer multi-epoch persistence test. It cannot rule out gains from larger corpora, longer schedules, bucketed curricula, or adaptive mixing.

## Claim scope

In a bounded GPT-2-small-from-scratch WikiText-2 probe with 512 training blocks, 64 validation blocks, 128-token context, 120 optimizer steps, and 3 seeds, easy-to-hard ordering by pretrained GPT-2 block perplexity did not produce a robust validation-perplexity improvement over a fixed random shuffle.

## Why it stopped

Proxy/early falsification: bounded GPT-2-small short-run evidence did not show a robust curriculum advantage, so the broad claim is not ready for paper writing or scale-up.

## Recommended next action

Stop this run as a no-paper useful signal; if pursued, run a bounded deepen study with 5+ seeds, longer matched-token schedules, and shuffled/easy-to-hard/hard-to-easy/bucketed controls before any larger-corpus scale-up.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-seed ordering ablation for pretrained-perplexity curricula in GPT-2-small
- Success threshold: Easy-to-hard or bucketed curriculum improves mean validation loss by at least 0.03 versus shuffled, wins at least 4/5 seeds, and does not lose to hard-to-easy by the same threshold at matched tokens.
- Stop condition: Stop if curriculum mean validation loss is within +/-0.01 of shuffled or loses in 3 or more seeds; classify as no robust curriculum effect for this setup.

## Evidence references

- Artifact root: `<local-path>/projects/perplexity-ordered-curriculum-vs-shuffled-pretraining-data-for-gpt-2-small-d955468a3d14`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
