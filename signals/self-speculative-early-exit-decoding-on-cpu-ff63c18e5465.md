# Self-Speculative Early-Exit Decoding on CPU

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `self-speculative-early-exit-decoding-on-cpu-ff63c18e5465`
Run ID: `self-speculative-early-exit-decoding-on-cpu-ff63c18e5465-20260523T050204402796+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/f59484ab16ec

## What looked useful

High early-layer confidence was not aligned with final-layer agreement on the bounded distilgpt2 probe. Meaningful compute-saving gates caused 50%-100% accepted-token mismatch; the only zero-mismatch gate accepted 1/8 tokens and saved too little compute to matter.

## Boundaries and scale limits

Small prompt sample, short contexts, NumPy fp32 CPU implementation, no KV-cache optimized serving path, no full autoregressive generation quality evaluation, no larger models, and no learned verifier.

## Claim scope

For cached distilgpt2 on 8 short-context CPU next-token probes, raw intermediate-layer margin gating does not provide a useful self-speculative early-exit tradeoff: layers 1-3 had 0% final top-1 agreement despite high margins, and the only zero-mismatch tested gate saved about 2.1% layer compute.

## Why it stopped

Early direct/proxy falsification: the direct metric was final-layer agreement for next-token exits on distilgpt2, while full generation and optimized serving were not tested.

## Recommended next action

Stop this raw-margin early-exit variant as a no-paper useful signal; only revisit with an optimized CPU backend plus a calibrated agreement verifier.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated agreement verifier for CPU early-exit decoding
- Success threshold: Accept at least 30% of candidate tokens with <=1% accepted-token mismatch and demonstrate at least 20% end-to-end CPU tokens/sec improvement versus full-depth decoding.
- Stop condition: Stop if no verifier can keep accepted-token mismatch <=1% at >=10% acceptance on 256 held-out positions, or if optimized end-to-end speedup is below 10%.

## Evidence references

- Artifact root: `<local-path>/projects/self-speculative-early-exit-decoding-on-cpu-ff63c18e5465`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
