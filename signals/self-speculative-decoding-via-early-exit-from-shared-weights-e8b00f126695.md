# Self-Speculative Decoding via Early Exit from Shared Weights

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `self-speculative-decoding-via-early-exit-from-shared-weights-e8b00f126695`
Run ID: `self-speculative-decoding-via-early-exit-from-shared-weights-e8b00f126695-20260523T165725741761+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/7d1a8c055254

## What looked useful

Intermediate GPT-2 layers show partial mechanism signal, especially layer 11 with 70.8% next-token top-1 agreement and 100% top-5 containment, but accepted draft prefixes are too short for speed: best gamma=4 effective token throughput was 0.651x baseline and gamma=8 at layer 11 was 0.448x.

## Boundaries and scale limits

No training, no auxiliary exit heads, no production KV-cache speculative kernel, no sampling distribution validation, no large-model validation, and only 24 prompts. Latency is a no-cache GPU proxy with one target block-verification pass.

## Claim scope

Bounded GPT-2-small probe of untrained shared-weight early exits projected through the final layer norm and tied LM head for greedy self-speculative decoding on 24 short prompts.

## Why it stopped

Proxy/direct bounded falsification: direct agreement and acceptance were measured on GPT-2-small, and the latency proxy showed below-baseline effective token throughput; full-scale production evidence would be required to overturn but is not justified for the untrained variant without a stronger small-model signal.

## Recommended next action

Stop this untrained shared-weight early-exit variant as no-paper; a bounded follow-up should test whether a trained/calibrated early-exit head or lightweight adapter can raise accepted-prefix length enough to beat a KV-cache baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Train calibrated early-exit heads for GPT-2-small self-speculative decoding
- Success threshold: At least 1.15x effective token throughput over a KV-cache full-model greedy baseline with identical greedy outputs, plus mean accepted prefix of at least 2.5 tokens for gamma=4 or 5 tokens for gamma=8.
- Stop condition: Stop if trained exits fail to exceed 1.0x effective token throughput or fail to improve mean accepted-prefix length by at least 2x over the untrained layer-11 control.

## Evidence references

- Artifact root: `<local-path>/projects/self-speculative-decoding-via-early-exit-from-shared-weights-e8b00f126695`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
