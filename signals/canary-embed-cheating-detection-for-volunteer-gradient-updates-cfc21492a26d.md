# Canary-Embed Cheating Detection for Volunteer Gradient Updates

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `canary-embed-cheating-detection-for-volunteer-gradient-updates-cfc21492a26d`
Run ID: `canary-embed-cheating-detection-for-volunteer-gradient-updates-cfc21492a26d-20260621T190002797200+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f179458392af

## What looked useful

Canary-gradient detection showed a clear dose response. One to four canary examples were weak; eight gave moderate AUC but poor low-FPR recall; 32 examples gave near-perfect synthetic detection for omit-canary and stale-replay cheating.

## Boundaries and scale limits

Not tested on real volunteer data, large models, secure aggregation, multi-round production FL, privacy constraints, or adaptive canary-aware attackers. High detection reliability required 32 canary examples in a 96-example client batch.

## Claim scope

Synthetic PyTorch federated-learning proxy with a 64-dimensional MLP, 96 task examples per client, private per-client canary batches, and cosine scoring against a canary-only reference update.

## Why it stopped

No-paper useful signal from a synthetic proxy: mechanism is supported at high canary dose but not validated on real volunteer gradients or adaptive adversaries.

## Recommended next action

Run a bounded deepen study on a public federated benchmark with adaptive spoof/suppress attackers and explicit utility overhead measurement.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Benchmark Canary-Gradient Detection Against Adaptive Volunteer Update Cheaters
- Success threshold: At a canary overhead below 10% of local training examples, achieve AUC >= 0.90 and TPR >= 0.80 at 1% FPR against omit/stale attackers while documenting failure modes against adaptive attackers.
- Stop condition: Stop if canary overhead below 10% cannot exceed AUC 0.75 or TPR 0.50 at 1% FPR on omit/stale attackers, or if adaptive attackers reduce TPR below 0.50 without unacceptable utility overhead.

## Evidence references

- Artifact root: `<local-path>/projects/canary-embed-cheating-detection-for-volunteer-gradient-updates-cfc21492a26d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
