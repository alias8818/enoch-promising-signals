# End-to-end calibrated residual-channel KV-cache quantization

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `end-to-end-calibrated-residual-channel-kv-cache-quantizati-fe43b6a7d9`
Run ID: `end-to-end-calibrated-residual-channel-kv-cache-quantizati-fe43b6a7d9-20260526T144021283863+0000`

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

- Parent run decision: Principled Residual Channels for KV-cache 2-bit: enoch://control-plane/projects/principled-residual-channels-for-kv-cache-2-bit-af6acae252ca/runs/principled-residual-channels-for-kv-cache-2-bit-af6acae252ca-20260526T070320984174+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/c5410934474a

## What looked useful

Calibrated residual-channel KV-cache quantization reduced the int4 NLL penalty from +0.01902 to +0.01330 versus fp cache, recovering about 30% of the loss. It also beat equal-budget random residual channels by a mean 0.00930 NLL across three random-control seeds.

## Boundaries and scale limits

Single small model, WikiText-2 test slices, 128-token windows, 64-token context, 8 calibration windows, 16 evaluation windows, three random-control seeds. The test validates numerical cache quality, not packed int4 storage, custom kernels, throughput, long-context behavior, or 7B-class robustness.

## Claim scope

Tier 1 controlled small direct test on distilgpt2 teacher-forced decoding: 4-bit per-token/per-head KV-cache quantization with 12.5% calibrated residual channels recovered part of the NLL loss versus plain int4 and beat equal-budget random residual channels over 1024 evaluated tokens per run.

## Why it stopped

No-paper useful signal: the Tier 1 direct test supports the mechanism, but the evidence is too small and lacks packed-kernel/memory-throughput validation for publication readiness.

## Recommended next action

Run a bounded deepen test on GPT-2 small or another locally feasible causal LM with at least 50000 evaluated tokens, multiple residual fractions, and packed-cache memory accounting before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small calibrated residual-channel KV-cache quantization with packed-cache accounting
- Success threshold: Calibrated residual-channel int4 recovers at least 20% of the plain int4 NLL penalty versus fp cache and beats equal-budget random residual channels on the primary metric without erasing the intended memory savings.
- Stop condition: Stop if calibrated residual channels fail to improve over plain int4 or random residual on the larger token budget, or if residual metadata/value overhead removes most of the KV-cache memory advantage.

## Evidence references

- Artifact root: `<local-path>/projects/end-to-end-calibrated-residual-channel-kv-cache-quantizati-fe43b6a7d9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
