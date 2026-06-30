# Quantized Self-Drafting

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `quantized-self-drafting-9e2dac555af5`
Run ID: `quantized-self-drafting-9e2dac555af5-20260530T002353505694+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/766a0e159b49

## What looked useful

Quantized self-drafting is mechanically plausible in a bounded synthetic probe: 3-bit group-32 at temperature 1.3 accepted 0.9464 of 196608 proposals with TV 0.0537, while 2-bit/group-128 at temperature 0.7 fell to 0.6794 acceptance. The signal is useful for selecting 3-4 bit drafts for a direct small-model follow-up, but not sufficient for a paper.

## Boundaries and scale limits

No pretrained transformer, no real text corpus, no KV-cache decode path, and no fused low-bit draft kernel was tested. Speedup is modeled from acceptance and a storage-ratio-capped cost proxy, not measured end-to-end serving throughput.

## Claim scope

Synthetic neural autoregressive proxy only: a low-bit quantized copy of the target distribution can preserve high speculative acceptance, with 3-4 bit per-group drafts reaching 0.93-0.98 sampled acceptance in the tested setup.

## Why it stopped

Proxy-only useful signal: acceptance mechanism was supported on a synthetic model, but real-model end-to-end speed and quality evidence required for a paper was not produced.

## Recommended next action

Run a GPT-2-small-class direct validation on real text with a dense decoding baseline and an actually faster low-bit draft path; treat this run as proxy evidence only.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small direct validation for quantized self-drafting
- Success threshold: 4-bit self-drafting reaches >=0.90 sampled acceptance and >=1.2x measured tokens/sec speedup versus dense decoding without a material quality regression on the selected validation metric.
- Stop condition: Stop if 4-bit acceptance is below 0.90, if measured speedup is below 1.2x, or if the low-bit draft path is not actually faster than the full-precision target path.

## Evidence references

- Artifact root: `<local-path>/projects/quantized-self-drafting-9e2dac555af5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
