# Cross-Tier Compressed KV Handoff in Home Model Cascade

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cross-tier-compressed-kv-handoff-in-home-model-cascade-67f0c86133f5`
Run ID: `cross-tier-compressed-kv-handoff-in-home-model-cascade-67f0c86133f5-20260609T112657448726+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/153d62b5b21c

## What looked useful

Cross-tier compressed KV handoff is mechanically plausible when the adapter is trained on continuation behavior, not merely KV MSE. The handoff improved NLL from 3.4743 no-prefix to 2.0221 versus 1.6067 full prefill, but it remains worse than full prefill.

## Boundaries and scale limits

Only tiny PyTorch transformers on a synthetic prefix-key language were tested; no real LLMs, natural text, tokenizer mismatch, production routing, quantized KV transport, or serving-latency economics were validated.

## Claim scope

In a tiny synthetic transformer cascade, a continuation-trained low-rank adapter can map small-model KV into a larger-model KV cache that recovers about 77.8% of the no-prefix continuation NLL gap at a 34.4% per-token float storage proxy.

## Why it stopped

Closed as no-paper useful signal because the result is synthetic/toy and still has a 0.4153 NLL gap to full prefill; it is not a full validation of home model cascades.

## Recommended next action

Run a bounded GPT-2-small-class or small open-model experiment with tokenizer-compatible tiers, prompt replay and soft-prefix controls, and measured adapter plus prefill latency before considering paper scope.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tokenizer-Compatible GPT-2-Class Cross-Tier KV Handoff
- Success threshold: Recover at least 50% of the no-prefix-to-full-prefill NLL gap, keep handoff top-1/logit agreement better than no-prefix, and show an end-to-end latency or memory-transfer advantage after adapter overhead.
- Stop condition: Stop if handoff recovers less than 25% of the NLL gap or if adapter plus transfer overhead eliminates the measured prefill-saving advantage.

## Evidence references

- Artifact root: `<local-path>/projects/cross-tier-compressed-kv-handoff-in-home-model-cascade-67f0c86133f5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
