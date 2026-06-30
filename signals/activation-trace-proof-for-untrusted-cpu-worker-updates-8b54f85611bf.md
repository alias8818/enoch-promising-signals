# Activation-Trace Proof for Untrusted CPU Worker Updates

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `activation-trace-proof-for-untrusted-cpu-worker-updates-8b54f85611bf`
Run ID: `activation-trace-proof-for-untrusted-cpu-worker-updates-8b54f85611bf-20260604T092417933089+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/a224e97984d2

## What looked useful

Activation-only verification false-accepted 2400/2400 malicious updates. Recomputed random gradient sketches false-accepted 0/2400 tested corruptions, while 64-coordinate sampling missed sparse 0.1% corruptions in 185/200 and 189/200 trials for sign-flip and zero attacks respectively.

## Boundaries and scale limits

Synthetic small MLP with 2762 update coordinates, one fixed challenge batch, non-adaptive dense and sparse corruptions, NumPy local verifier. Did not test large models, optimizer state, commitments, real worker networking, adaptive sketch-evasion strategies, or a complete cryptographic proof system.

## Claim scope

For the tested two-layer MLP proxy, a forward activation trace that is not cryptographically or probabilistically bound to the submitted gradient/update provides no sound proof of an untrusted CPU worker update; an adversary can send honest activations and an arbitrary malicious update.

## Why it stopped

Proxy early falsification: the direct tested activation-only verifier does not bind updates and accepts arbitrary malicious updates, so it is not viable as a proof of untrusted CPU worker updates without additional update-binding checks.

## Recommended next action

Stop this activation-only proof direction; any next attempt should define an update-binding protocol using gradient/optimizer commitments or random linear sketches and test it against adaptive sparse attacks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Update-Binding Gradient Sketch Proof Against Adaptive Sparse Corruption
- Success threshold: On at least a medium model/update path, detect dense and 0.1% sparse malicious update corruptions with empirical false-accept rate below 0.001 over at least 1000 trials, while verifier work is materially below full update recomputation or full coordinate checking.
- Stop condition: Stop if adaptive sparse corruptions exceed 1% false-accept at practical sketch counts or if verifier overhead approaches full recomputation, eliminating the claimed benefit.

## Evidence references

- Artifact root: `<local-path>/projects/activation-trace-proof-for-untrusted-cpu-worker-updates-8b54f85611bf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
