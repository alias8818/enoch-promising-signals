# Sliding-window residual channels for 2-bit long-context inference on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sliding-window-residual-channels-for-2-bit-long-context-inference-on-gb10-f3dd7fa7bfaa`
Run ID: `sliding-window-residual-channels-for-2-bit-long-context-inference-on-gb10-f3dd7fa7bfaa-20260613T201859144136+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/63c9cb3c594b

## What looked useful

With a 512-token fp16 window and 8 residual channels, mean relative L2 error improved by 6.00% on anisotropic traces and 4.63% on isotropic traces at mean 3.24x compression. At 8192 tokens, 32 residual channels improved error by about 19% but reduced compression to 1.78-2.67x depending on window. Absolute residual errors remained high.

## Boundaries and scale limits

No trained-model activations, tokenizer data, perplexity/task evaluation, production decode loop, or packed 2-bit kernel was tested. Metrics are synthetic attention-output reconstruction errors and memory estimates only.

## Claim scope

On synthetic GB10 CUDA attention-reconstruction probes up to 8192 tokens, retaining a small number of full-precision residual K/V channels consistently reduces 2-bit K/V attention-output relative L2 error, but the reduction is modest at useful compression.

## Why it stopped

No-paper useful signal: the proxy mechanism is measurable, but the effect is modest at useful compression and the run lacks real-model quality or packed-kernel throughput evidence.

## Recommended next action

Run a bounded direct-evidence follow-up on GPT-2-small-class real K/V activations measuring attention-output error and next-token loss for the same 2-bit, sliding-window, and residual-channel policies.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-activation validation of residual channels for 2-bit sliding-window K/V
- Success threshold: At a matched memory budget, variance-selected residual channels reduce next-token loss degradation by at least 20% relative to random residual channels and keep attention-output relative L2 below 0.25 on the evaluated layers/heads.
- Stop condition: Stop as negative if variance-selected residual channels fail to beat random residual channels by at least 10% on both attention-output error and next-token loss degradation, or if absolute attention-output relative L2 remains above 0.5 at memory budgets with at least 3x compression.

## Evidence references

- Artifact root: `<local-path>/projects/sliding-window-residual-channels-for-2-bit-long-context-inference-on-gb10-f3dd7fa7bfaa`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
