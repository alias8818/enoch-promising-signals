# Length Curriculum Data Scheduling for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `length-curriculum-data-scheduling-for-tiny-pretraining-f35fbc6410a0`
Run ID: `length-curriculum-data-scheduling-for-tiny-pretraining-f35fbc6410a0-20260604T110615314101+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/0c356b85ef28

## What looked useful

Curriculum reached 0.1132 longest-length query accuracy versus 0.0296 random and 0.0310 anti-curriculum; paired sign-flip tests favored curriculum over random for accuracy (p=0.00390625) and query loss (p=0.009765625).

## Boundaries and scale limits

Synthetic generated data, tiny 3-layer Transformer, max 16 distractor pairs, 10 seeds, 150 training steps, auxiliary query-token loss weight 4.0; no natural-text tiny pretraining, no no-auxiliary-loss confirmation, no downstream benchmark.

## Claim scope

In a synthetic tiny Transformer long-span recall language-modeling probe with an equal auxiliary query-token loss, a short-to-long length curriculum improved early longest-length query accuracy and query loss versus random length mixing and long-to-short scheduling at the same 150-step budget.

## Why it stopped

Closed as no-paper useful signal because current evidence is a synthetic auxiliary-loss mechanism probe, not direct tiny-pretraining validation.

## Recommended next action

Run a bounded deepen follow-up that removes the auxiliary query loss and tests length curriculum on realistic tiny GPT pretraining data with length-stratified validation perplexity.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: No-Auxiliary Length Curriculum for Realistic Tiny GPT Pretraining
- Success threshold: Curriculum improves long-length validation perplexity by at least 3% relative to random mixing without degrading short-length perplexity by more than 1%, with the direction holding in at least 3 seeds.
- Stop condition: Stop if curriculum fails to improve long-length validation perplexity after a calibrated equal-token-budget run, or if gains require an auxiliary/synthetic objective to appear.

## Evidence references

- Artifact root: `<local-path>/projects/length-curriculum-data-scheduling-for-tiny-pretraining-f35fbc6410a0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
