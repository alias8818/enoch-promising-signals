# Speculative Decoding via INT2 Draft with Residual Channel Compensation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `speculative-decoding-via-int2-draft-with-residual-channel-compensation-b6dd3e2cb481`
Run ID: `speculative-decoding-via-int2-draft-with-residual-channel-compensation-b6dd3e2cb481-20260619T104732024941+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/69005c8b0bbe

## What looked useful

On WikiText-2 held-out GPT-2 positions, naive INT2 projection acceptance mass was 0.1372. Restoring the top 8 residual channels selected on calibration prompts raised acceptance mass to 0.4052 at 0.1367x fp16 projection storage, while random 8-channel and bottom-score 8-channel controls stayed near 0.1377 and 0.1406.

## Boundaries and scale limits

Only the final vocabulary projection was quantized; transformer blocks, packed INT2 kernels, multi-token speculative decoding, verifier scheduling, end-to-end latency, and 7B+ models were not tested.

## Claim scope

Held-out GPT-2 output-projection proxy: selected residual channel compensation improves an INT2 draft token distribution versus naive INT2 and matched random/bottom channel controls.

## Why it stopped

Proxy mechanism evidence is useful but insufficient for a paper or full speculative-decoding claim because no full INT2 draft model or end-to-end decoder speedup was tested.

## Recommended next action

Run a bounded deepen follow-up that quantizes GPT-2-small transformer blocks to INT2, applies residual channel compensation per linear layer, and measures actual speculative decoding acceptance and tokens/sec against naive INT2 and fp16 draft baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Full GPT-2 INT2 Draft Speculative Decoding With Residual Channel Compensation
- Success threshold: At least 2x acceptance mass or accepted tokens per verifier call versus naive INT2, no more than 0.25x fp16 draft projection-equivalent storage for compensated weights where measured, and a positive end-to-end tokens/sec gain over non-speculative verifier decoding on held-out text.
- Stop condition: Stop if full-model RCC INT2 acceptance is within 10% of naive INT2 or if packed/quantized execution overhead eliminates end-to-end speedup despite improved output-distribution metrics.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-decoding-via-int2-draft-with-residual-channel-compensation-b6dd3e2cb481`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
