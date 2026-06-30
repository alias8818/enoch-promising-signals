# Perplexity-ranked data pruning for CPU tiny pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `perplexity-ranked-data-pruning-for-cpu-tiny-pretraining-5bc0405cfc30`
Run ID: `perplexity-ranked-data-pruning-for-cpu-tiny-pretraining-5bc0405cfc30-20260610T091839595330+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/75d3b4893976

## What looked useful

Low-perplexity pruning was consistently harmful across three seeds: mean relative test PPL 1.112 versus random with 0/3 wins. Middle-band pruning had the best mean test PPL, relative 0.988 versus random with 2/3 wins, but the effect is too small and confounded for a paper claim.

## Boundaries and scale limits

Small CPU-only proxy: trigram scorer instead of pretrained LM scorer, shallow neural bigram target instead of Transformer, one corpus, three seeds, equal retained line count but unequal token counts, and short training budget.

## Claim scope

On WikiText-2 with a trigram perplexity ranker and a NumPy word-level neural bigram LM trained for 650 steps on 35% retained training lines, lowest-perplexity pruning consistently worsened held-out test perplexity versus random, while middle-perplexity pruning produced a small mixed improvement.

## Why it stopped

No paper: the direct small-scale evidence falsifies naive lowest-perplexity retention and only provides a mixed proxy signal for middle-band pruning, not a full validation.

## Recommended next action

Stop this run; if continuing, run a token-matched follow-up using a tiny Transformer target and pretrained or stronger LM scorer to test whether middle-perplexity retention remains better than random.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Token-matched middle-perplexity pruning for tiny Transformer pretraining
- Success threshold: Middle-perplexity pruning beats random by at least 3% mean test perplexity with no more than one losing seed out of five, while low-perplexity pruning remains worse or neutral.
- Stop condition: Stop if token-matched middle-band pruning fails to beat random by 1% mean test perplexity or loses on two or more seeds.

## Evidence references

- Artifact root: `<local-path>/projects/perplexity-ranked-data-pruning-for-cpu-tiny-pretraining-5bc0405cfc30`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
