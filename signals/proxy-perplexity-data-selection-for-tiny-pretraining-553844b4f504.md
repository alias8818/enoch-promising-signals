# Proxy-perplexity data selection for tiny pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `proxy-perplexity-data-selection-for-tiny-pretraining-553844b4f504`
Run ID: `proxy-perplexity-data-selection-for-tiny-pretraining-553844b4f504-20260604T112710904383+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/25e28f9bf1f5

## What looked useful

Low proxy perplexity selected mostly easy target-like documents and reduced target validation perplexity by 17.64% versus random in the 8-seed confirmation run, with 8/8 paired wins. High proxy perplexity selected off-domain data and was catastrophically worse. The mechanism is useful but narrow: proxy perplexity appears to select learnable target-like data, not necessarily diverse or strictly target-balanced data.

## Boundaries and scale limits

Synthetic documents only; unigram proxy rather than a trained transformer proxy; tiny GRU target rather than transformer target; short local CUDA runs; no real web corpus, tokenizer, downstream task, or large-scale pretraining validation.

## Claim scope

In a synthetic mixed-domain token corpus, unigram proxy-perplexity selection improved equal-token tiny GRU language-model validation perplexity versus random selection across 8 confirmation seeds, while high-perplexity selection was a strong negative control.

## Why it stopped

No-paper closure: this is a synthetic local mechanism result, not direct publication-grade evidence on real pretraining data.

## Recommended next action

Run a bounded real-corpus deepen test with a small transformer proxy scorer and tiny transformer target model, keeping random, low-PPL, high-PPL, and oracle/control selection baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus proxy-perplexity selection for tiny transformer pretraining
- Success threshold: Low proxy perplexity selection reduces target validation perplexity by at least 5% versus random with paired wins in at least 80% of seeds, while high proxy perplexity underperforms random.
- Stop condition: Stop if low proxy perplexity fails to beat random by 5% mean relative validation perplexity or if selection diagnostics show it only exploits duplication/near-duplicates rather than useful target-like data.

## Evidence references

- Artifact root: `<local-path>/projects/proxy-perplexity-data-selection-for-tiny-pretraining-553844b4f504`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
