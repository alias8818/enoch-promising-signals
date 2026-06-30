# Tamper-Evident Replay Buffer for Small Agent Alignment

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tamper-evident-replay-buffer-for-small-agent-alignment-29a496e0a39c`
Run ID: `tamper-evident-replay-buffer-for-small-agent-alignment-29a496e0a39c-20260524T182400173324+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/0f353212c01e

## What looked useful

Across 500-trial main and stress runs, the plain replay buffer had 0.0 detection rate, while the hash-chain verifier had 1.0 detection rate. Under the 100% reward-flip stress attack, the plain learner selected the unsafe hazardous action in 100% of trials, while the chain-verified prefix loader kept hazardous unsafe rate at 0.0 with expected return 0.851028 versus clean 0.8735.

## Boundaries and scale limits

Toy three-state/three-action environment with a tabular learner; no neural agent, LLM, RLHF/RLAIF pipeline, production storage system, external anchoring, rollback protection, or compromised-writer threat model was tested.

## Claim scope

Synthetic tabular small-agent replay experiment: SHA-256 hash-chained replay records detected post-hoc reward edits and prevented those edited records from silently shifting a replay-trained hazardous-state policy under prefix-truncation recovery.

## Why it stopped

No-paper closure: local synthetic evidence supports the integrity mechanism but is not direct evidence for a real alignment training pipeline or production replay system.

## Recommended next action

Run a bounded deepen follow-up with a small neural replay learner and signed or externally anchored chain variants against reward-edit, deletion, and rollback attacks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Signed tamper-evident replay for a small neural alignment learner
- Success threshold: At least 0.95 detection across attack classes, no statistically meaningful degradation of clean safety metrics, and at least 50% reduction in poisoned-policy unsafe behavior versus plain replay under matched attacks.
- Stop condition: Stop if signed/anchored replay fails to detect deletion or rollback in the controlled attack suite, or if verification/recovery overhead makes the small neural training loop more than 3x slower without a safety-metric benefit.

## Evidence references

- Artifact root: `<local-path>/projects/tamper-evident-replay-buffer-for-small-agent-alignment-29a496e0a39c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
