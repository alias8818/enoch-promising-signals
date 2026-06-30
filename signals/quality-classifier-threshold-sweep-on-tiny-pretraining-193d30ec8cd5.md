# Quality classifier threshold sweep on tiny pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `quality-classifier-threshold-sweep-on-tiny-pretraining-193d30ec8cd5`
Run ID: `quality-classifier-threshold-sweep-on-tiny-pretraining-193d30ec8cd5-20260628T074927637151+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/bcfe059b0544

## What looked useful

Threshold 0.55 achieved clean NLL 3.1201 versus 3.1596 at threshold 0.00, improving mean clean NLL by 0.0395 while retaining 57.7% of documents with 100% clean retained fraction. Higher thresholds such as 0.70 and 0.80 retained too little data and worsened clean NLL to 3.3948 and 3.8781.

## Boundaries and scale limits

Synthetic token documents, hand-built quality score, n-gram LM, 5 seeds, 2400 training documents per seed, 500 clean dev documents per seed. No neural LM, no real web corpus, no real learned classifier, and no large-scale training evidence.

## Claim scope

In a deterministic synthetic tiny-pretraining proxy using an imperfect document-quality score and add-smoothed trigram language models, a moderate threshold improved held-out clean-domain loss versus training on all mixed-quality data, while aggressive thresholds over-filtered and hurt loss.

## Why it stopped

Proxy-only useful signal, not full validation: the experiment directly tested a synthetic n-gram threshold sweep and did not produce publication-grade neural pretraining evidence.

## Recommended next action

Stop this run as no-paper useful signal; the next concrete test is a bounded neural tiny-LM reproduction on real or semi-real quality-labeled text shards.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Neural tiny-LM quality-threshold sweep on real text shards
- Success threshold: Best non-oracle threshold improves mean clean validation loss by at least 1% versus all-data baseline across at least three seeds without retaining less than 25% of tokens.
- Stop condition: Stop if no threshold improves clean validation loss versus all-data baseline after matched-token training, or if gains appear only when retained tokens fall below 25%.

## Evidence references

- Artifact root: `<local-path>/projects/quality-classifier-threshold-sweep-on-tiny-pretraining-193d30ec8cd5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
