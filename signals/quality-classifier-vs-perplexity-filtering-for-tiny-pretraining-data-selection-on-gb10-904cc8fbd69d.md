# Quality classifier vs perplexity filtering for tiny pretraining data selection on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `quality-classifier-vs-perplexity-filtering-for-tiny-pretraining-data-selection-on-gb10-904cc8fbd69d`
Run ID: `quality-classifier-vs-perplexity-filtering-for-tiny-pretraining-data-selection-on-gb10-904cc8fbd69d-20260614T074646312849+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b8e093e8ed29

## What looked useful

Naive low-perplexity filtering selected repetitive junk and failed badly, but clean-reference perplexity matched the quality classifier closely; the broad quality-classifier-over-perplexity hypothesis is not supported beyond a warning that perplexity baseline design matters.

## Boundaries and scale limits

Synthetic corpus only; five seeds; tiny character-level Transformer; short training budget; no real web corpus, pretrained reference LM, tokenizer-level perplexity, or downstream task transfer.

## Claim scope

Synthetic tiny-pretraining probe on GB10 comparing simple quality-classifier selection, naive corpus perplexity filtering, clean-reference perplexity filtering, random, all-data, and oracle controls for a tiny CUDA causal LM evaluated on held-out high-quality synthetic text.

## Why it stopped

Proxy synthetic evidence is mixed: the classifier beats naive corpus low-perplexity filtering but does not robustly beat clean-reference perplexity or random/all controls, so this is not a paper-positive validation.

## Recommended next action

Stop this run as no-paper useful signal; a bounded follow-up should test equal-token selection on a real small public corpus with clean-reference perplexity and quality-classifier baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus equal-token quality classifier versus clean-reference perplexity selection
- Success threshold: Quality-classifier selection reduces held-out high-quality validation loss by at least 5% versus clean-reference perplexity and random controls across at least 4 of 5 seeds, without relying on more selected tokens.
- Stop condition: Stop if the quality classifier fails to beat clean-reference perplexity by 5% mean validation loss or if gains disappear under equal-token control.

## Evidence references

- Artifact root: `<local-path>/projects/quality-classifier-vs-perplexity-filtering-for-tiny-pretraining-data-selection-on-gb10-904cc8fbd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
