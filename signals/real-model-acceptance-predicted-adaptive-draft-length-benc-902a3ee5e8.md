# Real-model acceptance-predicted adaptive draft length benchmark

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `real-model-acceptance-predicted-adaptive-draft-length-benc-902a3ee5e8`
Run ID: `real-model-acceptance-predicted-adaptive-draft-length-benc-902a3ee5e8-20260607T041438509276+0000`

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

- Parent run decision: Adaptive Draft Length via Acceptance Prediction: enoch://control-plane/projects/adaptive-draft-length-via-acceptance-prediction-fd0293dfc97c/runs/adaptive-draft-length-via-acceptance-prediction-fd0293dfc97c-20260607T005434670431+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ef1d873df424

## What looked useful

Adaptive draft length preserved exact target-greedy output but did not beat the best fixed draft length. In the final valid run, fixed k=2 achieved 193.77 tokens/s, adaptive achieved 188.07 tokens/s, adaptive/best-fixed speed ratio was 0.9706, and adaptive was faster on only 2 of 12 prompts. Larger fixed k values showed the expected lower acceptance, with k=8 clearly over-drafting.

## Boundaries and scale limits

Reference implementation without KV-cache reuse, production batching, serving kernels, learned predictor, larger model pairs, or broad prompt distribution. Float32 was used for the final exact-output-valid run after float16 showed numerical exact-match failures for larger fixed draft lengths.

## Claim scope

Tier 1 controlled small direct test of acceptance-predicted adaptive draft length for greedy speculative decoding using distilgpt2 as draft and gpt2 as target on 12 prompts with 48 generated tokens each.

## Why it stopped

Early direct falsification of the local success threshold: adaptive needed at least 1.05x the best fixed draft length with exact output match, but reached only 0.9706x in the final valid float32 run.

## Recommended next action

Stop this run as a bounded negative useful signal; the tested adaptive policy fails the Tier 1 success threshold and any stronger claim needs a KV-cache-aware direct serving benchmark rather than another proxy.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache-aware adaptive speculative decoding benchmark
- Success threshold: Adaptive tokens/s at least 1.05x the best fixed draft length, exact target-greedy output match for every prompt, and no more than 10% prompts slower than the best fixed condition.
- Stop condition: Stop negative if adaptive remains below 1.02x best fixed or has any unexplained exact-output mismatch after KV-cache correctness is validated.

## Evidence references

- Artifact root: `<local-path>/projects/real-model-acceptance-predicted-adaptive-draft-length-benc-902a3ee5e8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
