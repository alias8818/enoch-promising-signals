# Real-logit validation of layered adaptive draft depth

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-logit-validation-of-layered-adaptive-draft-depth-25655f6b2d`
Run ID: `real-logit-validation-of-layered-adaptive-draft-depth-25655f6b2d-20260611T194542496356+0000`

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

- Parent run decision: Layered speculative decoding with adaptive draft depth: enoch://control-plane/projects/layered-speculative-decoding-with-adaptive-draft-depth-a4327fd40533/runs/layered-speculative-decoding-with-adaptive-draft-depth-a4327fd40533-20260611T181751051350+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/ecacc591180f

## What looked useful

Layer 4 showed top-1 agreement 0.324, margin/safe-depth correlation 0.381, and stability/safe-depth correlation 0.537. On held-out starts, adaptive depth accepted 0.408 tokens/start at 0.465 acceptance and 0.261 overdraft, versus fixed depth 1 at 0.343 tokens/start, 0.343 acceptance, and 0.657 overdraft. Fixed depths 2 and 4 accepted more tokens/start but overdrafted heavily, so the result supports risk-control signal rather than throughput dominance.

## Boundaries and scale limits

Single GPT-2-class 6-layer model, one short Wikitext-2 validation slice, offline teacher-forced contiguous top-1 agreement, max draft depth 4, no autoregressive draft execution, no wall-clock decoding benchmark, no learned calibration head, and no larger-model or cross-domain replication.

## Claim scope

On a 768-token Wikitext-2 validation sample with distilgpt2, projected intermediate-layer logits contain measurable held-out signal for choosing lower-risk draft depths against final-layer top-1 logits; the best simple adaptive policy improved accepted tokens per start versus fixed depth 1 while reducing overdraft.

## Why it stopped

Tier 1 direct real-logit test completed; evidence is useful but mixed and not paper-ready because it lacks end-to-end autoregressive decoding and speed measurements.

## Recommended next action

Run a bounded autoregressive speculative-decoding follow-up on a GPT-2-class model where intermediate layers actually draft tokens and final layers verify, with success requiring higher accepted tokens per verify pass or wall-clock speed than fixed-depth baselines at comparable overdraft and quality.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Autoregressive verification of layered adaptive draft depth on GPT-2-class decoding
- Success threshold: Adaptive depth must improve accepted tokens per verification pass or wall-clock tokens/sec by at least 10% versus the best fixed-depth baseline while keeping overdraft/rejection no worse than fixed depth 1 and preserving matched final-model output quality.
- Stop condition: Stop if adaptive depth fails to beat fixed depth 1 on accepted tokens per verification pass or fails to reduce overdraft/rejection relative to fixed depths on held-out prompts.

## Evidence references

- Artifact root: `<local-path>/projects/real-logit-validation-of-layered-adaptive-draft-depth-25655f6b2d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
