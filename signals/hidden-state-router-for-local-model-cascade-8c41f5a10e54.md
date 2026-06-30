# Hidden-State Router for Local Model Cascade

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hidden-state-router-for-local-model-cascade-8c41f5a10e54`
Run ID: `hidden-state-router-for-local-model-cascade-8c41f5a10e54-20260607T051228366401+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/2342148c1368

## What looked useful

Hidden-state routing learned hard-region structure and slightly beat confidence-family baselines in the full run, but the cascade lift was only +0.0013 absolute accuracy at 30% escalation and +0.0015 error AUROC, too small for a practical or paper-positive claim.

## Boundaries and scale limits

Not an LLM-scale or natural-language validation; cost is a parameter-ratio proxy rather than serving latency; hidden state is an MLP activation rather than transformer layer state; five seeds only.

## Claim scope

Toy local cascade with synthetic binary classification, a small MLP, a larger MLP, and a learned router using the small model's penultimate hidden activation.

## Why it stopped

Bounded proxy evidence shows hidden-state routing is at best marginally better than confidence routing in this setup, not a full validation.

## Recommended next action

Stop this run as a no-paper useful signal; a follow-up should test a direct language-model cascade only if the larger model demonstrably corrects most small-model errors.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hidden-state routing on a small local language-model cascade
- Success threshold: At least +2.0 absolute accuracy points or equivalent task-quality gain over the best confidence-family router at the same measured latency budget across at least three random splits or datasets.
- Stop condition: Stop if the larger model fixes under 70% of small-model errors or if hidden-state routing fails to exceed confidence-family baselines by 0.5 absolute points in a smoke run.

## Evidence references

- Artifact root: `<local-path>/projects/hidden-state-router-for-local-model-cascade-8c41f5a10e54`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
