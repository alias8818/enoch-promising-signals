# Forward-Only Surrogate Gradient Audits

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `forward-only-surrogate-gradient-audits-348b79e359ab`
Run ID: `forward-only-surrogate-gradient-audits-348b79e359ab-20260628T160521987195+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/afca895b5ac5

## What looked useful

Vanilla forward-only SPSA is a valid tiny-model descent surrogate but not a credible broad backprop replacement at fixed probe count: cosine fell from about 0.38 at ~400 parameters to about 0.016 at ~266k parameters.

## Boundaries and scale limits

Tested only synthetic tasks, MLPs, 3-5 seeds, widths up to 512, and short runs. Did not test LLMs, CNNs, real datasets, long training, structured forward-only estimators, or GPT-2-small-class baselines.

## Claim scope

On synthetic regression and spiral-classification MLPs, 64-probe central SPSA forward-only gradients can train tiny 2x32 models about as well as backprop over 120 steps, but fixed-probe full-vector gradient alignment decays sharply with parameter count.

## Why it stopped

Proxy early falsification rather than full validation: fixed-probe full-vector forward-only gradients showed near-random alignment as parameter count increased, despite tiny-model training success.

## Recommended next action

Stop this vanilla full-vector SPSA run as a no-paper useful signal; the concrete next test is a bounded structured/blockwise surrogate audit with the same alignment and training controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Blockwise Forward-Only Surrogate Gradient Audit
- Success threshold: At >=50k parameters, structured surrogate mean cosine >=0.10 and final validation metric within 10% relative of backprop while beating vanilla SPSA and random controls at matched probe budget.
- Stop condition: Stop if structured variants remain below 0.05 mean cosine or fail to beat vanilla SPSA training at matched probe budget on two tasks.

## Evidence references

- Artifact root: `<local-path>/projects/forward-only-surrogate-gradient-audits-348b79e359ab`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
