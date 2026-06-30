# Stochastic Worker Audits with Gradient Fingerprinting

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `stochastic-worker-audits-with-gradient-fingerprinting-4c82d4a8444b`
Run ID: `stochastic-worker-audits-with-gradient-fingerprinting-4c82d4a8444b-20260530T052913366930+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/12c22dd7eb68

## What looked useful

Signed gradient fingerprints are useful as a targeted audit for omitted/corrupted canary work: missing-fingerprint scenarios achieved AUROC 0.9998-1.000 and TPR 0.997-1.000 at 1% FPR with adequate fingerprint signal. Weak-fingerprint/high-noise detection fell to TPR 0.429 at 1% FPR, and attacks that preserve the expected fingerprint projection or simply scale gradients require other detectors.

## Boundaries and scale limits

Synthetic/proxy gradients only; no real distributed training loop, model convergence test, adaptive adversary, collusion analysis, secure challenge-delivery protocol, or end-to-end overhead measurement. Medium run covered 9 scenarios, 40 trials per scenario, 160 rounds, 128 workers, 1024-dimensional gradients.

## Claim scope

In a synthetic 128-worker gradient-vector simulation with stochastic audits, server-known signed fingerprint projection scores reliably detect workers that omit hidden fingerprint work, stale-gradient workers, and sign-flip workers at strict 1% honest-worker FPR when fingerprint signal-to-noise is adequate. The same mechanism is not a complete Byzantine-gradient detector.

## Why it stopped

Proxy simulation supports the fingerprint audit mechanism for specific fault classes but also falsifies the idea that gradient fingerprinting alone is a general worker-integrity detector; direct training evidence is required before any paper claim.

## Recommended next action

Stop this run as no-paper useful signal; a bounded follow-up should implement hidden fingerprint canary microbatches in a real small distributed training loop and test detection, convergence impact, overhead, and adaptive attacks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Minibatch Gradient Fingerprint Audits in a Small Distributed Training Loop
- Success threshold: At least 0.95 TPR at 1% honest-worker FPR for missing-fingerprint and stale workers, less than 5% training-throughput overhead at a documented audit rate, and no statistically meaningful final-quality degradation versus unaudited baseline on the small task.
- Stop condition: Stop if real-gradient fingerprint detection drops below 0.80 TPR at 1% FPR for missing-fingerprint workers under non-adaptive attacks, or if audit overhead exceeds 15% before adaptive attacks are considered.

## Evidence references

- Artifact root: `<local-path>/projects/stochastic-worker-audits-with-gradient-fingerprinting-4c82d4a8444b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
