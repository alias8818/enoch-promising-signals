# Real decoder KV-cache test for 2-bit plus per-head residual channels

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-decoder-kv-cache-test-for-2-bit-plus-per-head-residua-470b3969c3`
Run ID: `real-decoder-kv-cache-test-for-2-bit-plus-per-head-residua-470b3969c3-20260611T040401086494+0000`

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

- Parent run decision: 2-bit KV Cache with Per-Head Outlier Residual Channel: enoch://control-plane/projects/2-bit-kv-cache-with-per-head-outlier-residual-channel-efa81d9a27ed/runs/2-bit-kv-cache-with-per-head-outlier-residual-channel-efa81d9a27ed-20260611T034756178186+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/513f70c2ab91

## What looked useful

Residual channels materially helped: relative CE increase fell from 10.28% at pure 2-bit to 6.52% with 8 residual dims, 4.23% with 16, and 1.80% with 32; KL also fell from 0.4295 to 0.0762. However top-1 agreement remained low, rising only from 0.6235 to 0.8413, so the direct test supports the mechanism but not high-fidelity practical decoding.

## Boundaries and scale limits

Small pretrained decoder only; 64-token context prefixes; 2048 evaluated tokens; PyTorch functional dequantization rather than a packed serving kernel; no 7B+ model, long-context, latency, or memory-bandwidth validation.

## Claim scope

On a Tier 1 direct cached-decoder test with distilgpt2, Wikitext-2 snippets, 64-token prefixes, and 2048 evaluated cached next-token predictions, per-head residual channels monotonically reduce the quality loss from naive 2-bit KV-cache quantization, but the tested configurations do not meet the combined practical threshold of <=5% CE increase and >=0.95 top-1 agreement.

## Why it stopped

Controlled small direct test supports the residual-channel mechanism but fails the practical threshold because top-1 agreement remains below 0.95 even when half of each 64-dim head is preserved.

## Recommended next action

Stop this run as no-paper useful signal; next bounded work should test learned or outlier-aware residual selection plus a less naive 2-bit quantizer on the same direct cached-decoder metric before scaling model size.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Outlier-aware residual selection for 2-bit real decoder KV cache
- Success threshold: At 16 or fewer residual dimensions per head, achieve <=5% CE increase and >=0.90 top-1 agreement in the same direct cached-decoder setup; stop before scale-up unless the smaller benchmark clears both metrics.
- Stop condition: Stop if sensitivity-aware residual selection improves top-1 agreement by less than 0.05 absolute over the activation-energy selector at the same residual count, or if CE increase remains above 5% at 16 residual dimensions.

## Evidence references

- Artifact root: `<local-path>/projects/real-decoder-kv-cache-test-for-2-bit-plus-per-head-residua-470b3969c3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
