# Cheating-resistant gradient audits for home GPU volunteer training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cheating-resistant-gradient-audits-for-home-gpu-volunteer-training-b8757e347971`
Run ID: `cheating-resistant-gradient-audits-for-home-gpu-volunteer-training-b8757e347971-20260611T083503403545+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d5a821022275

## What looked useful

Secret canary projection audits strongly detected replay, random matched-norm, and partial-compute cheating that ignored canaries, but did not reliably detect stale-model submissions at audit strengths that preserve honest update fidelity.

## Boundaries and scale limits

No real distributed training, no large neural network, no network protocol, and no adaptive attacker implementation. CPU-only synthetic evidence; high audit strengths were shown to distort clean training gradients rather than validated in optimizer trajectories.

## Claim scope

Synthetic logistic-regression volunteer-gradient simulation with 8 secret canary examples in 128-example batches; canary projection audits were calibrated to about 1% honest false-positive rate and compared against norm/reference-gradient plausibility checks.

## Why it stopped

Closed as no-paper useful signal because the proxy experiment supports one mechanism but exposes a core limitation; it is not full validation of cheating-resistant volunteer training.

## Recommended next action

Run a bounded deepen follow-up testing canceling or orthogonal canary constructions in a small neural network, requiring high cheat detection while keeping audited-to-clean update cosine above 0.9.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Low-distortion canary gradient audits for stale-model and replay cheating
- Success threshold: At <=2% honest false positives, detect >=95% replay and partial-compute cheats and >=80% stale-model cheats while maintaining audited-to-clean update cosine >=0.9 and no measurable validation-loss regression versus clean training.
- Stop condition: Stop if stale-model detection remains below 50% at audited-to-clean update cosine >=0.9, or if validation loss regresses materially at the audit strengths needed for detection.

## Evidence references

- Artifact root: `<local-path>/projects/cheating-resistant-gradient-audits-for-home-gpu-volunteer-training-b8757e347971`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
