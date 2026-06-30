# Sliding-window difficulty curriculum for tiny GPT-2 pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `sliding-window-difficulty-curriculum-for-tiny-gpt-2-pretraining-957e4cfee534`
Run ID: `sliding-window-difficulty-curriculum-for-tiny-gpt-2-pretraining-957e4cfee534-20260630T065622070231+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a87d697cf665

## What looked useful

The tested naive sliding-window curriculum appears to trade easier validation retention for harder-window focus: at 400 steps curriculum-minus-random validation loss was positive for all seeds (+0.0149, +0.0246, +0.0326), with most harm on easy validation blocks while hard blocks were tied. At 1200 steps in seed 0, random reached validation loss 6.3667 while curriculum ended at 7.1204, suggesting order-induced forgetting or high-difficulty-tail overfitting.

## Boundaries and scale limits

Small Wikitext-2 proxy only: 4-layer 128-embedding GPT-2-like model, 128-token blocks, 4096 training blocks, 512 validation blocks, 400-step three-seed comparison plus one 1200-step persistence seed. This does not validate larger GPT-2-small-class models, larger corpora, teacher-model difficulty estimates, or replay-balanced curriculum variants.

## Claim scope

For a tiny 4-layer GPT-2-style causal LM trained from scratch on Wikitext-2 with GPT-2 tokenization, a unigram-difficulty easy-to-hard sliding-window sample order did not improve validation loss over shuffled training. Across three paired 400-step seeds it was worse on total validation loss, and a 1200-step seed-0 persistence check was substantially worse.

## Why it stopped

Proxy-scale direct experiment falsified the naive sliding-window curriculum under the tested tiny-GPT-2/Wikitext-2 setup; this is not a full-scale validation, but the consistent paired loss disadvantage and longer-run degradation make the current idea not worth paper development as tested.

## Recommended next action

Stop this run as a no-paper useful negative signal; if continuing, test a replay-balanced or mixture curriculum that keeps easy and medium blocks in distribution while advancing the hard-window frontier.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay-balanced difficulty frontier curriculum for tiny GPT-2 pretraining
- Success threshold: Mean final validation loss at 400 steps must be lower than random by at least 0.02 across three paired seeds with no easy-quartile validation regression greater than 0.02, and a persistence check must not degrade relative to random.
- Stop condition: Stop if replay-balanced curriculum is worse than random on mean final validation loss across three paired seeds or if the easy-quartile validation loss regression remains above 0.02.

## Evidence references

- Artifact root: `<local-path>/projects/sliding-window-difficulty-curriculum-for-tiny-gpt-2-pretraining-957e4cfee534`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
