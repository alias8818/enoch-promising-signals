# Merkle-Gradient Replay for Volunteer Verification

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `merkle-gradient-replay-for-volunteer-verification-87226884388f`
Run ID: `merkle-gradient-replay-for-volunteer-verification-87226884388f-20260602T130912583069+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2469cdae6780

## What looked useful

Replay sampling is useful for detecting tampered per-example gradient leaves, reaching 0.825 empirical detection for 5% leaf tampering with 32 sampled leaves and 0.968 for 10% tampering with 32 sampled leaves. Aggregate-only cheating had 0.0 detection for all sampled replay counts, showing the naive protocol is incomplete.

## Boundaries and scale limits

Single-host synthetic toy workload only; no distributed volunteer system, multi-step training, real dataset, privacy analysis, Sybil/adversarial network model, or large-model throughput validation was tested.

## Claim scope

On a deterministic toy MLP batch of 256 examples, Merkle commitments over per-example gradients support sampled replay detection of forged leaves at the expected sampling rate, but naive leaf replay does not verify that a claimed aggregate update equals the committed leaves.

## Why it stopped

Bounded local evidence supports the leaf replay mechanism but directly exposes an aggregate-only attack that naive replay cannot detect, so the original volunteer verification idea is incomplete without a binding extension.

## Recommended next action

Stop this run as no-paper useful signal; next test should add and evaluate an aggregate-binding mechanism rather than scaling the naive Merkle leaf replay protocol.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Aggregate-Bound Merkle Gradient Replay
- Success threshold: Detect 100% of aggregate-only tampering attempts in the tested threat model while keeping verifier work below 25% of full-batch gradient recomputation for sample counts up to 32.
- Stop condition: Stop if the aggregate-binding extension either requires full recomputation in the tested protocol or fails to detect aggregate-only tampering under deterministic replay.

## Evidence references

- Artifact root: `<local-path>/projects/merkle-gradient-replay-for-volunteer-verification-87226884388f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
