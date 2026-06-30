# Ternary-plus-residual GPT-2-small weight quantization

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `ternary-plus-residual-gpt-2-small-weight-quantization-b54b15544e40`
Run ID: `ternary-plus-residual-gpt-2-small-weight-quantization-b54b15544e40-20260608T113331417918+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/f51065dc37c2

## What looked useful

Exact sparse residuals monotonically recover perplexity, but compact residual fractions remain far from dense GPT-2 small perplexity; near-dense recovery required a 50% residual whose simple storage accounting is worse than fp16 target-weight storage.

## Boundaries and scale limits

This is a bounded local representation probe, not a trained quantizer, not activation quantization, not a packed-kernel latency result, and not a full WikiText/GPT-2-small publication-grade evaluation.

## Claim scope

Post-training ternary plus exact top-k residual quantization of GPT-2 small transformer compute weights, with embeddings and tied LM head left dense, evaluated on 256 WikiText-2 test blocks of 128 tokens.

## Why it stopped

Bounded direct probe found the practical compact representation unsupported: at 30% residual the model still had 1.66x dense perplexity, while the 50% residual needed for near recovery exceeded fp16 target-weight storage.

## Recommended next action

Stop this post-training exact-residual variant; a bounded follow-up should test learned or quantization-aware residuals with an explicit packed-storage budget before any larger-scale claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Quantization-aware learned residual for ternary GPT-2 small weights
- Success threshold: Perplexity ratio <=1.20 versus dense fp32 GPT-2 small at <=8.4 target-weight bits per weight on the bounded WikiText-2 probe.
- Stop condition: Stop if the learned/calibrated method cannot beat the exact top-k residual at the same bit budget or remains above 1.50x dense perplexity after the bounded calibration budget.

## Evidence references

- Artifact root: `<local-path>/projects/ternary-plus-residual-gpt-2-small-weight-quantization-b54b15544e40`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
