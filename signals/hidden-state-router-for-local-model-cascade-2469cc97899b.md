# Hidden-State Router for Local Model Cascade

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hidden-state-router-for-local-model-cascade-2469cc97899b`
Run ID: `hidden-state-router-for-local-model-cascade-2469cc97899b-20260526T073350872966+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/dfba6690e973

## What looked useful

Hidden states carry fallback-value signal above random and entropy, with mean AUROC 0.689 and AUPRC 0.612 across three 768-window runs, but practical cascade gain was not reliably better than the cheap small-model NLL baseline: at 30% fallback hidden captured 0.350 of oracle gain versus 0.352 for small-model NLL.

## Boundaries and scale limits

Only 64-token Wikitext windows and GPT-2-family models were tested; no instruction tasks, larger modern local models, generation-quality metrics, serving latency, or nonlinear/residual hidden-state routers were validated.

## Claim scope

Bounded local Wikitext-2 cascade test using distilgpt2 as the small model, gpt2 as the fallback model, and a linear router trained on mean-pooled distilgpt2 final hidden states to predict per-window NLL improvement.

## Why it stopped

Bounded local evidence is mixed: hidden-state routing is useful above random, but the simple hidden-only router does not clearly outperform a cheap scalar NLL baseline on the direct cascade metric.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should evaluate whether hidden states add residual value over NLL in a combined router across multiple model pairs and task families.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual Hidden-State Router Across Multiple Local Cascades
- Success threshold: Combined scalar-plus-hidden router improves mean cascade NLL or task loss by at least 5% of oracle gain over the best scalar baseline at 10%, 30%, and 50% fallback in both domains, with no material latency regression beyond small-model forward cost.
- Stop condition: Stop if hidden features fail to beat the best scalar baseline by at least 2% of oracle gain on validation for both model pairs, or if routing overhead removes the quality-cost benefit.

## Evidence references

- Artifact root: `<local-path>/projects/hidden-state-router-for-local-model-cascade-2469cc97899b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
