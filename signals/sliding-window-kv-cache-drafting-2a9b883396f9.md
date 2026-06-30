# Sliding-Window KV-Cache Drafting

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sliding-window-kv-cache-drafting-2a9b883396f9`
Run ID: `sliding-window-kv-cache-drafting-2a9b883396f9-20260526T034020967353+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/a28d37830bd4

## What looked useful

Sliding-window KV-cache drafting is dependency-sensitive. In the probe, sub-lag draft windows achieved large memory/work reductions and high acceptance when long-range dependence was weak, but acceptance fell to 0.5526 under full out-of-window dependence; windows at or above the dependency lag recovered exact acceptance.

## Boundaries and scale limits

Synthetic/proxy only: no trained transformer, no natural-text benchmark, no GPU/kernel latency, no hidden-state drift, sequence length 8192, dependency lag 1024, six windows and six long-range weights.

## Claim scope

Controlled NumPy distribution-overlap probe for speculative drafting where the drafter uses a shorter sliding-window KV context than the verifier. The result supports efficiency when target probabilities are local or within the window and shows acceptance degradation when verifier-relevant dependencies lie outside the window.

## Why it stopped

Closed as no-paper useful signal: the synthetic probe supports the mechanism and exposes a failure mode, but it is not direct transformer or serving evidence.

## Recommended next action

Run a bounded real-model follow-up on a small transformer or tiny pretrained LM, measuring acceptance, latency, and quality on local versus long-range prompts before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model sliding-window drafter acceptance probe
- Success threshold: At least one sub-full draft window achieves >=90% acceptance and >=1.5x measured or calibrated throughput on local prompts, while long-range prompts show the predicted acceptance penalty when dependencies exceed the window.
- Stop condition: Stop if all sub-full windows produce <1.2x throughput or <80% acceptance on local prompts, or if implementation cannot isolate KV-window truncation from other model changes.

## Evidence references

- Artifact root: `<local-path>/projects/sliding-window-kv-cache-drafting-2a9b883396f9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
