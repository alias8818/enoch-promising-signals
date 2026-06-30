# N-Gram Gradient Replay Detection

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-gradient-replay-detection-44b9b5acf09f`
Run ID: `n-gram-gradient-replay-detection-44b9b5acf09f-20260620T035412524873+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8af0377f90cd

## What looked useful

The gradient signal was above random/shuffled controls (ngram_gradient_replay AP 0.0481 vs shuffled AP 0.0315; ROC-AUC 0.7163 vs 0.4960), but exact train-count overlap was much stronger (AP 0.5614, ROC-AUC 0.9804, P@20 0.9625). False positives were singleton non-replay 4-grams in high-gradient documents, indicating document-level gradients contaminate incidental spans.

## Boundaries and scale limits

No real model training, no real per-example gradients, no natural text corpus, no GPT-2-small-class baseline. CPU-only run used 12 deterministic seeds, 900 train docs and 450 eval docs per seed, and completed in 5.34 seconds with 38.5 MB peak RSS.

## Claim scope

Bounded synthetic proxy: replayed 4-gram canaries in generated train/eval text with simulated replay-correlated document-level gradient norms. The tested n-gram-plus-gradient score shows weak signal over shuffled controls but poor top-k utility and loses badly to a plain train-count baseline.

## Why it stopped

Proxy evidence does not support the tested detector as practical: it gives only a weak lift over shuffled controls and is dominated by a simple exact-overlap/count baseline. This is an early proxy falsification, not a full real-model validation.

## Recommended next action

Stop this run as a no-paper useful negative proxy; next bounded action is a direct tiny-LM follow-up using real per-example loss or gradients and a span-local scoring rule compared against train-count overlap.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny-LM real-gradient replay span probe
- Success threshold: Span-local gradient detector improves average precision by at least 0.10 absolute over train-count overlap and achieves P@20 >= 0.75 across at least 5 seeds.
- Stop condition: Stop if real-gradient scoring fails to beat train-count overlap by at least 0.03 AP on an initial 3-seed smoke run or if top false positives remain dominated by incidental singleton n-grams.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-gradient-replay-detection-44b9b5acf09f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
