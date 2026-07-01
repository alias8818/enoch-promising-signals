# Robustness of quality-scored fixed-budget subset selection across clean and noisy text datasets

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `robustness-of-quality-scored-fixed-budget-subset-selection-52a77688c2`
Run ID: `robustness-of-quality-scored-fixed-budget-subset-selection-52a77688c2-20260610T065739346397+0000`

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

- Parent run decision: Quality-Scored Subset Selection Beats Random at fixed sequence-item budget: enoch://control-plane/projects/quality-scored-subset-selection-beats-random-at-fixed-token-budget-b9d9652ce49c/runs/quality-scored-subset-selection-beats-random-at-fixed-token-budget-b9d9652ce49c-20260610T011203070256+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/6e1da85b33ea

## What looked useful

The concrete quality-scored selector failed the pre-set cross-dataset robustness threshold: it improved macro-F1 under text noise on 20ng_4class by +0.0629 over random but was effectively tied on sms_spam (+0.00003), while clean performance stayed within the allowed loss. A low-quality control outperforming top-quality on 20ng_4class indicates the heuristic score can be confounded with length or genre signal rather than true data quality.

## Boundaries and scale limits

Small CPU-only benchmark: 20ng_4class and sms_spam only; Naive Bayes bag-of-words classifier; controlled injected noise; no learned quality scorer, transformer fine-tuning, human quality labels, naturally occurring web-scale noise, or broad dataset suite.

## Claim scope

Tier 1 controlled small direct test of class-balanced 25% fixed-budget text subset selection using a deterministic heuristic quality score on two public text classification datasets with clean, injected text-noise, and mixed text/label-noise candidate pools.

## Why it stopped

Controlled small direct test failed the cross-dataset noisy-text robustness threshold; this is an early falsification of the concrete heuristic selector, not a full validation or a broad rejection of all quality-scored subset-selection methods.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded action is a deepen follow-up that compares length-controlled and learned quality scorers under the same fixed-budget protocol.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Length-controlled quality scoring for fixed-budget noisy text subset selection
- Success threshold: Length-controlled or learned quality selection beats random by at least +0.02 macro-F1 under text_noise_30 on both datasets, loses no more than -0.01 macro-F1 on clean pools, and beats bottom_quality by at least +0.01 macro-F1 on both datasets.
- Stop condition: Stop if no tested scorer clears the threshold on both datasets or if gains disappear after length/class correlation controls.

## Evidence references

- Artifact root: `<local-path>/projects/robustness-of-quality-scored-fixed-budget-subset-selection-52a77688c2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
