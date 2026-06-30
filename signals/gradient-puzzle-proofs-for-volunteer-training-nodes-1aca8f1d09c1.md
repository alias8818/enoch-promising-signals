# Gradient Puzzle Proofs for Volunteer Training Nodes

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `gradient-puzzle-proofs-for-volunteer-training-nodes-1aca8f1d09c1`
Run ID: `gradient-puzzle-proofs-for-volunteer-training-nodes-1aca8f1d09c1-20260523T073915707656+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/c86288c1b4e1

## What looked useful

Gradient puzzle spot-checks are a plausible audit primitive: challenged-step verification worked reliably in the simulator, and audit sampling math gives clear challenge-rate tradeoffs, but the result is not enough for a paper or deployment claim.

## Boundaries and scale limits

Tested only synthetic data, a 4225-parameter-gradient MLP, 200-round local runs, deterministic CPU execution, and simulated cheat strategies. No real volunteer nodes, networking, transformer training, GPU nondeterminism, hidden challenge protocol, or incentive model was validated.

## Claim scope

In a deterministic CPU toy MLP setting, random-sign gradient sketches for challenged mini-batches accepted honest recomputation in all tested rounds and rejected replay, stale-checkpoint, wrong-label, random, zero, and partial-batch cheats at strict tolerance.

## Why it stopped

Closed as no-paper useful signal: the local proxy supports the challenged-step mechanism but does not validate secure volunteer training end to end.

## Recommended next action

Run a bounded real-training-loop follow-up with hidden post-hoc challenges, mixed-precision/GPU nondeterminism checks, and at least two worker processes before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hidden Gradient Puzzle Audits in a Real Training Loop
- Success threshold: Honest false reject rate below 0.1% at the chosen tolerance, zero observed cheat passes across the specified strategies over at least 1000 audited challenges, and verifier overhead below 5% at a 5% challenge rate.
- Stop condition: Stop as negative if honest false rejects exceed 1% after tolerance calibration or if any cheap cheat strategy passes more than 0.5% of audited challenges.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-puzzle-proofs-for-volunteer-training-nodes-1aca8f1d09c1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
