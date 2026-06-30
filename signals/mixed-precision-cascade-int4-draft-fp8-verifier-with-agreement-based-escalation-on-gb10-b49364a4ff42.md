# Mixed-precision cascade: INT4 draft + FP8 verifier with agreement-based escalation on GB10

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `mixed-precision-cascade-int4-draft-fp8-verifier-with-agreement-based-escalation-on-gb10-b49364a4ff42`
Run ID: `mixed-precision-cascade-int4-draft-fp8-verifier-with-agreement-based-escalation-on-gb10-b49364a4ff42-20260619T165459933162+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/c1312b6fa4da

## What looked useful

The cascade failed for a structural reason in the measured proxy: draft/verifier top-1 agreement was only about 2-7%, causing nearly all items to pay draft + verifier + FP16 escalation. The best lower-bound cascade speed was 0.540x of FP16 throughput, so the proxy was still slower than baseline.

## Boundaries and scale limits

Synthetic random projection proxy only; not a trained LLM, not native packed INT4 tensor-core kernels, and not end-to-end serving with KV cache or scheduler effects.

## Claim scope

On GB10 with PyTorch 2.12 synthetic projection workloads, an INT4 truncated draft plus FP8 verifier with agreement-only escalation did not beat direct FP16 matmul; even a prequantized-FP8 lower bound remained slower because escalation rates stayed about 93-98%.

## Why it stopped

Early proxy falsification, not full validation: measured agreement rates were too low and measured cascade cost was slower than FP16 across all tested shapes, including an optimistic prequantized-FP8 lower bound.

## Recommended next action

Stop this proxy line; only reopen with a trained paired draft/verifier or native packed INT4 GB10 kernels and require at least 80% acceptance plus end-to-end speedup over FP16/BF16 or FP8-only baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trained draft/verifier agreement test for mixed-precision cascade
- Success threshold: At least 80% accepted tokens or requests, no more than 1% relative quality degradation on the selected task metric, and at least 1.2x end-to-end throughput over the strongest non-cascade baseline.
- Stop condition: Stop if trained draft/verifier agreement remains below 60%, FP8-only already dominates cascade latency, or native INT4 draft runtime is not materially cheaper than the verifier.

## Evidence references

- Artifact root: `<local-path>/projects/mixed-precision-cascade-int4-draft-fp8-verifier-with-agreement-based-escalation-on-gb10-b49364a4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
