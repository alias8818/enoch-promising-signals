# CPU n-gram draft with GPU early-exit verifier cascade

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-n-gram-draft-with-gpu-early-exit-verifier-cascade-c611bf1bf1aa`
Run ID: `cpu-n-gram-draft-with-gpu-early-exit-verifier-cascade-c611bf1bf1aa-20260523T062204660292+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/01c8b93e0fc7

## What looked useful

Naive CPU n-gram drafting has enough coverage to be measurable but insufficient acceptance for a standalone acceleration claim, and an uncalibrated shallow top-1 early-exit cascade is too lossy before the final layer.

## Boundaries and scale limits

Small GPT-2-class model, one text corpus, independent fixed-context forwards, no integrated KV-cache speculative decoder, no learned/calibrated early-exit heads, no diverse-corpus or large-model serving benchmark.

## Claim scope

On a bounded distilgpt2 CUDA probe over a single public-domain text corpus, a CPU 2-5 gram proposer generated candidates for about 75.7% of evaluated positions, but only 28.5% of proposed tokens matched the full verifier greedy top-1 token; shallow GPT-2 layer top-1 filtering rejected many bad drafts while also falsely rejecting 12-22% of all proposals that the full model would have accepted, depending on layer.

## Why it stopped

Bounded direct probe found mixed/weak acceleration mechanics: proposal coverage was high, but full-verifier acceptance was only about 28.5% and simple shallow-layer rejection discarded many otherwise accepted drafts. This is an early bounded falsification of the naive cascade, not a full-scale validation.

## Recommended next action

Stop this run as no-paper useful signal; only pursue a follow-up if it implements calibrated early-exit heads inside an actual KV-cache speculative decoder and measures end-to-end latency against greedy decoding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated early-exit heads for CPU n-gram speculative decoding
- Success threshold: At least 1.15x wall-clock tokens/s over greedy decoding with unchanged greedy outputs, at least 95% retention of full-model accepted drafts after early-exit filtering, and reproducible gains on two corpora.
- Stop condition: Stop if calibrated early exits still reject more than 5% of full-model accepted drafts at thresholds that reject enough bad drafts to improve wall-clock throughput, or if end-to-end speed is not better than greedy decoding.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-n-gram-draft-with-gpu-early-exit-verifier-cascade-c611bf1bf1aa`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
