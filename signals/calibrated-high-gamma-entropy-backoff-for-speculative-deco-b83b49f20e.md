# Calibrated high-gamma entropy backoff for speculative decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `calibrated-high-gamma-entropy-backoff-for-speculative-deco-b83b49f20e`
Run ID: `calibrated-high-gamma-entropy-backoff-for-speculative-deco-b83b49f20e-20260520T023627339239+0000`

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

- Parent run decision: Unified Entropy and Acceptance Controller for Speculative Decoding: enoch://control-plane/projects/unified-entropy-and-acceptance-controller-for-speculative-decoding-ae0e751c63ff/runs/unified-entropy-and-acceptance-controller-for-speculative-decoding-ae0e751c63ff-20260519T232009327995+0000
- Parent run decision: Real-model entropy and acceptance controller probe for speculative decoding: enoch://control-plane/projects/real-model-entropy-and-acceptance-controller-probe-for-spe-ba9df27cdc/runs/real-model-entropy-and-acceptance-controller-probe-for-spe-ba9df27cdc-20260520T023107177553+0000

## What looked useful

Trace runs showed entropy backoff can cut wasted draft tokens by roughly 80% versus static high gamma in hard/bursty regimes while preserving exact target output. Direct real-model checks were mixed to negative for raw entropy: tiny GPT-2 draft accepted zero tokens, and calibrated entropy backoff on gpt2/distilgpt2 was exact but dominated by static gamma 4 on the target-plus-draft objective.

## Boundaries and scale limits

Real-model validation used only 8 prompts and 16 generated tokens per prompt on small GPT-2-class models. It did not test sampling, batched serving, KV-cache optimized kernels, larger draft/target pairs, long contexts, or production latency under optimized inference stacks.

## Claim scope

Fixed-seed trace simulation plus bounded real-model greedy speculative decoding on distilgpt2/tiny-gpt2 and gpt2/distilgpt2. Evidence supports adaptive high-gamma backoff as a waste-reduction mechanism in trace regimes, but not raw draft entropy as a robust calibrated controller over simple static gamma baselines on the tested real models.

## Why it stopped

Medium trace evidence supports the waste-reduction mechanism, but direct real-model evidence does not validate raw draft entropy backoff as superior to a simple static gamma baseline.

## Recommended next action

Stop this raw-entropy follow-up as no-paper useful signal; next bounded test should replace raw entropy with a calibrated acceptance/agreement predictor and require it to beat static gamma 4 and gamma 8 on real GPT-2-class prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Acceptance-predictor backoff for real-model speculative decoding
- Success threshold: Predictor backoff must preserve 100% exact greedy target outputs and improve the target-plus-draft objective by at least 5% over the best static gamma baseline on both real-model pairs.
- Stop condition: Stop negative if predictor backoff fails to beat the best static gamma baseline on either real-model pair or if exact-output match drops below 100%.

## Evidence references

- Artifact root: `<local-path>/projects/calibrated-high-gamma-entropy-backoff-for-speculative-deco-b83b49f20e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
