# Optimizer-Free Local Training via Contrastive Forward-Forward

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `optimizer-free-local-training-via-contrastive-forward-forward-0266e1e05c3e`
Run ID: `optimizer-free-local-training-via-contrastive-forward-forward-0266e1e05c3e-20260621T103803327347+0000`

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

- Provider-backed Research Facility batch: qwen/qwen3.7-max: enoch://research-facility/provider/qwen/qwen3.7-max/e2df2029c8a7

## What looked useful

Medium run mean test accuracy: candidate 0.759 on linear, 0.757 on XOR, 0.862 on moons; random control 0.496, 0.494, 0.540; AdamW MLP 0.983, 0.964, 0.994. Positive goodness exceeded negative goodness in every candidate medium run, showing the local contrastive update created a real signal, but accuracy and seed stability were not competitive.

## Boundaries and scale limits

Evidence is limited to synthetic linear, XOR, and two-moons tasks with 4096 training examples, 2048 test examples, 3 hidden layers of width 128, and 5 seeds. No real dataset, sequence model, GPT-2-small-class, or long training validation was run.

## Claim scope

On three synthetic two-class classification probes, a strict no-autograd/no-optimizer local contrastive Forward-Forward-style Hebbian update learns a measurable signal above random label-injection controls, but it does not approach a standard AdamW MLP baseline.

## Why it stopped

Synthetic medium evidence supports a mechanism but not a publication-grade optimizer-free training result; the candidate remains substantially below the AdamW baseline and lacks real-data validation.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should compare this update against gradient-trained Forward-Forward on a real small dataset such as MNIST or Fashion-MNIST with matched architecture and fixed hyperparameter budget.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-data Forward-Forward control for optimizer-free local contrastive updates
- Success threshold: Recommend deeper scale only if optimizer-free FF reaches at least 90% MNIST accuracy or at least 80% Fashion-MNIST accuracy and is within 10 percentage points of gradient-trained local FF under matched architecture.
- Stop condition: Stop as negative if optimizer-free FF fails to beat random controls by at least 15 percentage points or trails gradient-trained local FF by more than 20 percentage points on the real dataset.

## Evidence references

- Artifact root: `<local-path>/projects/optimizer-free-local-training-via-contrastive-forward-forward-0266e1e05c3e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
