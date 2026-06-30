# Distributed Commitment-Audit Gradient Verification with Adaptive Attackers

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `distributed-commitment-audit-gradient-verification-with-ad-6320e8112b`
Run ID: `distributed-commitment-audit-gradient-verification-with-ad-6320e8112b-20260605T094654058738+0000`

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

- Parent run decision: Cheating-Resistant Volunteer Training via Commitment-Based Gradient Verification: enoch://control-plane/projects/cheating-resistant-volunteer-training-via-commitment-based-gradient-verification-0fea379ad0db/runs/cheating-resistant-volunteer-training-via-commitment-based-gradient-verification-0fea379ad0db-20260605T054604023231+0000
- Provider-backed Research Facility batch: openrouter/owl-alpha: enoch://research-facility/provider/openrouter/owl-alpha/28a3c5acb135

## What looked useful

Commit-before-audit removed the adaptive no-commit escape hatch in which attackers open honest gradients only for audited slots. Main run detection was 0.903208 versus 0.899887 theoretical, adaptive no-commit detection was 0.0, and commit-then-audit reduced final L2 error by 87.71% relative to adaptive no-commit.

## Boundaries and scale limits

Synthetic CPU-only simulator; no real distributed transport, large-model gradients, cryptographic batching costs, network latency, rollback/checkpoint implementation, privacy constraints, colluding validators, or norm-bounded stealth attacks were tested.

## Claim scope

In a controlled synthetic linear-regression gradient simulation with 32 workers, 8 adaptive malicious workers, hash commitments before audit selection, and pre-aggregation rejection of detected poisoned rounds, commit-then-audit detected poisoned rounds at the predicted audit probability and reduced final L2 error versus adaptive audit without commitment.

## Why it stopped

Tier 1 direct mechanism support was achieved, but the evidence remains synthetic and idealizes recovery after detection, so it is not paper-ready.

## Recommended next action

Run a bounded deepen follow-up in a real distributed training harness that measures rollback/recompute latency and verifies the same adaptive attack under actual model gradients.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Distributed Commit-Audit Gradient Verification in a Real Training Harness
- Success threshold: Commit-then-audit detection remains within 0.03 of the theoretical audited-malicious probability, adaptive no-commit has materially lower detection, final validation degradation is at least 50% lower than adaptive no-commit, and audit overhead is measured rather than assumed.
- Stop condition: Stop if real training overhead or rollback semantics make the protocol impractical, or if adaptive attackers can evade committed recomputation without detection in more than 20% of audited poisoned rounds.

## Evidence references

- Artifact root: `<local-path>/projects/distributed-commitment-audit-gradient-verification-with-ad-6320e8112b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
