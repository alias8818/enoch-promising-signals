# Perplexity-Guided Pruning of Tiny Pretraining Corpus

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `perplexity-guided-pruning-of-tiny-pretraining-corpus-ba8d1898ee42`
Run ID: `perplexity-guided-pruning-of-tiny-pretraining-corpus-ba8d1898ee42-20260619T185602098454+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/86b6ef8f5ec2

## What looked useful

Across five seeds, low-reference-perplexity pruning beat random equal-budget subsets by -0.0733 +/- 0.0011 bits/char and beat all mixed data by -0.0266 +/- 0.0003 bits/char; high-perplexity selection was worse than random by +0.1200 +/- 0.0014 bits/char.

## Boundaries and scale limits

No neural pretraining, tokenizer dynamics, natural web-corpus noise, medium/large corpus, or multi-domain held-out validation was tested. The target model was a character 4-gram LM and the contamination was synthetic.

## Claim scope

In a tiny CPU-only n-gram probe using Tiny Shakespeare with injected synthetic/code-like noisy chunks, word-trigram reference perplexity selected a cleaner equal-budget subset and improved clean held-out character 4-gram loss versus random equal-budget pruning and keeping all mixed data.

## Why it stopped

No-paper useful signal: the mechanism is supported in a small proxy experiment, but evidence is not direct neural pretraining evidence and is not broad enough for publication-grade validation.

## Recommended next action

Run a bounded neural follow-up on naturally mixed small corpus shards using the same all-data, random equal-budget, low-PPL, high-PPL, and oracle/label controls before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Neural small-LM perplexity pruning on naturally mixed corpus shards
- Success threshold: Keep-low-reference-PPL improves held-out neural LM loss versus random equal-budget pruning in at least 3 of 3 seeds and beats all-data while keep-high-reference-PPL is worse than random.
- Stop condition: Stop as negative if low-PPL pruning fails to beat random equal-budget in two or more seeds or if gains only occur because of unmatched sequence-item budget or leaked held-out/domain labels.

## Evidence references

- Artifact root: `<local-path>/projects/perplexity-guided-pruning-of-tiny-pretraining-corpus-ba8d1898ee42`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
