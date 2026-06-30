# Entropy-Gated Model Cascade for Lazy VRAM Loading

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `entropy-gated-model-cascade-for-lazy-vram-loading-279a554e431c`
Run ID: `entropy-gated-model-cascade-for-lazy-vram-loading-279a554e431c-20260520T072545261702+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/9f7b7886bec8

## What looked useful

Measured 512 MiB CUDA alloc+copy+first-touch cost was 27.469 ms median. In 20k-request simulations, TTL=0 lazy loading produced 27.01 to 29.67 ms mean latency at accuracy >=0.94 versus a 27 ms always-large baseline. TTL caches improved latency only by keeping the large model resident 82% to 100% of requests.

## Boundaries and scale limits

No trained language models were evaluated, entropy calibration and request locality were synthetic, and the largest measured blob was 512 MiB rather than multi-GB 7B+ model weights.

## Claim scope

On a GB10 CUDA microbenchmark plus synthetic entropy-gated request traces, immediate lazy unload/reload of a 512 MiB large-model blob is not latency-beneficial at an accuracy-preserving escalation rate near 50%; speedups require TTL caching that keeps the large model resident most of the time.

## Why it stopped

Proxy/local evidence falsifies the lazy VRAM unload/reload benefit under the measured GB10 load cost, but it does not constitute full real-model validation.

## Recommended next action

Stop this run as a no-paper useful signal; only pursue a bounded real-model follow-up if the question is changed from lazy unloading to warm-cache entropy routing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model entropy routing with warm-cache residency telemetry
- Success threshold: At matched accuracy within 1 percentage point of always-large, warm-cache entropy routing must reduce mean latency by at least 25% while keeping large-model residency below 50%; otherwise close as operationally uninteresting for memory saving.
- Stop condition: Stop if the threshold needed for quality escalates more than 40% of requests or if the large model must remain resident above 50% to beat always-large latency.

## Evidence references

- Artifact root: `<local-path>/projects/entropy-gated-model-cascade-for-lazy-vram-loading-279a554e431c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
