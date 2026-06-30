# 1-bit gossip for home LAN distributed training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `1-bit-gossip-for-home-lan-distributed-training-d77df6177a39`
Run ID: `1-bit-gossip-for-home-lan-distributed-training-d77df6177a39-20260604T160230933230+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/787b7ccf8e16

## What looked useful

The mechanism is worth a bounded direct LAN follow-up: 1-bit error-feedback gossip matched fp32 ring final accuracy in the tested proxy and cut estimated 100 Mbps transfer time from 26.35s to 0.83s in the main run, but consensus error was consistently higher.

## Boundaries and scale limits

No real LAN sockets, no multi-host execution, no real image/text dataset, no large model, and only 3 seeds for the small proxy plus 1 seed for the larger-parameter probe.

## Claim scope

On a 4-worker simulated non-IID synthetic MLP training proxy, 1-bit sign+scale error-feedback ring gossip preserved fp32-ring-level final accuracy while reducing communicated bytes by about 31.9x.

## Why it stopped

Synthetic/proxy evidence supports the mechanism but is not direct home-LAN distributed-training validation.

## Recommended next action

Stop this worker run as no-paper useful signal; next run should perform a direct 2-4 host LAN implementation with actual network byte counters before any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct 2-4 host LAN validation of 1-bit error-feedback gossip
- Success threshold: At least 10x measured byte reduction and at least 2x communication-time reduction versus fp32 ring with final accuracy within 1 percentage point on the chosen small real task.
- Stop condition: Stop as negative if 1-bit gossip loses more than 2 percentage points accuracy versus fp32 ring or measured communication overhead fails to improve wall-clock step time by at least 25%.

## Evidence references

- Artifact root: `<local-path>/projects/1-bit-gossip-for-home-lan-distributed-training-d77df6177a39`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
