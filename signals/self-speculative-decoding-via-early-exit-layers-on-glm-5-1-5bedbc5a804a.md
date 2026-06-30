# Self-Speculative Decoding via Early Exit Layers on GLM-5.1

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `self-speculative-decoding-via-early-exit-layers-on-glm-5-1-5bedbc5a804a`
Run ID: `self-speculative-decoding-via-early-exit-layers-on-glm-5-1-5bedbc5a804a-20260530T042703349109+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/04b180cb9018

## What looked useful

Across 256 Wikitext-2 rows, the best distilgpt2 exit was layer 5/6 with 45.70% final-head agreement and modeled k=4 speedup 0.395x; the best gpt2 exit was layer 11/12 with 53.83% agreement and modeled k=4 speedup 0.452x. Earlier cheaper exits agreed less than 25% on GPT-2 small.

## Boundaries and scale limits

No GLM-5.1 weights were loaded; no MoE routing, quantized GLM inference, trained auxiliary heads, KV-cache verifier implementation, long-context workloads, or human/task quality metrics were tested.

## Claim scope

Bounded proxy result: untrained intermediate-layer logits projected through the final LM head on distilgpt2 and gpt2 do not provide enough agreement or compute savings for self-speculative decoding; GLM-5.1 metadata shows the target model is public but too large for this bounded local run and has no exposed early-exit heads in config.

## Why it stopped

Proxy early falsification: raw/untrained early exits were directly tested on small causal LMs and modeled slower than a full forward; this is not a full GLM-5.1 validation because GLM-5.1 weights were not locally runnable within the bounded worker budget.

## Recommended next action

Stop this run as a proxy early falsification; a bounded follow-up should train lightweight auxiliary exit heads on GPT-2-small-class models and require measured end-to-end decode speedup before attempting GLM-5.1 scale.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Train auxiliary early-exit heads for self-speculative decoding on GPT-2 small
- Success threshold: At least 1.15x measured end-to-end decode speedup at equal greedy-token outputs or a documented quality-equivalent threshold on a held-out text set, with acceptance above the break-even rate implied by measured draft/verifier costs.
- Stop condition: Stop if trained exits fail to reach modeled break-even acceptance after the bounded training budget or if measured end-to-end decoding remains below 1.0x baseline speed.

## Evidence references

- Artifact root: `<local-path>/projects/self-speculative-decoding-via-early-exit-layers-on-glm-5-1-5bedbc5a804a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
