# ResSpec: Extreme-Quant Draft with Residual Channel Rollback

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `resspec-extreme-quant-draft-with-residual-channel-rollback-ff30dad97040`
Run ID: `resspec-extreme-quant-draft-with-residual-channel-rollback-ff30dad97040-20260604T050445156648+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/84a2084c144e

## What looked useful

Error-ranked rollback preserved more fp-baseline distribution mass than random rollback. At 3-bit, 5% rollback improved one-step acceptance proxy from 0.2848 to 0.3753 and top-1 agreement from 22.6% to 31.0%; random 5% rollback reached only 0.2911 and 23.6%. At 2-bit, 5% error-ranked rollback improved acceptance proxy from 0.0960 to 0.1500, but absolute draft agreement remained too poor for a practical extreme-quant draft claim.

## Boundaries and scale limits

This run tested one small pretrained model, one validation corpus slice, one seed, dense quantize/dequantize weight simulation, and one-step distribution-overlap acceptance proxy. It did not test packed low-bit kernels, true speculative decoding throughput, trained low-bit drafts, larger model pairs, or multi-corpus robustness.

## Claim scope

On distilgpt2 evaluated over 8192 Wikitext-2 validation tokens, post-training error-ranked residual/output-channel rollback improves agreement metrics for 2-bit and 3-bit per-channel weight-quantized draft simulations compared with no rollback and same-budget random rollback.

## Why it stopped

Bounded local evidence supports the rollback mechanism but early-falsifies the practical 2-bit extreme-quant draft viability claim under post-training quantization; this is a proxy/speculative-decoding-adjacent result, not full validation.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded test should run actual speculative decoding acceptance and latency for a 3-bit rollback draft with a packed or emulated low-bit kernel.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Actual Speculative Decoding Test for 3-bit Residual Channel Rollback Drafts
- Success threshold: Error-ranked rollback must improve real speculative acceptance by at least 20% relative over no rollback and random rollback while retaining a net tokens/sec speedup over fp draft inference.
- Stop condition: Stop if error-ranked rollback fails to beat random rollback on real acceptance, or if rollback/emulation overhead removes the draft speed advantage.

## Evidence references

- Artifact root: `<local-path>/projects/resspec-extreme-quant-draft-with-residual-channel-rollback-ff30dad97040`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
