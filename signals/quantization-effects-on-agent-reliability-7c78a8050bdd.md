# Quantization Effects on Agent Reliability

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `quantization-effects-on-agent-reliability-7c78a8050bdd`
Run ID: `quantization-effects-on-agent-reliability-7c78a8050bdd-20260629T225546395008+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f57ede06da9f

## What looked useful

Low-bit quantization can fail first as JSON/tool-call format instability rather than merely slower or slightly less accurate reasoning; quantization granularity materially changes the failure boundary.

## Boundaries and scale limits

Single small instruct model, one fixed seed, synthetic one-step tool calls, greedy decoding, controlled fake-quantized fp16 weights rather than production AWQ/GPTQ/NF4 kernels, no real multi-step agent environment, and no cross-model statistical replication.

## Claim scope

On a 60-task synthetic deterministic JSON tool-routing suite using Qwen/Qwen2.5-0.5B-Instruct, symmetric post-training weight rounding showed a scheme-dependent reliability boundary: 8-bit stayed near the fp16 reference, row-wise 6-bit degraded but remained mostly usable, and 4-bit or lower collapsed under both tested schemes.

## Why it stopped

Current evidence is a small, synthetic proxy with one model and controlled rounding quantizers; it is useful for prioritizing follow-up but not a publication-grade validation of quantization effects on agent reliability.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded follow-up comparing calibrated production quantizers on a real multi-step tool-use benchmark before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Production quantizer comparison on multi-step agent tool reliability
- Success threshold: A calibrated 4-bit quantizer must recover at least 80% of fp16 trajectory success and avoid catastrophic JSON validity collapse on the benchmark, while 8-bit remains within 5 percentage points of fp16.
- Stop condition: Stop as negative if all tested calibrated 4-bit quantizers fall below 50% of fp16 trajectory success or JSON validity drops below 90% on both tested models.

## Evidence references

- Artifact root: `<local-path>/projects/quantization-effects-on-agent-reliability-7c78a8050bdd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
