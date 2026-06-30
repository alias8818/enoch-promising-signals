# Influence-proxy data selection for tiny GPT-2 pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `influence-proxy-data-selection-for-tiny-gpt-2-pretraining-f70d37212442`
Run ID: `influence-proxy-data-selection-for-tiny-gpt-2-pretraining-f70d37212442-20260621T123336054371+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/612f04cc27a5

## What looked useful

Influence-style selection selected target-domain examples and reduced validation loss versus random by mean 0.830 nats, but the best cheap control was always token similarity and the influence margin over that control averaged only 0.009 nats. Future claims should include strong lexical/domain-similarity controls.

## Boundaries and scale limits

Three seeds; synthetic locally generated text; tiny 2-layer GPT-2-style models; short 90-step training runs; no natural corpus, GPT-2-small-scale run, exact influence-function Hessian approximation, long pretraining, or downstream transfer validation.

## Claim scope

On a controlled synthetic mixed-domain corpus, gradient-cosine influence-proxy subset selection for tiny GPT-2-style pretraining improves target-domain validation loss versus random and high-proxy-loss selection, but is not meaningfully better than a cheap token-count similarity selector.

## Why it stopped

Bounded synthetic evidence is useful but mixed: the influence proxy beats weak controls but does not clearly outperform the cheap similarity baseline, so it is not paper-ready.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should make target and distractor examples lexically overlapping to determine whether gradient influence adds value when token similarity is insufficient.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Influence proxy under lexical-overlap distractors
- Success threshold: Influence_proxy_top beats similarity_top by at least 0.05 target validation loss on average across at least five seeds without increasing variance enough to erase the effect.
- Stop condition: Stop if token similarity remains within 0.05 loss of influence selection or if influence selection collapses to the same selected examples as similarity in the overlap-controlled corpus.

## Evidence references

- Artifact root: `<local-path>/projects/influence-proxy-data-selection-for-tiny-gpt-2-pretraining-f70d37212442`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
