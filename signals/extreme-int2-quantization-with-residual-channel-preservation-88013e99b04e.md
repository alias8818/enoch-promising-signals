# Extreme INT2 Quantization with Residual Channel Preservation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `extreme-int2-quantization-with-residual-channel-preservation-88013e99b04e`
Run ID: `extreme-int2-quantization-with-residual-channel-preservation-88013e99b04e-20260605T124605304002+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/870c2e23d256

## What looked useful

INT2 plus preserved high-error channels is useful when INT2 is mandatory and error is row-concentrated: mean relative-MSE reduction versus INT2 ranged from 5.9% at 0.5% preserved rows to 23.9% at 5%. The effect was strongest on row-outlier weights, but 5% preservation still averaged 4.73x the INT3 error across cases.

## Boundaries and scale limits

No real transformer weights, no token activations, no perplexity/downstream task metrics, no scale metadata accounting beyond effective weight bits, and no compressed-kernel latency or throughput measurement.

## Claim scope

Bounded NumPy synthetic linear-layer tests show that preserving 0.5%-5% high-residual output channels after per-row INT2 quantization reduces held-out output reconstruction error versus plain INT2, especially for row-outlier weight distributions, but remains worse than uniform INT3 and is not better than direct weight-error selection.

## Why it stopped

Early bounded proxy evidence supports an INT2 error-reduction mechanism but does not support a paper-ready residual-channel-preservation claim because INT3 dominates and simpler weight-error row selection is at least as good.

## Recommended next action

Stop this run as a no-paper useful-signal result; a bounded follow-up should test real transformer layers with token activations and compare RCP against weight-error selection and INT3 on perplexity plus metadata-aware storage.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Transformer-layer INT2 residual-channel preservation with real activations
- Success threshold: At 1%-5% preserved channels, RCP must beat weight-error selection by at least 10% relative perplexity-delta reduction versus INT2 and recover at least half of the INT2-to-INT3 perplexity gap at comparable effective bits.
- Stop condition: Stop if RCP does not beat weight-error selection on validation perplexity for two preserved fractions or if metadata-aware storage reaches/exceeds INT3 without matching INT3 quality.

## Evidence references

- Artifact root: `<local-path>/projects/extreme-int2-quantization-with-residual-channel-preservation-88013e99b04e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
