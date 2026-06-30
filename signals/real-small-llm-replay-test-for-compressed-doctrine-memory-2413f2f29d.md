# Real Small-LLM Replay Test for Compressed Doctrine Memory

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-small-llm-replay-test-for-compressed-doctrine-memory-2413f2f29d`
Run ID: `real-small-llm-replay-test-for-compressed-doctrine-memory-2413f2f29d-20260620T134702399026+0000`

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

- Parent run decision: Compressed Operator Doctrine Memory for Small Agents: enoch://control-plane/projects/compressed-operator-doctrine-memory-for-small-agents-416031423435/runs/compressed-operator-doctrine-memory-for-small-agents-416031423435-20260620T122542415482+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/0e65086e62ef

## What looked useful

Layered doctrine memory reached 25.0% accuracy versus the best non-compressed baseline at 12.5%, a 12.5 point lift below the required 20 points. Absolute accuracy was low, so compressed doctrine prompting alone was not reliable in this setup.

## Boundaries and scale limits

Small synthetic task set, one small instruction model, CPU-only inference, prompt-memory comparison only, no long-horizon persistence, no larger model validation, no broad corpus.

## Claim scope

A Tier 1 controlled direct test with google/flan-t5-small on 8 synthetic doctrine replay tasks found that compressed doctrine memory improved accuracy over noisy transcript and flat retrieval controls but did not meet the predefined 20 percentage-point lift threshold over the best non-compressed baseline.

## Why it stopped

Direct small-LLM evidence failed the predefined Tier 1 success threshold and showed low absolute doctrine adherence.

## Recommended next action

Stop as no-paper useful signal; a bounded follow-up should run a label-position-controlled replay test with more tasks and a stronger small model before any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Label-controlled compressed doctrine replay with a stronger small model
- Success threshold: layered_doctrine_memory accuracy at least 20 percentage points above the best non-compressed baseline and at least 70% absolute accuracy on the controlled task set.
- Stop condition: Stop if layered_doctrine_memory remains below either the 20 point lift threshold or 70% absolute accuracy after label balancing and prompt calibration.

## Evidence references

- Artifact root: `<local-path>/projects/real-small-llm-replay-test-for-compressed-doctrine-memory-2413f2f29d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
