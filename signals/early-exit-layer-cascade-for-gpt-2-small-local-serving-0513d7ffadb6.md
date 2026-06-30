# Early-Exit Layer Cascade for GPT-2-small Local Serving

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `early-exit-layer-cascade-for-gpt-2-small-local-serving-0513d7ffadb6`
Run ID: `early-exit-layer-cascade-for-gpt-2-small-local-serving-0513d7ffadb6-20260604T234315513624+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/8918b642850a

## What looked useful

Raw intermediate GPT-2-small hidden states are poorly aligned for high-fidelity early exit: threshold 0.999 saved only 6.23% theoretical layers with 0.9375 agreement and +1.10 NLL, while >=0.95 agreement required threshold 1.0, i.e. no early exits and 0% savings.

## Boundaries and scale limits

Single model, single held-out corpus, 512 windows, theoretical layer savings only; no trained auxiliary heads, no real early-stop serving kernel, no generation-quality evaluation, and no multi-dataset robustness.

## Claim scope

For GPT-2-small next-token local serving on 512 WikiText-2 validation context windows, a no-training logit-lens early-exit cascade using max-softmax confidence does not preserve full-model behavior while saving meaningful layers.

## Why it stopped

Bounded direct next-token evidence shows proxy/early falsification of the no-training confidence-exit mechanism, not a full validation of all possible trained early-exit methods.

## Recommended next action

Stop this no-training cascade as not viable; run a bounded follow-up that trains/calibrates lightweight exit heads and requires >=15% layer savings with >=0.95 agreement and NLL delta <=0.5 on held-out windows.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated Auxiliary Heads for GPT-2-small Early Exit
- Success threshold: >=15% average layer savings, >=0.95 agreement with full model, NLL delta <=0.5, and no more than 0.02 true-accuracy drop on held-out next-token windows.
- Stop condition: Stop if trained/calibrated exits cannot reach >=0.95 agreement with any nonzero meaningful layer savings or if NLL delta remains >0.5 at the required savings point.

## Evidence references

- Artifact root: `<local-path>/projects/early-exit-layer-cascade-for-gpt-2-small-local-serving-0513d7ffadb6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
