# KV-cache-aware multi-model validation of adaptive n-gram lookahead

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `kv-cache-aware-multi-model-validation-of-adaptive-n-gram-l-23c64d72be`
Run ID: `kv-cache-aware-multi-model-validation-of-adaptive-n-gram-l-23c64d72be-20260604T061145305397+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Adaptive N-gram Lookahead in a Serving Baseline: enoch://control-plane/projects/adaptive-n-gram-lookahead-in-a-serving-baseline-fb23737fcc/runs/adaptive-n-gram-lookahead-in-a-serving-baseline-fb23737fcc-20260604T020652574055+0000
- Parent run decision: Broader serving-harness validation for adaptive n-gram lookahead: enoch://control-plane/projects/broader-serving-harness-validation-for-adaptive-n-gram-loo-4e17d2053b/runs/broader-serving-harness-validation-for-adaptive-n-gram-loo-4e17d2053b-20260604T043914056004+0000

## What looked useful

Adaptive cache-aware selection had the best aggregate mean projected speedup, 1.355x versus baseline, with mean KV traffic ratio 1.032x. Fixed n2_k4 and n4_k8 had lower mean speedups, 1.244x and 1.299x, and higher KV traffic ratios, 1.340x and 1.227x. Adaptive won on decode iterations in 11 of 24 pairs, tied in 13, and lost in 0, but median speedup remained 1.0.

## Boundaries and scale limits

Validation used small Hugging Face models, short 384-token continuations, and replay-based cost accounting. It did not implement a real verifier kernel or measure end-to-end wall-clock decoding speed, paged attention, batching, long-context serving, or 7B+ models.

## Claim scope

On three small causal language models, eight fixed prompts, and replayed generated token streams, cache-aware adaptive n-gram prompt lookahead reduced mean projected decode iterations while keeping KV-token traffic close to the no-lookahead baseline; the effect was workload-sensitive and absent for many model/prompt pairs.

## Why it stopped

The result supports a cache-aware mechanism but is not paper-positive because speedup is projected from replay metrics, median speedup is 1.0, and no real KV-cache verifier wall-clock implementation was tested.

## Recommended next action

Stop this run as no-paper useful signal; the next concrete bounded step is to implement the adaptive verifier in a real generation loop and require measured tokens/sec improvement, not replay-only speedup.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Wall-clock adaptive n-gram verifier with real KV-cache generation
- Success threshold: Adaptive must improve measured tokens/sec by at least 10% over no-lookahead and at least 5% over the best fixed n-gram policy on repeated-span prompts, with no more than 5% slowdown on non-repeated controls.
- Stop condition: Stop if adaptive fails to beat the best fixed policy in measured tokens/sec or if KV/memory overhead erases the replay-projected iteration savings.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-aware-multi-model-validation-of-adaptive-n-gram-l-23c64d72be`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
