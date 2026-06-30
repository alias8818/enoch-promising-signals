# Trained Linear Probe from Early Hidden State as Draft

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `trained-linear-probe-from-early-hidden-state-as-draft-033b200362c2`
Run ID: `trained-linear-probe-from-early-hidden-state-as-draft-033b200362c2-20260525T000358268154+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/da180e9f4a95

## What looked useful

The medium run found trained-probe teacher top-1 agreement of 0.8740 versus 0.1665 for the early-hidden-state plus final-LM-head control, with teacher top-5 containment of 0.9927 versus 0.3721. Probe true next-token accuracy was 0.3267, nearly matching the final model reference accuracy of 0.3271 because the probe usually matched the final model's greedy token.

## Boundaries and scale limits

Single model, single early layer, single split/seed, short held-out text sample, no real speculative decoding verifier loop, no latency benchmark, no KV-cache integration, and no comparison to a separate small draft model. The probe uses a full vocabulary output matrix, so speed benefit is unproven.

## Claim scope

On a bounded distilgpt2 test using transformer layer 2 hidden states, 4096 train positions, and 2048 held-out evaluation positions, a trained full-vocabulary linear probe recovered the final model's greedy next-token decision much better than applying the final LM head directly to the same early hidden state.

## Why it stopped

Mechanism is supported in a bounded predictive-agreement proxy, but the run does not provide direct speculative-decoding acceptance or speed evidence required for a paper-positive claim.

## Recommended next action

Stop this run as no-paper useful-signal evidence; next run should implement an actual one-token speculative verifier loop for distilgpt2, sweep early layers, and measure acceptance rate plus wall-clock latency against greedy decoding and a separate small draft baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Layer-swept verifier-loop test for early-hidden linear draft probes
- Success threshold: At least one early-layer probe must achieve >=70% verifier acceptance and >=10% wall-clock tokens-per-second improvement over greedy decoding on the same CPU host, while beating the simple draft baseline on acceptance at similar or lower measured overhead.
- Stop condition: Stop if no swept layer reaches 50% verifier acceptance or if measured probe overhead makes tokens-per-second no better than greedy decoding despite high agreement.

## Evidence references

- Artifact root: `<local-path>/projects/trained-linear-probe-from-early-hidden-state-as-draft-033b200362c2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
