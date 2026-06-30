# CPU Memory-Bandwidth Fingerprinting for Hardware Trust

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-memory-bandwidth-fingerprinting-for-hardware-trust-cc7f14f87de9`
Run ID: `cpu-memory-bandwidth-fingerprinting-for-hardware-trust-cc7f14f87de9-20260620T100525978224+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/dd37f5976891

## What looked useful

Baseline repeat relative L2 distance was 0.09586164045168569 and cosine distance was 0.003996433483142936; contention increased these to 0.16003585255798028 and 0.012788193397300196. This indicates a measurable mechanism but also a material environment confound.

## Boundaries and scale limits

Single host only; no cross-machine uniqueness, reboot persistence, NUMA pinning, thermal control, VM/container migration, firmware drift, or adversarial spoofing tests. CPU-only run completed in under the 15-minute local budget.

## Claim scope

On this single local host, a 24-feature CPU memory-bandwidth vector is repeatable enough to show a measurable same-host signature, but ordinary CPU contention shifts the vector enough to prevent a standalone hardware-trust claim.

## Why it stopped

Proxy/local evidence only: the run directly tested repeatability and contention sensitivity, not full hardware trust. The contention confound prevents a paper-ready positive claim.

## Recommended next action

Stop this run as no-paper useful signal; a bounded deepen follow-up should add CPU affinity, NUMA/thermal controls, more repeated baselines, and pre-registered accept/reject thresholds before any cross-host trust claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Controlled CPU affinity and reboot-stability memory-bandwidth fingerprint test
- Success threshold: Controlled baseline relative L2 distance below 0.05 and at least 2x smaller than contended relative L2 distance across repeated runs.
- Stop condition: Stop if controlled baseline relative L2 remains above 0.08 or overlaps contention distance, because the fingerprint is too unstable for trust use without stronger external controls.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-memory-bandwidth-fingerprinting-for-hardware-trust-cc7f14f87de9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
