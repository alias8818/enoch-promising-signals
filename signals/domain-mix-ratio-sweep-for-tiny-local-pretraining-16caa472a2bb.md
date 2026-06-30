# Domain Mix Ratio Sweep for Tiny Local Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `domain-mix-ratio-sweep-for-tiny-local-pretraining-16caa472a2bb`
Run ID: `domain-mix-ratio-sweep-for-tiny-local-pretraining-16caa472a2bb-20260610T124857944747+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b43ee955d2aa

## What looked useful

Avoid pure single-domain endpoints for mixed-domain tiny pretraining proxies. For the tested prose/code synthetic domains, search the 25%-50% prose range first depending on whether the objective is worst-domain robustness or balanced average loss.

## Boundaries and scale limits

Synthetic corpora only, character-level tokenization, small NumPy MLP rather than Transformer, 900 optimization steps per run, 3 seeds per ratio, held-out next-token loss only, no downstream tasks or real web/code corpora.

## Claim scope

In a deterministic synthetic character-level tiny pretraining proxy with prose-like and code-like domains, training-domain mix ratio materially changes held-out loss; 50% prose minimizes balanced loss and 25% prose minimizes worst-domain loss over the tested grid.

## Why it stopped

Closed as no-paper useful signal because the evidence is a synthetic tiny proxy, not direct/full validation on real corpora or Transformer-scale pretraining.

## Recommended next action

Run a bounded deepen follow-up using a small Transformer on real tokenized prose/code shards, testing 25%, 50%, and neighboring ratios under equal token and compute budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus tiny Transformer prose/code mix confirmation
- Success threshold: A mixed ratio in the 25%-50% prose range beats both pure-domain endpoints by at least 5% on balanced loss or worst-domain loss, with consistent direction across at least 2 of 3 seeds.
- Stop condition: Stop if mixed ratios do not beat pure-domain endpoints on balanced or worst-domain validation metrics, or if variance across seeds is larger than the observed mean improvement.

## Evidence references

- Artifact root: `<local-path>/projects/domain-mix-ratio-sweep-for-tiny-local-pretraining-16caa472a2bb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
