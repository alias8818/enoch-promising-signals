# Tiny MLP router on bounded real small-model cascade traces

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tiny-mlp-router-on-bounded-real-small-model-cascade-traces-98e62c88e2`
Run ID: `tiny-mlp-router-on-bounded-real-small-model-cascade-traces-98e62c88e2-20260612T095444847024+0000`

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

- Parent run decision: Router training: tiny MLP on synthetic cascade traces: enoch://control-plane/projects/router-training-tiny-mlp-on-synthetic-cascade-traces-f4532f4f45a6/runs/router-training-tiny-mlp-on-synthetic-cascade-traces-f4532f4f45a6-20260611T143600045645+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d6ec3c49fcf5

## What looked useful

Across five seeds, matched-budget confidence thresholding averaged 73.9875% accuracy at 33.3% escalation; a logistic router averaged 74.6625% at 30.0% escalation; the tiny MLP averaged 74.5750% at 30.4125% escalation. The MLP's mean gain over threshold was +0.5875 pp and it lost to the threshold baseline on two of five seeds.

## Boundaries and scale limits

The test used real classifier traces, not LLM generation traces; it used at most 3,600 train and 1,600 test examples per seed, a cheap Naive Bayes model, and a logistic-regression fallback. It does not validate production LLM cascades, large model families, human quality labels, or serving latency.

## Claim scope

In a bounded 8-class 20 Newsgroups small-model classification cascade, a tiny 16-hidden-unit MLP router over cheap-model probability, margin, entropy, and class trace features produced only a modest mean accuracy gain over matched-budget confidence thresholding and did not robustly clear a predeclared +1.0 percentage point success criterion.

## Why it stopped

Direct Tier 1 classifier-cascade traces produced mixed evidence: the tiny MLP sometimes beat confidence thresholding but averaged below the predeclared +1.0 pp threshold and did not outperform a simpler logistic router.

## Recommended next action

Stop this run as no-paper useful signal; the bounded classifier-trace evidence does not support the specific tiny-MLP claim strongly enough, and any next work should test nonlinear routing on real generative small-model cascade traces rather than extend this proxy.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny nonlinear router on bounded real generative small-model cascade traces
- Success threshold: At about 30% escalation, the tiny MLP must beat confidence thresholding by at least +1.5 percentage points accuracy-equivalent utility and beat or match logistic routing within 0.25 percentage points across at least three seeds or folds.
- Stop condition: Stop as negative if the tiny MLP fails to beat confidence thresholding by +1.5 pp on mean utility or loses to logistic routing by more than 0.25 pp on the bounded generative trace test.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-mlp-router-on-bounded-real-small-model-cascade-traces-98e62c88e2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
