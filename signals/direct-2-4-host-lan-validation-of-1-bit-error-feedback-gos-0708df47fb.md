# Direct 2-4 host LAN validation of 1-bit error-feedback gossip

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `direct-2-4-host-lan-validation-of-1-bit-error-feedback-gos-0708df47fb`
Run ID: `direct-2-4-host-lan-validation-of-1-bit-error-feedback-gos-0708df47fb-20260604T203055328975+0000`

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

- Parent run decision: 1-bit gossip for home LAN distributed training: enoch://control-plane/projects/1-bit-gossip-for-home-lan-distributed-training-d77df6177a39/runs/1-bit-gossip-for-home-lan-distributed-training-d77df6177a39-20260604T160230933230+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/787b7ccf8e16

## What looked useful

Damped error-feedback is the key mechanism: alpha=0.05 achieved mean final RMSE 0.002186 for 2 workers and 0.001437 for 4 workers, versus raw sign RMSE 0.866799 and 0.538885 at the same bytes. The observed serialized byte count was about 27.8x lower than fp32.

## Boundaries and scale limits

Not a physical 2-4 host LAN run; no cross-machine latency, jitter, NIC contention, clock skew, or model-training gradient workload was tested. Stability was sensitive to mixing gain, with alpha=0.5 diverging for 2 workers.

## Claim scope

On one GB10 host using real TCP sockets between 2 and 4 local worker processes, damped 1-bit error-feedback gossip with alpha=0.05 preserved consensus-average accuracy far better than raw 1-bit sign at the same serialized byte count and much lower byte count than fp32.

## Why it stopped

No-paper closure: this is a bounded local TCP useful signal, not physical multi-host LAN validation or publication-grade evidence.

## Recommended next action

Run the same harness on 2-4 separate LAN machines with alpha fixed at 0.05 and require both low RMSE and bounded consensus spread versus raw sign before considering a deeper model-training follow-up.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Physical 2-4 host LAN replication of damped 1-bit error-feedback gossip
- Success threshold: For both 2 and 4 physical hosts, sign_ef alpha=0.05 must achieve mean final RMSE <= 0.01, consensus L2 <= 0.2, and at least 20x fewer serialized bytes than fp32, while outperforming raw sign RMSE by at least 10x.
- Stop condition: Stop as negative if either 2-host or 4-host sign_ef misses RMSE <= 0.01 or consensus L2 <= 0.2 across the 3-seed mean, or if raw sign matches sign_ef accuracy within 2x at the same bytes.

## Evidence references

- Artifact root: `<local-path>/projects/direct-2-4-host-lan-validation-of-1-bit-error-feedback-gos-0708df47fb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
