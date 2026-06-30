# Residual Channel Pruning During Quantization-Aware Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-channel-pruning-during-quantization-aware-training-6d5170d4946f`
Run ID: `residual-channel-pruning-during-quantization-aware-training-6d5170d4946f-20260527T101803384213+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/06b896041af3

## What looked useful

During-QAT residual channel pruning halved residual-branch channels and beat random/no-QAT pruning, but it did not beat dense QAT or a simpler post-hoc QAT importance prune on mean quantized accuracy.

## Boundaries and scale limits

No real image/language dataset, no convolutional or transformer residual block, no hardware latency measurement, and no large-scale training; residual MAC reduction is an analytic proxy only.

## Claim scope

NumPy synthetic residual-MLP proxy with 4-bit fake quantization and 50% structured residual-branch channel pruning over 8 seeds.

## Why it stopped

Proxy early falsification of the stronger claim: scheduled during-QAT pruning was -1.10 percentage points versus post-hoc QAT importance pruning and -1.12 points versus dense QAT on mean quantized accuracy, although it beat weaker random/no-QAT controls.

## Recommended next action

Stop this run as a no-paper proxy result; if continuing, run a real small residual CNN dataset test with dense QAT, during-prune QAT, post-hoc prune, post-prune QAT fine-tune, random prune, and no-QAT controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-data residual CNN check for during-QAT channel pruning
- Success threshold: During-QAT pruning improves mean quantized accuracy by at least 1.0 percentage point over post-hoc importance pruning plus QAT fine-tune at the same residual-channel budget, with wins in at least 2 of 3 seeds.
- Stop condition: Stop if during-QAT pruning is within 1.0 percentage point of, or worse than, post-hoc pruning plus QAT fine-tune after 3 seeds, because the simpler baseline is sufficient.

## Evidence references

- Artifact root: `<local-path>/projects/residual-channel-pruning-during-quantization-aware-training-6d5170d4946f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
